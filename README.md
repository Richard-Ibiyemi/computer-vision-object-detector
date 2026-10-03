# Computer Vision Object Detector

A Python application that detects objects in images and a live webcam feed using a pretrained YOLOv8 small model. It displays bounding boxes, class labels, confidence scores and a processing-FPS estimate.

I built this project to practise integrating a computer vision model with OpenCV and evaluating its behaviour under different conditions. The project uses pretrained weights; I did not train a model from scratch.

## Demonstration

[Watch the webcam demonstration](docs/webcam_demo.mp4)

The demonstration shows a bottle being moved in front of the webcam. Detection boxes appear at different positions, with occasional missed detections during movement.

## Tools and model

- Python
- Ultralytics YOLO, using `yolov8s-oiv7.pt`
- OpenCV for webcam capture, display and saving screenshots
- PyTorch as the model inference backend

## Features

- Object detection on a test image
- Live webcam detection with labels and confidence scores
- Configurable confidence threshold and inference image size
- Processing-FPS overlay
- Saving annotated webcam screenshots
- Evaluation across lighting, distance and partial occlusion conditions

## Setup on Windows

Download this repository and open its folder in VS Code. Run these commands in the terminal from the project folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install ultralytics opencv-python
```

These commands use the virtual environment directly, so activation is optional. The pretrained model weights are downloaded on first use when needed; an internet connection is required for setup and the initial download.

## Run the application

### Webcam

```powershell
.\.venv\Scripts\python.exe detect_webcam.py
```

With the webcam window selected:

- Press **S** to save an annotated screenshot.
- Press **Q** to close the application.

The demonstration configuration in `detect_webcam.py` is:

```python
MODEL_PATH = "yolov8s-oiv7.pt"
CAMERA_INDEX = 0
CONFIDENCE = 0.4
IMAGE_SIZE = 640
```

Saved screenshots go to the folder specified by `OUTPUT_DIR` in the script. The plugged-in test used `outputs/webcam_plugged`.

### Test image

Place an image at `assets/test.jpg`, then run:

```powershell
.\.venv\Scripts\python.exe detect_image.py
```

This script uses the small model at confidence 0.4 and saves the annotated image in `outputs/image_test/`. The terminal reports the output location.

### Evaluation images

Place the 12 evaluation photographs in `assets/evaluation/`, then run:

```powershell
.\.venv\Scripts\python.exe evaluation_images.py
```

The script uses the small model and runs thresholds 0.15, 0.4 and 0.6. Annotated results are saved in `docs/test_results_new/conf_0.15/`, `conf_0.4/` and `conf_0.6/`. These results are included by the current `.gitignore` because they are inside `docs/`.

## Evaluation results

### Photograph tests

I tested 12 photographs: a hand, a bottle and prescription glasses, each under normal, dim, partially obscured and distant conditions. Each image was evaluated at three confidence thresholds.

| Confidence threshold | Hand detected | Bottle detected | Glasses detected | Total |
|---|---:|---:|---:|---:|
| 0.15 | 3/4 | 4/4 | 2/4 | 9/12 |
| 0.4 | 1/4 | 4/4 | 2/4 | 7/12 |
| 0.6 | 0/4 | 1/4 | 2/4 | 3/12 |

Lowering the threshold retained more target detections but also introduced duplicate boxes and incorrect labels. These are visual detection counts on a small test set, not formal accuracy or mAP measurements.

### Webcam tests

Each mean below uses five readings of the displayed processing-FPS estimate. Confidence was 0.4 for every run.

| Laptop power | Inference image size | Mean processing FPS | Bottle detected in saved frames |
|---|---:|---:|---:|
| Battery | 640 | 9.06 | 5/5 |
| Battery | 320 | 9.06 | 5/5 |
| Plugged in | 640 | 15.78 | 5/5 |
| Plugged in | 320 | 43.12 | 0/5 |

In the plugged-in scene, size 320 produced a higher processing rate but missed the bottle at the selected threshold. I chose 640 and confidence 0.4 for the demonstration. The camera angle differed between battery and plugged-in tests, so the comparison does not isolate the effect of power alone.

Processing FPS is a smoothed estimate from the application, rather than the screen recording's frame rate or a measurement of end-to-end latency.

See [testing.md](testing.md) for detailed observations, limitations and the video demonstration notes.

## Limitations and future work

- Detection can disappear as an object moves or changes pose.
- Small, distant and partially hidden targets can be missed.
- Confidence scores do not represent measured accuracy percentages.
- The test set is small and lacks ground-truth bounding-box annotations.
- The application performs frame-by-frame detection without persistent object IDs.

Future work could include a larger annotated test set, formal precision/recall evaluation and object tracking across frames.

## Repository contents

| File or folder | Purpose |
|---|---|
| `detect_image.py` | Single-image detection |
| `detect_webcam.py` | Live webcam application |
| `evaluation_images.py` | Evaluation-image processing |
| `assets/` | Input images |
| `docs/webcam_demo.mp4` | Recorded demonstration |
| `testing.md` | Detailed testing notes |
| `.gitignore` | Excludes local environments, weights and generated outputs |

The `.venv/`, `outputs/` and `runs/` folders and downloaded `.pt` weights are excluded from Git. Selected demonstration material is stored in `docs/`.
