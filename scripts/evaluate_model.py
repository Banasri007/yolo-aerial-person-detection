from ultralytics import YOLO

model = YOLO("best (1).pt")

metrics = model.val(
    data="eval.yaml",
    imgsz=640,
    conf=0.25
)

print(metrics)
