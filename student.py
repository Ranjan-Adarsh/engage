from cProfile import label
from email import message
import tkinter as tk
from tkinter import *
from tkinter import ttk
from turtle import left, right
from PIL import Image,ImageTk
#from matplotlib.pyplot import ticklabel_format
import mysql.connector
from tkinter import messagebox
import cv2
from time import strftime
from datetime import datetime

SQL_USER="root"
SQL_SERVER_PASSWORD="Rasengan08.."
SQL_HOST="localhost"


class Student(tk.Toplevel):
    def __init__(self,parent):
        super().__init__(parent)
        self.geometry("1530x790+0+0")
        self.title("Student Management System")

         #=============variables=======
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_id=StringVar()
        self.var_name=StringVar()
        self.var_roll=StringVar()
        self.var_email=StringVar()

        self.var_radioButton1=StringVar()
        self.var_radioButton2=StringVar()
        
        main_frame=Frame(self,bd=1)
        main_frame.place(x=0,y=20,width=1500,height=650)

        #left pane
        left_pane=LabelFrame(main_frame,bg="white",bd=2,relief=SUNKEN,text="Student Details",font=("open sans",12,"bold"))
        left_pane.place(x=10,y=10,width=600,height=600)

        #course details

        #department
        departement_label=Label(left_pane,text="Department",font=("open sans",12,"bold"))
        departement_label.grid(row=0,column=1,padx=15,pady=20)

        department_combo=ttk.Combobox(left_pane,textvariable=self.var_dep,font=("open sans",12,"bold"),width=16,state="readonly")
        department_combo['values']=("Select Department","Computer","IT","Electrical","Mechanical")
        department_combo.current(0)
        department_combo.grid(row=0,column=2,padx=2,pady=20)

        #course
        course_label=Label(left_pane,text="Course",font=("open sans",12,"bold"))
        course_label.grid(row=1,column=1,padx=15,sticky=W)

        course_combo=ttk.Combobox(left_pane,textvariable=self.var_course,font=("open sans",12,"bold"),width=16,state="readonly")
        course_combo['values']=("Select Course","ME","CS","MA","BIO")
        course_combo.current(0)
        course_combo.grid(row=1,column=2,padx=2,pady=10)

        #year
        year_label=Label(left_pane,text="Year",font=("open sans",12,"bold"))
        year_label.grid(row=2,column=1,padx=15,sticky=W)

        year_combo=ttk.Combobox(left_pane,textvariable=self.var_year,font=("open sans",12,"bold"),width=16,state="readonly")
        year_combo['values']=("Select Year","2019-20","2020-21","2021-22","2022-23")
        year_combo.current(0)
        year_combo.grid(row=2,column=2,padx=2,pady=10)


        #Class Student Information
        #Student ID
        studentID_label=Label(left_pane,text="Student ID",font=("open sans",12,"bold"),bg="white")
        studentID_label.grid(row=3,column=1,padx=15,pady=10,sticky=W)

        studentID_entry=Entry(left_pane,textvariable=self.var_id,width=20,font=("open sans",12,"bold"))
        studentID_entry.grid(row=3,column=2,padx=5,pady=10,sticky=W)
        #Student Name
        studentName_label=Label(left_pane,text="Student Name",font=("open sans",12,"bold"),bg="white")
        studentName_label.grid(row=4,column=1,padx=15,pady=10,sticky=W)

        studentName_entry=Entry(left_pane,width=20,textvariable=self.var_name,font=("open sans",12,"bold"))
        studentName_entry.grid(row=4,column=2,padx=5,pady=10,sticky=W)

        #Roll Number
        rollNumber_label=Label(left_pane,text="Roll Number",font=("open sans",12,"bold"),bg="white")
        rollNumber_label.grid(row=5,column=1,padx=15,pady=10,sticky=W)

        rollNumber_entry=Entry(left_pane,textvariable=self.var_roll,width=20,font=("open sans",12,"bold"))
        rollNumber_entry.grid(row=5,column=2,padx=5,pady=10,sticky=W)

        #email
        email_label=Label(left_pane,text="Email",font=("open sans",12,"bold"),bg="white")
        email_label.grid(row=6,column=1,padx=15,pady=10,sticky=W)

        email_entry=Entry(left_pane,width=20,textvariable=self.var_email,font=("open sans",12,"bold"))
        email_entry.grid(row=6,column=2,padx=5,pady=10,sticky=W)


        #radio buttons
        radioButton1=ttk.Radiobutton(left_pane,variable=self.var_radioButton1,text="Take Photo Sample",value="Yes")
        radioButton1.grid(row=7,column=0)
        
        radioButton2=ttk.Radiobutton(left_pane,variable=self.var_radioButton1,text="No Photo",value="No")
        radioButton2.grid(row=7,column=1)

        #Buttons frame
        buttonFrame=Frame(left_pane,bd=2,relief=RIDGE)
        buttonFrame.place(x=0,y=450,width=580,height=50)

        save_btn=Button(buttonFrame,text="Save",command=self.add_data,width=13,font=("open sans",12,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0,padx=2)

        update_btn=Button(buttonFrame,text="Update",command=self.update_data,width=13,font=("open sans",12,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1,padx=2)

        delete_btn=Button(buttonFrame,text="Delete",command=self.delete_data,width=13,font=("open sans",12,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2,padx=2)

        reset_btn=Button(buttonFrame,text="Reset",command=self.reset_data,width=13,font=("open sans",12,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3,padx=2)

        buttonFrame2=Frame(left_pane,bd=2,relief=RIDGE)
        buttonFrame2.place(x=0,y=500,width=580,height=50)

        take_Photo_btn=Button(buttonFrame2,text="Take Photo Sample",command=self.generate_attend_dataset,width=16,font=("open sans",12,"bold"),bg="blue",fg="white")
        take_Photo_btn.grid(row=0,column=1,padx=2,pady=3)

        update_Photo_btn=Button(buttonFrame2,text="Update Photo Sample",command=self.generate_attend_dataset,width=16,font=("open sans",12,"bold"),bg="blue",fg="white")
        update_Photo_btn.grid(row=0,column=2,padx=2,pady=3)

        addMore_Photo_btn=Button(buttonFrame2,text="Add More Photo",command=self.add_more_attend_dataset,width=16,font=("open sans",12,"bold"),bg="blue",fg="white")
        addMore_Photo_btn.grid(row=0,column=3,padx=2,pady=3)


        #right pane
        right_pane=LabelFrame(main_frame,bd=2,relief=SUNKEN,text="Student Details",font=("open sans",12,"bold"))
        right_pane.place(x=650,y=10,width=600,height=600)

        Search_frame=LabelFrame(right_pane,bd=2,bg="white",relief=RIDGE,text="Search System",font=("open sans",12,"bold"))
        Search_frame.place(x=2,y=10,width=590,height=70)

        search_label=Label(Search_frame,text="Search By:",font=("open sans",12,"bold"),bg="white")
        search_label.grid(row=0,column=0,padx=3,pady=10)

        search_combo=ttk.Combobox(Search_frame,font=("open sans",12,"bold"),width=16,state="readonly")
        search_combo['values']=("Select","RollNumber","Email","Student ID")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=3,pady=10)

        search_entry=ttk.Entry(Search_frame,width=12,font=("opne sans",12,"bold"))
        search_entry.grid(row=0,column=2,padx=3,pady=10,sticky=W)

        search_button=Button(Search_frame,text="Search",width=12,font=("opne sans",10,"bold"),bg="blue",fg="white")
        search_button.grid(row=0,column=3)

        showAll_button=Button(Search_frame,text="Show All",width=12,font=("opne sans",10,"bold"),bg="blue",fg="white")
        showAll_button.grid(row=0,column=4)
        

        #======Table frame=====
        tableFrame=Frame(right_pane,bd=2,relief=RIDGE)
        tableFrame.place(x=0,y=100,width=580,height=450)

        scroll_bar_x=ttk.Scrollbar(tableFrame,orient=HORIZONTAL)
        scroll_bar_y=ttk.Scrollbar(tableFrame,orient=VERTICAL)

        self.student_table=ttk.Treeview(tableFrame,column=("dep","course","year","id","name","roll","email"),xscrollcommand=scroll_bar_x.set,yscrollcommand=scroll_bar_y.set)

        scroll_bar_x.pack(side=BOTTOM,fill=X)
        scroll_bar_y.pack(side=RIGHT,fill=Y)

        scroll_bar_x.config(command=self.student_table.xview)
        scroll_bar_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Department")
        self.student_table.heading("course",text="Course")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("id",text="StudentID")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("roll",text="Roll Number")
        self.student_table.heading("email",text="Email")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("course",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("email",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #====FUnctions=====
    #add data
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get=="Select Year" or self.var_id=="" or self.var_name=="" or self.var_roll=="" or self.var_email=="":
            messagebox.showerror("Error","All fields are required",parent=self)
        else:
            try:
                connect=mysql.connector.connect(host=SQL_HOST,user=SQL_USER,password=SQL_SERVER_PASSWORD,database="attendance")
                mySql_cursor=connect.cursor()
                mySql_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_id.get(),
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                ))
                connect.commit()
                self.fetch_data()
                connect.close()
                messagebox.showinfo("Success","Student Details has been added Successfully",parent=self)
            except Exception as e:
                messagebox.showerror("Error",f"Due to : {str(e)}",parent=self)

    #======fetch data===
    def fetch_data(self):
        connect=mysql.connector.connect(host=SQL_HOST,user=SQL_USER,password=SQL_SERVER_PASSWORD,database="attendance")
        mySql_cursor=connect.cursor()
        mySql_cursor.execute("select * from student")
        data=mySql_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            connect.commit()
        connect.close()

    #====get cursor function=============
    def get_cursor(self,event):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_id.set(data[3]),
        self.var_name.set(data[4]),
        self.var_roll.set(data[5]),
        self.var_email.set(data[6]),
    #==========updateion of data========
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get=="Select Year" or self.var_id=="" or self.var_name=="" or self.var_roll=="" or self.var_email=="":
            messagebox.showerror("Error","All fields are required",parent=self)
        else:
            try:
                updateData=messagebox.askyesno("Update","Do you want to update the student details? You can't update student ID since it's unique.",parent=self)
                if updateData>0:
                    connect=mysql.connector.connect(host=SQL_HOST,user=SQL_USER,password=SQL_SERVER_PASSWORD,database="attendance")
                    mySql_cursor=connect.cursor()
                    mySql_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, name=%s, RollNumber=%s, email=%s where StudentID=%s",(
                        self.var_dep.get(),
                        self.var_course.get(),
                        self.var_year.get(),
                        self.var_name.get(),
                        self.var_roll.get(),
                        self.var_email.get(),
                        self.var_id.get(),

                    ))

                else:
                    if not updateData:
                        return 
                messagebox.showinfo("Success","Student Details successfully updated",parent=self)
                connect.commit()
                self.fetch_data()
                connect.close()

            except Exception as e:
                messagebox.showerror("Error",f"Due to : {str(e)}",parent=self)


    #================delete function==========
    def delete_data(self):
        if self.var_id.get()=="":
            messagebox.showerror("Error","Student ID must be required",parent=self)
        else:
            try:
                deleteData=messagebox.askyesno("Delete","Do you want to update the student details?",parent=self)
                if deleteData>0:
                    connect=mysql.connector.connect(host=SQL_HOST,user=SQL_USER,password=SQL_SERVER_PASSWORD,database="attendance")
                    mySql_cursor=connect.cursor()
                    sql="delete from student where StudentID=%s"
                    val=(self.var_id.get(),)
                    mySql_cursor.execute(sql,val)
                else:
                    if not deleteData:
                        return
                connect.commit()
                self.fetch_data()
                connect.close()
                messagebox.showinfo("Delete","Student Details deleted successfully",parent=self)

            except Exception as e:
                messagebox.showerror("Error",f"Due to : {str(e)}",parent=self)

    #===========Reset=========
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Selecet Year"),
        self.var_id.set(""),
        self.var_name.set(""),
        self.var_roll.set(""),
        self.var_email.set(""),


    #=====Generate date set of takje photo samples=====
    def generate_attend_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get=="Select Year" or self.var_id=="" or self.var_name=="" or self.var_roll=="" or self.var_email=="":
            messagebox.showerror("Error","All fields are required",parent=self)
        else:
            try:
                connect=mysql.connector.connect(host=SQL_HOST,user=SQL_USER,password=SQL_SERVER_PASSWORD,database="attendance")
                mySql_cursor=connect.cursor()
                mySql_cursor.execute("select * from student")
                myres=mySql_cursor.fetchall()
                id=self.var_id.get()
                print(id)
                mySql_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, name=%s, RollNumber=%s, email=%s where StudentID=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_id.get()

                ))
                connect.commit()
                self.fetch_data()
                self.reset_data()
                connect.close()
    #=====================Load predef data on frontal face algo========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converted to grayscale
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0) #for web camera
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed.")

            except Exception as e:
                messagebox.showerror("Error",f"Due to : {str(e)}",parent=self)

    def add_more_attend_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_course.get=="Select Course" or self.var_year.get=="Select Year" or self.var_id=="" or self.var_name=="" or self.var_roll=="" or self.var_email=="":
            messagebox.showerror("Error","All fields are required",parent=self)
        else:
            try:
                connect=mysql.connector.connect(host=SQL_HOST,user=SQL_USER,password=SQL_SERVER_PASSWORD,database="attendance")
                mySql_cursor=connect.cursor()
                mySql_cursor.execute("select * from student")
                myres=mySql_cursor.fetchall()
                id=self.var_id.get()
                print(id)
                mySql_cursor.execute("update student set Dep=%s, Course=%s, Year=%s, name=%s, RollNumber=%s, email=%s where StudentID=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_name.get(),
                    self.var_roll.get(),
                    self.var_email.get(),
                    self.var_id.get()

                ))
                connect.commit()
                self.fetch_data()
                self.reset_data()
                connect.close()
    #=====================Load predef data on frontal face algo========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converted to grayscale
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    for(x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                
                cap=cv2.VideoCapture(0) #for web camera
                now=datetime.now()
                dtString=now.strftime("%H:%M:%S")
                img_id=int(1.25*((int)(dtString[:2]))+1.5*((int)(dtString[3:5]))+9.35*((int)(dtString[6:8])))
                img_id*=100
                img_id2=img_id+100
                #print(img_id)
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==img_id2:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed.")

            except Exception as e:
                messagebox.showerror("Error",f"Due to : {str(e)}",parent=self)

