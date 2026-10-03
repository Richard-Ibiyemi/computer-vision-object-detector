from pathlib import Path

from ultralytics import YOLO


model = YOLO("yolov8s-oiv7.pt")

image_folder = Path("assets/evaluation").resolve()
output_folder = Path("docs/test_results_new").resolve()

for threshold in [0.15, 0.4, 0.6]:
    model.predict(
        source=str(image_folder),
        conf=threshold,
        save=True,
        project=str(output_folder),
        name=f"conf_{threshold}",
        exist_ok=True,
    )