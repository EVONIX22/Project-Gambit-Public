#!/usr/bin/env python3
"""Validate the public repository disclosure boundary and published CSV data."""

from __future__ import annotations

import csv
import re
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROHIBITED_SUFFIXES = {
    ".3mf", ".7z", ".brep", ".fcbak", ".fcmacro", ".fcstd", ".iges",
    ".igs", ".mr", ".obj", ".rar", ".step", ".stl", ".stp", ".zip",
}
TEXT_SUFFIXES = {".csv", ".json", ".md", ".py", ".txt", ".yaml", ".yml"}
ALLOWED_STATUSES = {"PASS", "FAIL", "INCONCLUSIVE", "PRELIMINARY"}


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", "-C", str(ROOT), *args], text=True, encoding="utf-8"
    )


def tracked_paths() -> list[str]:
    return [line for line in git("ls-files").splitlines() if line]


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def validate_disclosure_boundary(paths: list[str], errors: list[str]) -> None:
    historical = []
    for line in git("rev-list", "--objects", "--all").splitlines():
        parts = line.split(" ", 1)
        if len(parts) == 2:
            historical.append(parts[1])

    for path in sorted(set(paths + historical)):
        if Path(path).suffix.lower() in PROHIBITED_SUFFIXES:
            fail(errors, f"prohibited public path: {path}")

    # Strings are assembled to avoid making the validator match its own source.
    sensitive_patterns = {
        "personal Windows path": re.compile(r"C:\\" + r"Users\\", re.IGNORECASE),
        "GitHub classic token": re.compile("gh" + "p_[A-Za-z0-9]{20,}"),
        "GitHub fine-grained token": re.compile("github" + "_pat_[A-Za-z0-9_]{20,}"),
        "private key": re.compile("BEGIN " + "(?:RSA |EC |OPENSSH )?PRIVATE KEY"),
    }
    for path in paths:
        file_path = ROOT / path
        if file_path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        text = file_path.read_text(encoding="utf-8")
        for label, pattern in sensitive_patterns.items():
            if pattern.search(text):
                fail(errors, f"{label} detected in {path}")


def validate_markdown_links(paths: list[str], errors: list[str]) -> None:
    link_pattern = re.compile(r"!?\[[^\]]*\]\((?:<)?([^)>#]+)(?:>)?\)")
    for path in paths:
        if not path.lower().endswith(".md"):
            continue
        file_path = ROOT / path
        for target in link_pattern.findall(file_path.read_text(encoding="utf-8")):
            if re.match(r"^(?:https?:|mailto:)", target):
                continue
            if not (file_path.parent / target).resolve().exists():
                fail(errors, f"broken local link in {path}: {target}")


def read_csv(relative_path: str) -> list[dict[str, str]]:
    with (ROOT / relative_path).open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def validate_csv_data(errors: list[str]) -> None:
    power = read_csv("results/engine-simulator/x16_boost_summary_metrics.csv")
    required_power = {
        "Configuration", "Target_RPM", "Manifold_Boost_PSI",
        "Simulated_Power_HP", "BMEP_Estimate_bar",
    }
    if len(power) != 3 or not required_power.issubset(power[0]):
        fail(errors, "powerband CSV schema or row count changed unexpectedly")
    for row in power:
        if float(row["Target_RPM"]) <= 0 or float(row["Simulated_Power_HP"]) <= 0:
            fail(errors, f"non-positive powerband value: {row['Configuration']}")

    screening = read_csv("results/engineering/x4_screening_status.csv")
    if not screening:
        fail(errors, "engineering screening CSV is empty")
    for row in screening:
        if row.get("status") not in ALLOWED_STATUSES:
            fail(errors, f"invalid evidence status: {row.get('status')}")

    kinematics = read_csv("results/kinematics/x4_validation_summary.csv")
    if len(kinematics) != 2 or any(row.get("status") != "PASS" for row in kinematics):
        fail(errors, "kinematic validation summary changed unexpectedly")
    for row in kinematics:
        if int(row["measured_dof"]) != int(row["expected_dof"]):
            fail(errors, f"DOF mismatch in {row['test_id']}")


def main() -> int:
    errors: list[str] = []
    paths = tracked_paths()
    validate_disclosure_boundary(paths, errors)
    validate_markdown_links(paths, errors)
    validate_csv_data(errors)
    if errors:
        print("PUBLIC REPOSITORY VALIDATION FAILED")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"PASS: {len(paths)} tracked files checked; disclosure boundary and public data are valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
