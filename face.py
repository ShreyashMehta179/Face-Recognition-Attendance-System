import cv2
import os
import csv
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        title_text = "FACE RECOGNITION"
        title = Label(self.root, font=("times new roman", 35, "bold"), bg="white", fg="green")
        title.place(x=0, y=0, width=1530, height=55)

        def update_title(index=0):
            if index > len(title_text):
                return
            title.config(text=title_text[:index])
            title.after(100, lambda: update_title(index + 1))

        update_title()

        # Top image
        img_top = Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\recog.jpeg")
        img_top = img_top.resize((1530, 325), Image.LANCZOS)
        self.photoimg_top = ImageTk.PhotoImage(img_top)
        Label(self.root, image=self.photoimg_top).place(x=0, y=55, width=1530, height=325)

        # Button for recognition
        Button(self.root, text="START FACE RECOGNITION", cursor="hand2",
               command=self.recognize_faces,
               font=("times new roman", 28, "bold"), bg="green", fg="white").place(x=0, y=380, width=1530,
                                                                                  height=60)

        # Bottom image
        img_bottom = Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\train.jpeg")
        img_bottom = img_bottom.resize((1530, 325), Image.LANCZOS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
        Label(self.root, image=self.photoimg_bottom).place(x=0, y=440, width=1530, height=325)

        # Load student details (mapping id → name, roll)
        self.student_details = self.load_student_details()

    def load_student_details(self, csv_path="student_details.csv"):
        """Load student details from CSV (id → name, roll)"""
        details = {}
        if not os.path.exists(csv_path):
            messagebox.showerror("Error", f"Missing student details CSV: {csv_path}")
            self.root.destroy()
            return details
        with open(csv_path, newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                details[int(row['id'])] = (row['name'], row['roll'])
        return details

    def draw_boundary(self, img, classifier, scaleFactor, minNeighbors, color, clf):
        """Detect faces and draw Name + Roll based on trained ID"""
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        features = classifier.detectMultiScale(gray_image, scaleFactor, minNeighbors)

        coords = []

        for (x, y, w, h) in features:
            id_, pred = clf.predict(gray_image[y:y + h, x:x + w])
            confidence = int(100 * (1 - pred / 300))  # Confidence %

            if confidence > 75:
                if id_ in self.student_details:   # Fetch from CSV using trained ID
                    name, roll = self.student_details[id_]
                    cv2.putText(img, f"Name: {name}", (x, y - 35), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                    cv2.putText(img, f"Roll: {roll}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
                else:
                    cv2.putText(img, f"User {id_}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
            else:
                cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)

            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            coords = [x, y, w, h]

        return coords

    def recognize_faces(self):
        """Start webcam and perform recognition"""
        if not os.path.exists("Classifier.xml"):
            messagebox.showerror("Error", "No trained model found! Train the data first.")
            return

        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("Classifier.xml")

        video_cap = cv2.VideoCapture(0)

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            self.draw_boundary(img, face_cascade, 1.1, 10, (255, 255, 255), clf)
            cv2.imshow("Face Recognition", img)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognition(root)
    root.mainloop()
