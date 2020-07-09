from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from PIL import ImageTk
import numpy as np
import cv2
import StudentRegister
import Take_Image
import Train_Image
import Track_Image
import Take_attendance
# import AttendanceReport
import Attendance
class HOME:
    def __init__(self, root):
        self.root = root
        self.root.title('Student Attendance System')
        self.root.geometry("1320x700+0+0")

        # self.home = Toplevel(self.root)
        # self.home = Toplevel(self.home)
        # self.root = home(self.home)
        # self.root=root
        # self.root.title('Student Attendance System')
        # self.root.geometry("1320x700+0+0")

        self.bg_icon = ImageTk.PhotoImage(file="C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\img\\register.jpg")
        
        self.bg_stdreg = ImageTk.PhotoImage(file="C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\img\\stdreg.jpg")
        self.bg_takeimg = ImageTk.PhotoImage(file="C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\img\\takeimg.jpg")
        self.bg_trainimg = ImageTk.PhotoImage(file="C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\img\\train.png")
        self.bg_trackimg = ImageTk.PhotoImage(file="C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\img\\images.jpg")
        self.bg_report = ImageTk.PhotoImage(file="C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\img\\take_atd.jpg")
        self.bg_close = ImageTk.PhotoImage(file="C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\img\\exit1.png")
        
        # self.bg_icon = ImageTk.PhotoImage(file="/home/ankur/PycharmProjects/StudentAttendanceSystem/img/register.jpg")
        # self.user_icon = PhotoImage(file="/home/ankur/PycharmProjects/StudentAttendanceSystem/img/name.png")
        # self.pass_icon = PhotoImage(file="/home/ankur/PycharmProjects/StudentAttendanceSystem/img/img/pass1.png")
        # self.logo_icon = PhotoImage(file="/home/ankur/PycharmProjects/StudentAttendanceSystem/img/login.png")
        
        
        self.uname = StringVar()
        self.pass_ = StringVar()
        bg_lbl = Label(self.root, image=self.bg_icon).pack()

        title = Label(self.root, text=" Student Attendance System ", font=('times new roman', 45, 'bold'), bg='yellow',
                      fg='red', bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        login_frame = Frame(self.root, bg="yellow")
        login_frame.place(x=400, y=100)
        
        title2 = Label(self.root, text="ADD STUDENT DETAILS", font=('times new roman', 15, 'bold'), bg='yellow',fg='red', bd=1, relief=GROOVE)
        title2.place(x=150, y=130)
        add_details = Button(self.root,image=self.bg_stdreg,command=self.register).place(x=150, y=160)

        title3 = Label(self.root, text="TAKE IMAGE", font=('times new roman', 15, 'bold'), bg='yellow',fg='red', bd=1, relief=GROOVE)
        title3.place(x=500, y=130)
        add_image = Button(root,image=self.bg_takeimg,command=self.TakeImage).place(x=500, y=160)
       
        title4 = Label(self.root, text="TRAIN IMAGE", font=('times new roman', 15, 'bold'), bg='yellow',fg='red', bd=1, relief=GROOVE)
        title4.place(x=850, y=130)                    
        train_image = Button(root,image=self.bg_trainimg,command=self.TrainImage).place(x=850, y=160)

        title5 = Label(self.root, text="TAKE ATTENDANCE", font=('times new roman', 15, 'bold'), bg='yellow',fg='red', bd=1, relief=GROOVE)
        title5.place(x=150, y=440)
        track_image = Button(root,image=self.bg_trackimg,command=self.TrackImage).place(x=150, y=470)

        title6 = Label(self.root, text="ATTENDANCE SHEET", font=('times new roman', 15, 'bold'), bg='yellow',fg='red', bd=1, relief=GROOVE)
        title6.place(x=500, y=440)
        att= Button(root,image=self.bg_report, text='ATTENDANCE',command=self.AttendanceReport).place(x=500, y=470)

        title7 = Label(self.root, text="EXIT", font=('times new roman', 15, 'bold'), bg='yellow',fg='red', bd=1, relief=GROOVE)
        title7.place(x=850, y=440)                           
        quite = Button(root,image=self.bg_close,command=root.destroy).place(x=850, y=470)

        # add_details = Button(root, text='ADD STUDENT DETAILS', command=self.register, height=10, width=30,
        #                      font=('times new roman', 14, 'bold'), bg='yellow', fg='red').place(x=100, y=130)
        # add_image = Button(root, text='TAKE IMAGE', command=self.TakeImage, height=10, width=30,
        #                    font=('times new roman', 14, 'bold'), bg='yellow', fg='red').place(x=500, y=130)
        # train_image = Button(root, text='TRAIN IMAGE', command=self.TrainImage,height=10, width=30, font=('times new roman', 14, 'bold'),
        #                      bg='yellow', fg='red').place(x=900, y=130)

        # track_image = Button(root, text='TRACK IMAGE',command=self.TrackImage, height=10, width=30, font=('times new roman', 14, 'bold'), bg='yellow',
        #                fg='red').place(x=100, y=400)
        # att= Button(root, text='ATTENDANCE', height=10, width=30, command="",
        #                    font=('times new roman', 14, 'bold'), bg='yellow', fg='red').place(x=500, y=400)
        # quite = Button(root, text='EXIT', height=10, width=30,command=root.destroy,font=('times new roman', 14, 'bold'),
        #                      bg='yellow', fg='red').place(x=900, y=400)

    def register(self):
        self.top = Toplevel(self.root)
        self.root = StudentRegister.Student(self.top)
        # root=Tk()
        # StudentRegister.Student(self.root)
        # # StudentRegister.Reg()
        # self.root.mainloop()

    def TakeImage(self):
        self.top = Toplevel(self.root)
        self.root = Take_Image.Student(self.top)
        # root=Tk()
        # obj2=Take_Image.Student(root)
        # root.mainloop()

    def TrainImage(self):
        Train_Image.TrainImages()
        # self.home = Toplevel(self.root)
        # self.root = HOME(self.home)

    def TrackImage(self):
        self.top = Toplevel(self.root)
        self.root = Take_attendance.Login(self.top)
        # root=Tk()
        # Take_attendance.Login(root)
        # root.mainloop()

    def AttendanceReport(self):
        root=Tk()
        obj3=Attendance.Student(root)
        root.mainloop()


# root = Tk()
# obj = HOME(root)
# root.mainloop()
        