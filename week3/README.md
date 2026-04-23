# Week 3 - Image Segmentation

## Overview
Performed semantic segmentation using YOLOv8 segmentation model.

## Steps
- Extracted frames from video using FFmpeg
- Applied YOLOv8 segmentation (yolov8n-seg)
- Generated pixel-level masks
- Converted frames to video
- Added background music
- Compressed video for sharing

## Output
- Sample segmented frames
- Final video (compressed)

## Model Used
- yolov8n-seg (pretrained)

## Notes
Segmentation assigns a class to each pixel, unlike detection which only 
provides bounding boxes.

