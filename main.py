from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from student import Student
from a import Developer
from chatbot import Chatbot
from train import Train
from camera import FaceRecognition       # ✅ use camera instead of face.py
import os
from tkinter import messagebox
from Attendance import Attendance


class face_recog_sys:
    def __init__(self, r):
        self.root = r
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        # ================= Top Images =================
        img = Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\stud.jpeg")
        img = img.resize((500, 130), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)
        Label(self.root, image=self.photo).place(x=0, y=0, width=500, height=130)

        img1 = Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\images.jpg")
        img1 = img1.resize((500, 130), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)
        Label(self.root, image=self.photo1).place(x=500, y=0, width=500, height=130)

        img2 = Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\mach.jpeg")
        img2 = img2.resize((500, 130), Image.LANCZOS)
        self.photo2 = ImageTk.PhotoImage(img2)
        Label(self.root, image=self.photo2).place(x=1000, y=0, width=540, height=130)

        # ================= Background =================
        img3 = Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\Student_bg.jpg")
        img3 = img3.resize((1530, 710), Image.LANCZOS)
        self.photo3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photo3)
        bg_img.place(x=0, y=130, width=1530, height=820)

        title_lbl = Label(bg_img, text="FACE  RECOGNITION  ATTENDANCE  SYSTEM  SOFTWARE",
                          font=("times new roman", 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1530, height=55)

        # ================= Buttons =================
        # Student
        self.create_button(bg_img, "stud.jpeg", "Student Details", 200, 100, self.stud)

        # Face Recognition (Camera)
        self.create_button(bg_img, "recog.jpeg", "Face Detector", 500, 100, self.FACE_DATA)

        # Attendance
        self.create_button(bg_img, "img.jpeg", "Attendance", 800, 100, self.Attendance)

        # Chatbot
        self.create_button(bg_img, "help.jpeg", "Help Desk", 1100, 100, self.chat)

        # Train Data
        self.create_button(bg_img, "train.jpeg", "Train Data", 200, 380, self.TRAIN)

        # Photos
        self.create_button(bg_img, "bg.jpeg", "Photos Storage", 500, 380, self.open_photo)

        # Developer
        self.create_button(bg_img, "backg.jpeg", "Developer Details", 800, 380, self.developer)

        # Exit
        self.create_button(bg_img, "exit.jpeg", "Exit Or Return", 1100, 380, self.Exit)

    # ============ Helper to Create Button ============
    def create_button(self, parent, img_name, text, x, y, command):
        path = fr"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\{img_name}"
        img = Image.open(path)
        img = img.resize((220, 220), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        btn = Button(parent, image=photo, cursor="hand2", command=command)
        btn.image = photo  # ✅ Keep reference to avoid garbage collection
        btn.place(x=x, y=y, width=220, height=220)

        btn1 = Button(parent, text=text, cursor="hand2", command=command,
                      font=("times new roman", 15, "bold"), bg="blue", fg="white")
        btn1.place(x=x, y=y+200, width=220, height=40)

    # ============ Functions ============
    def open_photo(self):
        os.startfile("dataset")   # ✅ corrected from "fphotos" to dataset folder

    def stud(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)

    def chat(self):
        self.new_window = Toplevel(self.root)
        self.app = Chatbot(self.new_window)

    def TRAIN(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def FACE_DATA(self):
        self.new_window = Toplevel(self.root)
        self.app = FaceRecognition(self.new_window)   # Using FaceRecognition class from camera.py

    def Attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def developer(self):
        self.new_window = Toplevel(self.root)
        self.app = Developer(self.new_window)

    def Exit(self):
        self.Exit = messagebox.askyesno("Face recognition", "Do you want to Exit", parent=self.root)
        if self.Exit:
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    a = face_recog_sys(root)
    root.mainloop()
