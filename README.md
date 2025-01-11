# FaceSecure: AI-Powered Facial Recognition System

## 📌 Overview
FaceSecure is an AI-powered facial recognition system that enables user authentication based on face recognition. This application uses OpenCV and face_recognition libraries to perform face detection and recognition. Additionally, it integrates anti-spoofing techniques to prevent fake entries.

## 🚀 Features
- **Face Recognition Login:** Seamless login using face recognition.
- **Anti-Spoofing:** Detects spoof attempts using pre-trained anti-spoofing models.
- **User Registration:** Allows users to register with their facial data and username.
- **Logging:** Logs user login/logout activity with timestamps.
- **Real-time Webcam Feed:** Displays live webcam feed during login and registration.

## 💻 Requirements
- **Python 3.x**: Make sure to have Python 3.x installed.
- **Libraries:** Install the necessary libraries using `pip`:
  ```bash
  pip install opencv-python pillow face_recognition tkinter

  Hardware Requirements
A webcam (internal or external) for real-time video feed.
Setup
1. Clone the Repository
bash
Copy code
git clone <repository_url>
cd <repository_name>
2. Create Necessary Directories
Ensure the following directories exist:

./db: For storing user face embeddings.
./log.txt: Activity log file is created automatically.
3. Update Anti-Spoof Model Path
Replace the placeholder in the code:

python
Copy code
model_dir='/path/to/anti_spoof_models'
Ensure the anti-spoofing model files are downloaded and the path is correct.

Usage
Run the Application
bash
Copy code
python <script_name>.py
User Actions
Login: Click the "Login" button to authenticate.
Logout: Click the "Logout" button to log out securely.
Register New User:
Click "Register New User."
Enter a username and follow on-screen instructions to register.
Code Structure
FaceRecognitionApp: Main application class.
Directories:
./db: Stores user embeddings as .pickle files.
./log.txt: Maintains user login/logout logs.
Key Methods:
login(): Handles user login.
logout(): Handles user logout.
register_new_user(): Handles user registration.
Screenshots
Login Window:

Registration Window:

Future Enhancements
Improved Anti-Spoofing:
Add advanced liveness detection techniques (e.g., blink detection).
Multi-Camera Support:
Enable switching between multiple cameras.
Database Integration:
Use SQL or cloud storage for scalable user data management.
License
This project is licensed under the MIT License. See the LICENSE file for more details.

Contributions
Feel free to contribute! Fork the repository, create a new branch, and submit a pull request.

For any questions or suggestions, please open an issue.
