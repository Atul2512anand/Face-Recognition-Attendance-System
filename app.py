from flask import Flask, render_template, request, jsonify, Response
from flask_cors import CORS
import cv2
import numpy as np
import base64
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Load face recognizer
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainer.yml')
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Attendance log
attendance_log = []

# User database
user_database = {
    1: {"name": "User 1", "id": "101"},
    2: {"name": "User 2", "id": "102"},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recognize', methods=['POST'])
def recognize_face():
    try:
        data = request.json
        image_data = data['image'].split(',')[1]
        
        nparr = np.frombuffer(base64.b64decode(image_data), np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        results = []
        for (x, y, w, h) in faces:
            face_img = gray[y:y+h, x:x+w]
            user_id, confidence = recognizer.predict(face_img)
            
            if confidence < 100:
                user_info = user_database.get(user_id, {"name": f"User {user_id}", "id": str(user_id)})
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                attendance_record = {
                    "name": user_info["name"],
                    "id": user_info["id"],
                    "timestamp": timestamp,
                    "confidence": round(100 - confidence, 2)
                }
                
                if not any(log["id"] == user_info["id"] for log in attendance_log[-10:]):
                    attendance_log.append(attendance_record)
                
                results.append({
                    "x": int(x), "y": int(y), "w": int(w), "h": int(h),
                    "name": user_info["name"],
                    "id": user_info["id"],
                    "confidence": round(100 - confidence, 2),
                    "recognized": True
                })
            else:
                results.append({
                    "x": int(x), "y": int(y), "w": int(w), "h": int(h),
                    "name": "Unknown",
                    "recognized": False
                })
        
        return jsonify({"faces": results, "count": len(faces)})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/attendance', methods=['GET'])
def get_attendance():
    return jsonify({"attendance": attendance_log})

@app.route('/attendance/export', methods=['GET'])
def export_attendance():
    import csv
    from io import StringIO
    
    output = StringIO()
    writer = csv.DictWriter(output, fieldnames=["name", "id", "timestamp", "confidence"])
    writer.writeheader()
    writer.writerows(attendance_log)
    
    return Response(
        output.getvalue(),
        mimetype="text/csv",
        headers={"Content-disposition": "attachment; filename=attendance.csv"}
    )

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
