# Aerial Human Detection using YOLOv8

This project implements a YOLOv8-based object detection model for detecting humans in aerial drone imagery.

The model was trained on the **VisDrone 2019 Detection Dataset** and optimized for detecting small-scale human targets in **1920×1080 aerial images captured from ~35m drone altitude**.

## Dataset

VisDrone 2019 Detection Dataset  
https://github.com/VisDrone/VisDrone-Dataset

Only the **person class** was used for training.

## Model

Architecture: YOLOv8n  
Framework: Ultralytics YOLO  
Training Platform: Kaggle

Best model weights are stored in:
weights/best(1).pt


## Installation

```bash
pip install -r requirements.txt


---

# 3. requirements.txt

Create `requirements.txt`



---

# 4. train.py

Create `train.py`

```python
from ultralytics import YOLO

# Load pretrained YOLOv8n model
model = YOLO("yolov8n.pt")

# Train on VisDrone dataset
model.train(
    data="visdrone.yaml",
    epochs=50,
    imgsz=640,
    batch=16
)

