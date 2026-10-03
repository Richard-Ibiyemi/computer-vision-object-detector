from pathlib import Path
from time import perf_counter, time_ns

import cv2
from ultralytics import YOLO


MODEL_PATH = "yolov8s-oiv7.pt"
CAMERA_INDEX = 0
CONFIDENCE = 0.4
IMAGE_SIZE = 640
OUTPUT_DIR = Path("outputs/webcam_plugged")


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    model = YOLO(MODEL_PATH)
    camera = cv2.VideoCapture(CAMERA_INDEX)

    if not camera.isOpened():
        camera.release()
        raise RuntimeError(
            "Could not open the webcam. Check camera permissions "
            "and close other apps using it."
        )

    print("Click the camera window.")
    print("Press S to save a screenshot. Press Q to quit.")

    smoothed_fps = None

    try:
        while True:
            start = perf_counter()

            # Read one image from the webcam.
            success, frame = camera.read()

            if not success:
                print("Could not read a camera frame.")
                break

            # Detect objects in this frame.
            result = model.predict(
                source=frame,
                conf=CONFIDENCE,
                imgsz=IMAGE_SIZE,
                verbose=False,
            )[0]

            # Draw the model's boxes, labels and confidence scores.
            annotated_frame = result.plot()

            # Approximate capture + detection + annotation throughput.
            elapsed = perf_counter() - start
            current_fps = 1.0 / max(elapsed, 0.000001)

            if smoothed_fps is None:
                smoothed_fps = current_fps
            else:
                smoothed_fps = (
                    0.9 * smoothed_fps + 0.1 * current_fps
                )

            cv2.putText(
                annotated_frame,
                f"Processing FPS: {smoothed_fps:.1f}",
                (20, 35),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 255, 0),
                2,
            )

            cv2.imshow("Object Detector", annotated_frame)

            key = cv2.waitKey(1) & 0xFF

            if key == ord("s"):
                save_path = OUTPUT_DIR / f"detection_{time_ns()}.jpg"
                saved = cv2.imwrite(str(save_path), annotated_frame)

                if saved:
                    print(f"Saved: {save_path}")
                else:
                    print("Could not save the screenshot.")

            elif key == ord("q"):
                break

    finally:
        camera.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()