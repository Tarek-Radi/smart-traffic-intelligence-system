# Smart Traffic Intelligence System

> **Master roadmap & progress tracker — Project-first workflow**  
> Last updated: 2026-11-27  
> Checked items reflect observed evidence, not planned work. Implementation, evaluation, and Git integration are tracked separately.

## 1. Project goal

Build a working, evaluated traffic intelligence system that detects, tracks, and counts vehicles, produces traffic analytics, and exposes results through a usable API and dashboard. Learn Computer Vision and Deep Learning while shipping real features, not by recreating existing libraries. Maintain an independently reusable `cv_core` foundation for future separate repositories, including AI Driver Monitoring.

## 2. Accelerated working method

**Project first. Learn just enough to make the next engineering decision. Ship small, verified increments.**

Target effort: 10% focused theory, 70% implementation and integration, 20% testing, debugging and evaluation. These are guidelines, not measured allocations.

- Start with a concrete problem, expected output, and acceptance criteria.
- For each new tool, cover what it does, why and when to use it, important parameters, limitations, and how to evaluate it. Avoid internal implementation details unless needed to debug or make a decision.
- Prefer OpenCV, NumPy, PyTorch, torchvision, and established detection/tracking libraries. Do not recreate existing algorithms or wrap individual library calls without added value.
- Use pretrained models and working baselines first. Train custom models only to meet a learning deliverable or address a measured gap.
- AI may generate scaffolding, routine implementation, tests, documentation, and debugging suggestions. The learner owns requirements, architectural decisions, code review, execution, and interpretation of results.
- Provide complete runnable examples when requested; do not enforce a hint-first exercise for routine code. Keep one active implementation task at a time, bundling related concepts into that task.
- Use one short conceptual check at meaningful checkpoints rather than quizzes after every API call. Do not skip core concepts such as tensor shapes, loss, gradients, IoU, evaluation, tracking identity, and physical calibration.
- Follow: **define → build → run → measure → fix → commit**. Learn deeper theory when an observed problem requires it.
- Introduce abstractions only for real reuse, a meaningful contract, or resource management. Avoid unnecessary notebooks, branches, services, and optimization.

## 3. Repository and engineering policy

| Branch | Purpose |
| --- | --- |
| `main` | Stable integrated traffic application |
| `foundation/cv-core` | Generic reusable CV, training, inference and geometry components only |
| `feature/*` | Scoped features from the appropriate base |
| `experiment/*` | Isolated experiments when necessary |
| `fix/*`, `refactor/*` | Targeted fixes and improvements |

Generic features merge into the foundation; integrate verified foundation changes into `main`. Traffic-specific classes, ROI definitions, counting rules, configuration and application logic belong on main-based branches. Never merge traffic-specific code back into the foundation. Keep future projects in separate repositories. Use Conventional Commits and inspect staged changes before committing. Do not force-push to resolve diverged branches.

- Python 3.12, `uv`, `pyproject.toml`, committed `uv.lock`, pytest and Ruff. Use `uv run` without manual environment activation where possible.
- Separate exploratory notebooks, reusable modules, and application code. Use type hints, short English docstrings and meaningful names; comments explain non-obvious decisions.
- Exclude `.venv/`, secrets, datasets, model checkpoints, generated videos and other large artifacts from Git.
- Record dataset provenance, license, privacy and permissions. Split related frames by video/camera/session to prevent leakage.
- Record seeds, configs, baseline metrics, representative failures and hardware. Keep validation and held-out test sets separate.
- Local hardware: RTX 3050 Laptop, 4 GB VRAM. Prefer compact models, small batches and appropriate image sizes; use Colab/Kaggle for heavier training if needed.
- Optimize after profiling. Do not assume preprocessing improves model accuracy; evaluate against an unmodified baseline.

## 4. Current verified status

| Field | Status |
| --- | --- |
| Current milestone | M1 implementation complete; exit/integration pending |
| Next learning milestone | M2 + M3 — practical PyTorch and vehicle classification |
| Last confirmed working branch | `foundation/cv-core` |
| Last observed local commit hash | `54f3ceb` — `chore: exclude datasets and video files from version control` (before attempted rebase; current hash unknown) |
| Git status | Push was rejected due to remote changes; rebase/push success and subsequent M1 integration not confirmed |
| Runtime | Ubuntu, Python 3.12.3; uv-managed environment |
| Latest full test suite | 19/19 passed in 0.14 s |
| Latest lint | `uv run ruff check src/ tests/` — passed |
| Latest formatting check | Not rerun in the latest M1 session |
| Next single task | Close M1: verify Git state, update this file, run final checks, commit/push and integrate foundation into main |

### M0 — Setup and repository foundation

**Technical setup operational; historical exit checks not fully verified.**

- [x] Repository, foundation branch, uv environment, package skeleton, Hatchling, pytest, Ruff and ignore rules established.
- [x] Package import/version test and development tooling demonstrated.
- [x] Environment rebuilt successfully after the mounted drive path changed.
- [ ] Fresh-clone README smoke test and final historical Git/exit-review verification (may be closed together with M1).

### M1 — Image and video processing

**Outcome:** reusable image/video components and demonstrated preprocessing operations.

- [x] Image representation, BGR/RGB/grayscale/HSV, brightness, contrast and clipping studied.
- [x] Histogram counting and benchmark; equalization and CLAHE studied and enhancement functions tested.
- [x] Kernels, filtering, edge detection, thresholding, morphology and contours covered in practical workflow; ROI result demonstrated.
- [x] Video read, resize, write and output metadata validation demonstrated on a 538-frame clip.
- [x] Reusable enhancement, streaming reader and composable preprocessing modules implemented and unit tested.
- [x] Full suite: 19 tests passed; source/test Ruff check passed.
- [x] Verify notebook-to-pipeline integration on the actual traffic clip, record visual failure cases and source/license before redistribution.
- [x] Complete short exit review, formatter check, Git verification and foundation integration into `main`.

The checked learning items indicate topics covered, not proof of independent mastery or exhaustive experimental validation.

#### Reusable components

| Module | Responsibility | Tests observed |
| --- | --- | --- |
| `cv_core.preprocessing.enhancement` | Brightness/contrast, histogram equalization, CLAHE | 11 |
| `cv_core.preprocessing.pipeline` | Sequential composition of frame transforms | 4 |
| `cv_core.video.reader` | Generator-based reading and resource release | 3 |
| `cv_core` | Package version smoke test | 1 |

#### Recorded benchmarks

| Experiment | Observed result |
| --- | --- |
| Histogram, Python loop | 350.9563 ms |
| Histogram, NumPy bincount | 2.8100 ms |
| Histogram, OpenCV | 1.1346 ms |
| Source video | 3840 × 2160, 25 FPS, 538 frames, 21.52 s |
| Output video | 1920 × 1080, metadata validation passed |
| Read/resize/write elapsed | 10.52 s |
| Read/resize/write throughput | 51.16 FPS |

Histogram timings were reported for the Full HD synthetic benchmark. Video throughput includes reading, resizing and writing; it is not detector/tracker throughput or measured live-stream latency. No model accuracy improvement from enhancement has been demonstrated.

#### Known gaps

- Enhancement parameter and dtype tests are not exhaustive; CLAHE settings and contrast edge cases need coverage when required.
- Camera/live-stream reliability, early generator termination and decoder errors need validation when live inputs are introduced.
- Video source redistribution/license verification, fresh-clone reproducibility, final formatting and Git integration remain open.
- No detector, tracker, classifier or calibrated speed results have been measured yet.

## 5. Remaining roadmap — deliverables over exercises

### Phase A — M2 + M3: Practical Deep Learning & Vehicle Classification

**Outcome:** a trained, evaluated small vehicle classifier and reusable training/inference foundations.

- [ ] Verify PyTorch installation, CUDA availability and memory; learn tensor shapes, dtype, devices, batching and normalization through actual images.
- [ ] Choose a permitted vehicle dataset; inspect labels and create leakage-safe splits.
- [ ] Use a compact pretrained torchvision backbone as the first practical baseline. Explain CNN feature maps, padding, stride, pooling, receptive fields and transfer learning in context; a tiny custom CNN is optional for comparison, not a prerequisite.
- [ ] Build Dataset/DataLoader and a transparent training/evaluation loop using PyTorch autograd, cross-entropy and a standard optimizer. Understand forward pass, backpropagation and gradient updates without manually recreating them.
- [ ] Train with a small batch; compare frozen features vs selective fine-tuning if useful. Diagnose overfitting using training/validation curves; use augmentation, regularization or early stopping as needed.
- [ ] Evaluate accuracy, per-class precision/recall/F1, confusion matrix and error examples; save config and weights outside Git, package inference and test label mapping.

**Exit:** reproducible classifier baseline, evaluation report and a runnable inference demo. The classifier is a learning deliverable, not an assumed dependency of YOLO. Generic training/inference utilities go to foundation; vehicle-specific labels and scripts go to main-based branches.

### Phase B — M4: Pretrained Object Detection

**Outcome:** first annotated traffic video with vehicle detections.

- [ ] Select a compact pretrained YOLO-family model; document model/version/license and supported classes.
- [ ] Run image and video inference on the existing traffic clip, using the reusable reader when beneficial; avoid unnecessary double resizing or enhancement.
- [ ] Understand bounding-box formats, IoU, confidence and NMS using actual predictions; use library implementations.
- [ ] Measure precision/recall, AP, mAP50 and mAP50-95 on labeled data; inspect misses, duplicates, occlusion and small vehicles.
- [ ] Benchmark inference and end-to-end throughput/latency separately, plus GPU memory; export annotated demo.

**Exit:** reproducible detector baseline, documented evaluation and working annotated video. Start tracking immediately after the baseline is usable; do not block the MVP on custom training.

### Phase C — M6 + M7: Tracking & Traffic Analytics (MVP)

**Outcome:** working vehicle tracking, directional counting and traffic-event export.

- [ ] Use an established tracker such as ByteTrack with the pretrained detector. Understand IDs, track lifecycle, association, occlusion and ID switches; study Kalman/Hungarian internals only as needed to diagnose behavior.
- [ ] Implement project-specific line/zone crossing, direction, anchor point and duplicate-prevention logic; unit-test edge cases.
- [ ] Configure ROI and counting lines per camera; support multiple lanes where required. Keep traffic-specific geometry/config in the application branch.
- [ ] Produce annotated video, time-windowed counts, flow rates, and JSON/CSV events. Add density/congestion proxies and stationary-vehicle events after counting is reliable; document definitions and limitations.
- [ ] Manually label short clips for count ground truth and tracking identities; evaluate count MAE/RMSE, false crossings, HOTA/IDF1/ID switches where labels support them. Inspect failures rather than assuming visual quality equals correctness.

**MVP exit:** one command processes a clip into annotated video and validated directional counts/events. This is the first complete traffic-specific vertical slice.

### Phase D — M10: System Integration & Usable Demo

**Outcome:** end-to-end traffic application that can be demonstrated to another engineer or user.

- [ ] Define minimal component diagram, configuration and event data contracts.
- [ ] Integrate ingestion, detection, tracking, counting and persistence; start with one camera/video and one processing job.
- [ ] Store events in PostgreSQL; expose health, processing jobs and event queries via FastAPI.
- [ ] Build minimal dashboard for counts, time windows and results; add structured logs, error handling and integration tests.
- [ ] Verify event consistency, duplicate prevention, and reproducible startup on a short clip.

**Exit:** usable application with tested end-to-end flow. Avoid distributed architecture and extra infrastructure until required.

### Phase E — M5: Custom Detector Training & Model Improvement

**Outcome:** measured custom training experiment against the pretrained baseline.

- [ ] Define classes/annotation policy, choose licensed data, audit missing boxes and class IDs, split by video/camera/session.
- [ ] Record pretrained baseline on validation data; choose resolution/batch to fit 4 GB VRAM or cloud resources.
- [ ] Fine-tune compact YOLO using the library training API; record configuration, seed and results.
- [ ] Compare targeted changes on validation data, evaluate the selected model on untouched test data, analyze per-class/condition failures and write a model card.
- [ ] Adopt custom weights only if they meet the measured accuracy/performance requirement; otherwise retain the pretrained model. Store weights outside Git.

**Exit:** reproducible training and evaluation report, even if custom weights are not selected. This milestone remains a learning deliverable but is removed from the MVP critical path.

### Phase F — M8: Calibrated Speed Estimation

**Outcome:** physically meaningful speed estimates on calibrated footage.

- [ ] Obtain ground-plane reference distances and independently measured speeds; explain why pixel displacement alone is insufficient.
- [ ] Use OpenCV homography/perspective mapping APIs, validate held-out reference points, convert tracked ground-contact points to world coordinates.
- [ ] Compute elapsed time using reliable timestamps; estimate and smooth speed and document uncertainty.
- [ ] Evaluate MAE/RMSE against independent measurements and record occlusion, camera-motion and perspective failures.

**Exit:** calibrated speed demo with reference-based evaluation. If calibration/reference data are missing, label the feature experimental or unavailable; never claim accurate physical speed from arbitrary clips. Do not block the core MVP on this external dependency.

### Phase G — M9: Road Segmentation

**Outcome:** evaluated road mask and assessment of its usefulness for traffic ROI.

- [ ] Understand semantic vs instance masks and encoder-decoder/U-Net concepts through a compact pretrained or library-based segmentation model.
- [ ] Select permitted labeled road data; use paired image/mask transforms and leakage-safe splits.
- [ ] Evaluate a baseline using Dice and mean IoU; fine-tune if needed within resource limits, inspect shadows, boundaries and weather failures.
- [ ] Compare automatic road masks against fixed ROI for the traffic application and integrate only if beneficial.

**Exit:** reproducible segmentation demo and evaluation. Not required for fixed-camera counting MVP; retain as a learning milestone.

### Phase H — M11: Optimization, Deployment & Portfolio Release

**Outcome:** reproducible, documented, deployable portfolio project.

- [ ] Profile stage latency, end-to-end FPS, and memory on target hardware; compare meaningful resolution/model/batch settings.
- [ ] Test ONNX export when deployment benefits; check output agreement/accuracy drift and performance before adoption.
- [ ] Create minimal Docker setup and CI for lint, tests and smoke integration. Validate fresh-clone setup, failure handling, license/privacy and secrets.
- [ ] Publish architecture, setup, measured metrics, limitations, annotated demo and reproducibility instructions; review foundation reuse and final Git state.

**Exit:** repeatable release/demo with measured behavior and known limitations. A first portfolio release may ship after Phase D plus the essential deployment checks; subsequent phases extend it rather than delay the MVP.

## 6. Evaluation rules

Explain each metric before use and report only measurements backed by real evaluation data.

| Area | Metrics / evidence |
| --- | --- |
| Classification | Accuracy, precision, recall, F1, confusion matrix |
| Detection | IoU, precision/recall, AP, mAP50, mAP50-95 |
| Tracking | HOTA, IDF1, ID switches on identity-labeled clips |
| Counting | MAE, RMSE, directional counts, false/double crossings |
| Speed | MAE/RMSE against physical reference, uncertainty |
| Segmentation | Dice, mean IoU |
| Performance | Throughput FPS, latency, GPU/CPU memory, hardware and workload |

## 7. Immediate next task and session tracking

Close M1 before starting new training work. From the repository root:

```bash
git status
git branch --show-current
git fetch origin
git log --oneline --decorate -5
uv run pytest -v
uv run ruff check src/ tests/
uv run ruff format --check src/ tests/
```

Review any divergence or formatting failure before committing; then stage the intended source/tests/notebooks and this tracker, commit, push, and integrate verified foundation updates into `main`. Do not mark integration complete until confirmed. Review the actual pipeline output on the clip and the short M1 conceptual checkpoint (CLAHE, streaming generators, optional preprocessing). Next implementation task: PyTorch CPU/CUDA smoke test and first vehicle-classifier dataset selection.

Update this compact checkpoint after each meaningful task or commit, rather than maintaining duplicate progress tables:

| Field | Value |
| --- | --- |
| Active task | M1 exit verification and integration |
| Last evidence | 19 passing tests; Ruff lint passed; 51.16 FPS read/resize/write benchmark |
| Decision | Use ready-made libraries and pretrained baselines; prioritize end-to-end delivery |
| Needs revision | Local vs global enhancement choice; generator memory/resource behavior; evidence-based preprocessing |
| Blockers | Final Git state, formatter, fresh-clone and pipeline demo verification; dataset license audit |
| Next task | M2 + M3 practical classifier setup after M1 exit |

## 8. Milestone exit checklist (reuse for each milestone)

- [ ] Working deliverable runs and has a reproducible command or demo.
- [ ] Acceptance tests and relevant metrics are recorded; limitations and representative failures are explicit.
- [ ] Learner can explain the core decisions in a short review.
- [ ] Branch boundary, lint/tests/formatting, documentation and commit/push are verified.
- [ ] Next single task is recorded.

> Maintenance rule: ship useful increments, update evidence as work finishes, and never mark planned work as completed. Prioritize a working MVP without sacrificing correctness, licensing, evaluation or independent engineering judgment.