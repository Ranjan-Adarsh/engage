from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image,ImageTk
from student import Student
import os
import numpy as np
import cv2
import mysql.connector
from time import strftime
from datetime import datetime


class Face_Recognisation_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

       

        # background image
        bg_Img=Image.open(r"C:\Users\adars\OneDrive\Desktop\engage\college_images\bg.jpg")
        bg_Img=bg_Img.resize((1500,650))
        self.photoBgImg=ImageTk.PhotoImage(bg_Img)

        background_Image_Label=Label(self.root,image=self.photoBgImg)
        background_Image_Label.place(x=0,y=0,width=1500,height=650)

        #title
        #title_label=Label(bg_Img,text="Facial Recognition System",font=("times new roman",35,"bold"),bg="white",fg="black")
        #title_label.place(x=0,y=0,width=500,height=45)

        #buttons
        #Student details
        img1=Image.open(r"college_images\userPic.png")
        img1=img1.resize((150,150))
        self.photoImg1=ImageTk.PhotoImage(img1)

        b1=Button(background_Image_Label,image=self.photoImg1,command=self.student_details,cursor="hand2")
        b1.place(x=100,y=100,width=150,height=150)

        b1_1=Button(background_Image_Label,text="Student Details",command=self.student_details,cursor="hand2",font=("opnen sans",12,"bold"),fg="white",bg="blue")
        b1_1.place(x=100,y=250,width=150,height=40)

        #Face Recognition
        img2=Image.open(r"college_images\face_detector1.jpg")
        img2=img2.resize((150,150))
        self.photoImg2=ImageTk.PhotoImage(img2)

        b2=Button(background_Image_Label,command=self.recognise_face,image=self.photoImg2,cursor="hand2")
        b2.place(x=350,y=100,width=150,height=150)

        b2_1=Button(background_Image_Label,text="Face Detector",command=self.recognise_face,cursor="hand2",font=("opnen sans",12,"bold"),fg="white",bg="blue")
        b2_1.place(x=350,y=250,width=150,height=40)

        #Train Data
        img3=Image.open(r"college_images\Train.jpg")
        img3=img3.resize((150,150))
        self.photoImg3=ImageTk.PhotoImage(img3)

        b3=Button(background_Image_Label,command=self.train_classifier,image=self.photoImg3,cursor="hand2")
        b3.place(x=600,y=100,width=150,height=150)

        b3_1=Button(background_Image_Label,command=self.train_classifier,text="Train Data",cursor="hand2",font=("opnen sans",12,"bold"),fg="white",bg="blue")
        b3_1.place(x=600,y=250,width=150,height=40)

#=================Function buttons=========

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
#================Train Data=============
    def train_classifier(self):
        data_directory=("data")
        path=[os.path.join(data_directory,file) for file in os.listdir(data_directory)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert("L")  #For gray scal conversion of image
            imageNp=np.array(img,"uint8")
            id=int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)

            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13

        ids= np.array(ids)
    #=========Train the classifier and save======
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("trainedClassifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed.")

    #=====Mark Attendance==========
    def mark_attendance(self,id,roll,name):
        with open("attendanceFile.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            nameList=[]
            for line in myDataList:
                entry=line.split((","))
                nameList.append(entry[0])
            if((id not in nameList) and (roll not in nameList) and (name not in nameList)):
                now=datetime.now()
                date1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{id},{roll},{name},{dtString},{date1},Present")



    #===============Face Recogniser==========
    def recognise_face(self):
        def draw_boundary(img,classifier,scaleFactor,minNeighbor,Color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbor)

            coordinate_list=[]
            for(x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))

                
                connect=mysql.connector.connect(host="localhost",user="root",password="Rasengan08..",database="attendance")
                mySql_cursor=connect.cursor()
                
                mySql_cursor.execute("select StudentID from student where StudentID ="+str(id))
                tempStoreId=mySql_cursor.fetchone()
                #tempStoreId="+".join(tempStoreId)

                mySql_cursor.execute("select name from student where StudentID ="+str(id))
                tempStoreName=mySql_cursor.fetchone()
                #tempStoreName="+".join(tempStoreName)

                mySql_cursor.execute("select RollNumber from student where StudentID ="+str(id))
                tempStoreRoll=mySql_cursor.fetchone()
                #tempStoreRoll="+".join(tempStoreRoll)

                if confidence>77:
                    cv2.putText(img,f"Id:{tempStoreId}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Roll:{tempStoreRoll}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"Name:{tempStoreName}",(x,y-15),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    self.mark_attendance(tempStoreId,tempStoreRoll,tempStoreName)
                else:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    cv2.putText(img,f"Unknown Face",(x,y-25),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)

                coordinate_list=[x,y,w,h]
            return coordinate_list
        
        def recognize(img,clf,faceCascade):
            coordinate_list=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"Face",clf)
            return img
        
        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("trainedClassifier.xml")

        video_camera_capture=cv2.VideoCapture(0) #for pc computer

        while TRUE:
            ret,img=video_camera_capture.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("Welcome to face recognisation",img)

            if cv2.waitKey(1)==13:
                break
        video_camera_capture.release()
        cv2.destroyAllWindows()

if __name__=="__main__":
    root=Tk()
    obj=Face_Recognisation_System(root)
    root.mainloop()


