# Smart Traffic Intelligence System

> A milestone-driven Computer Vision and Deep Learning project for understanding road traffic from video, built alongside a reusable, independently testable CV foundation.

**Status:** 🚧 In development — M0: Repository & Environment Setup  
**Current development branch:** `foundation/cv-core`  
**Language:** Python 3.12 · **Environment:** [uv](https://docs.astral.sh/uv/)

## Overview

The goal is to develop an end-to-end traffic video analysis system that can eventually detect and track vehicles, count movements, estimate speed, and report traffic conditions. Features are implemented and evaluated incrementally rather than presented as complete before they exist.

A second goal is to maintain a reusable Computer Vision foundation that can be carried into **a separate future repository**, such as an AI Driver Monitoring System, without importing traffic-specific application logic.

## Planned Capabilities

- Image and video preprocessing
- Vehicle classification and object detection
- Multi-object tracking with persistent IDs
- Vehicle counting, direction, and congestion analytics
- Camera geometry and vehicle speed estimation
- Road/scene segmentation
- Modular inference pipeline, API, and dashboard
- Benchmarking, evaluation, testing, and deployment

> These are **planned milestones**, not currently implemented functionality.

## Architecture (Target)

```text
Traffic application (main)
  ├── Detection + tracking pipeline
  ├── Counting / speed / congestion logic
  ├── Traffic events + API + dashboard
  └── Uses generic CV components
               │
               ▼
Reusable CV foundation (foundation/cv-core)
  ├── Image / video processing
  ├── General detection / tracking interfaces
  ├── Geometry + evaluation utilities
  └── Tests and examples
```

The diagram describes **logical responsibilities**, not directories that already exist. Packages and abstractions will be introduced only when required by a working task.

## Roadmap

| Milestone | Scope | Expected deliverable |
| --- | --- | --- |
| M0 | Repository, branches, environment, quality checks | Reproducible development setup |
| M1 | Image processing and video fundamentals | Tested preprocessing toolkit |
| M2 | Neural networks and PyTorch | Reproducible training baseline |
| M3 | CNNs and vehicle classification | Evaluated vehicle classifier |
| M4 | Object detection | Detector baseline and metrics |
| M5 | Custom detector training | Trained and evaluated vehicle detector |
| M6 | Multi-object tracking | Tracked vehicle trajectories |
| M7 | Traffic analytics | Counting and congestion metrics |
| M8 | Speed estimation | Calibrated speed estimates with error analysis |
| M9 | Segmentation | Evaluated road/scene segmentation |
| M10 | System integration | Modular pipeline, API, and dashboard |
| M11 | Deployment and optimization | Benchmarked, documented demonstration |

See [PROGRESS.md](PROGRESS.md) for the task-by-task checklist and verified progress.

## Getting Started (Current Setup)

### Prerequisites

- Git
- Ubuntu or another supported development environment
- [uv](https://docs.astral.sh/uv/getting-started/installation/)
- Python 3.12 (managed or located by uv)

### Clone and prepare

```bash
git clone https://github.com/Tarek-Radi/smart-traffic-intelligence-system.git
cd smart-traffic-intelligence-system

# The reusable foundation currently lives on this development branch:
git switch foundation/cv-core

# Install/synchronize the environment from the committed lockfile:
uv sync --locked

# Check the Python interpreter:
uv run python --version
```

**Note:** The application and CLI are not implemented yet; the commands above verify environment setup, not traffic inference. If the foundation branch has not been pushed yet, `git switch foundation/cv-core` will not work on a fresh clone until it is published.

## Branching Strategy

| Branch | Purpose |
| --- | --- |
| `main` | Stable integrated traffic application |
| `foundation/cv-core` | Generic reusable CV functionality only |
| `feature/*` | Small scoped features, branched from the appropriate base |
| `experiment/*` | Isolated trials and comparisons |
| `fix/*` | Bug fixes |
| `refactor/*` | Behavior-preserving structural improvements |

Foundation-focused changes are reviewed and merged into `foundation/cv-core`. Traffic-specific changes target `main` through the appropriate feature branches. **Traffic-specific logic must not be merged into the foundation.** A future driver-monitoring project will use its own repository.

## Engineering Principles

- Implement one concept at a time: understand → build → test → review → document → commit.
- Prefer small modules, type hints, docstrings, PEP 8, and focused tests.
- Keep experimentation separate from reusable code and application logic.
- Split data by source video/camera/session when related frames could leak across sets.
- Compare models with recorded baselines, metrics, configurations, and failure cases.
- Do not commit secrets, virtual environments, datasets, checkpoints, or generated videos.
- Respect data licensing and privacy requirements.
- Optimize for a local RTX 3050 Laptop GPU (4 GB VRAM); use cloud compute when appropriate.

### Commit conventions

```text
feat: add histogram calculation
fix: handle empty image inputs
test: cover grayscale conversion edge cases
docs: document local setup
refactor: simplify preprocessing interface
chore: configure uv environment
```

One logical change per commit; meaningful history matters more than commit count.

## Current Progress

The repository and `foundation/cv-core` branch have been created. Python 3.12 and `uv` have been configured, with `pyproject.toml`, `uv.lock`, and `.gitignore` committed. The detailed project roadmap has also been committed. The reusable CV modules, traffic application, and evaluation results are still to come.

For the authoritative current checklist, see **[PROGRESS.md](PROGRESS.md)**.

## License

A license has not yet been selected. Until one is added, no open-source reuse permission is granted by default. Dataset and pretrained-model licenses must also be reviewed separately.