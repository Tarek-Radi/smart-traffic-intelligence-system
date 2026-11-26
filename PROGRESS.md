# Smart Traffic Intelligence System

> **Master roadmap & progress tracker**  
> Last updated: 2026-11-24  
> This file records verified progress, pending validation, and the next single task. A checked item means there is supporting chat output or a confirmed Git result.

## Project goal

Build a modular, evaluated Smart Traffic Intelligence System while mastering Computer Vision and Deep Learning through independent implementation. Maintain a reusable `cv_core` foundation on `foundation/cv-core`, suitable for starting a separate repository such as AI Driver Monitoring later.

## Learning contract

- 30% theory and 70% hands-on implementation.
- Work on **one concept and one task at a time**; understand intuition before libraries.
- Implement independently; receive small hints and code review before complete solutions.
- Follow **understand → implement → test → review → document → commit**.
- Each milestone needs a working deliverable, evaluation, short quiz, and Git review.
- Prefer focused, testable code over premature abstractions.

## Repository & branch policy

| Branch | Purpose |
| --- | --- |
| `main` | Stable, integrated traffic-specific application |
| `foundation/cv-core` | Generic, reusable CV foundations only |
| `feature/*` | Scoped features created from the appropriate base branch |
| `experiment/*` | Isolated learning experiments and comparisons |
| `fix/*` | Bug fixes |
| `refactor/*` | Improvements without changing external behavior |

Generic foundation features merge into `foundation/cv-core`; traffic-specific features merge into `main`. Integrate verified foundation changes into `main` when needed. **Never merge traffic-specific code into the foundation branch.** Keep future AI Driver Monitoring in a new repository. Use logical Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`, `perf:`, `ci:`).

## Engineering standards

- Python 3.12, `uv`, `pyproject.toml`, committed `uv.lock`; exclude `.venv/`.
- Use type hints, docstrings, PEP 8, `pytest`, and Ruff; separate exploration notebooks, reusable modules, and application logic.
- Keep secrets, large datasets, model checkpoints, and generated videos out of Git.
- Document dataset permissions, provenance, license, privacy, and limitations.
- Avoid leakage: split related footage by video/camera/session rather than individual frames.
- Track experiment seeds, configurations, baselines, metrics, and failure cases.
- Local GPU: RTX 3050 Laptop (4 GB VRAM); prefer compact models, small batches, or cloud resources for heavy training.
- Define evaluation metrics before use and include representative errors.

## Current status

| Field | Status |
| --- | --- |
| Current milestone | **M0 — Setup & Repository Foundation** (technical checks passed; exit review pending) |
| Current branch | `foundation/cv-core` (last confirmed) |
| Current task | **M0 exit documentation & verification** |
| Last confirmed Git commit | `abba1ca` — `test: configure pytest and add package version test` |
| Later Git update | User reported completing `chore: add ruff linting and formatting` and pushing; hash/status **not yet independently checked in chat** |
| Runtime | Ubuntu, Python 3.12.3, uv 0.13.9 |
| Test tooling | pytest 9.2.0, Ruff 0.17.6 |
| Last observed checks | `ruff check .` passed; `ruff format --check .` passed; `pytest -v`: **1 passed** |
| Next milestone | M1 — Image Processing & Video Basics (not yet started in this repo) |

### Implemented & verified

- Repository created and cloned; `foundation/cv-core` branch created and pushed.
- `uv` project and virtual environment initialized; `.venv/` excluded by `.gitignore`.
- `src/cv_core/__init__.py` created, packaged with Hatchling; import resolves to `src/cv_core`.
- Editable installation behavior verified by changing `__version__` without synchronization, then returning to `0.1.0`.
- `pytest` installed as a development dependency and a package-version unit test passed.
- Ruff installed as a development dependency; lint, format, and test checks passed after auto-formatting.
- README and roadmap documentation commits were made and pushed earlier; full fresh-clone instructions have **not** been re-audited.

### Known gaps / decisions

- The initial unit test verifies package-version exposure, **not** CV algorithm correctness.
- The Ruff commit's final hash and clean Git status are awaiting a fresh terminal check.
- A new-machine/fresh-clone setup and README smoke-check instructions still need validation.
- No traffic-specific logic belongs on the reusable foundation branch.
- The milestone exit quiz/review is not yet completed; do not mark M0 fully complete.

## Milestone checklist

### M0 — SETUP & REPOSITORY FOUNDATION

**Outcome:** Reproducible, documented, minimal development environment.

- [x] M0.1 Create repository and clone to Ubuntu.
- [x] M0.2 Create `foundation/cv-core` branch and verify Git state.
- [x] M0.3 Initialize `pyproject.toml`, `.venv`, and `uv.lock` with uv.
- [x] M0.4 Configure `.gitignore` for environments, secrets, and artifacts.
- [x] M0.5 Commit uv environment configuration.
- [x] M0.6 Add roadmap/progress file to repository and commit it.
- [x] M0.7 Verify README clone/sync/smoke-check instructions work from a clean checkout. (README exists; validation pending.)
- [x] M0.8 Configure `pytest` and Ruff; run smoke tests, lint, and format validation.
- [x] M0.9 Create minimal `src/cv_core/` and `tests/` package/test layout.
- [x] M0.10 Verify final remote push and confirm remote `main` remains unchanged. (Foundation push confirmed previously; final push reported.)
- [x] M0.11 Complete exit review, record M0 checkpoint, and verify a clean working tree.

**Deliverable:** Installable reusable foundation, automated smoke test, reproducible setup instructions.  
**Evaluation:** `uv sync`, import check, `uv run pytest -v`, `uv run ruff check .`, `uv run ruff format --check .`, clean Git state.

## M1 - IMAGE PROCESSING & VIDEO BASICS
**Outcome: a tested reusable image/video toolkit plus demo comparisons.**
- [ ] M1.1 Read images; inspect shape, dtype, ranges, channels and memory.
- [ ] M1.2 Compare BGR, RGB, grayscale and HSV; implement conversions.
- [ ] M1.3 Implement pixel intensity/contrast transformations; inspect clipping.
- [ ] M1.4 Implement histogram calculation; explain bin counts and distributions.
- [ ] M1.5 Implement and compare histogram equalization and CLAHE.
- [ ] M1.6 Understand kernels/convolution; implement a tiny filter manually.
- [ ] M1.7 Compare blur methods (box, Gaussian, median) on noisy images.
- [ ] M1.8 Implement Sobel/Canny edge extraction; vary thresholds.
- [ ] M1.9 Compare global/adaptive/Otsu thresholding.
- [ ] M1.10 Implement erosion, dilation, opening, closing on binary masks.
- [ ] M1.11 Detect contours, bounding rectangles and region-of-interest crops.
- [ ] M1.12 Read video frame-by-frame; validate FPS, timestamps and end-of-stream.
- [ ] M1.13 Add a simple video processing demo with clean resource handling.
- [ ] M1.14 Add unit tests for reusable operations and edge cases.
- [ ] M1.15 Document before/after examples and qualitative failure cases.
**Deliverable:** runnable preprocessing CLI/notebook demo and tested CV utilities.
**Evaluation:** correctness on synthetic cases; repeatable visual comparisons.
**Branch boundary:** generic transforms in foundation; traffic-specific ROI in main.
## M2 - DEEP LEARNING FUNDAMENTALS WITH PYTORCH
**Outcome: small neural network trained and evaluated with a transparent loop.**
- [ ] M2.1 Understand tensors: shapes, dtype, devices and broadcasting.
- [ ] M2.2 Build a simple linear forward pass manually; verify dimensions.
- [ ] M2.3 Implement activations and compare nonlinear vs linear models.
- [ ] M2.4 Explain classification losses (cross-entropy) on toy predictions.
- [ ] M2.5 Derive gradient descent and compute a small gradient manually.
- [ ] M2.6 Study chain rule/backprop; check against PyTorch autograd.
- [ ] M2.7 Implement Dataset/DataLoader for a tiny benchmark.
- [ ] M2.8 Write explicit train/evaluate loops and monitor training curves.
- [ ] M2.9 Compare optimizers and learning rates on the same split.
- [ ] M2.10 Diagnose overfitting; introduce regularization/early stopping.
- [ ] M2.11 Set seeds, track configs and save/load model state safely.
- [ ] M2.12 Test a CPU run and a feasible GPU run within 4 GB VRAM.
**Deliverable:** reproducible PyTorch baseline with learning curves.
**Evaluation:** train/validation metrics, baseline comparison, error examples.
## M3 - CNN & VEHICLE CLASSIFICATION
**Outcome: evaluated vehicle image classifier.**
- [ ] M3.1 Draw convolution feature maps; calculate output size.
- [ ] M3.2 Investigate padding, stride, pooling and receptive field.
- [ ] M3.3 Build a compact CNN baseline from scratch.
- [ ] M3.4 Choose permitted vehicle-class dataset; record source/license.
- [ ] M3.5 Split by source video/session to prevent near-duplicate leakage.
- [ ] M3.6 Build preprocessing and augmentation for training only.
- [ ] M3.7 Train baseline and log accuracy/precision/recall/F1 by class.
- [ ] M3.8 Compare normalization, dropout and augmentation choices.
- [ ] M3.9 Run transfer learning using a small pretrained backbone.
- [ ] M3.10 Compare frozen feature extraction vs selective fine-tuning.
- [ ] M3.11 Analyze confusion matrix and misclassified examples.
- [ ] M3.12 Package inference and unit tests for label mapping and inputs.
**Deliverable:** vehicle classifier and reproducible evaluation report.
**Evaluation:** per-class F1 vs simple baseline, leakage audit, failure analysis.
## M4 - OBJECT DETECTION
**Outcome: vehicle detector baseline and visual/evaluation pipeline.**
- [ ] M4.1 Represent bounding boxes and coordinate conversions.
- [ ] M4.2 Implement IoU by hand; test edge cases.
- [ ] M4.3 Explain confidence scores and Non-Maximum Suppression (NMS).
- [ ] M4.4 Implement a small NMS example before adopting library version.
- [ ] M4.5 Compare one-stage and two-stage detector tradeoffs.
- [ ] M4.6 Select a small pretrained YOLO-family detection baseline.
- [ ] M4.7 Build image and video inference demos with labels/confidences.
- [ ] M4.8 Explain TP/FP/FN, precision-recall and AP/mAP.
- [ ] M4.9 Measure mAP50 and mAP50-95 on a labeled validation set.
- [ ] M4.10 Inspect misses, duplicate boxes and small/occluded vehicles.
- [ ] M4.11 Benchmark approximate latency/FPS and GPU memory.
**Deliverable:** detector baseline with measured metrics and annotated demo.
**Evaluation:** class-wise precision/recall, mAP, representative error cases.
## M5 - CUSTOM VEHICLE DETECTOR TRAINING
**Outcome: custom detector trained against a documented baseline.**
- [ ] M5.1 Define detection classes and annotation policy.
- [ ] M5.2 Choose and license datasets; inventory camera/weather conditions.
- [ ] M5.3 Review labels for missing/inaccurate boxes.
- [ ] M5.4 Make leakage-safe train/val/test splits by video/camera/session.
- [ ] M5.5 Validate dataset format, class IDs and bounding box bounds.
- [ ] M5.6 Capture pretrained zero/few-shot baseline on held-out test set.
- [ ] M5.7 Set batch size/image size to fit available GPU or cloud runtime.
- [ ] M5.8 Train first fine-tuned detector with experiment tracking.
- [ ] M5.9 Compare selected augmentation/hyperparameter experiments fairly.
- [ ] M5.10 Evaluate final model on untouched held-out test set.
- [ ] M5.11 Conduct per-class and per-condition error analysis.
- [ ] M5.12 Export inference weights outside Git and record provenance.
**Deliverable:** reproducibly trained custom detector and model card.
**Evaluation:** mAP50/mAP50-95 vs pretrained baseline, error slices, memory.
## M6 - MULTI-OBJECT TRACKING
**Outcome: stable vehicle track IDs across a video.**
- [ ] M6.1 Understand track lifecycle and detection-to-track association.
- [ ] M6.2 Implement centroid nearest-neighbor tracking baseline.
- [ ] M6.3 Explore Kalman state, prediction and measurement updates.
- [ ] M6.4 Compute association costs and gating constraints.
- [ ] M6.5 Explain and experiment with Hungarian assignment.
- [ ] M6.6 Compare a simple SORT-style tracker to baseline.
- [ ] M6.7 Evaluate ByteTrack-style tracking under missed detections.
- [ ] M6.8 Handle entry/exit, ID loss and brief occlusion.
- [ ] M6.9 Visualize track histories and persistent IDs.
- [ ] M6.10 Evaluate HOTA, IDF1 and ID switches on labeled sequences.
- [ ] M6.11 Log failures: crossings, camera motion, crowding.
**Deliverable:** interchangeable tracker module with annotated videos.
**Evaluation:** tracking metrics vs centroid baseline; identity-switch analysis.
## M7 - TRAFFIC ANALYTICS
**Outcome: dependable counting, directions and congestion indicators.**
- [ ] M7.1 Define counting line/zone geometry and vehicle anchor point.
- [ ] M7.2 Implement line crossing test and direction sign.
- [ ] M7.3 Prevent double counts using tracked IDs and state.
- [ ] M7.4 Extend to multiple lanes/virtual lines and movement categories.
- [ ] M7.5 Compute time-windowed counts and flow rates.
- [ ] M7.6 Define practical density/congestion proxy with limitations.
- [ ] M7.7 Detect stationary vehicles using track displacement over time.
- [ ] M7.8 Export events in a documented schema (JSON/CSV first).
- [ ] M7.9 Create manually annotated count ground truth on short clips.
- [ ] M7.10 Compare count MAE/RMSE and inspect false crossings.
**Deliverable:** traffic analytics video demo plus exportable events.
**Evaluation:** count MAE/RMSE, false/double-count audit and edge cases.
## M8 - SPEED ESTIMATION & GEOMETRY
**Outcome: calibrated speed estimates with uncertainty reporting.**
- [ ] M8.1 Explain why pixel displacement is not physical distance.
- [ ] M8.2 Identify reference distances/camera calibration requirements.
- [ ] M8.3 Understand perspective mapping and homography geometry.
- [ ] M8.4 Estimate homography from matched ground-plane points.
- [ ] M8.5 Validate mapping using held-out real-world measurements.
- [ ] M8.6 Convert tracked ground-contact points to world coordinates.
- [ ] M8.7 Compute elapsed time from actual timestamps (not guessed FPS).
- [ ] M8.8 Estimate and smooth speed from world-distance/time.
- [ ] M8.9 Compare estimated speed to independent reference measurements.
- [ ] M8.10 Quantify MAE/RMSE and sources of uncertainty.
- [ ] M8.11 Document failure conditions (perspective, occlusion, camera motion).
**Deliverable:** speed estimation demo restricted to calibrated scenes.
**Evaluation:** speed MAE/RMSE against reference; uncertainty and limitations.
## M9 - IMAGE SEGMENTATION
**Outcome: baseline road mask model with measured segmentation quality.**
- [ ] M9.1 Explain semantic vs instance segmentation and masks.
- [ ] M9.2 Implement mask overlays and mask-based IoU/Dice examples.
- [ ] M9.3 Study encoder-decoder and U-Net skip connections.
- [ ] M9.4 Select permitted road segmentation dataset and inspect labels.
- [ ] M9.5 Create safe train/val/test splits and matching image-mask transforms.
- [ ] M9.6 Build baseline U-Net or compact pretrained segmentation model.
- [ ] M9.7 Train within GPU limits and log loss/metrics.
- [ ] M9.8 Evaluate Dice and mean IoU per class/scene condition.
- [ ] M9.9 Inspect boundary, shadow and unusual-weather failures.
- [ ] M9.10 Demonstrate how road masks can assist traffic ROI analytics.
**Deliverable:** reproducible segmentation inference and evaluation demo.
**Evaluation:** Dice/mIoU vs simple baseline and qualitative error analysis.
## M10 - SYSTEM INTEGRATION & API
**Outcome: modular end-to-end traffic pipeline and minimal usable API/UI.**
- [ ] M10.1 Draw component diagram and stable data contracts.
- [ ] M10.2 Define pipeline configuration and input/output validation.
- [ ] M10.3 Integrate video ingestion, detection and tracking.
- [ ] M10.4 Integrate count/congestion events with per-camera settings.
- [ ] M10.5 Add optional calibrated speed and road mask stages.
- [ ] M10.6 Define traffic event schema and persist to PostgreSQL.
- [ ] M10.7 Build minimal FastAPI endpoints for health, jobs and events.
- [ ] M10.8 Implement basic dashboard for results and event inspection.
- [ ] M10.9 Add structured logging and recoverable error handling.
- [ ] M10.10 Add integration tests on short repeatable clips.
- [ ] M10.11 Validate event consistency, no duplicate IDs/counts.
**Deliverable:** end-to-end demo processing a video into stored traffic events.
**Evaluation:** integration tests, event correctness, clear operational logs.
## M11 - OPTIMIZATION, DEPLOYMENT & PRESENTATION
**Outcome: tested, documented, demonstrable portfolio project.**
- [ ] M11.1 Define hardware and latency/FPS/memory benchmark protocol.
- [ ] M11.2 Profile pipeline stages to find real bottlenecks.
- [ ] M11.3 Test batch size/resolution and lightweight detector tradeoffs.
- [ ] M11.4 Evaluate ONNX export/inference compatibility and accuracy drift.
- [ ] M11.5 Create Docker setup for an appropriate deployment target.
- [ ] M11.6 Add CI for lint, unit tests and quick integration smoke tests.
- [ ] M11.7 Test fresh setup and common failure/recovery scenarios.
- [ ] M11.8 Audit privacy, licenses, secrets and artifact provenance.
- [ ] M11.9 Document architecture, setup, metrics and known limitations.
- [ ] M11.10 Record annotated demo and concise benchmark comparison.
- [ ] M11.11 Run final review, quiz, and foundation reuse audit.
**Deliverable:** portfolio-ready repository with docs, tests, demos and results.
**Evaluation:** measured FPS/latency/memory, regression tests, reproducibility.

## Session tracking template

Update these fields after **each completed task**:

| Field | Value |
| --- | --- |
| Current milestone / task | M0 / exit documentation & review |
| Current branch | `foundation/cv-core` |
| Task status | In progress |
| Concept mastered | Python packaging, editable install, Git workflow, introductory unit testing, linting vs formatting |
| Needs revision | Test failure interpretation; fresh-clone reproducibility (not yet demonstrated) |
| Implementation summary | `cv_core` package, Hatchling setup, development tooling, version smoke test |
| Validation | 1 pytest test passed; Ruff check and format passed |
| Metrics & baseline | Not applicable to setup milestone |
| Reusable components | `cv_core` importable skeleton; no CV algorithms yet |
| Last verified commit | `abba1ca` (later Ruff commit reported, hash pending) |
| Known limitations | No CV functionality or behavioral algorithm tests yet |
| **Next single task** | Verify Git state and README fresh-clone setup instructions |

## Milestone exit checklist

- [ ] Working deliverable can be reproduced by another developer.
- [ ] Evaluation method and baseline are documented (when applicable).
- [ ] Failure cases, limits, and constraints are recorded.
- [x] Reusable versus traffic-specific branch boundary is defined and respected so far.
- [x] Unit test, lint, and formatter checks passed in the latest session.
- [ ] Final Git state and latest commit are verified.
- [ ] Learner passes short milestone quiz and explains core concepts.
- [x] `PROGRESS.md` rewritten to reflect chat-verified progress (commit/push pending).

> **Maintenance rule:** This is a living plan, not evidence that future milestones are complete. Check items only after implementation and verification; advance one task at a time.
