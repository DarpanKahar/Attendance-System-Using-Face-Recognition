
from tkinter import *
from tkinter import ttk
import numpy as np
import os
import glob
import pandas as pd
import csv
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Studetn Report")
        self.root.geometry("600x700+20+80")
        # Table Frame
        Table_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=90,width=600,height=600)

        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        self.listBox=ttk.Treeview(Table_Frame,column=('Id','Name','Date','Time','subject'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.configure(command=self.listBox.xview)
        scroll_y.configure(command=self.listBox.yview)
        self.listBox.heading('Id',text='ID')
        self.listBox.heading('Name',text='NAME')
        self.listBox.heading('Date',text='DATE')
        self.listBox.heading('Time',text='TIME')
        self.listBox.heading('subject',text='SUBJECT')
        self.listBox['show']='headings' # auto index stop to commnad to heading

        # set the width
        self.listBox.column('Id',width=100)
        self.listBox.column('Name',width=100)
        self.listBox.column('Date',width=100)
        self.listBox.column('Time',width=100)
        self.listBox.column('subject',width=100)
        self.listBox.pack(fill=BOTH,expand=1)
        self.fetch_data()
        showReport = Button(self.root, text = "Show Report",width = 15, command = self.update).grid(row = 4, column = 0)
        closeButton = Button(self.root, text = "Close",width = 15, command = exit).grid(row = 4, column = 1)

    def fetch_data(self):
        with open('C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\Attendance\\Attendance.csv',newline='') as myfile:
            reader= csv.reader(myfile)
            for row in reader:
                self.listBox.insert('',END,values=row)

    def update(self):
        extension = 'csv'
        all_filenames = [i for i in glob.glob('C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\Attendance\\Attendance_*.{}'.format(extension))]
        #combine all files in the list
        combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames ])
        #export to csv
        combined_csv.to_csv( "C:\\Users\\Darpan\\Desktop\\StudentAttendanceSystem\\Attendance\\Attendance.csv", index=False, encoding='utf-8-sig')
        with open('Attendance/Attendance.csv',newline='') as myfile:
            reader= csv.reader(myfile)
            for row in reader:
                self.listBox.insert('',END,values=row)

# root=Tk()
# obj3=Student(root)
# root.mainloop()

