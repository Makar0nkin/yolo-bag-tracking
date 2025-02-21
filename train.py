from ultralytics import YOLO

model = YOLO("weights/yolo11n.pt")

model.train(
    data='dataset/data.yaml', 
    epochs=10,
    imgsz=500,
)

metrics = model.val()