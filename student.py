import datetime
from tkinter import *
from tkinter import ttk
import tkinter as tk
from PIL import ImageTk,Image
from tkinter.font import BOLD #import tkinter module external
import PIL
 #import pillow module externaly
from tkinter import messagebox
import mysql.connector
import cv2
import re
import os
# code to make main window
class Student:
    def __init__(self,r):
        self.root=r
        self.root.geometry("1530x790+0+0")
        self.root.title("FACE RECOGNITION SYSTEM")
        
        # variables
        self.var_department=StringVar()
        self.var_gender=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_stud_id=StringVar()
        self.var_name=StringVar()
        self.var_roll_no=StringVar()
        self.var_phone_no=StringVar()
        self.var_address=StringVar()
        self.var_country=StringVar()
        self.var_birth=StringVar()
        self.var_cast=StringVar()
        self.var_enrollment=StringVar()
        self.var_teacher_n=StringVar()
        self.var_radiobutton1=StringVar()
                                      

        # image 1 code

        img=Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\stud.jpeg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photo=ImageTk.PhotoImage(img)

        f_label=Label(self.root,image=self.photo)
        f_label.place(x=0,y=0,width=500,height=130)

        # image 2 code

        img1=Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\images.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photo1=ImageTk.PhotoImage(img1)

        f_label=Label(self.root,image=self.photo1)
        f_label.place(x=500,y=0,width=500,height=130)

        # image 3 code
        img2=Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\mach.jpeg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photo2=ImageTk.PhotoImage(img2)

        f_label=Label(self.root,image=self.photo2)
        f_label.place(x=1000,y=0,width=540,height=130)
        # bg img
        img3=Image.open(r"C:\Users\hp\OneDrive\Desktop\NOTES\face recognition\back.jpeg")
        img3=img3.resize((1530,710),Image.LANCZOS)
        self.photo3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photo3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        # title=lab=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        # title.place(x=0,y=0,width=1530,height=45)
        title_text = "STUDENT MANAGEMENT SYSTEM"
        title = Label(bg_img, font=("times new roman", 35, "bold"), bg="white", fg="red")
        title.place(x=0, y=0, width=1530, height=55)

        def update_title_text(index=0):
            if index >= len(title_text):
                return
            title.config(text=title_text[:index+1])
            title.after(100, lambda: update_title_text(index+1))

        update_title_text()
        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1510,height=590)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,BOLD))
        left_frame.place(x=10,y=10,width=660,height=570)
        

        #current course info frame
        current_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Cousrse Information",font=("times new roman",12,BOLD))
        current_frame.place(x=5,y=10,width=650,height=150)

        # department
        dept_label=Label(current_frame,text="Department",font=("times new roman",12,BOLD),bg="white")
        dept_label.grid(row=0,column=0,padx=10)

        dept_combo=ttk.Combobox(current_frame,textvariable=self.var_department,font=("times new roman",12,BOLD),state="readonly")
        dept_combo["values"]=("select department","Computer","Mechnical","Civil","Electrical","Aritficial--Intelligence")
        dept_combo.current(0)
        dept_combo.grid(row=0, column=1,padx=4,pady=10,sticky=W)
        
        # gender
        gender_label=Label(current_frame,text="Gender",font=("times new roman",12,BOLD),bg="white")
        gender_label.grid(row=0,column=2,padx=10)

        gender_combo=ttk.Combobox(current_frame,textvariable=self.var_gender,font=("times new roman",12,BOLD),state="readonly")
        gender_combo["values"]=("select gender","Male","Female")
        gender_combo.current(0)
        gender_combo.grid(row=0, column=3,padx=4,pady=10,sticky=W)
        
        # year
        year_label=Label(current_frame,text="Year",font=("times new roman",12,BOLD),bg="white")
        year_label.grid(row=1,column=0,padx=10)

        year_combo=ttk.Combobox(current_frame,textvariable=self.var_year,font=("times new roman",12,BOLD),state="readonly")
        year_combo["values"]=("select year","FY","SY","TY","BE","B-TECH","M-TECH")
        year_combo.current(0)
        year_combo.grid(row=1, column=1,padx=4,pady=10,sticky=W)

        # semester
        semester_label=Label(current_frame,text="Semester",font=("times new roman",12,BOLD),bg="white")
        semester_label.grid(row=1,column=2,padx=10)

        semester_combo=ttk.Combobox(current_frame,textvariable=self.var_semester,font=("times new roman",12,BOLD),state="readonly")
        semester_combo["values"]=("select semester","1-SEM","2-SEM","3-SEM","4-SEM","5-SEM","6-SEM")
        semester_combo.current(0)
        semester_combo.grid(row=1, column=3,padx=4,pady=10,sticky=W)

        #class student info frame
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class Student Information",font=("times new roman",12,BOLD))
        class_student_frame.place(x=5,y=160,width=650,height=380)

        # student id label
        stud_id_label=Label(class_student_frame,text="Student ID",font=("times new roman",12,BOLD),bg="white")
        stud_id_label.grid(row=0,column=0,padx=10)

        student_id=ttk.Entry(class_student_frame,textvariable=self.var_stud_id,width=20,font=("times new roman",12,BOLD))
        student_id.grid(row=0,column=1,padx=4,pady=10,sticky=W)
      

          # student name label
        stud_name_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,BOLD),bg="white")
        stud_name_label.grid(row=0,column=2,padx=10)

        student_name=ttk.Entry(class_student_frame,textvariable=self.var_name,width=20,font=("times new roman",12,BOLD))
        student_name.grid(row=0,column=3,padx=4,pady=10,sticky=W)
        
 
          # student roll no label
        stud_roll_label=Label(class_student_frame,text="ROll--No  ",font=("times new roman",12,BOLD),bg="white")
        stud_roll_label.grid(row=1,column=0,padx=10)

        student_roll=ttk.Entry(class_student_frame,textvariable=self.var_roll_no,width=20,font=("times new roman",12,BOLD))
        student_roll.grid(row=1,column=1,padx=4,pady=10,sticky=W)
      
          
          # student phone no label
        stud_phone_label=Label(class_student_frame,text="Phone No",font=("times new roman",12,BOLD),bg="white")
        stud_phone_label.grid(row=1,column=2,padx=10)

        student_phone=ttk.Entry(class_student_frame,textvariable=self.var_phone_no,width=20,font=("times new roman",12,BOLD))
        student_phone.grid(row=1,column=3,padx=4,pady=10,sticky=W)
       

          # student address label
        stud_address_label=Label(class_student_frame,text="Student Address",font=("times new roman",12,BOLD),bg="white")
        stud_address_label.grid(row=2,column=0,padx=10)

        student_address=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",12,BOLD))
        student_address.grid(row=2,column=1,padx=4,pady=10,sticky=W)
     
        
          # student country label
        stud_country_label=Label(class_student_frame,text="Student country",font=("times new roman",12,BOLD),bg="white")
        stud_country_label.grid(row=2,column=2,padx=10)

        student_country=ttk.Entry(class_student_frame,textvariable=self.var_country,width=20,font=("times new roman",12,BOLD))
        student_country.grid(row=2,column=3,padx=4,pady=10,sticky=W)
        

          # Date_Of_Birth label
        stud_birth_label=Label(class_student_frame,text="Date_Of_Birth",font=("times new roman",12,BOLD),bg="white")
        stud_birth_label.grid(row=3,column=0,padx=10)

        student_birth=ttk.Entry(class_student_frame,textvariable=self.var_birth,width=20,font=("times new roman",12,BOLD))
        student_birth.grid(row=3,column=1,padx=4,pady=10,sticky=W)
     

          # student cast
        stud_cast_label=Label(class_student_frame,text="Student cast",font=("times new roman",12,BOLD),bg="white")
        stud_cast_label.grid(row=3,column=2,padx=10)

        student_cast=ttk.Entry(class_student_frame,textvariable=self.var_cast,width=20,font=("times new roman",12,BOLD))
        student_cast.grid(row=3,column=3,padx=4,pady=10,sticky=W)
        

          # student enrollnemt no
        stud_enroll_label=Label(class_student_frame,text="Enrollment no",font=("times new roman",12,BOLD),bg="white")
        stud_enroll_label.grid(row=4,column=0,padx=10)

        student_enroll=ttk.Entry(class_student_frame,textvariable=self.var_enrollment,width=20,font=("times new roman",12,BOLD))
        student_enroll.grid(row=4,column=1,padx=4,pady=10,sticky=W)
    

          # teacher name
        stud_teacher_name_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",12,BOLD),bg="white")
        stud_teacher_name_label.grid(row=4,column=2,padx=10)

        student_teacher_name=ttk.Entry(class_student_frame,textvariable=self.var_teacher_n,width=20,font=("times new roman",12,BOLD))
        student_teacher_name.grid(row=4,column=3,padx=4,pady=10,sticky=W)
        
        # radio buttons
        self.var_radiobutton1=StringVar()
        Radiobutton1=ttk.Radiobutton(class_student_frame,variable=self.var_radiobutton1,text="Take photo sample",value="yes")
        Radiobutton1.grid(row=6,column=0)

       
        Radiobutton2=ttk.Radiobutton(class_student_frame,variable=self.var_radiobutton1,text="No photo sample",value="no")
        Radiobutton2.grid(row=6,column=1)
        # buttons frame1
        button_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button_frame.place(x=0,y=255,width=650,height=40)
        # save button
        save_btn=Button(button_frame,text="save",command=self.Add_data,font=("times new roman",12,BOLD),width=17,bg="blue",fg="white")
        save_btn.grid(row=0,column=0) 
        # update button
        u_btn=Button(button_frame,text="update",command=self.update_data,font=("times new roman",12,BOLD),width=17,bg="blue",fg="white")
        u_btn.grid(row=0,column=2)
        # delete button
        d_btn=Button(button_frame,text="delete",command=self.delete_data,font=("times new roman",12,BOLD),width=17,bg="blue",fg="white")
        d_btn.grid(row=0,column=3)
        # reset button
        r_btn=Button(button_frame,text="reset",command=self.reset_data,font=("times new roman",12,BOLD),width=17,bg="blue",fg="white")
        r_btn.grid(row=0,column=4)  
           # buttons frame2
        button1_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        button1_frame.place(x=0,y=300,width=650,height=40)
        # take photo
        t_btn=Button(button1_frame,text="Take photo sample",command=self.Take_photo,font=("times new roman",12,BOLD),width=35,bg="blue",fg="white")
        t_btn.grid(row=1,column=0)
        # do not take photo
        do_not_btn=Button(button1_frame,text="Update photo sample",command=self.update_photo_sample,font=("times new roman",12,BOLD),width=35,bg="blue",fg="white")
        do_not_btn.grid(row=1,column=3)

        
        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Database",font=("times new roman",12,BOLD))
        right_frame.place(x=680,y=10,width=820,height=570)
        #================================searching system==========================================================

        s_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",12,BOLD))
        s_frame.place(x=5,y=5,width=810,height=70)
      
      # search label and combo-box
        search_label=Label(s_frame,text="Search By:",font=("times new roman",12,BOLD),bg="red",fg="white")
        search_label.grid(row=0,column=0,padx=10,sticky=W)

        search_combo=ttk.Combobox(s_frame,font=("times new roman",12,BOLD),state="readonly")
        search_combo["values"]=("select","Roll-no","phone no")
        search_combo.current(0)
        search_combo.grid(row=0, column=1,padx=4,pady=10,sticky=W)

        search_entry=ttk.Entry(s_frame,width=20,font=("times new roman",12,BOLD))
        search_entry.grid(row=0,column=2,padx=4,pady=10,sticky=W)

         #search button
        search_btn=Button(s_frame,text="Search",font=("times new roman",12,BOLD),width=17,bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=8) 
        
         # show all button
        showAll_btn=Button(s_frame,text="Show-ALL",font=("times new roman",12,BOLD),width=17,bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4) 

        # database frame
        database_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        database_frame.place(x=5,y=80,width=810,height=460)

        scroll_x=ttk.Scrollbar(database_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(database_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(database_frame,column=("Department","Gender","Year","Semester","ID","Name","Roll-no","phone-no","address","country","Date_Of_Birth","cast","Enrollment-no","Teacher name","Photo_sample"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("Department",text="Department")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Semester",text="Semester")
        self.student_table.heading("ID",text="ID")
        self.student_table.heading("Name",text="Name")
        self.student_table.heading("Roll-no",text="Roll-no")
        self.student_table.heading("phone-no",text="phone-no")
        self.student_table.heading("address",text="address")
        self.student_table.heading("country",text="country")
        self.student_table.heading("Date_Of_Birth",text="Date_Of_Birth")
        self.student_table.heading("cast",text="cast")
        self.student_table.heading("Enrollment-no",text="Enrollment-no")
        self.student_table.heading("Teacher name",text="Teacher name")
        self.student_table.heading("Photo_sample",text="Photo_sample")

        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_coursor)
        self.fetch_data()


        # ==============================================for search button=========================================================

#  =============================== data function definition+================================================================

    def Add_data(self):
        if self.var_department.get()=="select department" or self.var_gender.get() == "select gender"  or self.var_year.get() == "select year" or self.var_semester.get() == "select semester" or self.var_stud_id.get()  =="" or self.var_name.get() =="" or self.var_roll_no.get() =="" or self.var_phone_no.get() =="" or self.var_address.get()== "" or self.var_country.get()=="" or self.var_birth.get()=="" or self.var_cast.get()=="" or self.var_enrollment.get()=="" or self.var_teacher_n.get()=="" or self.var_radiobutton1.get()=="":
            messagebox.showerror("Error","ALL FIELD'S ARE REQUIRED !!!!!",parent=self.root)
        else:
          try:
            conn=mysql.connector.Connect(host="localhost",user="root",passwd="Shreyash@123",database="mydata")
            mycursor=conn.cursor(buffered=True)
            mycursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",( 
                                                                                                            self.var_department.get(),
                                                                                                            self.var_gender.get(),
                                                                                                            self.var_year.get(),
                                                                                                            self.var_semester.get(),
                                                                                                            self.var_stud_id.get(),
                                                                                                            self.var_name.get(),
                                                                                                            self.var_roll_no.get(),
                                                                                                            self.var_phone_no.get(),
                                                                                                            self.var_address.get(),
                                                                                                            self.var_country.get(),
                                                                                                            self.var_birth.get(),
                                                                                                            self.var_cast.get(),
                                                                                                            self.var_enrollment.get(),
                                                                                                            self.var_teacher_n.get(),
                                                                                                            self.var_radiobutton1.get()
                                                                                                           
                                                                                                          ))
            conn.commit()
            self.fetch_data()
            conn.close()
              
    
            
            messagebox.showinfo("Success","Student details has been added  successfully",parent=self.root)
          except Exception as es:
            messagebox.showerror("Error",f"Due to :{str(es)}",parent=self.root)
    # =================fetch data function========================
    def fetch_data(self):
          conn=mysql.connector.Connect(host="localhost",user="root",passwd="Shreyash@123",database="mydata")
          mycursor=conn.cursor()
          mycursor.execute("select * from student")
          data=mycursor.fetchall()

          if len(data)!=0:
                self.student_table.delete(*self.student_table.get_children())
                for i in data:
                      self.student_table.insert("",END,values=i)
          conn.commit()
          conn.close()
    # ========get cursor=================
    def get_coursor(self,event=""):
          focus=self.student_table.focus()
          content=self.student_table.item(focus)
          data_c=content["values"]
          self.var_department.set(data_c[0]),
          self.var_gender.set(data_c[1]),
          self.var_year.set(data_c[2]),
          self.var_semester.set(data_c[3]),
          self.var_stud_id.set(data_c[4]),
          self.var_name.set(data_c[5]),
          self.var_roll_no.set(data_c[6]),
          self.var_phone_no.set(data_c[7]),
          self.var_address.set(data_c[8]),
          self.var_country.set(data_c[9]),
          self.var_birth.set(data_c[10]),
          self.var_cast.set(data_c[11]),
          self.var_enrollment.set(data_c[12]),
          self.var_teacher_n.set(data_c[13]),
          self.var_radiobutton1.set(data_c[14])

    # update function

    def update_data(self):
      if self.var_department.get()=="select department" or self.var_gender.get() == "select gender"  or self.var_year.get() == "select year" or self.var_semester.get() == "select semester" or self.var_stud_id.get()  =="" or self.var_name.get() =="" or self.var_roll_no.get() =="" or self.var_phone_no.get() =="" or self.var_address.get()== "" or self.var_country.get()=="" or self.var_birth.get()=="" or self.var_cast.get()=="" or self.var_enrollment.get()=="" or self.var_teacher_n.get()=="" or self.var_radiobutton1.get()=="":
          messagebox.showerror("Error","ALL FIELD'S ARE REQUIRED !!!!!",parent=self.root)
      else:
        try:

          update=messagebox.askyesno("Update","Do you want to update the student details",parent=self.root)
          if update>0:
            conn=mysql.connector.Connect(host="localhost",user="root",passwd="Shreyash@123",database="mydata")
            mycursor=conn.cursor()
            mycursor.execute("update student set var_department=%s,var_gender=%s,var_year=%s,var_Semester=%s,var_name=%s,var_roll_no=%s,var_phone_no=%s,var_address=%s,var_country=%s,var_birth=%s,var_cast=%s,var_enrollment=%s,var_teacher_n=%s,var_radiobutton1=%s where var_stud_id=%s",(
                                                                                                                                                                                                                                                          self.var_department.get(),
                                                                                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                                                                                          self.var_semester.get(),
                                                                                                                                                                                                                                                          self.var_name.get(),
                                                                                                                                                                                                                                                          self.var_roll_no.get(),
                                                                                                                                                                                                                                                          self.var_phone_no.get(),
                                                                                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                                                                                          self.var_country.get(),
                                                                                                                                                                                                                                                          self.var_birth.get(),
                                                                                                                                                                                                                                                          self.var_cast.get(),
                                                                                                                                                                                                                                                          self.var_enrollment.get(),
                                                                                                                                                                                                                                                          self.var_teacher_n.get(),
                                                                                                                                                                                                                                                          self.var_radiobutton1.get(),
                                                                                                                                                                                                                                                          self.var_stud_id.get()
                                                                                                                                                                                                                                                          ))
          else:
            if not update:
     
              return
          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Success","student details successfully updated",parent=self.root)
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)

  #  delete funciton
    # def delete_data(self):
    #   if self.var_stud_id.get() =="":
    #     messagebox.showerror("Error","Student Id Must be Required",parent=self.root)
    #   else:
    #     try:
    #       delete=messagebox.askyesno("Student delete page","Do you want to delete student details",parent=self.root)
    #       if delete>0:
    #         conn=mysql.connector.Connect(host="localhost",user="root",passwd="Shreyash@123",database="mydata")
    #         mycursor=conn.cursor()
    #         sql="delete from student where Student_id=%s"
    #         val=(self.var_stud_id.get(),)
    #         mycursor.execute(sql,val)
    #       else:
    #         if not delete:
    #           return
    #       conn.commit()
    #       self.fetch_data()
    #       conn.close()
    #       messagebox.showinfo("Delete","successfully data deleted",parent=self.root)
    #     except Exception as es:
    #       messagebox.showerror("error",f"Due to:{str(es)},",parent=self.root)


  

    def delete_data(self):
        if self.var_stud_id.get() == "":
            messagebox.showerror("Error","Student Id Must be Required",parent=self.root)
        else:
            try:
                delete = messagebox.askyesno("Student delete page", "Do you want to delete student details", parent=self.root)
                if delete > 0:
                    conn = mysql.connector.Connect(host="localhost", user="root", passwd="Shreyash@123", database="mydata")
                    mycursor = conn.cursor()
                    # get the student's image file names from the database
                    mycursor.execute("SELECT var_stud_id FROM student WHERE var_stud_id = %s", (self.var_stud_id.get(),))
                    var_stud_id = mycursor.fetchone()
                    if var_stud_id is not None:
                        # remove the student's image files from the directory
                        for i in range(1, 101):
                            image_path = os.path.join('fphotos', f'user.{var_stud_id[0]}.{i}.jpg')
                            if os.path.exists(image_path):
                                os.remove(image_path)
                        # delete the student's data from the database
                        sql = "DELETE FROM student WHERE var_stud_id=%s"
                        val = (self.var_stud_id.get(),)
                        mycursor.execute(sql, val)
                        conn.commit()
                        self.fetch_data()
                        conn.close()
                        messagebox.showinfo("Delete", "Successfully deleted data", parent=self.root)
                    else:
                        messagebox.showerror("Error", f"Student with id {self.var_stud_id.get()} does not exist", parent=self.root)
                else:
                    if not delete:
                        return
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)



  #  reset button
    def reset_data(self):
          self.var_department.set("select department")
          self.var_gender.set("select gender")
          self.var_year.set("select year")
          self.var_semester.set("select semester")
          self.var_stud_id.set("")
          self.var_name.set("")
          self.var_roll_no.set("")
          self.var_phone_no.set("")
          self.var_address.set("")
          self.var_country.set("")
          self.var_birth.set("")
          self.var_cast.set("")
          self.var_enrollment.set("")
          self.var_teacher_n.set("")
          self.var_radiobutton1.set("")

  # ================Generate data set or take a photo smaples =======================
    def Take_photo(self):
          if self.var_department.get()=="select department" or self.var_gender.get() == "select gender"  or self.var_year.get() == "select year" or self.var_semester.get() == "select semester" or self.var_stud_id.get()  =="" or self.var_name.get() =="" or self.var_roll_no.get() =="" or self.var_phone_no.get() =="" or self.var_address.get()== "" or self.var_country.get()=="" or self.var_birth.get()=="" or self.var_cast.get()=="" or self.var_enrollment.get()=="" or self.var_teacher_n.get()=="" or self.var_radiobutton1.get()=="":
                messagebox.showerror("Error","ALL FIELD'S ARE REQUIRED !!!!!",parent=self.root)
          else:
                try:
                  conn=mysql.connector.Connect(host="localhost",user="root",passwd="Shreyash@123",database="mydata")
                  mycursor=conn.cursor()
                  # Use the actual student ID entered in the form for dataset labels
                  id=self.var_stud_id.get()
                  mycursor.execute("update student set var_department=%s,var_gender=%s,var_year=%s,var_Semester=%s,var_name=%s,var_roll_no=%s,var_phone_no=%s,var_address=%s,var_country=%s,var_birth=%s,var_cast=%s,var_enrollment=%s,var_teacher_n=%s,var_radiobutton1=%s where var_stud_id=%s",(
                                                                                                                                                                                                                                                          self.var_department.get(),
                                                                                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                                                                                          self.var_semester.get(),
                                                                                                                                                                                                                                                          self.var_name.get(),
                                                                                                                                                                                                                                                          self.var_roll_no.get(),
                                                                                                                                                                                                                                                          self.var_phone_no.get(),
                                                                                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                                                                                          self.var_country.get(),
                                                                                                                                                                                                                                                          self.var_birth.get(),
                                                                                                                                                                                                                                                          self.var_cast.get(),
                                                                                                                                                                                                                                                          self.var_enrollment.get(),
                                                                                                                                                                                                                                                          self.var_teacher_n.get(),
                                                                                                                                                                                                                                                          self.var_radiobutton1.get(),
                                                                                                                                                                                                                                                          self.var_stud_id.get()
                                                                                                                                                                                                                                                          ))
                  conn.commit()
                  self.fetch_data()
                  self.reset_data()
                  conn.close()
          # ==================load predefined data from frontal face from open cv file===========================
                  face_recog=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                  def face_crop(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_recog.detectMultiScale(gray,1.3,5)
              # scaling factor 1.3
              # minimum neighbor=5 
                        for(x,y,w,h) in faces:
                              face_crop=img[y:y+h,x:x+w]
                              return face_crop

                  cap=cv2.VideoCapture(0)
                  

                  
                  img_id=0
                  while True:
                        ret,my_frame=cap.read()
                        if face_crop(my_frame) is not None:
                          img_id+=1
                          face=cv2.resize(face_crop(my_frame),(450,450))
                          face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                          file_name_path="fphotos/user."+str(id)+"."+str(img_id)+".jpg"
                          cv2.imwrite(file_name_path,face)
                          cv2.putText(face,str(img_id),(200,200),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                          cv2.imshow("Cropped Face",face)
                        
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                  cap.release()
                  cv2.destroyAllWindows()
                  messagebox.showinfo("Result,","Generating Data sets Completed!!!",parent=self.root)
                except Exception as es:
                  messagebox.showerror("error",f"Due to:{str(es)},",parent=self.root)


                  
    def update_photo_sample(self):
        if self.var_department.get()=="select department" or self.var_gender.get() == "select gender"  or self.var_year.get() == "select year" or self.var_semester.get() == "select semester" or self.var_stud_id.get()  =="" or self.var_name.get() =="" or self.var_roll_no.get() =="" or self.var_phone_no.get() =="" or self.var_address.get()== "" or self.var_country.get()=="" or self.var_birth.get()=="" or self.var_cast.get()=="" or self.var_enrollment.get()=="" or self.var_teacher_n.get()=="" or self.var_radiobutton1.get()=="":
                messagebox.showerror("Error","ALL FIELD'S ARE REQUIRED !!!!!",parent=self.root)
        else:
                try:
                  conn=mysql.connector.Connect(host="localhost",user="root",passwd="Shreyash@123",database="mydata")
                  mycursor=conn.cursor()
                  # Use the actual student ID entered in the form for dataset labels
                  id=self.var_stud_id.get()
                  mycursor.execute("update student set Department=%s,Gender=%s,year=%s,Semester=%s,Student_name=%s,Roll_no=%s,Phone_no=%s,Student_address=%s,Country=%s,Date_Of_Birth=%s,Cast=%s,Enrollment_no=%s,Teacher_name=%s,Photo_sample=%s where Student_id=%s",(
                                                                                                                                                                                                                                                          self.var_department.get(),
                                                                                                                                                                                                                                                          self.var_gender.get(),
                                                                                                                                                                                                                                                          self.var_year.get(),
                                                                                                                                                                                                                                                          self.var_semester.get(),
                                                                                                                                                                                                                                                          self.var_name.get(),
                                                                                                                                                                                                                                                          self.var_roll_no.get(),
                                                                                                                                                                                                                                                          self.var_phone_no.get(),
                                                                                                                                                                                                                                                          self.var_address.get(),
                                                                                                                                                                                                                                                          self.var_country.get(),
                                                                                                                                                                                                                                                          self.var_birth.get(),
                                                                                                                                                                                                                                                          self.var_cast.get(),
                                                                                                                                                                                                                                                          self.var_enrollment.get(),
                                                                                                                                                                                                                                                          self.var_teacher_n.get(),
                                                                                                                                                                                                                                                          self.var_radiobutton1.get(),
                                                                                                                                                                                                                                                          self.var_stud_id.get()
                                                                                                                                                                                                                                                          ))
                  conn.commit()
                  self.fetch_data()
                  self.reset_data()
                  conn.close()
          # ==================load predefined data from frontal face from open cv file===========================
                  face_recog=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                
                  def face_crop(img):
                        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                        faces=face_recog.detectMultiScale(gray,1.3,5)
              # scaling factor 1.3
              # minimum neighbor=5 
                        for(x,y,w,h) in faces:
                              face_crop=img[y:y+h,x:x+w]
                              return face_crop

                  cap=cv2.VideoCapture(0)
                  

                  
                  img_id=0
                  while True:
                        ret,my_frame=cap.read()
                        if face_crop(my_frame) is not None:
                          img_id+=1
                          face=cv2.resize(face_crop(my_frame),(450,450))
                          face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                          file_name_path="fphotos/user."+str(id)+"."+str(img_id)+".jpg"
                          cv2.imwrite(file_name_path,face)
                          cv2.putText(face,str(img_id),(200,200),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                          cv2.imshow("Cropped Face",face)
                        
                        if cv2.waitKey(1)==13 or int(img_id)==100:
                            break
                  cap.release()
                  cv2.destroyAllWindows()
                  messagebox.showinfo("Result,","Generating Data sets Completed!!!",parent=self.root)
                except Exception as es:
                  messagebox.showerror("error",f"Due to:{str(es)},",parent=self.root)


if __name__=="__main__":
      
      root=Tk()
      a=Student(root)
      root.mainloop()
