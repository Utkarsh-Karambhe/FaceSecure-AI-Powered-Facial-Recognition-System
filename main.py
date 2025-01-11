import os
import datetime
import pickle
import tkinter as tk
from tkinter import messagebox
import cv2
from PIL import Image, ImageTk
import face_recognition

import util
from test import test


class FaceRecognitionApp:
    def __init__(self, db_dir='./db', log_path='./log.txt'):
        self.db_dir = db_dir
        self.log_path = log_path

        self.setup_directories()
        self.setup_gui()
        self.setup_webcam()

    def setup_directories(self):
        """Ensure necessary directories exist."""
        if not os.path.exists(self.db_dir):
            os.mkdir(self.db_dir)

    def setup_gui(self):
        """Set up the main application window."""
        self.main_window = tk.Tk()
        self.main_window.geometry("1200x520+350+100")

        self.create_buttons()
        self.create_webcam_label()

    def create_buttons(self):
        """Create and place buttons in the main window."""
        self.login_button = util.get_button(self.main_window, 'Login', 'green', self.login)
        self.login_button.place(x=750, y=200)

        self.logout_button = util.get_button(self.main_window, 'Logout', 'red', self.logout)
        self.logout_button.place(x=750, y=300)

        self.register_button = util.get_button(self.main_window, 'Register New User', 'gray', self.register_new_user,
                                               fg='black')
        self.register_button.place(x=750, y=400)

    def create_webcam_label(self):
        """Create a label to display the webcam feed."""
        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=0, width=700, height=500)

    def setup_webcam(self):
        """Initialize the webcam for capturing images."""
        self.cap = cv2.VideoCapture(2)
        self.capture_webcam_feed()

    def capture_webcam_feed(self):
        """Capture and display webcam feed."""
        ret, frame = self.cap.read()
        if ret:
            self.most_recent_capture_arr = frame
            self.update_webcam_label()
        self.webcam_label.after(20, self.capture_webcam_feed)

    def update_webcam_label(self):
        """Update the webcam label with the most recent frame."""
        img_rgb = cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
        self.most_recent_capture_pil = Image.fromarray(img_rgb)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self.webcam_label.imgtk = imgtk
        self.webcam_label.configure(image=imgtk)

    def login(self):
        """Handle the login process."""
        label = test(
            image=self.most_recent_capture_arr,
            model_dir='/path/to/anti_spoof_models',
            device_id=0
        )

        if label == 1:
            self.authenticate_user()
        else:
            self.show_message('Warning', 'Spoof detected! You are fake.')

    def authenticate_user(self):
        """Authenticate the user based on face recognition."""
        name = util.recognize(self.most_recent_capture_arr, self.db_dir)
        if name in ['unknown_person', 'no_persons_found']:
            self.show_message('Error', 'Unknown user. Please register or try again.')
        else:
            self.log_user_activity(name, 'in')
            self.show_message('Welcome', f'Welcome back, {name}!')

    def logout(self):
        """Handle the logout process."""
        label = test(
            image=self.most_recent_capture_arr,
            model_dir='/path/to/anti_spoof_models',
            device_id=0
        )

        if label == 1:
            self.authenticate_user_for_logout()
        else:
            self.show_message('Warning', 'Spoof detected! You are fake.')

    def authenticate_user_for_logout(self):
        """Authenticate the user for logging out."""
        name = util.recognize(self.most_recent_capture_arr, self.db_dir)
        if name in ['unknown_person', 'no_persons_found']:
            self.show_message('Error', 'Unknown user. Please register or try again.')
        else:
            self.log_user_activity(name, 'out')
            self.show_message('Goodbye', f'Goodbye, {name}!')

    def log_user_activity(self, name, status):
        """Log user activity (login/logout) to a file."""
        with open(self.log_path, 'a') as log_file:
            log_file.write(f'{name},{datetime.datetime.now()},{status}\n')

    def show_message(self, title, message):
        """Show a message box."""
        messagebox.showinfo(title, message)

    def register_new_user(self):
        """Open a window for registering a new user."""
        self.register_window = tk.Toplevel(self.main_window)
        self.register_window.geometry("1200x520+370+120")

        self.create_registration_buttons()
        self.create_registration_gui_elements()

    def create_registration_buttons(self):
        """Create and place buttons in the registration window."""
        self.accept_button = util.get_button(self.register_window, 'Accept', 'green', self.accept_register_new_user)
        self.accept_button.place(x=750, y=300)

        self.try_again_button = util.get_button(self.register_window, 'Try Again', 'red',
                                                self.try_again_register_new_user)
        self.try_again_button.place(x=750, y=400)

    def create_registration_gui_elements(self):
        """Create and place the GUI elements for user registration."""
        self.capture_label = util.get_img_label(self.register_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_image_to_label(self.capture_label)

        self.username_entry = util.get_entry_text(self.register_window)
        self.username_entry.place(x=750, y=150)

        self.username_label = util.get_text_label(self.register_window, 'Enter Username:')
        self.username_label.place(x=750, y=70)

    def add_image_to_label(self, label):
        """Display the captured image on the registration window."""
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_capture = self.most_recent_capture_arr.copy()

    def try_again_register_new_user(self):
        """Close the registration window without saving."""
        self.register_window.destroy()

    def accept_register_new_user(self):
        """Save the new user's face encoding and username."""
        username = self.username_entry.get(1.0, "end-1c").strip()

        if not username:
            self.show_message('Error', 'Username cannot be empty.')
            return

        embeddings = face_recognition.face_encodings(self.register_capture)
        if embeddings:
            self.save_user_data(username, embeddings[0])
            self.show_message('Success', 'User registered successfully!')
            self.register_window.destroy()
        else:
            self.show_message('Error', 'No face detected. Please try again.')

    def save_user_data(self, username, embeddings):
        """Save the user's face embeddings to a pickle file."""
        with open(os.path.join(self.db_dir, f'{username}.pickle'), 'wb') as file:
            pickle.dump(embeddings, file)

    def start(self):
        """Start the main application loop."""
        self.main_window.mainloop()


if __name__ == "__main__":
    app = FaceRecognitionApp()
    app.start()
