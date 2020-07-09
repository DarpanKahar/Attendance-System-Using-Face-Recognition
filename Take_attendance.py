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
import Dashboad


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('Login Admin')
        self.root.geometry("1320x750+0+0")

        # Images
        self.bg_icon = ImageTk.PhotoImage(file="C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\img\\register.jpg")
        # bg_lbl = Label(self.root, image=self.bg_icon).pack()

        title = Label(self.root, text=" Take Attendance ", font=('times new roman', 45, 'bold'), bg='yellow', fg='blue',
                      bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=500, y=150)

        logolbl = Label(login_frame, bd=1).grid(row=0, columnspan=2, pady=20)
        self.subj_var = StringVar()
        lbluser = Label(login_frame, text="Subject Name ", compound=LEFT,font=('times new roman', 30, 'bold')).grid(row=1, column=0, padx=50, pady=20)
        self.txtuser = Entry(login_frame,textvariable = self.subj_var , bd=10,relief=GROOVE, font=("", 15)).grid(row=2, column=0,padx=20, pady=20, sticky="W")
        # self.txt_name = Entry(Manage_Frame, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        # self.txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="W")                                                                               

        btn_log = Button(login_frame, text=" Take ", width=20, command=self.recognize_attendence,font=('times new roman', 14, 'bold'),bg='yellow', fg='red').grid(row=4, column=0, pady=20)
        
        btn_clear = Button(login_frame, text=" Clear ", width=20,command=self.clear,font=('times new roman', 14, 'bold'),bg='yellow', fg='red').grid(row=6, column=0, pady=20)
    
        btn_close = Button(login_frame, text=" close ", width=20,command=self.close,font=('times new roman', 14, 'bold'),bg='yellow', fg='red').grid(row=9, column=0, pady=20)

    def close(self):
        self.home = Toplevel(self.root)
        self.root = Dashboad.HOME(self.home)  
      
    def clear(self):
        self.txtuser.delete(0, 'end')
        res = ''
        self.msg.configure(text=res)
    def recognize_attendence(self):
        subject = (self.subj_var.get())
        recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        # recognizer = cv2.face.LBPHFaceRecognizer_create()  # cv2.createLBPHFaceRecognizer()
        recognizer.read("C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\TrainingImageLabel\\Trainner.yml")
        harcascadePath = "C:\\Users\\Darpan\\AppData\\Local\\Programs\\Python\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
        faceCascade = cv2.CascadeClassifier(harcascadePath)
        df = pd.read_csv("C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\StudentDetails\\StudentDetails.csv")
        cam = cv2.VideoCapture(0)
        font = cv2.FONT_HERSHEY_SIMPLEX
        col_names = ['Id', 'Name', 'Date', 'Time','subject']
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
                    attendance.loc[len(attendance)] = [Id, aa, date, timeStamp,subject]
                else:
                    Id = 'Unknown'
                    tt = str(Id)
                if(conf > 75):
                    noOfFile = len(os.listdir("C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\ImagesUnkown"))+1
                    cv2.imwrite("C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\ImagesUnkown\\Image"+str(noOfFile) +".jpg", im[y:y+h, x:x+w])
                cv2.putText(im, str(tt), (x, y+h), font, 1, (255, 255, 255), 2)
            attendance = attendance.drop_duplicates(subset=['Id'], keep='first')
            cv2.imshow('im', im)
            if (cv2.waitKey(10) == ord('q')):
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


# root=Tk()
# obj=Login(root)
# root.mainloop()





# Subject = tx.get()
# fileName = "C:\\Users\\Darpan\\Desktop\\Python_Program\\Attendace_management_system-master\\Attendance\\" + Subject + "_" + date + "_" + Hour + "-" + Minute + "-" + Second + ".csv"
# sub = tk.Label(windo, text="Enter Subject", width=15, height=2, fg="white", bg="blue2", font=('times', 15, ' bold '))
# sub.place(x=30, y=100)

# tx = tk.Entry(windo, width=20, bg="yellow", fg="red", font=('times', 23, ' bold '))
# tx.place(x=250, y=105)