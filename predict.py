from ultralytics import YOLO

# Load trained model
model = YOLO("weights/best (1).pt")

# Run inference on sample images
results = model.predict(
    source="sample_images",
    conf=0.25,
    save=True
)

print("Predictions saved to runs/detect/predict")