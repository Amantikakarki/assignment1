from tkinter import*
from tkinter import ttk
import mysql.connector
from tkinter import messagebox



class StudentLogin:
    def __init__(self, root):
        self.root=root
        self.root.title("Student Management Login system")

        self.root.geometry("700x325+250+180")

        self.root.config(bg='azure')
        self.frame=Frame(self.root,bg='azure')
        self.frame.pack()
        self.Username=StringVar()
        self.Password=StringVar()



       #===========================Login frame===============================================================
        self.LoginFrame1=LabelFrame(self.frame,width=750,height=150,
         text="Login" ,font=('arial',10,'bold'),relief='ridge',bg='azure',bd=20)
        self.LoginFrame1.grid(row=1,column=0)

        self.LoginFrame2 = LabelFrame(self.frame, width=500, height=100,text="Log" ,
                                      font=('arial', 10, 'bold'), relief='ridge', bg='snow', bd=20)
        self.LoginFrame2.grid(row=2, column=0)



        #=====================================label===================================================
        self.lblusername=Label(self.LoginFrame1,text='Username',font=('arial',10,'bold'),bd=20,
                               bg='black',fg='Cornsilk')
        self.lblusername.grid(row=0,column=0)
        self.txtusername=Entry(self.LoginFrame1,font=('arial',15,'bold'),bd=7,textvariable=self.Username,
                               width=33)
        self.txtusername.grid(row=0,column=1,padx=78)

        self.lblpassword = Label(self.LoginFrame1, text='Password', font=('arial', 10, 'bold'), bd=20,
                                 bg='black', fg='Cornsilk')
        self.lblpassword.grid(row=1, column=0)
        self.txtpassword = Entry(self.LoginFrame1, font=('arial', 15, 'bold'),show='*', bd=7, textvariable=self.Password,
                                 width=33)
        self.txtpassword.grid(row=1, column=1,columnspan=2,pady=30)

    #==========================================btn=========================================================================

        self.btnLogin=Button(self.LoginFrame2,text='Login',width=15,font=('arial',10,'bold'),
                             bg='black',fg='Cornsilk',command=self.Login_system)
        self.btnLogin.grid(row=3,column=0,pady=20,padx=8)

        self.btnReset = Button(self.LoginFrame2, text='Reset', width=15, font=('arial', 10, 'bold'),
                               bg='black', fg='Cornsilk',command=self.iReset)
        self.btnReset.grid(row=3, column=1, pady=20, padx=8)

        self.btnExit = Button(self.LoginFrame2, text='Exit', width=15, font=('arial', 10, 'bold'),
                               bg='black', fg='Cornsilk',command=self.iExit)
        self.btnExit.grid(row=3, column=2, pady=20, padx=8)



#===========function=================================

    def Login_system(self):
        user = (self.Username.get())
        pas = (self.Password.get())
        if (user == str(123456) and pas == str(123456)):
            self.Login_window()

        else:
            messagebox.askyesno("StudentManagement Login System", "Invalid Login details")
            self.Username.set("")
            self.Password.set("")





    def iReset(self):
        self.Username.set("")
        self.Password.set("")

    def iExit(self):
        iExit = messagebox.askyesno("Student Database Management System", "Confirm if you want to exit")
        if iExit > 0:
            root.destroy()
            return

    def sExit(self):
        iExit = messagebox.askyesno("Student Database Management System", "Confirm if you want to exit")
        if iExit > 0:
            StudentWindow.destroy()
            return

    def Login_window(self):
        self.root.destroy()
        reg()


def reg():
    global StudentWindow
    StudentWindow = Tk()
    app = register(StudentWindow)
    StudentWindow.protocol('WM_DELETE_WINDOW', app.sExit)
    StudentWindow.mainloop()



class register():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("700x400+200+150")

        self.title = Label(self.root, text="students management system", font=("times new roman", 40,
                                                                         "bold"), bd=10, relief=GROOVE, bg="snow",
                      fg="red")
        self.title.pack(side=TOP)
        self.root.resizable(height=False, width=False)
        #==================frame================================

        self.ragistry_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="azure")
        self.ragistry_Frame.place(x=150, y=100, width=480, height=250)

        self.m_title = Label(self.ragistry_Frame, text="Manage Student", bg="azure", fg="black",
                        font=("times new roman", 20, "bold"))
        self.m_title.grid(row=0, columnspan=2, pady=20)
        #===============btn========================================

        self.Addregistry = Button(self.ragistry_Frame, text="register student", width=20,font=('arial',12,'bold'),
                             bg='black',fg='Cornsilk',command= self.studentManagement).grid(row=1, column=0, padx=10,pady=10)

        self.searchbtn = Button(self.ragistry_Frame, text="search data", width=20,font=('arial',12,'bold'),
                             bg='black',fg='Cornsilk',command= self.Search).grid(row=1, column=1, padx=10,pady=10)

        self.sortbtn = Button(self.ragistry_Frame, text="Sort data", width=20,font=('arial',12,'bold'),
                             bg='black',fg='Cornsilk', command= self.Sort).grid(row=2, column=0, padx=10,pady=10)
        self.sortbtn = Button(self.ragistry_Frame, text="Exit", width=20, font=('arial', 12, 'bold'),
                         bg='black', fg='Cornsilk', command=self.iExit).grid(row=2, column=1, padx=10, pady=10)

#============function============================================

    def Sort(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = sort(self.newWindow)

    def studentManagement(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = StudentManagement(self.newWindow)




    def Search(self):
        self.root.withdraw()
        self.newWindow = Toplevel(self.root)
        self.app = search(self.newWindow)

    def iExit(self):
        iExit = messagebox.askyesno("Student Database Management System", "Confirm if you want to exit")
        if iExit > 0:
            self.root.destroy()
            return

    def sExit(self):
        iExit = messagebox.askyesno("Student Database Management System", "Confirm if you want to exit")
        if iExit > 0:
            StudentWindow.destroy()
            return

    def Login_window(self):
        self.root.withdraw()
        self.StudentWindow = Tk()
        self.StudentWindow.protocol('WM_DELETE_WINDOW', self.sExit)

        self.app = StudentManagement(self.StudentWindow)
        self.StudentWindow.mainloop()

    def back(self):
        reg()


class StudentManagement():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        self.title = Label(self.root, text="students management system", font=("times new roman", 40,
                                                                         "bold"), bd=10, relief=GROOVE, bg="snow",
                      fg="red")
        self.title.pack(side=TOP)
        self.root.resizable(height=False, width=False)

#============================All variable
        self.StdID_var=StringVar()
        self.Name_var = StringVar()
        self.Email_var = StringVar()
        self.Age_var = StringVar()
        self.Gender_var = StringVar()
        self.Programme_var = StringVar()
        self.contact_var = StringVar()

        self.sorts_by=StringVar()
        self.search_txt=StringVar()
        self.sort_by=StringVar()
        self.sort_txt=StringVar()



#=================manage frame
        self.manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="azure")
        self.manage_Frame.place(x=20,y=100,width=415,height=600)

        self.m_title=Label(self.manage_Frame,text="Manage Student",bg="azure",fg="black",font=("times new roman",20,"bold"))
        self.m_title.grid(row=0,columnspan=2,pady=20)

        self.lbl_ID=Label(self.manage_Frame,text="StdID",bg="azure",fg="black",font=("times new roman",15,"bold"))
        self.lbl_ID.grid(row=1, column=0,padx=20, pady=10,sticky="W")
        self.txt_ID=Entry(self.manage_Frame,textvariable=self.StdID_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        self.txt_ID.grid(row=1,column=1,padx=20,pady=10,sticky="W")

        self.lbl_name = Label(self.manage_Frame, text="Name", bg="azure", fg="black", font=("times new roman", 15, "bold"))
        self.lbl_name.grid(row=2, column=0, padx=20, pady=10, sticky="W")
        self.txt_name = Entry(self.manage_Frame,textvariable=self.Name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_name.grid(row=2, column=1, padx=20, pady=10, sticky="W")

        self.lbl_Email = Label(self.manage_Frame, text="Email", bg="azure", fg="black", font=("times new roman", 15, "bold"))
        self.lbl_Email.grid(row=3, column=0, padx=20, pady=10, sticky="w")
        self.txt_Email = Entry(self.manage_Frame,textvariable=self.Email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_Email.grid(row=3, column=1, padx=20, pady=10, sticky="w")

        self.lbl_Age = Label(self.manage_Frame, text="Age", bg="azure", fg="black", font=("times new roman", 15, "bold"))
        self.lbl_Age.grid(row=4, column=0, padx=20, pady=10, sticky="W")
        self.txt_Age = Entry(self.manage_Frame,textvariable=self.Age_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_Age.grid(row=4, column=1, padx=20, pady=10, sticky="W")

        self.lbl_Gender = Label(self.manage_Frame, text="Gender", bg="azure", fg="black", font=("times new roman", 15, "bold"))
        self.lbl_Gender.grid(row=5, column=0, padx=20, pady=10, sticky="W")
        self.combo_gender = ttk.Combobox(self.manage_Frame,textvariable=self.Gender_var, font=("times new roman", 15, "bold"),state='readonly')
        self.combo_gender['values'] = ("male", "female", "other")
        self.combo_gender.grid(row=5, column=1, padx=20, pady=10)


        self.lbl_Address = Label(self.manage_Frame, text="Address", bg="azure", fg="black", font=("arial", 15, "bold"))
        self.lbl_Address.grid(row=8, column=0, padx=20, pady=10, sticky="W")
        self.txt_Address=Text(self.manage_Frame,width=30,height=3,font=("",10))
        self.txt_Address.grid(row=8,column=1,pady=10,padx=20,sticky="w")

        self.lbl_contact = Label(self.manage_Frame, text="contact", bg="azure", fg="black", font=("times new roman", 15, "bold"))
        self.lbl_contact.grid(row=7, column=0, padx=20, pady=10, sticky="W")
        self.txt_contact = Entry(self.manage_Frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_contact.grid(row=7, column=1, padx=20, pady=10, sticky="W")

        self.lbl_programme = Label(self.manage_Frame, text="Programme", bg="azure", fg="black", font=("times new roman", 15, "bold"))
        self.lbl_programme.grid(row=6, column=0, padx=20, pady=10, sticky="W")
        self.combo_programme = ttk.Combobox(self.manage_Frame,textvariable=self.Programme_var, font=("times new roman", 15, "bold"),state='readonly')
        self.combo_programme['values'] = ("Bsc Hons incomputing", "Bsc Hons in Ethical Hacking")
        self.combo_programme.grid(row=6, column=1, padx=20, pady=10)

#==================Button=========================================================

        self.btn_Frame = Frame(self.manage_Frame, bd=4, relief=RIDGE, bg="azure")
        self.btn_Frame.place(x=10, y=530, width=430)

        self.Addbtn=Button(self.btn_Frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        self.updatebtn = Button(self.btn_Frame, text="Update", width=10,command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        self.deletebtn = Button(self.btn_Frame, text="Delete", width=10,command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        self.clearbtn = Button(self.btn_Frame, text="Clear", width=10,command=self.clear).grid(row=0, column=3, padx=10, pady=10)



#======================================Detail frame=================================================




        self.Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="azure")
        self.Detail_Frame.place(x=500, y=100, width=1050, height=560)

        self.lbl_search=Label(self.Detail_Frame,text="Search By",bg="azure",fg="black",font=("times new roaman",
                                10,"bold"))
        self.lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")





        self.txt_search = Entry(self.Detail_Frame,textvariable=self.search_txt,width=13, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, padx=20, pady=10, sticky="W")



        self.searchbtn = Button(self.Detail_Frame, text="Search", width=10,pady=5,command=self.search_data).grid(row=0, column=2, padx=10, pady=10)
        self.searchbtn = Button(self.Detail_Frame, text="Sort", width=10, pady=5, command=self.Sort).grid(row=0,
                                                                                                         column=3,
                                                                                                         padx=10,
                                                                                                         pady=10)
        self.showallbtn = Button(self.Detail_Frame, text="showall", width=10, pady=5, command=self.fetch_data).grid(row=0, column=6,
                                                                                                      padx=10, pady=10)
        self.homebtn = Button(self.Detail_Frame, text="Back", width=10, pady=5, command=self.back).grid(
            row=0, column=7,
            padx=10, pady=10)

        self.testing_Frame = Frame(self.Detail_Frame, bd=4, relief=RIDGE, bg="azure")
        self.testing_Frame.place(x=10, y=530, width=430)





#=================================Table Frame==========================================================

        self.Table_Frame = Frame(self.Detail_Frame, bd=4, relief=RIDGE, bg="azure")
        self.Table_Frame.place(x=10, y=70, width=830, height=450)

        self.scroll_x=Scrollbar(self.Table_Frame,orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(self.Table_Frame,columns=("StdID","Name","Email","Age","Gender",
                            "Programme","contact","Address"),xscrollcommand=self.scroll_x.set,
                                   yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM,fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("StdID",text="StdID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Age", text="Age")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Programme", text="Programme")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("Address", text="Address")
        self.student_table['show']='headings'
        self.student_table.column("StdID", width=50)
        self.student_table.column("Name", width=100)
        self.student_table.column("Email", width=160)
        self.student_table.column("Age", width=40)
        self.student_table.column("Gender", width=50)
        self.student_table.column("Programme", width=150)
        self.student_table.column("contact", width=50)
        self.student_table.column("Address", width=80)
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        #===============function=======================

    def back(self):
        self.iExit()
        reg()


    def add_students(self):
        try:

            if int(self.StdID_var.get()) == "" or str(self.Name_var.get()) == "" or str(
                    self.Email_var.get()) == "" or int(self.Age_var.get()) == "" \
                    or str(self.Gender_var.get()) == "" or str(self.Programme_var.get()) == "" or \
                    int(self.contact_var.get()) == "" or str(self.txt_Address.get('1.0', END)) == "":

                messagebox.showerror("Error", "All fields are required!!!")

            else:

                con = mysql.connector.connect(host="localhost", user="root", password="A123%anisha",
                                              database="softwarica")
                cur = con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s,%s)", (int(self.StdID_var.get()),
                                                                                     self.Name_var.get(),
                                                                                     self.Email_var.get(),
                                                                                     self.Age_var.get(),
                                                                                     self.Gender_var.get(),
                                                                                     self.Programme_var.get(),
                                                                                     self.contact_var.get(),
                                                                                     self.txt_Address.get('1.0', END)
                                                                                     ))

                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Sucess", "Record has been inserted")

        except ValueError as error:
            print(error)



    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="A123%anisha", database="softwarica")
        cur = con.cursor()
        cur.execute("select *from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('',END,values=row)
                con.commit()

        con.close()

    def clear(self):
        self.StdID_var.set(""),
        self.Name_var.set(""),
        self.Email_var.set(""),
        self.Age_var.set(""),
        self.Gender_var.set(""),
        self.Programme_var.set(""),
        self.contact_var.set(""),
        self.txt_Address.delete('1.0', END)

    def get_cursor(self,ev):
        curosor_row=self.student_table.focus()
        contents=self.student_table.item(curosor_row)
        row=contents['values']

        self.StdID_var.set(row[0])
        self.Name_var.set(row[1])
        self.Email_var.set(row[2])
        self.Age_var.set(row[3])
        self.Gender_var.set(row[4])
        self.Programme_var.set(row[5])
        self.contact_var.set(row[6])
        self.txt_Address.delete('1.0', END)
        self.txt_Address.insert('1.0',row[7])

    def update_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="A123%anisha", database="softwarica")
        cur = con.cursor()
        cur.execute("update students set Namel=%s,Email=%s,Age=%s,Gender=%s,programme=%s,contact=%s,Address=%s where StdID=%s",
                                                (
                                                  self.Name_var.get(),
                                                  self.Email_var.get(),
                                                  self.Age_var.get(),
                                                  self.Gender_var.get(),
                                                  self.Programme_var.get(),
                                                  self.contact_var.get(),
                                                  self.txt_Address.get('1.0', END),
                                                  int(self.StdID_var.get())
                                                  ))



        con.commit()
        self.fetch_data()
        self.clear()
        con.close()



    def delete_data(self):

        con=mysql.connector.connect(host="localhost",user="root",password="A123%anisha",database="softwarica")
        cur=con.cursor()

        cur.execute("Delete from students where Age=%s", (self.txt_Age.get(),))
        print(self.txt_Age.get())
        con.commit()
        print('success')

        con.close()

        self.clear()
        self.fetch_data()
        print('success')



#===================use lineear search algorithem=============
    def search(self,rows):
        #con = mysql.connector.connect(host="localhost", user="root", password="A123%anisha", database="softwarica")
        #cur = con.cursor()

        data = rows
        def LinearSearch():
            found_list = []
            for i in data:
                if self.txt_search.get() in i:
                    found_list.append(i)

            return found_list
        #con.close()

        return LinearSearch()

    def search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="A123%anisha", database="softwarica")
        cur = con.cursor()

        cur.execute('select * from students')
        rows=cur.fetchall()
        print("rows")
        print(rows)
        row=self.search(rows)

        print("searchedRow")
        print(row)

        if len(rows):
            self.student_table.delete(*self.student_table.get_children())

        for i in row:
            self.student_table.insert('',END,values=i)

        con.close()

    def iExit(self):
        self.root.destroy()


    def Sort(self):
        self.newWindow = Toplevel(self.root)
        self.app = sort(self.newWindow)
#=========use linear search algorithem==================
class search():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("950x700+150+0")

        self.title = Label(self.root, text="students management system", font=("times new roman", 40,
                                                                          "bold"), bd=10, relief=GROOVE, bg="snow",
                      fg="red")
        self.title.pack(side=TOP)
        self.root.resizable(height=False, width=False)

        self.search_txt=StringVar()

        self.search_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="azure")
        self.search_Frame.place(x=30, y=100, width=900, height=560)

        self.lbl_search = Label(self.search_Frame, text="Search By", bg="azure", fg="black", font=("times new roaman",
                                                                                         10, "bold"))
        self.lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        self.txt_search = Entry(self.search_Frame, textvariable=self.search_txt, width=13,
                                font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        self.txt_search.grid(row=0, column=1, padx=20, pady=10, sticky="W")

        self.searchbtn = Button(self.search_Frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0,
                                                                                                         column=2,
                                                                                                         padx=10,
                                                                                                         pady=10)

        self.showallbtn = Button(self.search_Frame, text="showall", width=10, pady=5, command=self.fetch_data).grid(row=0,
                                                                                                        column=5,
                                                                                                        padx=10,
                                                                                                        pady=10)
        self.Homebtn = Button(self.search_Frame, text="Back", width=10, pady=5,command=self.back ).grid(row=0,
                                                                           column=6,
                                                                           padx=10,
                                                                           pady=10)

        self.testing_Frame = Frame(self.search_Frame, bd=4, relief=RIDGE, bg="azure")
        self.testing_Frame.place(x=10, y=530, width=430)

        # =================================Table Frame==========================================================

        self.Table_Frame = Frame(self.search_Frame, bd=4, relief=RIDGE, bg="azure")
        self.Table_Frame.place(x=10, y=70, width=830, height=450)

        self.scroll_x = Scrollbar(self.Table_Frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(self.Table_Frame, columns=("StdID", "Name", "Email", "Age", "Gender",
                                                                "Programme", "contact", "Address"),
                                          xscrollcommand=self.scroll_x.set,
                                          yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("StdID", text="StdID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Age", text="Age")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Programme", text="Programme")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("Address", text="Address")
        self.student_table['show'] = 'headings'
        self.student_table.column("StdID", width=50)
        self.student_table.column("Name", width=100)
        self.student_table.column("Email", width=160)
        self.student_table.column("Age", width=40)
        self.student_table.column("Gender", width=50)
        self.student_table.column("Programme", width=150)
        self.student_table.column("contact", width=50)
        self.student_table.column("Address", width=80)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>")
        self.fetch_data()

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="A123%anisha", database="softwarica")
        cur = con.cursor()
        cur.execute("select *from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
                con.commit()

        con.close()

    def back(self):
        self.iExit()
        reg()

    def search(self,rows):

        data = rows
        def LinearSearch():
            found_list = []
            for i in data:
                if self.txt_search.get() in i:
                    found_list.append(i)

            return found_list


        return LinearSearch()

    def search_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="A123%anisha", database="softwarica")
        cur = con.cursor()

        cur.execute('select * from students')
        rows = cur.fetchall()
        print("rows")
        print(rows)
        row = self.search(rows)

        print("searchedRow")
        print(row)

        if row:
            if len(rows):
                self.student_table.delete(*self.student_table.get_children())

            for i in row:
                self.student_table.insert('', END, values=i)

            con.close()

        else:
            messagebox.showinfo("No student", "Student is not found.")

    def iExit(self):
        self.root.destroy()


#use ==================bubble sort algorithem
class sort():
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("950x700+150+0")

        self.title = Label(self.root, text="students management system", font=("times new roman", 40,
                                                                          "bold"), bd=10, relief=GROOVE, bg="snow",
                      fg="red")
        self.title.pack(side=TOP)
        self.root.resizable(height=False, width=False)


        self.sorts_by=StringVar()
        self.sort_by=StringVar()
        self.sort_txt=StringVar()

        self.sort_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="azure")
        self.sort_Frame.place(x=30, y=100, width=900, height=560)

        self.lbl_sort = Label(self.sort_Frame, text="Sort By", bg="azure", fg="black", font=("times new roaman",
                                                                                        10, "bold"))
        self.lbl_sort.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        self.combo_sort = ttk.Combobox(self.sort_Frame, textvariable=self.sorts_by, font=("times new roman", 10, "bold"),
                                         width=10, state='readonly')
        self.combo_sort['values'] = ("StdID", "Name", "Email", "Age", "Gender", "Programme", "Contact", "Address")
        self.combo_sort.grid(row=0, column=1, padx=20, pady=10)

        self.lbl_sort = Label(self.sort_Frame, text="order", bg="azure", fg="black", font=("times new roaman",
                                                                                  10, "bold"))
        self.lbl_sort.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        self.combo_sortBy = ttk.Combobox(self.sort_Frame, textvariable=self.sort_by,
                                         font=("times new roman", 10, "bold"), width=10, state='readonly')
        self.combo_sortBy['values'] = ("Ascending", "Descending")
        self.combo_sortBy.grid(row=0, column=3, padx=20, pady=10)

        self.sortallbtn = Button(self.sort_Frame, text="Sort", width=10, pady=5, command=self.sort_data).grid(row=0, column=4,
                                                                                                      padx=10, pady=10)
        self.showallbtn = Button(self.sort_Frame, text="showall", width=10, pady=5, command=self.fetch_data).grid(row=0,
                                                                                                          column=5,
                                                                                                          padx=10,
                                                                                                          pady=10)
        self.Homebtn = Button(self.sort_Frame, text="Back", width=10, pady=5,command=self.back ).grid(row=0,
                                                                                column=6,
                                                                                padx=10,
                                                                            pady=10)

        self.testing_Frame = Frame(self.sort_Frame, bd=4, relief=RIDGE, bg="azure")
        self.testing_Frame.place(x=10, y=530, width=430)

 # =================================Table Frame==========================================================

        self.Table_Frame = Frame(self.sort_Frame, bd=4, relief=RIDGE, bg="azure")
        self.Table_Frame.place(x=10, y=70, width=830, height=450)

        self.scroll_x = Scrollbar(self.Table_Frame, orient=HORIZONTAL)
        self.scroll_y = Scrollbar(self.Table_Frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(self.Table_Frame, columns=("StdID", "Name", "Email", "Age", "Gender",
                                                                "Programme", "contact", "Address"),
                                          xscrollcommand=self.scroll_x.set,
                                          yscrollcommand=self.scroll_y.set)
        self.scroll_x.pack(side=BOTTOM, fill=X)
        self.scroll_y.pack(side=RIGHT, fill=Y)
        self.scroll_x.config(command=self.student_table.xview)
        self.scroll_y.config(command=self.student_table.yview)
        self.student_table.heading("StdID", text="StdID")
        self.student_table.heading("Name", text="Name")
        self.student_table.heading("Email", text="Email")
        self.student_table.heading("Age", text="Age")
        self.student_table.heading("Gender", text="Gender")
        self.student_table.heading("Programme", text="Programme")
        self.student_table.heading("contact", text="Contact")
        self.student_table.heading("Address", text="Address")
        self.student_table['show'] = 'headings'
        self.student_table.column("StdID", width=50)
        self.student_table.column("Name", width=100)
        self.student_table.column("Email", width=160)
        self.student_table.column("Age", width=40)
        self.student_table.column("Gender", width=50)
        self.student_table.column("Programme", width=150)
        self.student_table.column("contact", width=50)
        self.student_table.column("Address", width=80)
        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease-1>")
        self.fetch_data()

    def fetch_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="A123%anisha", database="softwarica")
        cur = con.cursor()
        cur.execute("select *from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for row in rows:
                self.student_table.insert('', END, values=row)
                con.commit()

        con.close()

    def Sort(self,list_i):
        #con = mysql.connector.connect(host="localhost", user="root", password="A123%anisha", database="softwarica")
        #cur = con.cursor()
        l = len(list_i)
        fieldId = 0

        if(self.combo_sort.get()=="StdID"):
            fieldId = 0
        elif(self.combo_sort.get()=="Name"):
            fieldId = 1
        elif(self.combo_sort.get()=="Email"):
            fieldId = 2
        elif (self.combo_sort.get() == "Age"):
            fieldId = 3
        elif (self.combo_sort.get() == "Gender"):
            fieldId = 4
        elif (self.combo_sort.get() == "Programme"):
            fieldId = 5
        elif (self.combo_sort.get() == "Contact"):
            fieldId = 6
        elif (self.combo_sort.get() == "Address"):
            fieldId = 7

        for i in range(0, l):
            for j in range(0, l - i - 1):
                if(fieldId == 0 or fieldId == 3 or fieldId == 6):
                    if (self.combo_sortBy.get() == "Ascending"):
                        if int(list_i[j][fieldId]) > int(list_i[j + 1][fieldId]):
                            list_i[j], list_i[j + 1] = list_i[j + 1], list_i[j]
                    elif (self.combo_sortBy.get() == "Descending"):
                        if int(list_i[j][fieldId]) < int(list_i[j + 1][fieldId]):
                            list_i[j], list_i[j + 1] = list_i[j + 1], list_i[j]
                else:
                    if (self.combo_sortBy.get() == "Ascending"):
                        if list_i[j][fieldId] > list_i[j + 1][fieldId]:
                            list_i[j], list_i[j + 1] = list_i[j + 1], list_i[j]
                    elif (self.combo_sortBy.get() == "Descending"):
                        if list_i[j][fieldId] < list_i[j + 1][fieldId]:
                            list_i[j], list_i[j + 1] = list_i[j + 1], list_i[j]




        #con.close()
        return list_i

    def sort_data(self):
        con = mysql.connector.connect(host="localhost", user="root", password="A123%anisha", database="softwarica")
        cur = con.cursor()

        cur.execute('select * from students')
        list_i=cur.fetchall()
        rows=self.Sort(list_i)
        if len(rows) != 0:
            self.student_table.delete(*self.student_table.get_children())

        for row in rows:
            self.student_table.insert('',END,values=row)

        con.close()

    def iExit(self):
        self.root.destroy()
        return

    def back(self):
        self.iExit()
        reg()


if __name__=='__main__':
    root=Tk()
    application=StudentLogin(root)
    root.resizable(height=False, width=False)
    root.mainloop()



