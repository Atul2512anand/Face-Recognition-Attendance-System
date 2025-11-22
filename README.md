# 🎯 Face Recognition Attendance System

A real-time, cloud-hosted face recognition attendance system built with OpenCV and Flask. Features live camera integration, automated attendance logging, and an admin panel for managing the face database.

[![Python](https://img.shields.io/badge/Python-3.10-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.1.2-green.svg)](https://flask.palletsprojects.com/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.12.0-red.svg)](https://opencv.org/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## 📸 Screenshots

### Main Attendance System
Real-time face detection with automatic attendance marking and confidence scores.

### Admin Panel
Upload face images, train the model, and manage user database with an intuitive interface.

---

## ✨ Key Features

- 🎥 **Live Face Recognition** - Real-time camera feed with instant face detection and identification
- 👥 **User Management** - Easy-to-use admin panel for adding/removing users
- 📊 **Attendance Tracking** - Automatic logging with timestamps and confidence scores
- 💾 **Export Data** - Download attendance records in CSV format
- 🎨 **Modern UI** - Beautiful gradient design with responsive layout
- 🔄 **Easy Training** - One-click model retraining with new face data
- ☁️ **Cloud Ready** - Deployed on Azure VM for 24/7 availability
- 🔒 **Secure** - OpenCV-based local processing, no external APIs required

---

## 🌐 Live Demo

**🔗 Main Attendance System:** `http://57.158.24.17`
- Mark attendance with live camera
- View real-time attendance log
- Export attendance to CSV

**⚙️ Admin Panel:** `http://57.158.24.17:8080`
- Upload face images for new users
- Train recognition model
- Manage user database

> **Note:** Camera access requires Chrome with special settings (see setup below)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Webcam/Camera
- Modern web browser (Chrome recommended)

### Installation

1. **Clone the repository**
git clone https://github.com/YOUR_USERNAME/face-attendance.git
cd face-attendance

text

2. **Install dependencies**
pip install -r requirements.txt

text

3. **Run the applications**

**Main App (Port 5000):**
python3 app.py

text

**Admin Panel (Port 5001):**
python3 admin.py

text

4. **Access the system**
- Main App: http://localhost:5000
- Admin Panel: http://localhost:5001

---

## 🎓 How to Use

### 📹 Marking Attendance

1. **Open the main app** at `http://57.158.24.17` (or `http://localhost:5000` for local)

2. **Enable camera access** (first-time setup):
   - Open Chrome
   - Go to: `chrome://flags/#unsafely-treat-insecure-origin-as-secure`
   - Add: `http://57.158.24.17` (or your server IP)
   - Click **"Enable"**
   - **Restart Chrome**

3. **Start the camera**:
   - Click the **"Start Camera"** button
   - Allow camera permissions when prompted
   - Your camera feed will appear

4. **Begin recognition**:
   - Click **"Start Recognition"**
   - System will automatically detect and recognize faces
   - Attendance is logged in real-time on the right panel

5. **Export data**:
   - Click **"Export CSV"** to download attendance records

### 👤 Adding New Users (Admin Panel)

1. **Open admin panel** at `http://57.158.24.17:8080` (or `http://localhost:5001` for local)

2. **Navigate to "Add New Person" section**

3. **Enter user details**:
   - **Person Name**: Enter full name (e.g., "John Doe")
   - **User ID**: Enter a unique number (e.g., 3, 4, 5...)
   - Each person must have a different User ID

4. **Upload face images**:
   - Click the upload area
   - Select **15-20 images** of the person
   - **Tips for best results**:
     - Use different angles (front, left, right)
     - Include different lighting conditions
     - Vary expressions (neutral, smile, etc.)
     - Ensure face is clear (no sunglasses, masks)
     - Use high-quality images (not blurry)

5. **Upload the images**:
   - Click **"Upload Images"**
   - Wait for confirmation message

6. **Train the model**:
   - Scroll to **"Train Recognition Model"** section
   - Click **"Train Model with New Data"**
   - Wait 10-30 seconds for training to complete
   - You'll see a success message when done

7. **Update user database** (optional):
   - Edit `app.py` file
   - Find the `user_database` section (around line 18)
   - Add the new user:
user_database = {
1: {"name": "User 1", "id": "101"},
2: {"name": "User 2", "id": "102"},
3: {"name": "John Doe", "id": "103"}, # New user
}

text
- Restart the main app: `sudo systemctl restart face-attendance`

8. **Test recognition**:
- Go back to main app
- Start camera and recognition
- The new person should now be recognized!

---

## 🔧 Configuration

### Camera Access Setup (Important!)

Modern browsers require HTTPS for camera access. For HTTP testing:

**Chrome:**
1. Open: `chrome://flags/#unsafely-treat-insecure-origin-as-secure`
2. Add your server URL (e.g., `http://57.158.24.17`)
3. Enable the flag
4. Restart Chrome

**Firefox:**
1. Go to `about:config`
2. Search for `media.devices.insecure.enabled`
3. Set to `true`

**For Production:** Set up HTTPS with Let's Encrypt SSL certificate.

### Updating User Database

Edit `app.py` to match uploaded users:

user_database = {
1: {"name": "Atul Anand", "id": "101"},
2: {"name": "John Doe", "id": "102"},
3: {"name": "Jane Smith", "id": "103"},
# Add more users as needed
}

text

### Adjusting Recognition Sensitivity

In `app.py`, line ~55, adjust the confidence threshold:

if confidence < 100: # Lower = stricter matching
# Face recognized

text

- **Lower value (e.g., 70)**: More strict, fewer false positives
- **Higher value (e.g., 120)**: More lenient, may have false positives

---

## 📁 Project Structure

face-attendance/
├── app.py # Main Flask app (attendance system)
├── admin.py # Admin panel Flask app
├── train.py # Model training script
├── recognize.py # Standalone recognition script
├── trainer.yml # Trained LBPH model
├── haarcascade_frontalface_default.xml # Haar Cascade face detector
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore rules
├── README.md # This file
├── templates/
│ ├── index.html # Main app UI
│ └── admin.html # Admin panel UI
└── dataset/ # Face images (User.ID.Number.jpg)
├── User.1.1.jpg
├── User.1.2.jpg
└── ...

text

---

## ☁️ Deployment on Azure

### Current Deployment

The system is deployed on Azure VM with:
- **Main App**: Running on port 80 (http://57.158.24.17)
- **Admin Panel**: Running on port 8080 (http://57.158.24.17:8080)
- **Auto-restart**: Services restart automatically on reboot
- **24/7 Availability**: Runs continuously on cloud infrastructure

### Deploying Your Own Instance

1. **Create Azure VM** (Ubuntu 22.04)

2. **Install dependencies**:
sudo apt update && sudo apt upgrade -y
sudo apt install -y python3-pip python3-venv python3-opencv libopencv-dev nginx
pip3 install -r requirements.txt

text

3. **Create systemd services**:

**Main App:**
sudo tee /etc/systemd/system/face-attendance.service > /dev/null <<'EOF'
[Unit]
Description=Face Attendance Flask App
After=network.target

[Service]
User=azureuser
WorkingDirectory=/home/azureuser/face-attendance
Environment="PATH=/home/azureuser/.local/bin:/usr/bin"
ExecStart=/home/azureuser/.local/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 app:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

text

**Admin Panel:**
sudo tee /etc/systemd/system/face-admin.service > /dev/null <<'EOF'
[Unit]
Description=Face Admin Panel
After=network.target

[Service]
User=azureuser
WorkingDirectory=/home/azureuser/face-attendance
Environment="PATH=/home/azureuser/.local/bin:/usr/bin"
ExecStart=/home/azureuser/.local/bin/gunicorn --workers 2 --bind 0.0.0.0:5001 admin:app
Restart=always

[Install]
WantedBy=multi-user.target
EOF

text

4. **Configure Nginx**:
sudo tee /etc/nginx/sites-available/face-attendance > /dev/null <<'EOF'
server {
listen 80;
server_name _;
location / {
proxy_pass http://127.0.0.1:5000;
proxy_set_header Host $host;
proxy_set_header X-Real-IP $remote_addr;
}
}
EOF

sudo ln -s /etc/nginx/sites-available/face-attendance /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl restart nginx

text

5. **Enable and start services**:
sudo systemctl enable face-attendance face-admin
sudo systemctl start face-attendance face-admin

text

6. **Open firewall ports** in Azure Portal:
   - Port 80 (HTTP)
   - Port 8080 (Admin Panel)

---

## 🐛 Troubleshooting

### Camera Not Working

**Problem:** "Cannot read properties of undefined (reading 'getUserMedia')"

**Solutions:**
1. ✅ Enable Chrome insecure origins flag (see Configuration section)
2. ✅ Check browser camera permissions (Settings → Privacy → Camera)
3. ✅ Try using HTTPS instead of HTTP
4. ✅ Test with different browser (Chrome recommended)

### Face Not Recognized

**Problem:** System shows "Unknown" for known person

**Solutions:**
1. ✅ Upload more training images (20+ recommended)
2. ✅ Use varied images (different angles, lighting)
3. ✅ Ensure images are clear and high quality
4. ✅ Retrain the model after adding images
5. ✅ Lower confidence threshold in `app.py`
6. ✅ Check if User ID matches in database

### Service Not Starting

**Check logs:**
sudo journalctl -u face-attendance -n 50
sudo journalctl -u face-admin -n 50

text

**Restart services:**
sudo systemctl restart face-attendance
sudo systemctl restart face-admin

text

### Training Failed

**Common causes:**
- Not enough images (need minimum 10 per user)
- Images don't contain clear faces
- Dataset folder doesn't exist

**Fix:**
mkdir -p dataset

Upload images via admin panel
Ensure images follow naming: User.ID.Number.jpg
text

---

## 🛠️ Technologies Used

| Category | Technology |
|----------|-----------|
| **Backend** | Flask 3.1.2, Python 3.10 |
| **Computer Vision** | OpenCV 4.12.0 |
| **Face Recognition** | LBPH (Local Binary Pattern Histogram) |
| **Face Detection** | Haar Cascade Classifier |
| **Frontend** | HTML5, CSS3, Vanilla JavaScript |
| **Deployment** | Gunicorn, Nginx, Systemd |
| **Cloud Platform** | Microsoft Azure (Ubuntu 22.04) |
| **Data Processing** | NumPy 2.2.6, Pillow 12.0.0 |

---

## 📊 How It Works

1. **Face Detection**: Haar Cascade detects faces in camera feed
2. **Feature Extraction**: LBPH algorithm extracts facial features
3. **Recognition**: Compares features with trained model (trainer.yml)
4. **Confidence Score**: Calculates similarity percentage
5. **Attendance Logging**: Records timestamp and user details
6. **Database**: Stores in-memory (can be extended to SQL database)

---

## 🤝 Contributing

Contributions are welcome! Here's how:

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/AmazingFeature`
3. Commit your changes: `git commit -m 'Add some AmazingFeature'`
4. Push to the branch: `git push origin feature/AmazingFeature`
5. Open a Pull Request

**Areas for contribution:**
- Database integration (PostgreSQL/MySQL)
- HTTPS/SSL configuration
- Mobile app integration
- Advanced face recognition algorithms
- Multi-camera support
- Email/SMS notifications

---

## 📝 Future Enhancements

- [ ] Database integration for permanent storage
- [ ] User authentication and roles
- [ ] Email notifications for attendance
- [ ] Advanced analytics and reports
- [ ] Mobile application
- [ ] Multi-camera support
- [ ] Attendance scheduling
- [ ] HTTPS/SSL by default

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Atul Anand**

- GitHub: [@atul2512anand](https://github.com/atul2512anand)
- LinkedIn: [Atul Anand](https://linkedin.com/in/yourprofile)
- Email: atulanandit@example.com

---

## 🙏 Acknowledgments

- OpenCV team for computer vision capabilities
- Flask community for the lightweight web framework
- Azure for reliable cloud infrastructure
- All contributors and users of this project

---

## 📞 Support

Having issues? Here's how to get help:

1. 📖 Check the [Troubleshooting](#-troubleshooting) section
2. 🐛 [Open an issue](https://github.com/YOUR_USERNAME/face-attendance/issues) on GitHub
3. 📧 Email: your.email@example.com

---

## ⭐ Star History

If you find this project useful, please consider giving it a star! ⭐

It helps the project grow and reach more developers.

---

**Built with ❤️ by Atul Anand**


note -------------
🖥️ Working from a New Laptop
Option 1: SSH to Azure VM (Recommended for Quick Edits)
This lets you edit files directly on the Azure server from any laptop.

Setup on New Laptop:
1. Transfer SSH Key

Copy atul_key.pem to your new laptop:

Via USB drive, email (secure), or cloud storage

Place it somewhere safe (e.g., C:\Users\YourName\Keys\)

2. Connect via SSH

Open PowerShell on new laptop:

powershell
# Connect to Azure VM
ssh -i C:\path\to\atul_key.pem azureuser@57.158.24.17

# You're now connected to the server!
3. Edit Files

bash
cd ~/face-attendance

# Edit main app
nano app.py

# Edit admin panel
nano admin.py

# Edit templates
nano templates/index.html
nano templates/admin.html

# After changes, restart services
sudo systemctl restart face-attendance
sudo systemctl restart face-admin
4. View Logs (if needed)

bash
sudo journalctl -u face-attendance -n 50 -f
Option 2: Clone from GitHub + Push Changes
Best for major development work with proper version control.

Setup on New Laptop:
1. Install Git

Windows: Download from git-scm.com

Mac: brew install git

Linux: sudo apt install git

2. Clone Your Repository

bash
# Open terminal/PowerShell
git clone https://github.com/YOUR_USERNAME/face-attendance.git
cd face-attendance
3. Make Changes Locally

Edit files with any editor (VS Code, Notepad++, etc.)

4. Test Locally (Optional)

bash
# Install dependencies
pip install -r requirements.txt

# Run locally
python app.py
5. Push Changes to GitHub

bash
git add .
git commit -m "Updated recognition logic"
git push origin main
6. Deploy to Azure VM

SSH into Azure from new laptop:

powershell
ssh -i C:\path\to\atul_key.pem azureuser@57.158.24.17
Pull changes:

bash
cd ~/face-attendance
git pull origin main
sudo systemctl restart face-attendance
sudo systemctl restart face-admin
Option 3: VS Code Remote SSH (Best Developer Experience)
Edit Azure files directly in VS Code from any laptop!

Setup on New Laptop:
1. Install VS Code

Download from code.visualstudio.com

2. Install Remote SSH Extension

Open VS Code

Go to Extensions (Ctrl+Shift+X)

Search "Remote - SSH"

Click Install

3. Connect to Azure

Click green button (bottom-left corner: ><)

Select "Connect to Host"

Click "Add New SSH Host"

Enter: ssh -i C:\path\to\atul_key.pem azureuser@57.158.24.17

Select config file to update

Click "Connect"

4. Open Project Folder

File → Open Folder

Navigate to /home/azureuser/face-attendance

Edit files with full VS Code features!

5. Restart Services After Changes

Open VS Code terminal (Ctrl+`):

bash
sudo systemctl restart face-attendance
sudo systemctl restart face-admin
📋 Quick Reference Card
Save this for quick access from any laptop:

text
═══════════════════════════════════════════════
  FACE ATTENDANCE SYSTEM - QUICK ACCESS
═══════════════════════════════════════════════

🌐 LIVE URLS:
  Main App:     http://57.158.24.17
  Admin Panel:  http://57.158.24.17:8080

🔑 SSH ACCESS:
  ssh -i /path/to/atul_key.pem azureuser@57.158.24.17

📁 PROJECT LOCATION:
  /home/azureuser/face-attendance

🔄 RESTART SERVICES:
  sudo systemctl restart face-attendance
  sudo systemctl restart face-admin

📊 VIEW LOGS:
  sudo journalctl -u face-attendance -n 50 -f

🐙 GITHUB:
  git clone https://github.com/YOUR_USERNAME/face-attendance.git
  
═══════════════════════════════════════════════
🔐 Security Best Practices
For SSH Key:

✅ Store in secure location

✅ Don't commit to GitHub

✅ Keep backup in cloud (private, encrypted)

✅ Use password manager for key location

For GitHub:

✅ Use SSH keys for GitHub auth

✅ Enable 2FA on GitHub account

✅ Don't commit sensitive data
