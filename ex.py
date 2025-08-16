# # # import csv
# # # import tkinter as tk
# # # from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# # # from matplotlib.figure import Figure

# # # # Read the attendance data from a CSV file
# # # with open('mega.csv', 'r') as file:
# # #     reader = csv.reader(file)
# # #     next(reader) # skip header row
# # #     data = [row for row in reader]

# # # # Calculate the attendance percentage for each student
# # # attendance_percentage = []
# # # for row in data:
# # #     attendance_count = 0
# # #     for i in range(1, len(row)):
# # #         if row[i] == 'present':
# # #             attendance_count += 1
# # #     percentage = attendance_count / (len(row) - 1) * 100
# # #     attendance_percentage.append(percentage)

# # # # Create a Matplotlib figure
# # # fig = Figure(figsize=(5, 4), dpi=100)
# # # ax = fig.add_subplot(111)
# # # ax.bar([row[0] for row in data], attendance_percentage)
# # # ax.set_xlabel('Student')
# # # ax.set_ylabel('Attendance Percentage')
# # # ax.set_title('Attendance Percentage of Students')

# # # # Create a Tkinter window
# # # root = tk.Tk()
# # # root.title('Student Attendance Averages')

# # # # Add a Matplotlib canvas widget to the Tkinter window
# # # canvas = FigureCanvasTkAgg(fig, master=root)
# # # canvas.draw()
# # # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# # # # Display the Tkinter window
# # # tk.mainloop()'



# # # import tkinter as tk
# # # import time

# # # class TypewriterLabel(tk.Label):
# # #     def __init__(self, master, text, font, delay=80, **kwargs):
# # #         super().__init__(master, text='', font=font, **kwargs)
# # #         self.delay = delay
# # #         self.text = text
# # #         self.index = 0
# # #         self.animate()

# # #     def animate(self):
# # #         if self.index < len(self.text):
# # #             self.config(text=self.text[:self.index+1])
# # #             self.index += 1
# # #             self.after(self.delay, self.animate)

# # # # Create a Tkinter window
# # # root = tk.Tk()
# # # root.geometry("700x600")

# # # # Animate the label
# # # title_lb1 = TypewriterLabel(root, text="FACE RECOGNITION ", font=("times new roman",35,"bold"), bg="red", fg="white")
# # # title_lb1.place(x=0, y=0, width=1530, height=45)

# # # # Display the label on the screen
# # # title_lb1.pack()

# # # # Display the Tkinter window
# # # root.mainloop()


# # import tkinter as tk
# # import time

# # # define the colors
# # colors = ["#FF00FF", "#00FFFF"]

# # # create the main window
# # root = tk.Tk()

# # # create a canvas widget to hold the frame
# # canvas = tk.Canvas(root, bg="#000000")
# # canvas.pack(fill="both", expand=True)

# # # define the size of the frame
# # width = 400
# # height = 300

# # # define the thickness of the frame
# # thickness = 20

# # # define the initial color index
# # color_index = 0

# # # create a function to draw the frame
# # def draw_frame():
# #     # get the current time
# #     now = int(time.time() * 1000)

# #     # calculate the color index based on the time
# #     global color_index
# #     color_index = (now // 500) % len(colors)

# #     # clear the canvas
# #     canvas.delete("all")

# #     # draw the frame
# #     x1 = (canvas.winfo_width() - width) // 2
# #     y1 = (canvas.winfo_height() - height) // 2
# #     x2 = x1 + width
# #     y2 = y1 + height
# #     for i in range(thickness):
# #         canvas.create_rectangle(x1 + i, y1 + i, x2 - i, y2 - i, outline=colors[color_index], width=1)

# #     # schedule the next frame
# #     canvas.after(10, draw_frame)

# # # start the animation loop
# # draw_frame()

# # # start the main loop
# # root.mainloop()

# # import tkinter as tk
# # import time

# # # define the colors
# # colors = ["#FF00FF", "#00FFFF"]

# # # create the main window
# # root = tk.Tk()

# # # create a canvas widget to hold the frame
# # canvas = tk.Canvas(root, bg="#000000")
# # canvas.pack(fill="both", expand=True)

# # # define the size of the frame
# # width = 400
# # height = 300

# # # define the thickness of the frame
# # thickness = 20

# # # define the delay between frames
# # delay = 100

# # # create a list to store the previous colors
# # prev_colors = []

# # # create a function to draw the frame
# # def draw_frame():
# #     # get the current time
# #     now = int(time.time() * 1000)

# #     # calculate the color index based on the time
# #     color_index = (now // delay) % len(colors)

# #     # append the current color to the list
# #     prev_colors.append(colors[color_index])

# #     # remove the oldest color from the list if it exceeds the thickness
# #     if len(prev_colors) > thickness:
# #         prev_colors.pop(0)

# #     # clear the canvas
# #     canvas.delete("all")

# #     # draw the frame in a snake-like pattern using the previous colors
# #     x1 = (canvas.winfo_width() - width) // 2
# #     y1 = (canvas.winfo_height() - height) // 2
# #     x2 = x1 + width
# #     y2 = y1 + height
# #     for i in range(thickness):
# #         for j in range(len(prev_colors)):
# #             canvas.create_rectangle(x1 + i + j * 2, y1 + i + j * 2, x2 - i - j * 2, y2 - i - j * 2, outline=prev_colors[j], width=1)

# #     # schedule the next frame
# #     canvas.after(delay, draw_frame)

# # # start the animation loop
# # draw_frame()

# # # start the main loop
# # root.mainloop()

# import csv
# import datetime

# # Step 1: Read CSV file
# with open('mega.csv', mode='r') as file:
#     reader = csv.reader(file)
#     data = [row for row in reader]

# # Step 2: Calculate total number of days and total number of days present for each student for each month
# attendance = {}  # Store attendance data in a dictionary
# for row in data[1:]:  # Skip header row
#     rollno, name, dept, time, date, status = row
#     month = date.split('-')[0]  # Extract month from date
#     if rollno not in attendance:
#         attendance[rollno] = {}  # Create nested dictionary for rollno if it doesn't exist
#     if month not in attendance[rollno]:
#         attendance[rollno][month] = {'total': 0, 'present': 0}  # Create nested dictionary for month if it doesn't exist
#     attendance[rollno][month]['total'] += 1
#     if status == 'Present':
#         attendance[rollno][month]['present'] += 1

# # Step 3: Calculate percentage of attendance for each student for each month
# percentage = {}
# for rollno in attendance:
#     percentage[rollno] = {}
#     for month in attendance[rollno]:
#         total = attendance[rollno][month]['total']
#         present = attendance[rollno][month]['present']
#         percentage[rollno][month] = round(present / total * 100, 2) if total != 0 else 0

# # Step 4: Calculate average percentage of attendance for each month
# average = {}
# for month in range(1, 13):
#     month_str = str(month).zfill(2)  # Zero-pad month number as string
#     month_name = datetime.datetime.strptime(month_str, '%m').strftime('%B')  # Convert month number to month name
#     percentages = [percentage[rollno][month_str] for rollno in percentage if month_str in percentage[rollno]]
#     average[month_name] = round(sum(percentages) / len(percentages), 2) if len(percentages) != 0 else 0

# # Step 5: Display average percentage of attendance for each month in GUI
# for month_name, percentage in average.items():
#     print(f'{month_name}: {percentage}%')









# # import csv
# # import matplotlib.pyplot as plt

# # # Step 1: Read CSV file
# # with open('mega.csv', mode='r') as file:
# #     reader = csv.reader(file)
# #     data = [row for row in reader]

# # # Step 2: Calculate total number of days and total number of days present for each student for each month
# # attendance = {}  # Store attendance data in a dictionary
# # for row in data[1:]:  # Skip header row
# #     rollno, name, dept, time, date, status = row
# #     month = date.split('-')[0]  # Extract month from date
# #     if rollno not in attendance:
# #         attendance[rollno] = {}  # Create nested dictionary for rollno if it doesn't exist
# #     if month not in attendance[rollno]:
# #         attendance[rollno][month] = {'total': 0, 'present': 0}  # Create nested dictionary for month if it doesn't exist
# #     attendance[rollno][month]['total'] += 1
# #     if status == 'Present':
# #         attendance[rollno][month]['present'] += 1

# # # Step 3: Calculate percentage of attendance for each student for each month
# # percentage = {}
# # for rollno in attendance:
# #     percentage[rollno] = {}
# #     for month in attendance[rollno]:
# #         total = attendance[rollno][month]['total']
# #         present = attendance[rollno][month]['present']
# #         percentage[rollno][month] = round(present / total * 100, 2) if total != 0 else 0

# # # Step 4: Plot graph of average percentage of attendance for each student for each month
# # for rollno in percentage:
# #     percentages = [percentage[rollno][month] for month in percentage[rollno]]
# #     plt.plot(list(percentage[rollno].keys()), percentages, label=f"Roll No: {rollno}")

# # plt.legend()
# # plt.xlabel("Month")
# # plt.ylabel("Attendance Percentage")
# # plt.show()



# # import csv
# # import datetime
# # import matplotlib.pyplot as plt

# # # Step 1: Read CSV file
# # with open('mega.csv', mode='r') as file:
# #     reader = csv.reader(file)
# #     data = [row for row in reader]

# # # Step 2: Calculate total number of days and total number of days present for each student for each month
# # attendance = {}  # Store attendance data in a dictionary
# # for row in data[1:]:  # Skip header row
# #     rollno, name, dept, time, date, status = row
# #     month = date.split('-')[0]  # Extract month from date
# #     if rollno not in attendance:
# #         attendance[rollno] = {}  # Create nested dictionary for rollno if it doesn't exist
# #     if month not in attendance[rollno]:
# #         attendance[rollno][month] = {'total': 0, 'present': 0}  # Create nested dictionary for month if it doesn't exist
# #     attendance[rollno][month]['total'] += 1
# #     if status == 'Present':
# #         attendance[rollno][month]['present'] += 1

# # # Step 3: Calculate percentage of attendance for each student for each month
# # percentage = {}
# # for rollno in attendance:
# #     percentage[rollno] = {}
# #     for month in attendance[rollno]:
# #         total = attendance[rollno][month]['total']
# #         present = attendance[rollno][month]['present']
# #         percentage[rollno][month] = round(present / total * 100, 2) if total != 0 else 0

# # # Step 4: Calculate average percentage of attendance for each month for each student
# # average = {}
# # for rollno in percentage:
# #     name = ""
# #     for row in data[1:]:  # Search for name associated with rollno
# #         if row[0] == rollno:
# #             name = row[1]
# #             break
# #     for month in range(1, 13):
# #         month_str = str(month).zfill(2)  # Zero-pad month number as string
# #         month_name = datetime.datetime.strptime(month_str, '%m').strftime('%B')  # Convert month number to month name
# #         if month_str in percentage[rollno]:
# #             if name not in average:
# #                 average[name] = {}
# #             average[name][month_name] = percentage[rollno][month_str]

# # # Step 5: Plot bar chart of average percentage of attendance for each month for each student
# # for name in average:
# #     months = list(average[name].keys())
# #     percentages = list(average[name].values())
# #     plt.bar(months, percentages)
# #     plt.title(f'Attendance percentage averages for {name}')
# #     plt.xlabel('Month')
# #     plt.ylabel('Attendance percentage')
# #     plt.show()

# # import csv
# # import datetime
# # import matplotlib.pyplot as plt

# # # Step 1: Read CSV file and calculate attendance percentage for each student for each month
# # with open('mega.csv', mode='r') as file:
# #     reader = csv.reader(file)
# #     data = [row for row in reader]

# # attendance = {}  # Store attendance data in a dictionary
# # for row in data[1:]:  # Skip header row
# #     rollno, name, dept, time, date, status = row
# #     month = date.split('-')[0]  # Extract month from date
# #     if rollno not in attendance:
# #         attendance[rollno] = {}  # Create nested dictionary for rollno if it doesn't exist
# #     if month not in attendance[rollno]:
# #         attendance[rollno][month] = {'total': 0, 'present': 0}  # Create nested dictionary for month if it doesn't exist
# #     attendance[rollno][month]['total'] += 1
# #     if status == 'Present':
# #         attendance[rollno][month]['present'] += 1

# # percentage = {}
# # for rollno in attendance:
# #     percentage[rollno] = {}
# #     for month in attendance[rollno]:
# #         total = attendance[rollno][month]['total']
# #         present = attendance[rollno][month]['present']
# #         percentage[rollno][month] = round(present / total * 100, 2) if total != 0 else 0

# # # Step 2: Calculate average percentage of attendance for each month for all students
# # average = {}
# # for month in range(1, 13):
# #     month_str = str(month).zfill(2)  # Zero-pad month number as string
# #     percentages = [percentage[rollno][month_str] for rollno in percentage if month_str in percentage[rollno]]
# #     average[month_str] = round(sum(percentages) / len(percentages), 2) if len(percentages) != 0 else 0

# # # Step 3: Create bar graph with months on x-axis and average attendance percentage on y-axis for all students
# # fig, ax = plt.subplots(figsize=(10, 6))
# # ax.bar(average.keys(), average.values())
# # ax.set_xlabel('Month')
# # ax.set_ylabel('Average Attendance Percentage')
# # ax.set_title('Average Attendance Percentage by Month for All Students')
# # plt.show()


from inspect import FrameInfo
from tkinter import messagebox
from tkinter.font import BOLD
import mysql.connector
import tkinter
from tkinter import *

class Login_window:
    def __init__(self, root):
        # ...
        
        # create a database connection
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Shreyash@123",
            database="mydata"
        )
        
        # get the cursor
        self.cursor = self.db.cursor()

        # ...
        
        login_b = Button(FrameInfo, text="Login", font=("times new roman", 15,BOLD),
                          command=self.check_login, bd=3, relief=RIDGE,
                          fg="white", bg="red", activeforeground="white", activebackground="red")
        login_b.place(x=110, y=300, width=120, height=45)

    def check_login(self):
        # get the username and password entered by the user
        username = self.text_user.get()
        password = self.text_passwd.get()

        # prepare the query to fetch the user from the database
        query = "SELECT * FROM register WHERE username = %s AND password = %s"
        values = (username, password)

        # execute the query
        self.cursor.execute(query, values)

        # fetch the user
        user = self.cursor.fetchone()

        if user:
            # if the user is found, show login success message
            messagebox.showinfo("Login Success", "Login successful!")
        else:
            # if the user is not found, show login failed message
            messagebox.showerror("Login Failed", "Invalid username or password.")
