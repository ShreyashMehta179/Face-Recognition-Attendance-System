from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk

class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")

        # Main frame
        main_frame = Frame(self.root, bg="black")
        main_frame.place(x=0, y=0, width=1530, height=790)

        # Title Label
        title_text = "DEVELOPER DETAILS"
        title = Label(main_frame, font=("times new roman", 35, "bold"), bg="red", fg="white")
        title.place(x=0, y=0, width=1530, height=55)

        # Animate title text
        def animate_title(index=0):
            if index >= len(title_text):
                return
            title.config(text=title_text[:index+1])
            title.after(100, lambda: animate_title(index+1))

        animate_title()

        # Inner frame for content
        content_frame = Frame(main_frame, bg="black")
        content_frame.place(x=50, y=70, width=1430, height=700)

        # Developer information lines
        lines = [
            "Hello Everyone!",
            "This is Face Recognition Attendance System",
            "Developed by Students of DYP:-",
            "YASH PANDURANG SHELAR",
            "SHREYASH NILESH MEHTA"
        ]

        self.labels = []
        for i, line in enumerate(lines):
            lbl = Label(content_frame, text="", font=("times new roman", 28, BOLD), fg="white", bg="black")
            lbl.pack(pady=10)
            self.labels.append((lbl, line))

        # Animate lines
        self.animate_lines(0, 0)

    def animate_lines(self, line_index, char_index):
        if line_index >= len(self.labels):
            return

        lbl, text = self.labels[line_index]
        lbl.config(text=text[:char_index+1])

        if char_index < len(text):
            lbl.after(100, lambda: self.animate_lines(line_index, char_index + 1))
        else:
            # Move to next line
            lbl.after(200, lambda: self.animate_lines(line_index + 1, 0))


if __name__ == "__main__":
    root = Tk()
    app = Developer(root)
    root.mainloop()
