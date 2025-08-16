from tkinter import *
from PIL import Image, ImageTk
import mysql.connector
import cv2
import pyttsx3
from datetime import datetime
import os
from tkinter import messagebox

class FaceRecognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Title animation
        self.title_text = "FACE RECOGNITION"
        self.title_label = Label(self.root, font=("times new roman", 35, "bold"), bg="white", fg="red")
        self.title_label.place(x=0, y=0, width=1530, height=55)
        self.update_title_text()

        # Left image
        try:
            img_top1 = Image.open(r"C:\\Users\\hp\\OneDrive\\Desktop\\NOTES\\face recognition\\recog.jpeg")
            img_top1 = img_top1.resize((750, 700), Image.LANCZOS)
            self.photoimg_top = ImageTk.PhotoImage(img_top1)
            f_lb1 = Label(self.root, image=self.photoimg_top)
            f_lb1.place(x=0, y=55, width=750, height=700)
        except Exception as e:
            messagebox.showerror("Image Error", f"Could not load left image: {e}")

        # Right image
        try:
            img_bottom = Image.open(r"C:\\Users\\hp\\OneDrive\\Desktop\\NOTES\\face recognition\\detect.jpeg")
            img_bottom = img_bottom.resize((800, 700), Image.LANCZOS)
            self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)
            self.right_frame = Label(self.root, image=self.photoimg_bottom)
            self.right_frame.place(x=750, y=55, width=800, height=700)
        except Exception as e:
            messagebox.showerror("Image Error", f"Could not load right image: {e}")

        # Detect face button
        btn_1 = Button(self.right_frame, text="DETECT FACE", cursor="hand2",
                        command=self.recog, font=("times new roman", 20, "bold"),
                        bg="red", fg="white")
        btn_1.place(x=300, y=620, width=200, height=40)

    def update_title_text(self, index=0):
        if index <= len(self.title_text):
            self.title_label.config(text=self.title_text[:index])
            self.root.after(100, lambda: self.update_title_text(index+1))

    def mark_attendance(self, name, roll, dept):
        """Mark attendance in mega.csv for recognized student."""
        csv_path = "mega.csv"
        today = datetime.now().strftime("%d/%m/%Y")

        # Prevent duplicate attendance
        if os.path.exists(csv_path):
            with open(csv_path, "r") as f:
                for line in f.readlines():
                    entry = line.strip().split(",")
                    if len(entry) >= 6 and entry[0] == name and entry[4] == today:
                        return

        # Append attendance
        with open(csv_path, "a") as f:
            now = datetime.now()
            dtstring = now.strftime("%H:%M:%S")
            d1 = now.strftime("%d/%m/%Y")
            f.write(f"{name},{roll},{dept},{dtstring},{d1},Present\n")
        
        # Speech greeting
        try:
            engine = pyttsx3.init()
            engine.say(f"Welcome to class {name}")
            engine.runAndWait()
        except Exception as e:
            print(f"Speech error: {e}")

    def recog(self):
        """Trigger face recognition and attendance marking."""
        try:
            # Use buffered cursor to prevent "unread result" error
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                passwd="Shreyash@123",
                database="mydata"
            )
            mycursor = conn.cursor(buffered=True)
        except mysql.connector.Error as err:
            messagebox.showerror("Database Error", f"Cannot connect to DB: {err}")
            return

        try:
            faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
            clf = cv2.face.LBPHFaceRecognizer_create()
            clf.read("Classifier.xml")
        except Exception as e:
            messagebox.showerror("Model Error", f"Cannot load classifier: {e}")
            conn.close()
            return

        video_cap = cv2.VideoCapture(0)
        if not video_cap.isOpened():
            messagebox.showerror("Camera Error", "Cannot access webcam.")
            conn.close()
            return

        while True:
            ret, img = video_cap.read()
            if not ret:
                break

            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                try:
                    id, predict = clf.predict(gray[y:y+h, x:x+w])
                    confidence = int(100 * (1 - predict / 300))
                except:
                    id = None
                    confidence = 0

                if id is not None:
                    mycursor.execute("SELECT var_name, var_roll_no, var_department FROM student WHERE var_stud_id=%s", (int(id),))
                    result = mycursor.fetchone()
                    if result:
                        name, roll, dept = result
                    else:
                        name, roll, dept = "Unknown", "Unknown", "Unknown"
                else:
                    name, roll, dept = "Unknown", "Unknown", "Unknown"

                if confidence > 60 and name != "Unknown":
                    cv2.putText(img, f"Name: {name}", (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,255,0),2)
                    cv2.putText(img, f"Roll: {roll}", (x, y-35), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img, f"Dept: {dept}", (x, y-55), cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    self.mark_attendance(name, roll, dept)
                else:
                    cv2.putText(img, "Unknown", (x, y-15), cv2.FONT_HERSHEY_COMPLEX, 0.8, (0,0,255), 2)

                cv2.rectangle(img, (x, y), (x+w, y+h), (255,0,255), 2)

            cv2.imshow("FACE RECOGNITION", img)
            if cv2.waitKey(1) == 13:  # Enter key to exit
                break

        video_cap.release()
        cv2.destroyAllWindows()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    app = FaceRecognition(root)
    root.mainloop()
