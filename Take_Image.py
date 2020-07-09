import tkinter as tk
from tkinter import Message, Text
import cv2, os
from cv2 import *
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
from tkinter import *

from tkinter import *
from tkinter import ttk

import os
import cv2
import numpy as np
from PIL import Image
import pymysql


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Studetn Register")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Face Recognition Based Attendance System", bd=10, relief=GROOVE,
                      font=("times new roman", 30, "bold"), bg="yellow", fg="red")
        title.pack(side=TOP)

        # All Variables
        # self.enroll_var=StringVar()
        # self.name_var=StringVar()
        # self.noti_var=StringVar()
        # self.attend_var=StringVar()
        # self.is_number=StringVar()

        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=600)

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=850, height=560)

        m_title = Label(Manage_Frame, text="Student Attendance", font=("times new roman", 20, "bold"), bg='crimson',
                        fg="white")
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_enroll = Label(Manage_Frame, text="Enrollment No.", font=("times new roman", 15, "bold"), bg='crimson',
                           fg="white")
        lbl_enroll.grid(row=1, column=0, pady=10, padx=20, sticky="W")

        self.txt_enroll = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_enroll.grid(row=1, column=1, pady=10, padx=20, sticky="W")

        lbl_name = Label(Manage_Frame, text="Name", font=("times new roman", 15, "bold"), bg='crimson', fg="white")
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="W")

        self.txt_name = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="W")

        lbl_noti = Label(Manage_Frame, text="Notification:", font=("times new roman", 15, "bold"), bg='crimson',
                         fg="white")
        lbl_noti.grid(row=3, column=0, pady=10, padx=20, sticky="W")

        self.msg = Label(Manage_Frame, text="", font=("times new roman", 15, "bold"), width=20, height=1, bd=5,
                         fg="black", relief=GROOVE)
        self.msg.grid(row=3, column=1, pady=10, padx=20, sticky="W")

        lbl_attend = Label(Manage_Frame, text="Attendance:", font=("times new roman", 15, "bold"), bg='crimson',
                           fg="white")
        lbl_attend.grid(row=4, column=0, pady=10, padx=20, sticky="W")

        message2 = Label(Manage_Frame, text="", font=("times new roman", 15, "bold"), width=20, height=1, bd=5,
                         fg="white", relief=GROOVE)
        message2.grid(row=4, column=1, pady=10, padx=20, sticky="W")

        lbl_noti2 = Label(Manage_Frame, text="Train Module:", font=("times new roman", 15, "bold"), bg='crimson',
                          fg="white")
        lbl_noti2.grid(row=5, column=0, pady=10, padx=20, sticky="W")

        self.msg2 = Label(Manage_Frame, text="", font=("times new roman", 15, "bold"), width=20, height=1, bd=5,
                          fg="black", relief=GROOVE)
        self.msg2.grid(row=5, column=1, pady=10, padx=20, sticky="W")
        self.msg3 = Label(Manage_Frame, text="", font=("times new roman", 10, "bold"), width=30, height=1, bd=5,
                          fg="black", relief=GROOVE)
        self.msg3.grid(row=6, column=1, pady=10, padx=20, sticky="W")
        # Button Frame

        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=1, y=400, width=440)

        takebtn = Button(btn_Frame, text="Take Image", width=7, command=self.TakeImage).grid(row=0, column=0, padx=20,
                                                                                             pady=10)
        trainbtn = Button(btn_Frame, text="Train Image", width=7, command=self.TrainImages).grid(row=0, column=1,
                                                                                                padx=10, pady=10)
        trackbtn = Button(btn_Frame, text="Track Image", width=7,command=self.recognize_attendence).grid(row=0, column=2, padx=10, pady=10)
        quitbtn = Button(btn_Frame, text="Quit", width=7, command=root.destroy).grid(row=0, column=3, padx=10, pady=10)

        deletebtn = Button(btn_Frame, text="Delete", width=7).grid(row=1, column=1, padx=10, pady=10)
        clearbtn = Button(btn_Frame, text="Clear", width=7, command=self.clear).grid(row=1, column=2, padx=10, pady=10)

        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=850, height=560)

        lbl = Label(Detail_Frame, text="Student Register List", font=("times new roman", 15, "bold"), bg='crimson',
                           fg="white")
        lbl.grid(row=0, column=0, pady=10, padx=20, sticky="W")
        # combo_search = ttk.Combobox(Detail_Frame, font=("times new roman", 12, "bold"), state='readonly')
        # combo_search['values'] = ("Enroll", "Name")
        # combo_search.grid(row=0, column=1, pady=10, padx=20, sticky="W")

        # txt_search = Entry(Detail_Frame, width=15, font=("times new roman", 14), bd=5, relief=GROOVE)
        # txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="W")

        # searchbtn=Button(Detail_Frame,text="Search",width=10).grid(row=0,column=3,padx=10,pady=10)
        # showbtn=Button(Detail_Frame,text="Show All",width=10).grid(row=0,column=4,padx=10,pady=10)

        # Table Frame
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=800, height=480)

        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        self.student_table = ttk.Treeview(Table_Frame, column=('Id','Name','Date','Time'), xscrollcommand=scroll_x.set,
                                     yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.configure(command=self.student_table.xview)
        scroll_y.configure(command=self.student_table.yview)
        self.student_table.heading('Id',text='ID')
        self.student_table.heading('Name',text='NAME')
        self.student_table.heading('Date',text='DATE')
        self.student_table.heading('Time',text='TIME')
        self.student_table['show']='headings' # auto index stop to commnad to heading

        # set the width
        self.student_table.column('Id',width=100)
        self.student_table.column('Name',width=100)
        self.student_table.column('Date',width=100)
        self.student_table.column('Time',width=100)
        self.student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        # student_table.heading('Enroll', text='EnrollmentNo')
        # student_table.heading('Name', text='Name')
        # student_table['show'] = 'headings'  # auto index stop to commnad to heading

        # # set the width
        # student_table.column('Enroll', width=100)
        # student_table.column('Name', width=100)
        # student_table.pack(fill=BOTH, expand=1)
    def fetch_data(self):
        with open('C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\Attendance\\Attendance.csv',newline='') as myfile:
            reader= csv.reader(myfile)
            for row in reader:
                self.student_table.insert('',END,values=row)
    def clear(self):
        self.txt_enroll.delete(0, 'end')
        self.txt_name.delete(0, 'end')
        res = ''
        self.msg.configure(text=res)

    def TakeImage(self):
        Id = (self.txt_enroll.get())
        name = (self.txt_name.get())
        # checkName=("SELECT name FROM student WHERE name=%s")
        # checkId=("SELECT enroll_no FROM student WHERE enroll_no=%s")
        con=pymysql.connect(host='localhost',user='root',password='admin',database="stm")
        cur=con.cursor()
        if len(self.txt_enroll.get())==0 and len(self.txt_name.get())==0:
            res="Please fill in the missing info"
            self.msg3.configure(text=res)
        if len(self.txt_enroll.get())==0 and len(self.txt_name.get())!=0:
            res="Please Enter a Enrollment Number"
            self.msg3.configure(text=res)

        elif len(self.txt_enroll.get())!=0 and len(self.txt_name.get())==0:
            res="Please Enter a Name"
            self.msg3.configure(text=res)

        else:
            # cur.execute("SELECT name,enroll_no FROM student WHERE name=%s,enroll_no=%s")
            # cur.execute("SELECT name,enroll_no FROM student WHERE name=%s,enroll_no=%s")
            cur.execute("SELECT * FROM student WHERE enroll_no=%s",(Id))
            # cur.execute("SELECT * FROM student WHERE name=%s",(name))

            row=cur.fetchall()
            for rows in row:
                if rows[0]:
                    
                    cam = cv2.VideoCapture(0)
                    # harcascadePath="haarcascade_frontalface_default.xml"
                    face_decte = "C:\\Users\\Darpan\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
                    detector = cv2.CascadeClassifier(face_decte)
                    sampleNum = 0
                    while (True):
                        ret, img = cam.read()
                        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                        faces = detector.detectMultiScale(gray, 1.3, 5)
                        for (x, y, w, h) in faces:
                            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                            sampleNum = sampleNum + 1
                            cv2.imwrite("C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\TrainingImages\\ " + name + "." + Id + '.' + str(sampleNum) + ".jpg ", gray[y:y + h, x:x + w])
                            cv2.imshow('Frame', img)
                        if cv2.waitKey(100) & 0xFF == ord('q'):
                            break
                        elif sampleNum > 24:
                            break
                    cam.release()
                    cv2.destroyAllWindows()
                    res = Id + "," + name
                    row = [Id, name]
                    with open('C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\StudentDetails\\StudentDetails.csv','a+') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow(row)
                    csvfile.close()
                    self.msg.configure(text=res)
                    res="Successfuly "
                    # subf(self)
                    self.msg3.configure(text=res)
                else:
                    res="Please Check Name and Enrollment"
                    self.msg3.configure(text=res)

    def TrainImages(self):
        recognizer=cv2.face_LBPHFaceRecognizer.create()
        path='C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\TrainingImages'
        def getImageWithID(path):
            imagePaths=[os.path.join(path,f) for f in os.listdir(path)]
            faces=[]
            Ids=[]
            for imagePath in imagePaths:
                faceImg=Image.open(imagePath).convert('L')
                faceNp=np.array(faceImg,'uint8')
                Id=int(os.path.split(imagePath) [-1].split(".")[1])
                faces.append(faceNp)
                Ids.append(Id)
                cv2.imshow("trainnig",faceNp)
                cv2.waitKey(10)
                res="Image Training"
                self.msg2.configure(text=res)
            return Ids,faces
        Ids,faces=getImageWithID(path)
        recognizer.train(faces,np.array(Ids))
        recognizer.save('C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\TrainingImageLabel\\Trainner.yml')
        cv2.destroyAllWindows()
        
    def recognize_attendence(self):
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        # recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        recognizer.read("C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\TrainingImageLabel\\Trainner.yml")
        harcascadePath = "C:\\Users\\Darpan\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)
        df = pd.read_csv("C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\StudentDetails\\StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', 'Name', 'Date', 'Time']
        attendance = pd.DataFrame(columns=col_names)

        while True:
            ret, im = cam.read()
            gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.2, 5)
            for(x, y, w, h) in faces:
                cv2.rectangle(im, (x, y), (x+w, y+h), (225, 0, 0), 2)
                Id, conf = recognizer.predict(gray[y:y+h, x:x+w])

                if(conf < 50):
                    ts = time.time()
                    date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
                    timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
                    aa = df.loc[df['Id'] == Id]['Name'].values
                    tt = str(Id)+"-"+aa
                    attendance.loc[len(attendance)] = [Id, aa, date, timeStamp]

                else:
                    Id = 'Unknown'
                    tt = str(Id)
                if(conf > 75):
                    noOfFile = len(os.listdir("C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\ImagesUnkown"))+1
                    cv2.imwrite("C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\ImagesUnkown\\Image"+str(noOfFile) +".jpg", im[y:y+h, x:x+w])
                cv2.putText(im, str(tt), (x, y+h), font, 1, (255, 255, 255), 2)
            attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
            cv2.imshow('im', im)
            if (cv2.waitKey(1) == ord('q')):
                break
        ts = time.time()
        date = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
        Hour, Minute, Second = timeStamp.split(":")
        fileName = "C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\Attendance\\Attendance_"+date+"_"+Hour+"-"+Minute+"-"+Second+".csv"
        attendance.to_csv(fileName, index=False)
        cam.release()
        cv2.destroyAllWindows()
        print("Attendance Successfull")
        # res="Attendance Successfull"
        # self.message2.configure(text=res)
# root=Tk()
# obj2=Student(root)
# root.mainloop()