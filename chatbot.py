from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD
from PIL import Image, ImageTk

class Chatbot:
    def __init__(self, Root):
        self.root = Root
        self.root.title("ChatBot")
        self.root.geometry("900x700+0+0")

        # Main Frame
        main_frame = Frame(self.root, bd=4, bg='powder blue', width=660)
        main_frame.pack()

        # Title Image
        imgchat = Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\stud.jpeg")
        imgchat = imgchat.resize((200, 70), Image.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(imgchat)

        Titlelab = Label(main_frame, bd=3, relief=RAISED, anchor='w',
                         width=730, compound=LEFT, image=self.photoimg,
                         text=' WELCOME TO AI BOT ',
                         font=("times new roman", 30, BOLD), fg="red", bg="white")
        Titlelab.pack(side=TOP)

        # Chat window with scrollbar
        self.scrolly = ttk.Scrollbar(main_frame, orient=VERTICAL)
        self.text = Text(main_frame, width=65, height=20, bd=3, relief=RAISED,
                         font=('arial', 14), yscrollcommand=self.scrolly.set, wrap=WORD)
        self.scrolly.config(command=self.text.yview)
        self.scrolly.pack(side=RIGHT, fill=Y)
        self.text.pack()

        # Button frame
        btn_frame = Frame(self.root, bd=4, bg='white', width=610)
        btn_frame.pack(pady=10)

        label1 = Label(btn_frame, text="ASK YOUR QUESTION HERE",
                       font=('arial', 14, 'bold'), fg='green', bg='white')
        label1.grid(row=0, column=0, padx=5, sticky=W)

        self.entry = ttk.Entry(btn_frame, width=40, font=('times new roman', 14, 'bold'))
        self.entry.grid(row=0, column=1, padx=5, sticky=W)
        self.entry.bind("<Return>", lambda e: self.send())  # Press Enter to send

        self.send_btn = Button(btn_frame, text="SEND", command=self.send,
                               font=('arial', 15, 'bold'), width=8, bg='green', fg="white")
        self.send_btn.grid(row=0, column=2, padx=5, sticky=W)

        self.clear_btn = Button(btn_frame, text="CLEAR CHAT", command=self.clear_chat,
                                font=('arial', 15, 'bold'), width=15, bg='red', fg="white")
        self.clear_btn.grid(row=1, column=0, columnspan=3, pady=5)

    def send(self):
        user_input = self.entry.get().strip()
        if user_input == "":
            return

        # Display user message
        send_msg = f"\t\t\tYou: {user_input}"
        self.text.insert(END, '\n' + send_msg)
        self.text.yview(END)
        self.entry.delete(0, END)

        # Bot responses dictionary
        responses = {
            "hi": "Hello! How can I help you?",
            "hey": "Hey there!",
            "please help": "Sure! Tell me your problem.",
            "yes": "Ask me anything!",
            "face is not recognize": "Please stay in one position and one angle."
        }

        # Default reply if not found
        reply = responses.get(user_input.lower(), "Sorry, I didn't understand that.")
        self.text.insert(END, '\n\nBot: ' + reply)
        self.text.yview(END)

    def clear_chat(self):
        self.text.delete('1.0', END)

if __name__ == "__main__":
    root = Tk()
    chatbot = Chatbot(root)
    root.mainloop()
