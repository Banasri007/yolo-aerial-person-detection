import os
import cv2

anno_dir = "annotations"
img_dir = "images"
out_dir = "labels"

os.makedirs(out_dir, exist_ok=True)

for file in os.listdir(anno_dir):
    if not file.endswith(".txt"):
        continue

    in_path = os.path.join(anno_dir, file)
    out_path = os.path.join(out_dir, file)

    with open(in_path) as f:
        lines = f.readlines()

    yolo_lines = []

    img_path = os.path.join(img_dir, file.replace(".txt",".jpg"))
    img = cv2.imread(img_path)
    if img is None:
        continue

    H, W = img.shape[:2]

    for line in lines:
        parts = line.strip().split(",")
        if len(parts) < 6:
            continue

        x, y, w, h = map(float, parts[:4])
        category = int(parts[5])

        # keep pedestrians + persons
        if category not in [1,2]:
            continue

        x_center = (x + w/2) / W
        y_center = (y + h/2) / H
        w_norm = w / W
        h_norm = h / H

        yolo_lines.append(
            f"0 {x_center} {y_center} {w_norm} {h_norm}\n"
        )

    with open(out_path,"w") as f:
        f.writelines(yolo_lines)

print("Conversion complete.")