# import os  # accessing the os functions
# import check_camera
# import Capture_Image
# import Train_Image
# import Recognize
from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
from PIL import ImageTk
import numpy as np
import cv2
from Dashboad import *


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title('Login Admin')
        self.root.geometry("1320x700+0+0")

        # Images
        self.bg_icon = ImageTk.PhotoImage(file="C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\img\\register.jpg")
        self.user_icon = PhotoImage(file="C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\img\\name.png")
        self.pass_icon = PhotoImage(file="C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\img\\pass1.png")
        self.logo_icon = PhotoImage(file="C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\img\\login.png")

        # variables
        self.uname = StringVar()
        self.pass_ = StringVar()

        bg_lbl = Label(self.root, image=self.bg_icon).pack()

        title = Label(self.root, text=" Welcome Admin ", font=('times new roman', 45, 'bold'), bg='yellow', fg='blue',
                      bd=10, relief=GROOVE)
        title.place(x=0, y=0, relwidth=1)

        login_frame = Frame(self.root, bg="white")
        login_frame.place(x=400, y=100)

        logolbl = Label(login_frame, image=self.logo_icon, bd=0).grid(row=0, columnspan=2, pady=20)

        lbluser = Label(login_frame, text="Username", image=self.user_icon, compound=LEFT,
                        font=('times new roman', 20, 'bold')).grid(row=1, column=0, padx=20, pady=10)
        txtuser = Entry(login_frame, bd=5, textvariable=self.uname, relief=GROOVE, font=("", 15)).grid(row=1, column=1,
                                                                                                       padx=20, )

        lblpass = Label(login_frame, text="Password", image=self.pass_icon, compound=LEFT,
                        font=('times new roman', 20, 'bold')).grid(row=2, column=0, padx=20, pady=10)
        txtpass = Entry(login_frame, show='*', bd=5, textvariable=self.pass_, relief=GROOVE, font=("", 15)).grid(row=2,
                                                                                                                 column=1,
                                                                                                                 padx=20, )

        btn_log = Button(login_frame, text="Login", width=15, command=self.login, font=('times new roman', 14, 'bold'),
                         bg='yellow', fg='red').grid(row=3, column=1, pady=10)

    def login(self):
        if self.uname.get() == "" or self.pass_.get() == "":
            messagebox.showerror("Error", "All fields are required")
        elif self.uname.get() == "admin" and self.pass_.get() == "admin":
            messagebox.showinfo("Successful", f"Welcome {self.uname.get()}")
            self.home = Toplevel(self.root)
            self.root = HOME(self.home)
        else:
            messagebox.showerror("Error", "Invalid Username or Password")

root = Tk()
obj = Login(root)
root.mainloop()