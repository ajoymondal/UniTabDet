from ultralytics import YOLO

# Load a model
model = YOLO("yolo11x.pt")
# Train the model
train_results = model.train(
    data="data.yaml",  
    epochs=100,  
    imgsz=1280,  
    batch=4,
    iou=0.95,
    device="0,1,2,3",  
)

