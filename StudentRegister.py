from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Studetn Register")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Student Attendance System",bd=10,relief=GROOVE,font=("times new roman",30,"bold"),bg="yellow",fg="red")
        title.pack(side=TOP)

        # All Variables
        self.enroll_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Manage_Frame.place(x=20,y=100,width=450,height=600)

        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=850,height=560)

        m_title=Label(Manage_Frame,text="Manage Student",font=("times new roman",20,"bold"),bg='crimson',fg="white")
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_enroll=Label(Manage_Frame,text="Enrollment No.",font=("times new roman",15,"bold"),bg='crimson',fg="white")
        lbl_enroll.grid(row=1,column=0,pady=10,padx=20,sticky="W")

        txt_enroll=Entry(Manage_Frame,textvariable=self.enroll_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_enroll.grid(row=1,column=1,pady=10,padx=20,sticky="W")

        lbl_name=Label(Manage_Frame,text="Name",font=("times new roman",15,"bold"),bg='crimson',fg="white")
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="W")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="W")

        
        lbl_email=Label(Manage_Frame,text="Email",font=("times new roman",15,"bold"),bg='crimson',fg="white")
        lbl_email.grid(row=3,column=0,pady=10,padx=20,sticky="W")

        txt_email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_email.grid(row=3,column=1,pady=10,padx=20,sticky="W")

        lbl_gender=Label(Manage_Frame,text="Gender",font=("times new roman",15,"bold"),bg='crimson',fg="white")
        lbl_gender.grid(row=4,column=0,pady=20,sticky="W")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_gender['values']=("Male","Female","other")
        combo_gender.grid(row=4,column=1,pady=10,padx=20,sticky="W")

        lbl_contact=Label(Manage_Frame,text="Contact No.",font=("times new roman",15,"bold"),bg='crimson',fg="white")
        lbl_contact.grid(row=5,column=0,pady=10,padx=20,sticky="W")

        txt_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_contact.grid(row=5,column=1,pady=10,padx=20,sticky="W")

        lbl_Dob=Label(Manage_Frame,text="D.O.B",font=("times new roman",15,"bold"),bg='crimson',fg="white")
        lbl_Dob.grid(row=6,column=0,pady=10,padx=20,sticky="W")

        txt_Dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Dob.grid(row=6,column=1,pady=10,padx=20,sticky="W")

        lbl_address=Label(Manage_Frame,text="Address",font=("times new roman",15,"bold"),bg='crimson',fg="white")
        lbl_address.grid(row=7,column=0,pady=10,padx=20,sticky="W")

        self.txt_address=Text(Manage_Frame,width=30,height=4,font=("",10))
        self.txt_address.grid(row=7,column=1,pady=10,padx=20,sticky="W")

        # Button Frame

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="crimson")
        btn_Frame.place(x=1,y=520,width=440)

        addbtn=Button(btn_Frame,text="Add",width=7,command=self.add_student).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="Update",width=7,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="Delete",width=7,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="Clear",width=7,command=self.clear).grid(row=0,column=3,padx=10,pady=10)

        # Detail Frame
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="crimson")
        Detail_Frame.place(x=500,y=100,width=850,height=560)

        lbl_search=Label(Detail_Frame,text="Search By.",font=("times new roman",15,"bold"),bg='crimson',fg="white")
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="W")
        
        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,font=("times new roman",12,"bold"),state='readonly')
        combo_search['values']=("enroll_no")
        combo_search.grid(row=0,column=1,pady=10,padx=20,sticky="W")

        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=15,font=("times new roman",14),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="W")

        searchbtn=Button(Detail_Frame,text="Search",width=10,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showbtn=Button(Detail_Frame,text="Show All",width=10,command=self.search_data).grid(row=0,column=4,padx=10,pady=10)

        # Table Frame
        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="crimson")
        Table_Frame.place(x=10,y=70,width=800,height=480)

        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        self.student_table=ttk.Treeview(Table_Frame,column=('Enroll','Name','Email','gender','contact','dob','address'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.configure(command=self.student_table.xview)
        scroll_y.configure(command=self.student_table.yview)
        self.student_table.heading('Enroll',text='EnrollmentNo')
        self.student_table.heading('Name',text='Name')
        self.student_table.heading('Email',text='Email')
        self.student_table.heading('gender',text='Gender')
        self.student_table.heading('contact',text='Contact')
        self.student_table.heading('dob',text='D.O.B')
        self.student_table.heading('address',text='Address')
        self.student_table['show']='headings' # auto index stop to commnad to heading

        # set the width
        self.student_table.column('Enroll',width=100)
        self.student_table.column('Name',width=100)
        self.student_table.column('Email',width=100)
        self.student_table.column('gender',width=100)
        self.student_table.column('contact',width=100)
        self.student_table.column('dob',width=100)
        self.student_table.column('address',width=150)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

# register to sudents details
    def add_student(self):
        if self.enroll_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.gender_var.get()=="" or self.contact_var.get()=="" or self.txt_address.get('1.0',END)=="":
            messagebox.showerror("Error","All fields are required!!")
        else:
            con=pymysql.connect(host='localhost',user='root',password='admin',database="stm")
            cur=con.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.enroll_var.get(),self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has been Inserted")
# All Fetcha data to sql
    def fetch_data(self):
        con=pymysql.connect(host='localhost',user='root',password='admin',database="stm")
        cur=con.cursor()
        cur.execute("SELECT * FROM student")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

# CLaer the all entryt to register data 
    def clear(self):
        self.enroll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.student_table.focus()
        contents=self.student_table.item(cursor_row)
        row=contents['values']
        # print(row)
        self.enroll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0",END)
        self.txt_address.insert(END,row[6])

    # UPDATE functions
    def update_data(self):
        con=pymysql.connect(host='localhost',user='root',password='admin',database="stm")
        cur=con.cursor()
        cur.execute("UPDATE student SET name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s WHERE enroll_no=%s", (self.name_var.get(),self.email_var.get(),self.gender_var.get(),self.contact_var.get(),self.dob_var.get(),self.txt_address.get('1.0',END),self.enroll_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host='localhost',user='root',password='admin',database="stm")
        cur=con.cursor()
        cur.execute("delete from student where enroll_no=%s",self.enroll_var.get())
        con.commit()
        con.close()

        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host='localhost',user='root',password='admin',database="stm")
        cur=con.cursor()
        cur.execute("select * from student where enroll_no=%s",(self.search_txt.get()))
# cur.execute("select * from student where"+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
            con.commit()
        con.close()

# def Reg():
#     root=Tk()
#     obj=Student(root)
#     root.mainloop()
# Reg()