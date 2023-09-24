from itertools import product
import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector
from tkinter import *
import time
import mysql.connector as ms
import datetime
from tkinter import filedialog
import csv
from tkinter import *
import tkinter.messagebox

def Login():
    e1 = Entry1.get()
    e2 = Entry2.get()

    if e1 == "" or e2 == "":
        tkinter.messagebox.showinfo('Error', 'Enter all the values in!')
    
    else:
        x = 0
        with open('Login.csv', 'r') as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if x == 0:
                    for field in row:
                        if field == e1 and row[1] == e2 and x==0:
                            tkinter.messagebox.showinfo('Login', 'Logged in Successfully')
                            x = 1
                            top.destroy()


                            def main(): #Whole Program
                                root = Tk()
                                root.title("1314 Supermarket")
                                root.state("zoomed")
                                bg_color='#008080'
                                b_color='#f5f5dc'

                                title=Label(root,text="Supermarket Managment",bd=12,bg=bg_color,fg='white',relief=GROOVE,font=("Times New Roman",30,"bold"),pady=2).pack(fill=X)

                                def bac(): #Exit button
                                    op=messagebox.askyesno("Exiting","Are You Sure You Want To Exit?")
                                    if op>0:
                                        root.destroy()


                                def check(): #CheckOut
                                    bb = Tk()
                                    bb.geometry("1100x625")
                                    bb.state('zoomed')
                                    bg_color='#52088a'
                                    

                                    title=Label(bb,text="Billing",bd=12,bg=bg_color,fg='white',relief=GROOVE,font=("Times New Roman",30,"bold"),pady=2).pack(fill=X)
                                    with open('num.txt','r+') as numFile:
                                        IDlist = numFile.readlines()
                                        lastValue = IDlist[-1]
                                        recieptNumber = str(int(lastValue)+1)
                                        numFile.write(f'\n{recieptNumber}')
                                    o1= StringVar()
                                    o2=StringVar()
                                    o3=IntVar()
                                    o4=IntVar()
                                    dat=StringVar()
                                    y=datetime.datetime.now().strftime("%Y/%m/%d")
                                    dat.set(str(y))
                                    tim= StringVar()
                                    z= datetime.datetime.now().strftime("%H:%M:%S")
                                    tim.set(str(z))

                                    global l
                                    l=[]


                                    def GetValue(event):
                                        e1.delete(0, END)
                                        e2.delete(0, END)
                                        e3.delete(0, END)
                                        e4.delete(0, END)
                                        row_id = listBox.selection()[0]
                                        select = listBox.set(row_id)
                                        e1.insert(0,select['Pid'])
                                        e2.insert(0,select['Pname'])
                                        e4.insert(0,select['Price'])


                                    def welcome(): #Prints top part of the bill
                                        textarea.delete(1.0,END)
                                        textarea.insert(END,"\t           Thank You for Shopping")
                                        textarea.insert(END,f"\n\nBill Number:\t{recieptNumber}")
                                        textarea.insert(END,f'\nDate:\t\t{dat.get()}')
                                        textarea.insert(END,f'\nTime:\t\t{tim.get()}')
                                        textarea.insert(END,f"\n\n==========================================")
                                        textarea.insert(END,"\nPID\tProduct\t\tQTY\t\tPrice")
                                        textarea.insert(END,f"\n==========================================\n")
                                        textarea.configure(font='arial 15 bold')

                                    def additm(): #add items to bill
                                        n=e4.get()
                                        m=float(e3.get())*float(n)
                                        l.append(m)
                                        if e2.get()!='':
                                            textarea.insert((10.0+float(len(l)-1)),f"{e1.get()}\t{e2.get()}\t\t{e3.get()}\t\t{m}\n")
                                        else:
                                            messagebox.showerror("Error","Please Enter Item")
                                    
                                    def updd():
                                        additm()
                                        pdd=int(e1.get())
                                        qttyy= int(e3.get())
                                        
                                        mysqldb=mysql.connector.connect(host="localhost",user="root",password="12345",database="supermarket")
                                        mycursor=mysqldb.cursor()
                                        mycursor.execute("Select * from products")
                                        data=mycursor.fetchall()
                                        product_quantity = mycursor.execute('SELECT quantity from products where pid={}'.format(pdd))
                                        value = mycursor.fetchone()
                                        new_product_quantity = value[0] - int(qttyy)
                                        mycursor.execute('update products set quantity={} where pid={}'.format(new_product_quantity,pdd))
                                        mysqldb.commit()          

                                    def Gbill(): #Generates bills
                                        textAreaText = textarea.get(10.0,(10.0+float(len(l))))
                                        welcome()
                                        textarea.insert(END, textAreaText)
                                        textarea.insert(END, f"\n==========================================")
                                        textarea.insert(END, f"\nTotal Paybill Amount :\t\t  Dhs{sum(l)}")
                                        textarea.insert(END, f"\n\n==========================================")
                                        sav()
                                        bb.destroy()

                                    def sav(): #SAving bill
                                        op=messagebox.askyesno("Save bill","Do you want t o save the Bill?")
                                        if op>0:
                                            bill_details=textarea.get('1.0',END)
                                            f1=open("bills/"+str(recieptNumber)+".txt","w")
                                            f1.write(bill_details)
                                            f1.close()
                                            messagebox.showinfo("Saved",f"Bill no, :{recieptNumber} Saved Successfully")
                                        else:
                                            return

                                    def show(): #Displays Database
                                            mysqldb = mysql.connector.connect(host="localhost", user="root", password="12345", database="supermarket")
                                            mycursor = mysqldb.cursor()
                                            mycursor.execute("SELECT Pid,pname,quantity,price FROM products")
                                            records = mycursor.fetchall()
                                    
                                            for i, (Pid,Pname, Quantity,Price) in enumerate(records, start=1):
                                                listBox.insert("", "end", values=(Pid,Pname, Quantity,Price))
                                                mysqldb.close()

                                    def bacc():
                                        bb.destroy()

                                    global e1
                                    global e2
                                    global e3
                                    global e4


                                    i1=LabelFrame(bb,bd=10,relief=GROOVE,font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
                                    i1.place(x=0,y=73,width=900,height=767)

                                    i2=LabelFrame(bb,bd=10,relief=GROOVE,font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
                                    i2.place(x=900,y=73,width=636,height=767)

                                    f1=Label(i1, text="Product ID",bg=bg_color,font=('times new romon',25,'bold'),fg='white').place(x=10,y= 10)
                                    f2=Label(i1, text="Product Name",bg=bg_color,font=('times new romon',25,'bold'),fg='white').place(x=10, y=143)
                                    f3=Label(i1, text="Quantity",bg=bg_color,font=('times new romon',25,'bold'),fg='white').place(x=10, y=276)
                                    f4=Label(i1, text="Price",bg=bg_color,font=('times new romon',25,'bold'),fg='white').place(x=10, y=410)

                                    bb3= Button(bb,text="BACK", command= bacc ,height=2, width= 10,bg="blue",fg="white",font=("arial",10 ,"bold"))
                                    bb3.place(x=20, y=17)        

                                    e1 = Entry(i1,width=15,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=o1)
                                    e1.place(x=270,y=10)
                                    
                                    e2 = Entry(i1,width=15,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=o2)
                                    e2.place(x=270,y=143)
                                    
                                    e3 = Entry(i1,width=15,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=o3)
                                    e3.place(x=270, y=276)
                                    
                                    e4 = Entry(i1,width=15,font='arial 15 bold',relief=SUNKEN,bd=7,textvariable=o4)
                                    e4.place(x=270, y=400)

                                    g1= Button(i1,command=updd, text='Add Item',height=5, width= 15,bg="blue",fg="white",font=("arial",12 ,"bold"))
                                    g1.place(x= 550, y=50)

                                    g2= Button(i1,command=Gbill, text='Generate Bill',height=5, width= 15,bg="blue",fg="white",font=("arial",12 ,"bold"))
                                    g2.place(x=550, y=250)

                                    F3=Frame(i2,relief=GROOVE,bd=10)
                                    F3.place(x=40,y=20,width=550,height=700)
                                    bill_title=Label(F3,text='1314 Supermarket',font='arial 15 bold',bd=7,relief=GROOVE).pack(fill=X)
                                    scrol_y=Scrollbar(F3,orient=VERTICAL)
                                    textarea=Text(F3,yscrollcommand=scrol_y)
                                    scrol_y.pack(side=RIGHT,fill=Y)
                                    scrol_y.config(command=textarea.yview)
                                    textarea.pack()
                                    welcome()

                                    cols = ('Pid', 'Pname', 'Quantity','Price')
                                    listBox = ttk.Treeview(i1, columns=cols, show='headings' )
                                    
                                    for col in cols:
                                        listBox.heading(col, text=col)
                                        listBox.place(x=30, y=500)
                                    
                                    show()
                                    listBox.bind('<Double-Button-1>',GetValue)

                                    bb.mainloop()


                                def ad(): #Add/Update database

                                    au = Tk()
                                    au.geometry( "1100x625")
                                    au.state('zoomed')
                                    bg_color='#9659eb'
                                    b_colour="#4169E1"

                                    def GetValue(event):
                                        e1.delete(0, END)
                                        e2.delete(0, END)
                                        e3.delete(0, END)
                                        e4.delete(0, END)
                                        row_id = listBox.selection()[0]
                                        select = listBox.set(row_id)
                                        e1.insert(0,select['Pid'])
                                        e2.insert(0,select['Pname'])
                                        e3.insert(0,select['Quantity'])
                                        e4.insert(0,select['Price'])
                                    
                                    def Add(): #Add item to Database
                                        piid = e1.get()
                                        prname = e2.get()
                                        qty = e3.get()
                                        saal = e4.get()
                                    
                                        mysqldb=mysql.connector.connect(host="localhost",user="root",password="12345",database="supermarket")
                                        mycursor=mysqldb.cursor()
                                    
                                        try:
                                            sql = "INSERT INTO  products (PID,Pname,Quantity,Price) VALUES (%s, %s, %s, %s)"
                                            val = (piid,prname,qty,saal)
                                            mycursor.execute(sql, val)
                                            mysqldb.commit()
                                            lastid = mycursor.lastrowid
                                            messagebox.showinfo("information", "Product inserted successfully...")
                                            e1.delete(0, END)
                                            e2.delete(0, END)
                                            e3.delete(0, END)
                                            e4.delete(0, END)
                                            e1.focus_set()
                                        except Exception as e:
                                            print(e)
                                            mysqldb.rollback()
                                            mysqldb.close()

                                        au.destroy()

                                    def update(): #Change any value in database
                                        piid = e1.get()
                                        prname = e2.get()
                                        qty = e3.get()
                                        pce = e4.get()
                                        mysqldb=mysql.connector.connect(host="localhost",user="root",password="12345",database="supermarket")
                                        mycursor=mysqldb.cursor()
                                    
                                        try:
                                            sql = "Update  products set Pname= %s,Quantity= %s,Price=%s where PID= %s"
                                            val = (prname,qty,pce,piid)
                                            mycursor.execute(sql, val)
                                            mysqldb.commit()
                                            lastid = mycursor.lastrowid
                                            messagebox.showinfo("information", "Record Updated successfully...")
                                        
                                            e1.delete(0, END)
                                            e2.delete(0, END)
                                            e3.delete(0, END)
                                            e4.delete(0, END)
                                            e1.focus_set()
                                    
                                        except Exception as e:
                                    
                                            print(e)
                                            mysqldb.rollback()
                                            mysqldb.close()

                                        au.destroy()

                                    def delete(): #Delete any value from database
                                        piid = e1.get()
                                    
                                        mysqldb=mysql.connector.connect(host="localhost",user="root",password="12345",database="supermarket")
                                        mycursor=mysqldb.cursor()
                                    
                                        try:
                                            sql = "delete from products where pid = %s"
                                            val = (piid,)
                                            mycursor.execute(sql, val)
                                            mysqldb.commit()
                                            lastid = mycursor.lastrowid
                                            messagebox.showinfo("information", "Product Deleted successfully...")
                                        
                                            e1.delete(0, END)
                                            e2.delete(0, END)
                                            e3.delete(0, END)
                                            e4.delete(0, END)
                                            e1.focus_set()
                                    
                                        except Exception as e:
                                    
                                            print(e)
                                            mysqldb.rollback()
                                            mysqldb.close()

                                        au.destroy()

                                    def show():
                                            mysqldb = mysql.connector.connect(host="localhost", user="root", password="12345", database="supermarket")
                                            mycursor = mysqldb.cursor()
                                            mycursor.execute("SELECT Pid,pname,quantity,price FROM products")
                                            records = mycursor.fetchall()
                                            print(records)
                                    
                                            for i, (Pid,Pname, Quantity,Price) in enumerate(records, start=1):
                                                listBox.insert("", "end", values=(Pid,Pname, Quantity,Price))
                                                mysqldb.close()

                                    def Backs():
                                        au.destroy()

                                    global e1
                                    global e2
                                    global e3
                                    global e4

                                    p3=LabelFrame(au,bd=10,relief=GROOVE,font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
                                    p3.place(x=775,y=0,width=770,height=450)
                                    
                                    tk.Label(p3, text="ADD/UPDATE", fg="black",bg=bg_color, font=(None, 30,'underline')).place(x=270, y=150)

                                    p2=LabelFrame(au,bd=10,relief=GROOVE,text='Stock Details',font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
                                    p2.place(x=0,y=0,width=775,height=450)

                                    y1= Label(p2, text="Product ID",bg=bg_color,font=('times new romon',23,'bold'),fg='white')
                                    y1.place(x=30, y=10)

                                    y2= Label(p2, text="Product Name",bg=bg_color,font=('times new romon',23,'bold'),fg='white')
                                    y2.place(x=30, y=73)

                                    y3= Label(p2, text="Quantity",bg=bg_color,font=('times new romon',23,'bold'),fg='white')
                                    y3.place(x=30, y=140)

                                    y4= Label(p2, text="Price",bg=bg_color,font=('times new romon',23,'bold'),fg='white')
                                    y4.place(x=30, y=200)
                                    
                                    e1 = Entry(p2,width=18,font='arial 15 bold',relief=SUNKEN,bd=7)
                                    e1.place(x=300, y=10)
                                    
                                    e2 = Entry(p2,width=18,font='arial 15 bold',relief=SUNKEN,bd=7)
                                    e2.place(x=300, y=73)
                                    
                                    e3 = Entry(p2,width=18,font='arial 15 bold',relief=SUNKEN,bd=7)
                                    e3.place(x=300, y=140)
                                    
                                    e4 = Entry(p2,width=18,font='arial 15 bold',relief=SUNKEN,bd=7)
                                    e4.place(x=300, y=200)

                                    Button(au,text="Back",command=Backs,height=4, width= 13,bg=b_colour,fg="white",font=("arial",10 ,"bold")).place(x=1125, y=230)
                                    Button(p2, text="Add",command = Add,height=3, width= 14,bg=b_colour,fg="white",font=("arial",14 ,"bold")).place(x=30, y=270)
                                    Button(p2, text="Update",command = update,height=3, width= 14,bg=b_colour,fg="white",font=("arial",14 ,"bold")).place(x=240, y=270)
                                    Button(p2, text="Delete",command = delete,height=3, width= 14,bg=b_colour,fg="white",font=("arial",14 ,"bold")).place(x=450, y=270)

                                    p4=LabelFrame(au,bd=10,relief=GROOVE,font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
                                    p4.place(x=0,y=450,width=1550,height=390)

                                    cols = ('Pid', 'Pname', 'Quantity','Price')
                                    listBox = ttk.Treeview(p4, columns=cols, show='headings', height=15)
                                    
                                    for col in cols:
                                        listBox.heading(col, text=col)
                                        listBox.grid(row=1, column=0, columnspan=2)
                                        listBox.place(x=387, y=10)
                                    
                                    show()
                                    listBox.bind('<Double-Button-1>',GetValue)
                                    
                                    au.mainloop()


                                def ref(): #to view bills and database
                                    dd = Tk()
                                    dd.geometry("1100x625")
                                    dd.state('zoomed')
                                    bg_color='#52088a'
                                    root.destroy()

                                    title=Label(dd,text="Databases",bd=12,bg=bg_color,fg='white',relief=GROOVE,font=("Times New Roman",30,"bold"),pady=2).pack(fill=X)

                                    def stk(): #to View Stock

                                        def show():
                                            mysqldb = mysql.connector.connect(host="localhost", user="root", password="12345", database="supermarket")
                                            mycursor = mysqldb.cursor()
                                            mycursor.execute("SELECT Pid,pname,quantity,price FROM products")
                                            records = mycursor.fetchall()
                                        
                                            for i, (Pid,Pname, Quantity,Price) in enumerate(records, start=1):
                                                listBox.insert("", "end", values=(Pid,Pname, Quantity,Price))
                                                mysqldb.close()

                                        cols = ('Pid', 'Pname', 'Quantity','Price')
                                        listBox = ttk.Treeview(j1, columns=cols, show='headings' )
                                        
                                        for col in cols:
                                            listBox.heading(col, text=col)
                                            listBox.place(x=0, y=500)
                                        
                                        show()
                                        listBox.bind('<Double-Button-1>')

                                    j2=LabelFrame(dd,bd=10,relief=GROOVE,font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
                                    j2.place(x=775,y=73,width=775,height=767)

                                    my_text= Text(j2, width=45, height= 25, font=("Helvetica",16))
                                    my_text.pack(pady=20)

                                    def opn_bils(): #to View Bills
                                        txt_file= filedialog.askopenfilename()
                                        if txt_file:
                                            fh= open(txt_file, 'r')
                                            read= fh.read()
                                            my_text.insert(END, read)
                                            fh.close() 


                                    def bac():
                                        dd.destroy()
                                        main()

                                    j1=LabelFrame(dd,bd=10,relief=GROOVE,font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
                                    j1.place(x=0,y=73,width=775,height=767)


                                    dd1= Button(j1,text="Stock", command= stk,height=3, width= 11,bg='#008080',fg="white",font=("arial",15 ,"bold"))
                                    dd1.pack(pady=10)

                                    dd3= Button(dd,text="BACK", command= bac ,height=2, width= 10,bg='#008080',fg="white",font=("arial",10 ,"bold"))
                                    dd3.place(x=20, y=17)

                                    ob= Button(j2,text="Open Bills", command= opn_bils,height=4, width= 13,bg='#008080',fg="white",font=("arial",13 ,"bold"))
                                    ob.pack(pady=20)

                                    dd.mainloop()


                                def ctt(): #to create table in MySQL
                                    mydb = ms.connect(host='localhost',
                                            user='root',
                                            password='12345')
                                    mc = mydb.cursor()
                                    mc.execute('show databases')
                                    data = mc.fetchall()

                                    print(data)

                                    time.sleep(2)

                                    a = 0

                                    for i in data:
                                        if i == ('supermarket',):
                                            print("Database Already Exists")
                                            a = a + 1
                                            break

                                    if a == 0:
                                        print("Creating database")
                                        time.sleep(1)
                                        mc.execute('create database supermarket')

                                    mc.execute('use supermarket')

                                    mc.execute('show tables')
                                    data = mc.fetchall()

                                    prod = 0

                                    for i in data:
                                        if i == ('products',):
                                            prod = prod + 1
                                            print("products table present")

                                    if prod == 0:
                                        messagebox.showinfo("information", "Creating Table!!!")
                                        print("Creating table...")

                                        mc.execute("create table products(PID int primary key,Pname varchar(20),Quantity int,Price float)")
                                        mc.execute('insert into products values(001,"Milk",100,"10.00")')
                                        mc.execute('insert into products values(002,"Bread",100,"4.50")')
                                        mc.execute('insert into products values(003,"Banana",100,"1.50")')
                                        mc.execute('insert into products values(004,"Apple",100,"1.50")')
                                        mc.execute('insert into products values(005,"Chips",100,"2.00")')
                                        mc.execute('insert into products values(006,"Pepsi",100,"4.00")')
                                        mc.execute('insert into products values(007,"7up",100,"4.00")')
                                        mc.execute('insert into products values(008,"Cheese",100,"10.00")')
                                        mc.execute('insert into products values(009,"Yogurt",100,"3.50")')
                                        mc.execute('insert into products values(010,"Pen",100,"2.00")')
                                        mc.execute('insert into products values(011,"Tennis Ball",100,"3.50")')
                                        mc.execute('insert into products values(012,"Football",100,"5.00")')
                                        mc.execute('insert into products values(013,"Biscuit",100,"4.00")')
                                        mc.execute('insert into products values(014,"Ice Cream",100,"3.50")')
                                        mc.execute('insert into products values(015,"Chocolate",100,"6.50")')
                                        mydb.commit()
                                        mc.execute("select*from products")
                                        d = mc.fetchall()
                                        print('PID', '%18s' % 'Pname', '%20s' % 'Quantity', '%20s' % 'Price')
                                        print('-' * 65)

                                        for i in d:
                                            print(i[0], '%20s' % i[1], '%20s' % i[2], '%20s' % i[3])
                                        print('-' * 65)
                                        print("Table created")
                                        messagebox.showinfo("information", "Table Created successfully...")

                                    else:
                                        mc.execute("use supermarket")
                                        mc.execute("select*from products")
                                        d = mc.fetchall()
                                        print('PID', '%18s' % 'Pname', '%20s' % 'Quantity', '%20s' % 'Price')
                                        print('-' * 65)

                                        for i in d:
                                            print(i[0], '%20s' % i[1], '%20s' % i[2], '%20s' % i[3])
                                        print('-' * 65)
                                        time.sleep(3)
                                        exit()

                                p1= LabelFrame(root,bd=10,relief=GROOVE,font=('times new romon',15,'bold'),fg='gold',bg=bg_color)
                                p1.pack(fill="both", expand="yes")

                                cout = Button(p1, text='CheckOut', fg='black', bg=b_color, font=('Times', 20, 'bold'), width=12, height=6, bd=3, command=check)

                                add = Button(p1, text='Add/Update', fg='black', bg=b_color, font=('Times', 20, 'bold'), width=12, height=6, bd=3, command=ad)

                                refund = Button(p1, text='Databases', fg='black', bg=b_color, font=('Times', 20, 'bold'), width=12, height=6, bd=3,command=ref)

                                ct = Button (p1, text='Create Database', fg='black', bg=b_color, font=('Times', 18), width=14, height=3, bd=1, command=ctt)

                                bkb= Button(p1,text="Exit", command=bac,fg='black', bg=b_color, font=('Times', 18), width=8, height=1, bd=1,)


                                cout.place(x= 50, y=30)

                                add.place(x= 650, y=30)

                                refund.place(x= 1250, y=30)

                                ct.place(x=655,y=550)

                                bkb.place(x=685,y=675)

                                mainloop()

                            main()


top = Tk()
top.geometry("500x500")
title=Label(top,text="Supermarket Management",bd=12,bg='black',fg='white',relief=GROOVE,font=("Times New Roman",30,"bold"),pady=2).pack(fill=X)

t1= LabelFrame(top,bd=10,relief=GROOVE,font=('times new romon',15,'bold'),fg='gold',bg="#040405")
t1.pack(fill="both", expand="yes")

Button1 = Button(t1,text="Submit", command=Login, font=('Times', 18), width=8, height=1, bd=1)
Button1.place(x=180, y=200)

text1 = Label(t1, text="Username:", bg="#040405", fg="White", font=('times new romon',13,'bold'))
text1.place(x=20, y= 80)

text2 = Label(t1, text="Password:", bg="#040405", fg="White", font=('times new romon',13,'bold'))
text2.place(x=20, y= 140)

Entry1 = Entry(t1, highlightthickness=0, relief=FLAT, bg="#040405",fg="white", font=('times new romon',13,'bold'),width=35)
Entry1.place(x=125, y=82)

Entry1l = Canvas(t1,width=300, height=2,highlightthickness=0,bg="#bdb9b1")
Entry1l.place(x=125, y=100)

Entry2 = Entry(t1, highlightthickness=0, relief=FLAT, bg="#040405",fg="white", font=('times new romon',13,'bold'),width=35)
Entry2.place(x=125, y=142)

Entry2l = Canvas(t1,width=300, height=2,highlightthickness=0,bg="#bdb9b1")
Entry2l.place(x=125, y=160)

top.mainloop()