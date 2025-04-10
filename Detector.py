import torch
import cv2
import time
import os

# YOLOv5 model load karo
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model.conf = 0.05  # Confidence threshold

# Fishy keywords list
fishy_keywords = ['cell phone', 'mobile phone', 'laptop', 'headphones', 'earphone']

def detect_from_webcam():
    # Webcam activate karo
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("🚫 Can't open Webcam ")
        return

    print("🎥 Live detection has been started. Press q to exit.")

    frame_count = 0
    os.makedirs("saved_frames", exist_ok=True)  # Folder bana lo if not exists

    while True:
        ret, frame = cap.read()
        if not ret:
            print("⚠️ Frame couldn't be able to get ready")
            break

        # YOLO se detect karo
        results = model(frame)
        df = results.pandas().xyxy[0]

        fishy_found = False

        # Sabhi detected objects par loop
        for _, row in df.iterrows():
            label = row['name']
            conf = row['confidence']
            if label in fishy_keywords:
                fishy_found = True
                x1, y1, x2, y2 = map(int, [row['xmin'], row['ymin'], row['xmax'], row['ymax']])
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
                # Show custom label
                text = f"Fishy Object ({conf:.2f})"
                cv2.putText(frame, text, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

        # Frame save karo agar koi fishy object mila
        if fishy_found:
            frame_filename = f"saved_frames/frame_{frame_count}.jpg"
            cv2.imwrite(frame_filename, frame)
            print(f"⚠️ Fishy Object Detected: Frame has been saved {frame_filename}")
            frame_count += 1

        # Frame display karo
        try:
            cv2.imshow("📸 Fishy Object Detector", frame)
        except Exception as e:
            print(f"⚠️ imshow error: {e}")
            break

        # 'q' dabao to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    print("🛑 Detection turned off")

if __name__ == "__main__":
    detect_from_webcam()
