from pathlib import Path

from ultralytics import YOLO


def main():
    image_path = Path("assets/test.jpg")

    if not image_path.is_file():
        raise FileNotFoundError(
            "Add a photograph at assets/test.jpg first."
        )

    # Download/load the pretrained detector.
    model = YOLO("yolov8s-oiv7.pt")

    # Run detection on the image.
    results = model.predict(
        source=str(image_path),
        conf=0.4,
        save=True,
        project=str(Path("outputs").resolve()),
        name="image_test",
        exist_ok=True,
    )

    # Print each detected object's name and confidence.
    for box in results[0].boxes:
        class_id = int(box.cls.item())
        confidence = float(box.conf.item())
        label = model.names[class_id]

        print(f"{label}: {confidence:.2f}")


if __name__ == "__main__":
    main()