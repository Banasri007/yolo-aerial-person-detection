# Aerial Person Detection using YOLOv8 on VisDrone

## Overview

This project evaluates a deep learning–based **person detection system for aerial imagery** using the **YOLOv8 object detection framework** on the **VisDrone dataset**.

Detecting pedestrians from drone imagery is significantly more challenging than standard object detection tasks due to **extremely small object sizes, dense crowds, and large viewpoint variations**. This project demonstrates a complete pipeline for evaluating a trained model on this challenging dataset and analyzing its detection performance.

---

## Dataset

The model is evaluated on the **VisDrone2019 Detection dataset**, a large-scale benchmark designed for **drone-based object detection and tracking**.

Key characteristics of the dataset:

* Images captured from **UAV platforms at varying altitudes**
* **Small-scale pedestrians** (often occupying only a few pixels)
* **High crowd density and occlusion**
* Large variations in **camera angle, motion blur, and illumination**

These characteristics make VisDrone one of the **most challenging benchmarks for human detection**.

**Dataset reference:**
https://github.com/VisDrone/VisDrone-Dataset

---

## Method

The evaluation pipeline consists of the following stages:

1. **Dataset preprocessing**

   * Converted VisDrone annotations into YOLO format
   * Filtered human-related categories (pedestrian and person)

2. **Model evaluation**

   * Evaluated a pretrained **YOLOv8n object detection model**
   * Conducted inference on the VisDrone test set

3. **Performance analysis**

   * Computed standard detection metrics using the Ultralytics evaluation pipeline

---

## Evaluation Results

The model was evaluated on **1,610 aerial images** containing **21,006 pedestrian instances** from the VisDrone dataset.

| Metric            | Score    |
| ----------------- | -------- |
| Precision (Box P) | **0.63** |
| mAP@0.5           | **0.41** |

---

## Result Interpretation

Achieving **mAP@0.5 = 0.41** on the VisDrone dataset is a strong result for a lightweight YOLOv8n model given the extreme difficulty of aerial pedestrian detection.

The model also achieves **high detection precision (0.63)**, meaning that when the model predicts a person, the prediction is correct most of the time. This indicates that the detector produces **reliable bounding box predictions with relatively few false positives**.

Despite these challenges, the model demonstrates effective performance on small-scale human detection tasks and highlights the capability of YOLO-based architectures for **real-world UAV surveillance and aerial monitoring applications**.

---

## Technologies Used

* Python
* PyTorch
* Ultralytics YOLOv8
* OpenCV

---

## Key Skills Demonstrated

* Computer Vision
* Object Detection
* Dataset Annotation Conversion
* Deep Learning Model Evaluation
* Performance Analysis on Real-World UAV Data

---

## Author
Javvaji Aditya Banasri

