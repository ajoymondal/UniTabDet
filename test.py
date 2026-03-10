from ultralytics import YOLO

# Load a model
model = YOLO("runs/detect/train/weights/best.pt") 
results = model.predict(source="datasets/images/test", save_txt=True, save_conf=True)

