from flask import Flask, render_template, request, jsonify, redirect, url_for
import os
import cv2
import numpy as np
from werkzeug.utils import secure_filename
import subprocess

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'dataset'
app.config['MAX_CONTENT_LENGTH'] = 20 * 1024 * 1024  # 20MB max

# Ensure dataset folder exists
os.makedirs('dataset', exist_ok=True)

@app.route('/')
def index():
    return render_template('admin.html')

@app.route('/upload', methods=['POST'])
def upload_face():
    try:
        name = request.form.get('name')
        user_id = request.form.get('user_id')
        files = request.files.getlist('images')
        
        if not name or not user_id or not files:
            return jsonify({'error': 'Missing required fields'}), 400
        
        # Count existing images for this user
        existing_count = 0
        if os.path.exists(app.config['UPLOAD_FOLDER']):
            for filename in os.listdir(app.config['UPLOAD_FOLDER']):
                if filename.startswith(f"User.{user_id}."):
                    existing_count += 1
        
        uploaded_count = 0
        for idx, file in enumerate(files):
            if file and file.filename:
                # Save with format: User.ID.ImageNumber.jpg
                img_number = existing_count + idx + 1
                filename = f"User.{user_id}.{img_number}.jpg"
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                uploaded_count += 1
        
        return jsonify({
            'success': True,
            'message': f'Uploaded {uploaded_count} images for {name}',
            'user_id': user_id,
            'name': name
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/train', methods=['POST'])
def train_model():
    try:
        # Run training script
        result = subprocess.run(['python3', 'train.py'], 
                                capture_output=True, 
                                text=True, 
                                cwd='/home/azureuser/face-attendance')
        
        if result.returncode == 0:
            # Restart the main app to load new model
            subprocess.run(['sudo', 'systemctl', 'restart', 'face-attendance'])
            
            return jsonify({
                'success': True,
                'message': 'Training completed! Model updated successfully.',
                'output': result.stdout
            })
        else:
            return jsonify({
                'error': 'Training failed',
                'output': result.stderr
            }), 500
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/users')
def list_users():
    try:
        users = {}
        if os.path.exists('dataset'):
            for filename in os.listdir('dataset'):
                if filename.endswith('.jpg') or filename.endswith('.png'):
                    parts = filename.split('.')
                    if len(parts) >= 2:
                        user_id = parts[1]
                        if user_id not in users:
                            users[user_id] = {'count': 0, 'images': []}
                        users[user_id]['count'] += 1
                        users[user_id]['images'].append(filename)
        
        return jsonify({'users': users})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/delete-user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    try:
        deleted_count = 0
        if os.path.exists('dataset'):
            for filename in os.listdir('dataset'):
                if filename.startswith(f"User.{user_id}."):
                    os.remove(os.path.join('dataset', filename))
                    deleted_count += 1
        
        return jsonify({
            'success': True,
            'message': f'Deleted {deleted_count} images for User {user_id}'
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
