from tkinter import *
from tkinter import ttk, messagebox
from tkinter.font import BOLD
from PIL import ImageTk, Image
import mysql.connector
from main import face_recog_sys
from register import Register

class Login_window:
    def __init__(self, root):
        self.root = root
        self.root.title("LOGIN SYSTEM")
        self.root.geometry("1550x750+0+0")
        
        # Background image
        img = Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\background.jpg")
        img = img.resize((1550, 750), Image.LANCZOS)
        self.photo = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photo)
        bg_img.place(x=0, y=0, width=1550, height=750)

        # Login frame
        frame = Frame(self.root, bg="black", borderwidth=2, relief=RIDGE)
        frame.place(x=610, y=170, width=340, height=500) 

        # Logo image
        img1 = Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\download.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)
        log_img = Label(image=self.photo1, bg="black", borderwidth=0)
        log_img.place(x=730, y=175, width=100, height=100)

        # Title
        get_label = Label(frame, text="Get Started!!!", font=("times new roman", 20, BOLD), fg="white", bg="black")
        get_label.place(x=95, y=105)

        # Username
        user_n = Label(frame, text="Username", font=("times new roman", 15, BOLD), fg="white", bg="black")
        user_n.place(x=70, y=155)
        self.text_user = ttk.Entry(frame, font=("times new roman", 15, BOLD))
        self.text_user.place(x=40, y=180, width=270)

        # Password
        passwd = Label(frame, text="Password", font=("times new roman", 15, BOLD), fg="white", bg="black")
        passwd.place(x=70, y=230)
        self.text_passwd = ttk.Entry(frame, font=("times new roman", 15, BOLD), show="*")  # Masked password
        self.text_passwd.place(x=40, y=260, width=270)

        # Login button
        login_b = Button(frame, text="Login", font=("times new roman", 15, BOLD), 
                         command=self.check_login, bd=3, relief=RIDGE, fg="white", bg="red",
                         activeforeground="white", activebackground="red")
        login_b.place(x=110, y=300, width=120, height=45)

        # Registration button
        register_b = Button(frame, text="New User Register", font=("times new roman", 15, BOLD),
                            command=self.register, borderwidth=0, fg="white", bg="black",
                            activeforeground="white", activebackground="black")
        register_b.place(x=20, y=350, width=160)

        # Admin button (optional)
        admin_b = Button(frame, text="Admin", font=("times new roman", 15, BOLD),
                         command=self.register, borderwidth=0, fg="white", bg="black",
                         activeforeground="white", activebackground="black")
        admin_b.place(x=20, y=400, width=160)

        # Forget password button
        passwd_b = Button(frame, text="Forget Password", font=("times new roman", 15, BOLD),
                          borderwidth=0, fg="white", bg="black",
                          activeforeground="white", activebackground="black")
        passwd_b.place(x=20, y=450, width=160)

    # ================= LOGIN FUNCTION =================
    def check_login(self):
        username = self.text_user.get()
        password = self.text_passwd.get()

        if username == "" or password == "":
            messagebox.showerror("Error", "All fields are required")
            return

        try:
            conn = mysql.connector.connect(host="localhost", user="root", passwd="Shreyash@123", database="mydata")
            mycursor = conn.cursor()
            query = "SELECT * FROM register WHERE username=%s AND password=%s"
            values = (username, password)
            mycursor.execute(query, values)
            user = mycursor.fetchone()
            conn.close()

            if user:
                messagebox.showinfo("Login Success", f"Welcome {username}")
                self.face()
            else:
                messagebox.showerror("Login Failed", "Invalid username or password")
        except Exception as e:
            messagebox.showerror("Error", f"Database connection error: {e}")

    # Open face recognition window
    def face(self):
        self.new_window = Toplevel(self.root)
        self.app = face_recog_sys(self.new_window) 

    # Open registration window
    def register(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)


if __name__ == "__main__":
    root = Tk()
    log = Login_window(root)
    root.mainloop()
