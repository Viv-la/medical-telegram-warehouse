from pathlib import Path
from ultralytics import YOLO

# Load pretrained YOLO model
model = YOLO("yolov8n.pt")

# Input and output folders
image_folder = Path("data/raw/images/CheMed123")
output_folder = Path("data/processed/yolo_results")

output_folder.mkdir(parents=True, exist_ok=True)

# Run detection on every image
for image in image_folder.glob("*.jpg"):
    print(f"Processing {image.name}...")

    model.predict(
        source=str(image),
        save=True,
        project=str(output_folder),
        name="detections",
        exist_ok=True
    )

print("YOLO detection completed.")