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
A functional webcam (internal or external) for real-time video feed.
⚙️ Setup
Step 1: Clone the Repository
Clone the repository and navigate to the project folder:

bash
Copy code
git clone <repository_url>
cd <repository_name>
Step 2: Create Necessary Directories
Ensure the following directories and files are set up:

./db: Directory for storing user face embeddings.
./log.txt: This file will be created automatically during the first login/logout attempt.
Step 3: Configure Anti-Spoofing Models
Download the required pre-trained anti-spoofing models. Update the model_dir variable in the script:

python
Copy code
model_dir = '/path/to/anti_spoof_models'
Replace /path/to/anti_spoof_models with the actual file path to the anti-spoofing models.

🚀 Usage
Run the Application
Start the application with:

bash
Copy code
python <script_name>.py
User Actions
Login: Click the "Login" button to authenticate using facial data.
Logout: Click the "Logout" button to securely log out.
Register New User:
Click the "Register New User" button.
Enter a username and follow the on-screen instructions to register your face.
📂 Code Structure
Main Class: FaceRecognitionApp
Directories:
./db: Stores user face embeddings as .pickle files.
./log.txt: Logs all user login/logout events.
Key Methods:
login(): Handles user login functionality.
logout(): Handles user logout functionality.
register_new_user(): Manages the registration process for new users.
📂 Screenshots
Login Window
Add a screenshot of the login window.

Registration Window
Add a screenshot of the registration window.

🛠️ Future Enhancements
Improved Anti-Spoofing: Incorporate advanced liveness detection techniques, such as blink detection or 3D face modeling.
Multi-Camera Support: Add support for multiple camera switching.
Database Integration: Migrate to SQL or cloud storage for secure and scalable user data management.
📜 License
This project is licensed under the MIT License. Refer to the LICENSE file for more details.

🤝 Contributions
We welcome contributions! Follow these steps to contribute:

Fork the repository.
Create a new branch.
Submit a pull request with your proposed changes.
For questions or suggestions, please open an issue.



For any questions or suggestions, please open an issue.
