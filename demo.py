import cv2
weight_path= "./src/weights/best.onnx"
model = cv2.dnn.readNetFromONNX(onnxFile=weight_path)
print('1')
from ultralytics import YOLO
print('2')
print(model)
results = model.predict(source="12.jpg")[0]
print(results)