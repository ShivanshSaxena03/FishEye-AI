# FishEye-AI
**AquaSentinel** is a real-time object detection tool using YOLOv5 and OpenCV to detect "fishy" items like phones, laptops, and headphones via webcam. Suspicious objects are highlighted and frames are auto-saved for review. Ideal for monitoring restricted zones or exam halls.

🎣 AquaSentinel – Fishy Object Detection System
AquaSentinel is a real-time fishy object detection system powered by YOLOv5 and OpenCV. It detects and flags suspicious or "fishy" objects such as mobile phones, laptops, and headphones through a webcam feed.

🚀 Features
Live webcam object detection using YOLOv5 (yolov5s model).

Alerts and highlights fishy objects (e.g., mobile phone, laptop, headphones).

Automatically saves frames containing such objects.

Confidence threshold control for accurate results.

🧠 Fishy Objects
These objects are considered suspicious:

Mobile Phone / Cell Phone

Laptop

Headphones

Earphones

🛠️ Tech Stack
Python 🐍

YOLOv5 (via PyTorch Hub)

OpenCV

📦 Requirements
torch

opencv-python

Internet connection (for initial YOLOv5 model download)
HOW TO RUN:
pip install torch opencv-python
python fishy_detector.py
