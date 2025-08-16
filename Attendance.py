from tkinter import *
from tkinter import ttk
from tkinter.font import BOLD #import tkinter module externaly
from PIL import Image,ImageTk #import pillow module externaly
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog


mydata=[]
# code to make main window
class Attendance:
    def __init__(self,r):
        self.root=r
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
       
       
       ###########################variables===================================
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()

                # image 1 code

        img=Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\stud.jpeg")
        img=img.resize((800,200),Image.LANCZOS)
        self.photo=ImageTk.PhotoImage(img)

        f_label=Label(self.root,image=self.photo)
        f_label.place(x=0,y=0,width=800,height=200)

        # image 2 code

        file_path = r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\images.jpg"
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        img1 = Image.open(file_path)
        img1 = img1.resize((800, 200), Image.LANCZOS)
        self.photo1 = ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photo1)
        f_label.place(x=800,y=0,width=800,height=200)
    # bg img
        img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\back.jpeg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photo3)
        bg_img.place(x=0,y=220,width=1530,height=710)

        # title=lab=Label(bg_img,text="ATTENDANCE MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        # title.place(x=0,y=0,width=1530,height=45)
        title_text = "ATTENDENCE  MANAGEMENT  SYSTEM "
        title = Label(bg_img, font=("times new roman", 35, "bold"), bg="white", fg="red")
        title.place(x=0, y=0, width=1530, height=55)

        def update_title_text(index=0):
            if index >= len(title_text):
                return
            title.config(text=title_text[:index+1])
            title.after(100, lambda: update_title_text(index+1))

        update_title_text()
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(y=55,width=1520,height=590)

         # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Attendance Details",font=("times new roman",12,BOLD))
        left_frame.place(x=10,y=10,width=660,height=485)

          # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Database",font=("times new roman",12,BOLD))
        right_frame.place(x=680,y=10,width=825,height=485)

        # ROllno label
        Roll_no_id_label=Label(left_frame,text="Roll--NO:",font=("times new roman",12,BOLD),bg="white")
        Roll_no_id_label.grid(row=0,column=0,padx=10)

        Roll_no_id=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_roll,font=("times new roman",12,BOLD))
        Roll_no_id.grid(row=0,column=1,padx=4,pady=10,sticky=W)

        #   # Student_id label
        # student_id_label=Label(left_frame,text="Student-ID:",font=("times new roman",12,BOLD),bg="white")
        # student_id_label.grid(row=0,column=2,padx=10)

        # student_id=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_id,font=("times new roman",12,BOLD))
        # student_id.grid(row=0,column=3,padx=4,pady=10,sticky=W)
          
          # Name label
        Name_label=Label(left_frame,text="Name:",font=("times new roman",12,BOLD),bg="white")
        Name_label.grid(row=0,column=2,padx=10)

        Name_id=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_name,font=("times new roman",12,BOLD))
        Name_id.grid(row=0,column=3,padx=4,pady=10,sticky=W)
          
          # department label
        dep_id_label=Label(left_frame,text="Department:",font=("times new roman",12,BOLD),bg="white")
        dep_id_label.grid(row=1,column=0,padx=10)

        dep_id=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_dep,font=("times new roman",12,BOLD))
        dep_id.grid(row=1,column=1,padx=4,pady=10,sticky=W)

         # date label
        date_label=Label(left_frame,text="Date:",font=("times new roman",12,BOLD),bg="white")
        date_label.grid(row=1,column=2,padx=10)

        date_id=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_date,font=("times new roman",12,BOLD))
        date_id.grid(row=1,column=3,padx=4,pady=10,sticky=W)
          # time label
        Time_label=Label(left_frame,text="Time:",font=("times new roman",12,BOLD),bg="white")
        Time_label.grid(row=2,column=0,padx=10)

        Time_id=ttk.Entry(left_frame,width=20,textvariable=self.var_atten_time,font=("times new roman",12,BOLD))
        Time_id.grid(row=2,column=1,padx=4,pady=10,sticky=W)
          # attendance status
        attendance_label=Label(left_frame,text="Attendance Status:",font=("times new roman",12,BOLD),bg="white")
        attendance_label.grid(row=2,column=2,padx=10)

        # combobox
        self.combo_id_type=ttk.Combobox(left_frame,textvariable=self.var_atten_attendance,font=("times new roman",12),justify="center",state="readonly",width=18)
        self.combo_id_type["values"]=("Status","Present","Absent")
        self.combo_id_type.grid(row=2,column=3,padx=4,pady=10,sticky=W)
        self.combo_id_type.current(0)

        # buttons frame1
        button_frame=Frame(left_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=215,width=650,height=40)
        # import button
        import_btn=Button(button_frame,text="Import",command=self.Importcsv,font=("times new roman",12,BOLD),width=17,bg="blue",fg="white")
        import_btn.grid(row=0,column=0) 
        # export button
        ex_btn=Button(button_frame,text="Export",command=self.exportcsv,font=("times new roman",12,BOLD),width=17,bg="blue",fg="white")
        ex_btn.grid(row=0,column=2)
        # update button
        up_btn=Button(button_frame,text="Udpate",command=self.update_data,font=("times new roman",12,BOLD),width=17,bg="blue",fg="white")
        up_btn.grid(row=0,column=3)
        # reset button
        r_btn=Button(button_frame,text="Reset",command=self.reset,font=("times new roman",12,BOLD),width=17,bg="blue",fg="white")
        r_btn.grid(row=0,column=4)  

        
        # image 1 code

        img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\stud.jpeg")
        img3=img3.resize((800,200),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        f_label=Label(left_frame,image=self.photo3)
        f_label.place(x=0,y=260,width=650,height=200)

        # Table frame
        Table_frame=LabelFrame(right_frame,bd=2,bg="white")
        Table_frame.place(x=5,y=5,width=812,height=455)
        
        scroll_x=ttk.Scrollbar(Table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame,orient=VERTICAL)

        self.AttendanceReportTable=ttk.Treeview(Table_frame,column=("Name","Roll--NO","Department","Time","Date","Attendance_Status"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

       
        # self.AttendanceReportTable.heading("Student_ID",text="Student_ID")
        self.AttendanceReportTable.heading("Name",text="Name")
        self.AttendanceReportTable.heading("Roll--NO",text="Roll--NO")
        self.AttendanceReportTable.heading("Department",text="Department")
        self.AttendanceReportTable.heading("Time",text="Time")
        self.AttendanceReportTable.heading("Date",text="Date")
        self.AttendanceReportTable.heading("Attendance_Status",text="Attendance_Status")
        
        
        self.AttendanceReportTable["show"]="headings"
        self.AttendanceReportTable.column("Name",width=100)
        self.AttendanceReportTable.column("Roll--NO",width=100)
        # self.AttendanceReportTable.column("Student_ID",width=100)
        
        self.AttendanceReportTable.column("Department",width=100)
        self.AttendanceReportTable.column("Time",width=100)
        self.AttendanceReportTable.column("Date",width=100)
        self.AttendanceReportTable.column("Attendance_Status",width=100)
        self.AttendanceReportTable.pack(fill=BOTH,expand=1)
        
        self.AttendanceReportTable.bind("<ButtonRelease>",self.get_cursor)
        # =======================================fetch data=================================
    def fetchData(self,rows):
      self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
      for i in rows:
         self.AttendanceReportTable.insert("",END,values=i)
        
    def Importcsv(self):
      global mydata
      mydata.clear()
      fin=filedialog.askopenfilename(initialdir=os.getcwd(),title='opencsv',filetypes=(("CSV FILE","*.csv"),("ALL FILE","*.*")),parent=self.root)
      with open(fin) as myfile:
        csvread=csv.reader(myfile,delimiter=",")
        for i in csvread:
          mydata.append(i)
          self.fetchData(mydata)
          
    def exportcsv(self):
      try:
             if len(mydata)<1:
                 messagebox.showerror("No Data Found"," Please select the valid file",parent=self.root)
                 return False
             fin=filedialog.asksaveasfilename(initialdir=os.getcwd(),title='opencsv',filetypes=(("CSV FILE","*.csv"),("ALL FILE","*.*")),parent=self.root)
             with open(fin,mode='w',newline="") as myfile:
                 exp_write=csv.writer(myfile,delimiter=",")
                 for i in mydata:
                     exp_write.writerow(i)
                 messagebox.showinfo("data export","Your data exported with File name  "+os.path.basename(fin)+"   successfully")
                        
      except Exception as es:
         messagebox.showerror("error",f"due to :{str(es)}",parent=self.root)
                            
    
    def get_cursor(self,event=""):
         cursor_row=self.AttendanceReportTable.focus()
         content=self.AttendanceReportTable.item(cursor_row)
         rows=content['values']
         self.var_atten_name.set(rows[0])
         self.var_atten_roll.set(rows[1])
         self.var_atten_dep.set(rows[2])
      
         self.var_atten_time.set(rows[3])
         self.var_atten_date.set(rows[4])
         self.var_atten_attendance.set(rows[5])

    def reset(self):
        self.var_atten_name.set("")
        self.var_atten_roll.set("")
        self.var_atten_dep.set("")
      
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")
        self.var_atten_id.set("")
    

    # def update_data(self):
    #   if self.var_atten_name.get()=="" or self.var_atten_roll.get() == ""  or self.var_atten_dep.get() == "" or self.var_atten_time.get() =="" or self.var_atten_date.get()  =="" or self.var_atten_attendance.get() =="":
    #       messagebox.showerror("Error","ALL FIELD'S ARE REQUIRED !!!!!",parent=self.root)
    #   else:
    #       try:
    #           update = messagebox.askyesno("Update","Do you want to update the student details",parent=self.root)
    #           if update:
    #               # Check if the record already exists
    #               rollno = self.var_atten_roll.get()
    #               name = self.var_atten_name.get()
    #               existing_record = None
    #               for record in mydata:
    #                   if record[0] == rollno and record[1] == name:
    #                       existing_record = record
    #                       break
    #               if existing_record:
    #                   # Update existing record
    #                   index = mydata.index(existing_record)
    #                   mydata[index] = [self.var_atten_name.get(), self.var_atten_roll.get(), self.var_atten_dep.get(), self.var_atten_time.get(), self.var_atten_date.get(), self.var_atten_attendance.get()]

    #                   # Write updated data to CSV file
    #                   with open('mega.csv', mode='w', newline='') as myfile:
    #                       exp_write = csv.writer(myfile, delimiter=',')
    #                       for i in mydata:
    #                           exp_write.writerow(i)

    #                   self.fetchData(mydata)
    #                   messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
    #               else:
    #                   # Add new record
    #                   new_record = [self.var_atten_name.get(), self.var_atten_roll.get(), self.var_atten_dep.get(), self.var_atten_time.get(), self.var_atten_date.get(), self.var_atten_attendance.get()]
    #                   mydata.append(new_record)

    #                   # Write updated data to CSV file
    #                   with open('mega.csv', mode='a', newline='') as myfile:
    #                       exp_write = csv.writer(myfile, delimiter=',')
    #                       exp_write.writerow(new_record)

    #                   self.fetchData(mydata)
    #                   messagebox.showinfo("Success","New student record added successfully",parent=self.root)
    #       except Exception as es:
    #           messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)
    def update_data(self):
      if self.var_atten_name.get()=="" or self.var_atten_roll.get() == ""  or self.var_atten_dep.get() == "" or self.var_atten_time.get() =="" or self.var_atten_date.get()  =="" or self.var_atten_attendance.get() =="":
          messagebox.showerror("Error","ALL FIELD'S ARE REQUIRED !!!!!",parent=self.root)
      else:
          try:
              with open('mega.csv', mode='r') as f:
                  reader = csv.reader(f)
                  mydata = list(reader)

              roll_no = self.var_atten_roll.get()
              name = self.var_atten_name.get()
              
              
              
              
              updated = False

              for i in range(len(mydata)):
                  if mydata[i][0] == name and mydata[i][1] == roll_no:
                      mydata[i][2] = self.var_atten_dep.get()
                      mydata[i][3] = self.var_atten_time.get()
                      mydata[i][4] = self.var_atten_date.get()
                      mydata[i][5] = self.var_atten_attendance.get()
                      updated = True
                      break

              if not updated:
                  
                  mydata.append([ self.var_atten_name.get(),self.var_atten_roll.get(), self.var_atten_dep.get(), self.var_atten_time.get(), self.var_atten_date.get(), self.var_atten_attendance.get()])

              with open('mega.csv', mode='w', newline='') as myfile:
                  exp_write = csv.writer(myfile, delimiter=',')
                  for i in mydata:
                      exp_write.writerow(i)

              self.fetchData(mydata)
              if updated:
                  messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
              else:
                  messagebox.showinfo("Success","New student details successfully added",parent=self.root)
          except Exception as es:
              messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)



if __name__=="__main__":
    root=Tk()
    a=Attendance(root)
    root.mainloop()
