# Week 2 - YOLOv8 Object Detection

## Overview
In this task, object detection was performed using the YOLOv8 model from 
the Ultralytics library. The model detects objects in an image and draws 
bounding boxes with class labels and confidence scores.

---

## Model Used
- YOLOv8 (Ultralytics)
- Pretrained weights: `yolov8n.pt`

---

## Implementation

### Code (detect.py)
```python
from ultralytics import YOLO

# Load pretrained model
model = YOLO("yolov8n.pt")

# Run detection
results = model("bus.jpg", save=True)

print("Detection completed. Output saved in runs/detect/")

OUTPUT -

https://drive.google.com/file/d/1EV7zAvnA_AKTTVdEBQ1YA5ZU2WPJtn25/view?usp=drive_link


