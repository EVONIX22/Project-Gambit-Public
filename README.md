# Project Gambit

An experimental internal combustion engine research project and hyper-GT architectural exploration.

---

> [!WARNING]
> **Confidentiality Notice:**
> This public repository intentionally omits proprietary CAD assemblies, detailed manufacturing blueprints, enabling kinematic geometry, patent-sensitive mechanisms, finite element meshes, internal solver sources, and confidential engineering datasets. All proprietary rights are strictly reserved.

---

## 🌟 Overview

**Project Gambit** is a long-term engineering and research initiative focused on high-RPM compact internal combustion engine architectures, multi-bank packaging, and advanced vehicle dynamics.

The core research explores novel engine layouts (including X8, X16, and theoretical X32 configurations) designed for high power density and ultra-compact physical packaging, integrated into a four-passenger luxury hyper-GT vehicle platform.

```
┌─────────────────────────────────────────────────────────────┐
│                       PROJECT GAMBIT                        │
│                                                             │
│   [ Powertrain ]         [ Vehicle Packaging ]   [ Testing ]│
│   • X-Engine Layouts     • 4 Adult Occupants     • Dyno     │
│   • High-RPM Kinematics  • Distributed Dry Sump  • Virtual  │
│   • Novel Cranktrain     • Thermal Capsule       • Acoustic │
└─────────────────────────────────────────────────────────────┘
```

---

## 🔬 Core Research Pillars

### 1. Engine Architecture & Kinematics
- Exploration of compact four-bank X-configurations (X8 and X16 platforms).
- Study of high rotational speed dynamics (10,000–13,000+ RPM redline targets).
- Research into novel compact cranktrain and connecting-rod architectures to resolve multi-cylinder bank spacing and longitudinal packaging constraints.
- Kinematic multi-body constraint analysis, collision modeling, and clearance optimization.

### 2. Tribology & Fluid Film Dynamics
- Evaluation of high-speed journal and slipper bearing interfaces under intense reciprocating loads.
- Hydrodynamic film retention studies and transient cyclic squeeze/wedge pressure modeling.
- Tribological survivability assessments for high-RPM operation.

### 3. Thermal Management & Lubrication Systems
- Multi-circuit thermal management concepts utilizing exterior cooling jackets and high-capacity thermal buffers.
- Distributed dry-sump lubrication architectures designed for multi-bank engines operating under high lateral and longitudinal accelerations (*"Pressure to deliver, Scavenge to evacuate"*).
- Dedicated deaeration, cyclonic separation, and independent bank scavenging.

### 4. Airflow, Boost & Combustion Modeling
- Volumetric efficiency and tuned runner resonance studies across 8,000–13,000 RPM bands.
- Quad electric-assisted turbocharging (e-turbo) proxy simulations (8 psi and 13 psi manifold boundaries).
- Acoustic tuning and firing order synthesis.

---

## 📊 Public Deliverables & Structure

This public archive provides non-enabling documentation, high-level performance summaries, and research milestones:

```text
Project-Gambit-Public/
├── README.md                                    # Project overview and public scope
├── NOTICE.md                                    # Legal notice and IP rights reservation
├── CHANGELOG.md                                 # Public development history
├── docs/
│   ├── overview/
│   │   ├── project_manifesto.md                 # Complete project manifesto and philosophy
│   │   └── vehicle_architecture_concept.md      # Vehicle packaging & systems overview
│   ├── development/
│   │   └── roadmap_and_learning_stages.md       # Research ladder and virtual-to-physical roadmap
│   └── public-results/
│       ├── powerband_summary.md                 # Engine simulation findings (NA vs Boosted)
│       └── tribology_high_level_statement.md    # Hydrodynamic lubrication statement
├── results/
│   ├── engine-simulator/
│   │   └── x16_boost_summary_metrics.csv        # Simulated powerband metrics
│   ├── tribology-summary/
│   └── performance/
│       └── high_level_specifications.csv        # Architectural target specifications
└── media/
```

---

## ⚖️ License & Intellectual Property

All technical concepts, architectures, and engineering data of Project Gambit / Ledesma technology remain proprietary. See [NOTICE.md](NOTICE.md) for full terms.
