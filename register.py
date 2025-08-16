from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import re
import mysql.connector
import pyttsx3

class Register:
    def __init__(self, r):
        self.root = r
        self.root.title("Registration Page")
        self.root.geometry("1530x790+0+0")

        # Speech engine
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty('voices')
        self.engine.setProperty('voice', self.voices[0].id)

        # Variables
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.contact_var = StringVar()
        self.Confirm_password_var = StringVar()
        self.Password_var = StringVar()
        self.gender_var = StringVar(value="Male")
        self.staff_name_var = StringVar()
        self.department_var = StringVar(value="Select Your Department")
        self.check_var = IntVar()

        # Background
        try:
            img = Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\stud.jpeg")
            img = img.resize((1900, 970), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)
            bg_img = Label(self.root, image=self.photo, bd=2, relief=RAISED)
            bg_img.place(x=0, y=0, width=1540, height=790)
        except Exception as e:
            messagebox.showerror("Image Error", f"Cannot load background: {e}")

        # Title
        self.title_frame = Frame(self.root, bd=1, relief=RIDGE, bg="white")
        self.title_frame.place(x=490, y=30, width=570, height=80)
        title_text = "USER REGISTRATION FORM"
        self.title = Label(self.title_frame, font=("times new roman", 25, "bold"), bg="white", fg="red")
        self.title.place(x=0, y=10)

        def update_title_text(index=0):
            if index >= len(title_text):
                return
            self.title.config(text=title_text[:index + 1])
            self.title.after(100, lambda: update_title_text(index + 1))
        update_title_text()

        # Main Frame
        self.main_frame = Frame(self.root, bd=1, relief=RIDGE)
        self.main_frame.place(x=490, y=110, width=570, height=600)

        # Form Fields
        self.create_form_fields()

    # ====================== FORM FIELDS ======================
    def create_form_fields(self):
        # Username
        ttk.Label(self.main_frame, text="Username:", font=("times new roman", 16, "bold")).grid(row=0, column=0, padx=10, pady=10, sticky=W)
        self.user_entry = ttk.Entry(self.main_frame, textvariable=self.name_var, font=("times new roman", 16, "bold"), width=30)
        self.user_entry.grid(row=0, column=1, padx=10, pady=10)

        # Email
        ttk.Label(self.main_frame, text="Email-ID:", font=("times new roman", 16, "bold")).grid(row=1, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(self.main_frame, textvariable=self.email_var, font=("times new roman", 16, "bold"), width=30).grid(row=1, column=1, padx=10, pady=10)

        # Contact
        ttk.Label(self.main_frame, text="Mobile-No:", font=("times new roman", 16, "bold")).grid(row=2, column=0, padx=10, pady=10, sticky=W)
        contact_entry = ttk.Entry(self.main_frame, textvariable=self.contact_var, font=("times new roman", 16, "bold"), width=30)
        contact_entry.grid(row=2, column=1, padx=10, pady=10)
        self.validate_contact = self.root.register(self.check_contact)
        contact_entry.config(validate="key", validatecommand=(self.validate_contact, "%P"))

        # Staff Name
        ttk.Label(self.main_frame, text="Staff Name:", font=("times new roman", 16, "bold")).grid(row=3, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(self.main_frame, textvariable=self.staff_name_var, font=("times new roman", 16, "bold"), width=30).grid(row=3, column=1, padx=10, pady=10)

        # Gender
        ttk.Label(self.main_frame, text="Select Gender:", font=("times new roman", 16, "bold")).grid(row=4, column=0, padx=10, pady=10, sticky=W)
        gender_frame = Frame(self.main_frame)
        gender_frame.grid(row=4, column=1, padx=10, pady=10)
        Radiobutton(gender_frame, text="Male", variable=self.gender_var, value="Male", font=("times new roman", 15)).grid(row=0, column=0, padx=20)
        Radiobutton(gender_frame, text="Female", variable=self.gender_var, value="Female", font=("times new roman", 15)).grid(row=0, column=1, padx=20)

        # Department
        ttk.Label(self.main_frame, text="Department:", font=("times new roman", 16, "bold")).grid(row=5, column=0, padx=10, pady=10, sticky=W)
        self.combo_dept = ttk.Combobox(self.main_frame, textvariable=self.department_var, font=("times new roman", 16), state="readonly", width=28)
        self.combo_dept["values"] = ("Select Your Department", "Computer", "Civil", "Electrical", "Auto-Mobile", "Mechanical")
        self.combo_dept.grid(row=5, column=1, padx=10, pady=10)
        self.combo_dept.current(0)

        # Password
        ttk.Label(self.main_frame, text="Enter Password:", font=("times new roman", 16, "bold")).grid(row=6, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(self.main_frame, textvariable=self.Password_var, font=("times new roman", 16, "bold"), width=30, show="*").grid(row=6, column=1, padx=10, pady=10)

        # Confirm Password
        ttk.Label(self.main_frame, text="Confirm Password:", font=("times new roman", 16, "bold")).grid(row=7, column=0, padx=10, pady=10, sticky=W)
        ttk.Entry(self.main_frame, textvariable=self.Confirm_password_var, font=("times new roman", 16, "bold"), width=30, show="*").grid(row=7, column=1, padx=10, pady=10)

        # Terms Checkbox
        Checkbutton(self.main_frame, text="I Agree", variable=self.check_var, font=("times new roman", 16)).grid(row=8, column=0, padx=10, pady=10, sticky=W)

        # Buttons
        btn_frame = Frame(self.main_frame)
        btn_frame.grid(row=9, column=0, columnspan=2, pady=20)
        Button(btn_frame, text="Save", command=self.Validation, bg="blue", fg="white", font=("times new roman", 16, "bold"), width=12).grid(row=0, column=0, padx=10)
        Button(btn_frame, text="Verify", command=self.verify_data, bg="green", fg="white", font=("times new roman", 16, "bold"), width=12).grid(row=0, column=1, padx=10)
        Button(btn_frame, text="Clear", command=self.clear_data, bg="red", fg="white", font=("times new roman", 16, "bold"), width=12).grid(row=0, column=2, padx=10)

    # ====================== VALIDATIONS ======================
    def check_contact(self, contact):
        return contact.isdigit() or contact == ""

    def check_email(self, email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return re.match(pattern, email) is not None

    def check_password(self, password):
        pattern = r'^(?=.*[0-9])(?=.*[a-z])(?=.*[A-Z])(?=.*[^a-zA-Z0-9]).{6,21}$'
        return re.match(pattern, password) is not None

    def Validation(self):
        if not self.name_var.get().isalnum():
            messagebox.showerror("Error", "Enter valid username")
        elif not self.check_email(self.email_var.get()):
            messagebox.showerror("Error", "Enter valid email")
        elif len(self.contact_var.get()) != 10:
            messagebox.showerror("Error", "Enter valid 10-digit contact")
        elif self.department_var.get() == "Select Your Department":
            messagebox.showerror("Error", "Select a department")
        elif not self.check_password(self.Password_var.get()):
            messagebox.showerror("Error", "Password must include uppercase, lowercase, digit, special char")
        elif self.Password_var.get() != self.Confirm_password_var.get():
            messagebox.showerror("Error", "Passwords do not match")
        elif self.check_var.get() == 0:
            messagebox.showerror("Error", "Please accept Terms and Conditions")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", passwd="Shreyash@123", database="mydata")
                mycursor = conn.cursor(buffered=True)
                mycursor.execute(
                    "INSERT INTO register (username, email, contact, staff_name, gender, department, password, confirm_password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                    (self.name_var.get(), self.email_var.get(), self.contact_var.get(), self.staff_name_var.get(),
                     self.gender_var.get(), self.department_var.get(), self.Password_var.get(), self.Confirm_password_var.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registration Successful!")
                self.engine.say(f"Welcome {self.name_var.get()}")
                self.engine.runAndWait()
            except Exception as e:
                messagebox.showerror("Database Error", str(e))

    def verify_data(self):
        data = f"Name: {self.name_var.get()}\nEmail: {self.email_var.get()}\nContact: {self.contact_var.get()}\nStaff: {self.staff_name_var.get()}\nGender: {self.gender_var.get()}\nDepartment: {self.department_var.get()}\nPassword: {self.Password_var.get()}"
        messagebox.showinfo("Verify Data", data)

    def clear_data(self):
        self.name_var.set('')
        self.email_var.set('')
        self.contact_var.set('')
        self.staff_name_var.set('')
        self.gender_var.set('Male')
        self.department_var.set('Select Your Department')
        self.Password_var.set('')
        self.Confirm_password_var.set('')
        self.check_var.set(0)


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
