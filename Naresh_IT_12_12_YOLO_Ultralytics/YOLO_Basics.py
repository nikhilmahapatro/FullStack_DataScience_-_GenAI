from ultralytics import YOLO

# load a pretrained YOLOv8n model
model = YOLO("yolov8n.pt", "v8")


# predict on an image
detection_output = model.predict(source=r"C:\Users\nikhi\PycharmProjects\NARESH_IT\12_NARESH_IT_DEEP_LEARNING\Naresh_IT_12_12_YOLO_Ultralytics\Img.webp", conf=0.25, save=True)

# Display tensor array
print(detection_output)

# Display numpy array
print(detection_output[0].numpy())
