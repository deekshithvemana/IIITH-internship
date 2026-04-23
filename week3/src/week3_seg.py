from ultralytics import YOLO

# Load segmentation model (IMPORTANT)
model = YOLO("yolov8n-seg.pt")

# Run segmentation on all frames
model("frames/", save=True)

print("Segmentation done!")


