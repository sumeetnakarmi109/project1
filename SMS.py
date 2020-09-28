from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
class student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x800+0+0")

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,
                                    font=("times new roman",40,"bold"),bg="blue",fg="white")
        title.pack(side=TOP,fill=X)


        #.......All variables..........

        self.Roll_No_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()

        self.search_by=StringVar()
        self.search_txt=StringVar()


        #......frame...........
        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Manage_Frame.place(x=20,y=100,width=450,height=600)

        m_title=Label(Manage_Frame,text="Manage Students",bg="blue",fg="white",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)


        lbl_roll=Label(Manage_Frame,text="Roll no.",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")


        lbl_name=Label(Manage_Frame,text="Name",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        txt_name=Entry(Manage_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")


        lbl_Email=Label(Manage_Frame,text="Email",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        txt_Email=Entry(Manage_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Email.grid(row=3,column=1,pady=10,padx=20,sticky="w")


        lbl_Gender=Label(Manage_Frame,text="Gender",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman",14,"bold"),state='readonly')
        combo_gender['values']=("male","female","others")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)


        lbl_Contact=Label(Manage_Frame,text="Contact",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        txt_Contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_Contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")


        lbl_dob=Label(Manage_Frame,text="D.O.B.",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_dob.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        txt_dob=Entry(Manage_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_dob.grid(row=6,column=1,pady=10,padx=20,sticky="w")


        lbl_Address=Label(Manage_Frame,text="Address",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_Address.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_Address=Text(Manage_Frame,width=26,height=4)
        self.txt_Address.grid(row=7,column=1,pady=10,padx=20,sticky="w")

        #......button frame...............

        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="blue")
        btn_Frame.place(x=10,y=530,width=430)

        Addbtn=Button(btn_Frame,text="Add",width=10,command=self.add_students)
        Addbtn.grid(row=0,column=0,padx=10,pady=10)
        Updatebtn=Button(btn_Frame,text="Update",width=10,command=self.update_data)
        Updatebtn.grid(row=0,column=1,padx=10,pady=10)
        Deletebtn=Button(btn_Frame,text="Delete",width=10,command=self.delete_data)
        Deletebtn.grid(row=0,column=2,padx=10,pady=10)
        Clearbtn=Button(btn_Frame,text="Clear",width=10,command=self.clear)
        Clearbtn.grid(row=0,column=3,padx=10,pady=10)


        
        #.......Detail frame...........
        Detail_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="blue")
        Detail_Frame.place(x=500,y=100,width=800,height=600)


        lbl_search=Label(Detail_Frame,text="search by",bg="blue",fg="white",font=("times new roman",20,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")


        combo_search=ttk.Combobox(Detail_Frame,textvariable=self.search_by,width=10,font=("times new roman",14,"bold"),state='readonly')
        combo_search['values']=("Roll_no.","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)


        txt_search=Entry(Detail_Frame,textvariable=self.search_txt,width=15,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")


        searchbtn=Button(Detail_Frame,text="Search",width=10,pady=5,command=self.search_data)
        searchbtn.grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Detail_Frame,text="Show ALL",width=10,pady=5,command=self.fetch_data)
        showallbtn.grid(row=0,column=4,padx=10,pady=10)





        #................Table Frame................

        Table_Frame=Frame(Detail_Frame,bd=4,relief=RIDGE,bg="blue")
        Table_Frame.place(x=10,y=70,width=760,height=510)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.Student_table=ttk.Treeview(Table_Frame,columns=("roll","name","email","gender","contact","dob","Address")
                                                             ,xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll",text="Roll No.")
        self.Student_table.heading("name",text="Name")
        self.Student_table.heading("email",text="Email")
        self.Student_table.heading("gender",text="Gender")
        self.Student_table.heading("contact",text="Contact")
        self.Student_table.heading("dob",text="D.O.B.")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("roll",width=100)
        self.Student_table.column("name",width=100)
        self.Student_table.column("email",width=100)
        self.Student_table.column("gender",width=100)
        self.Student_table.column("contact",width=100)
        self.Student_table.column("dob",width=100)
        self.Student_table.column("Address",width=150)
        self.Student_table.pack(fill=BOTH,expand=1)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error","All Fields are required!")
        else:

    
            con=pymysql.connect(host="localhost",user="root",password="",database="assignment")
            cur=con.cursor()
            cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get()
                                                                              ,self.name_var.get()
                                                                              ,self.email_var.get()
                                                                              ,self.gender_var.get()
                                                                              ,self.contact_var.get()
                                                                              ,self.dob_var.get()
                                                                              ,self.txt_Address.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success","Record has beed inserted")

    def fetch_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="std")
        cur=con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_Address.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']

        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_Address.delete("1.0",END)
        self.txt_Address.insert(END,row[6])


    def update_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="assignment")
        cur=con.cursor()
        cur.execute("update student set name=%s,email=%s,gender=%s,contact=%s,dob=%s,address=%s where roll_no=%s",
                                                                                              (self.name_var.get()
                                                                                              ,self.email_var.get()
                                                                                              ,self.gender_var.get()
                                                                                              ,self.contact_var.get()
                                                                                              ,self.dob_var.get(),self.txt_Address.get('1.0',END)
                                                                                              ,self.Roll_No_var.get()))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="std")
        cur=con.cursor()
        cur.execute("delete from students where roll_no-%s",self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="std")
        cur=con.cursor()

        cur.execute("select * from students where"+str(self.search_by.get())+"LIKE '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
            con.commit()
        con.close()




root=Tk()
ob=student(root)
root.mainloop()
