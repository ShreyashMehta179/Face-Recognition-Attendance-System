from tkinter import *
from tkinter import ttk, messagebox
import cv2
import os
import numpy as np
import csv
from datetime import datetime


class Train:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition System")
        self.root.geometry("800x600+200+50")

        title_lbl = Label(self.root, text="Face Recognition System",
                          font=("times new roman", 30, "bold"), bg="navy", fg="white")
        title_lbl.pack(side=TOP, fill=X)

        # Buttons
        btn_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=200, y=100, width=400, height=400)

        b1 = Button(btn_frame, text="Capture Dataset", command=self.generate_dataset,
                    font=("times new roman", 15, "bold"), bg="blue", fg="white", width=25)
        b1.grid(row=0, column=0, pady=20)

        b2 = Button(btn_frame, text="Train Data", command=self.train_classifier,
                    font=("times new roman", 15, "bold"), bg="green", fg="white", width=25)
        b2.grid(row=1, column=0, pady=20)

        b3 = Button(btn_frame, text="Face Recognition", command=self.recognize_faces,
                    font=("times new roman", 15, "bold"), bg="orange", fg="white", width=25)
        b3.grid(row=2, column=0, pady=20)

        b4 = Button(btn_frame, text="Exit", command=self.root.quit,
                    font=("times new roman", 15, "bold"), bg="red", fg="white", width=25)
        b4.grid(row=3, column=0, pady=20)

    # ------------------- Dataset Generator -------------------
    def generate_dataset(self):
        face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

        def face_cropped(img):
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                return img[y:y + h, x:x + w]
            return None

        id = int(input("Enter numeric Student ID: "))
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")

        # Save student details into CSV
        if not os.path.exists("student_details.csv"):
            with open("student_details.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["id", "roll", "name"])
        with open("student_details.csv", "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([id, roll, name])

        cap = cv2.VideoCapture(0)
        img_id = 0
        os.makedirs("fphotos", exist_ok=True)

        while True:
            ret, frame = cap.read()
            if face_cropped(frame) is not None:
                img_id += 1
                face = cv2.resize(face_cropped(frame), (200, 200))
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                file_path = f"fphotos/user.{id}.{roll}.{name}.{img_id}.jpg"
                cv2.imwrite(file_path, face)
                cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
                cv2.imshow("Cropped Face", face)

            if cv2.waitKey(1) == 13 or img_id == 50:  # Press Enter or capture 50 samples
                break

        cap.release()
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Dataset Generated Successfully!")

    # ------------------- Train Classifier -------------------
    def train_classifier(self):
        data_dir = "fphotos"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []

        for image in path:
            img = cv2.imread(image, cv2.IMREAD_GRAYSCALE)
            id = int(image.split(".")[1])
            faces.append(img)
            ids.append(id)

        ids = np.array(ids)
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("Classifier.xml")
        messagebox.showinfo("Result", "Training Dataset Completed!")

    # ------------------- Mark Attendance -------------------
    def mark_attendance(self, roll, name):
        os.makedirs("attendance_report", exist_ok=True)
        file = "attendance_report/Attendance.csv"

        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

        # Prevent duplicate entries
        existing_entries = []
        if os.path.exists(file):
            with open(file, "r") as f:
                reader = csv.reader(f)
                existing_entries = [row[0] for row in reader]

        with open(file, "a", newline="") as f:
            writer = csv.writer(f)
            if roll not in existing_entries:
                writer.writerow([roll, name, dt_string])

    # ------------------- Recognize Faces -------------------
    def recognize_faces(self):
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        # Load student details
        student_dict = {}
        if os.path.exists("student_details.csv"):
            with open("student_details.csv", "r") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    student_dict[int(row["id"])] = (row["roll"], row["name"])

        faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        cap = cv2.VideoCapture(0)

        while True:
            ret, img = cap.read()
            if not ret:
                break
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                id_, distance = clf.predict(gray[y:y + h, x:x + w])
                confidence = int(100 * (1 - distance / 300))

                if confidence > 60:
                    roll, name = student_dict.get(id_, ("Unknown", "Unknown"))
                    self.mark_attendance(roll, name)
                    text = f"Roll:{roll}, Name:{name} ({confidence}%)"
                    cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.8, (0, 255, 0), 2)
                else:
                    cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
                                0.8, (0, 0, 255), 2)

                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 3)

            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) == 13:  # Press Enter to exit
                break

        cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    root = Tk()
    obj = Train(root)
    root.mainloop()
