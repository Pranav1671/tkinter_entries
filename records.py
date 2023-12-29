import tkinter
from tkinter import ttk
from tkinter import *
import mysql.connector
from tkinter import messagebox
win=tkinter.Tk()
h=win.winfo_screenheight()
w=win.winfo_screenwidth()
win.geometry('1356x800')

mycon=mysql.connector.connect(host='localhost',user='root',password='pass',database='dedentry')
mycursor=mycon.cursor()
'''
mycursor.execute('drop table if exists entry')
mycursor.execute('create table entry(id int(5),name varchar(20),position varchar(20),salary int(10),mobile varchar(14))')
'''
bgimg=tkinter.PhotoImage(file="blue3d.png") 
limg=tkinter.Label(win,image=bgimg)
limg.place(x=-270,y=0)

s=ttk.Style()
s.theme_use('clam')
s.configure('Treeview.Heading',font=('copper',15))
s.configure('Treeview',rowheight=28)

tree=ttk.Treeview(win)
tree['columns']=('id','name','position','salary','mobile')
tree.column('#0',width=0,stretch='NO')
tree.column('#1',width=50,anchor='center')
tree.column('#2',width=100,anchor='center')
tree.column('#3',width=150,anchor='center')
tree.column('#4',width=100,anchor='center')
tree.column('#5',width=150,anchor='center')

tree.heading('#0',text='')
tree.heading('#1',text='Id')
tree.heading('#2',text='Name')
tree.heading('#3',text='Position')
tree.heading('#4',text='Salary')
tree.heading('#5',text='MobileNumber')

'''
qry='insert into entry values(%s,%s,%s,%s,%s)'
data=[[1001,'Treadway','Manager',85000,9878652398],[1002,'Desmond','HR Manager',85000,9523785945],[1003,'Lucifer','Cloud Admin',95000,9878956989],[1004,'Shelby','Boss',500000,9452318976]]
for f in data:
    mycursor.execute(qry,f)
    mycon.commit()
'''

g1=[]
g2=[]
g3=[]
g4=[]
g5=[]
fo='select * from entry'
mycursor.execute(fo)
go=mycursor.fetchall()
for c in go:
    g1.append(c[0])
    g2.append(c[1])
    g3.append(c[2])
    g4.append(c[3])
    g5.append(c[4])


global count
count=0
for i in range(len(g1)):
    tree.insert(parent='',index='end',iid=count,values=(g1[i],g2[i],g3[i],g4[i],g5[i]))
    count+=1

tree.pack(pady=20)


frm=tkinter.Frame(win)
frm.pack(pady=20)

lb0=tkinter.Label(frm,text='Id',font=('arialblack',15,'bold'))
lb1=tkinter.Label(frm,text='Name',font=('arialblack',15,'bold'))
lb2=tkinter.Label(frm,text='Position',font=('arialblack',15,'bold'))
lb3=tkinter.Label(frm,text='Salary',font=('arialblack',15,'bold'))
lb4=tkinter.Label(frm,text='MobileNumber',font=('arialblack',15,'bold'))

lb0.grid(row=0,column=0)
lb1.grid(row=0,column=1)
lb2.grid(row=0,column=2)
lb3.grid(row=0,column=3)
lb4.grid(row=0,column=4)

tb0=tkinter.Entry(frm,font=('arialblack',15,'bold'))
tb1=tkinter.Entry(frm,font=('arialblack',15,'bold'))
tb2=tkinter.Entry(frm,font=('arialblack',15,'bold'))
tb3=tkinter.Entry(frm,font=('arialblack',15,'bold'))
tb4=tkinter.Entry(frm,font=('arialblack',15,'bold'))

tb0.grid(row=1,column=0)
tb1.grid(row=1,column=1)
tb2.grid(row=1,column=2)
tb3.grid(row=1,column=3)
tb4.grid(row=1,column=4)

def add_record():
    global count
    if (len(tb0.get())==0 and len(tb1.get())==0 and len(tb2.get())==0 and len(tb3.get())==0 and len(tb4.get())==0)==True:
        messagebox.showinfo('Info','All The Entries Are Empty')
    elif (tb3.get().isnumeric() and tb4.get().isnumeric() and len(tb0.get())!=0 and len(tb1.get())!=0 and len(tb2.get())!=0 and len(tb3.get())!=0 and len(tb4.get())!=0)==True:
        tree.insert(parent='',index='end',iid=count,values=(tb0.get(),tb1.get(),tb2.get(),tb3.get(),tb4.get()))
        qry='insert into entry values(%s,%s,%s,%s,%s)'
        dat=[tb0.get(),tb1.get(),tb2.get(),tb3.get(),tb4.get()]
        mycursor.execute(qry,dat)
        count+=1
        tb0.delete(0,'end')
        tb1.delete(0,'end')  #To remove the typed data in the boxes
        tb2.delete(0,'end')
        tb3.delete(0,'end')
        tb4.delete(0,'end')
        tb0.focus()          #To Reset the Cursor to the Beginning
        mycon.commit()
    elif ((tb3.get().isnumeric() or len(tb3.get())==0)==False and (tb4.get().isnumeric() or len(tb4.get())==0)==False and (tb0.get().isnumeric() or len(tb0.get())==0)==False):
        messagebox.showinfo('Info','ID , Salary and MobileNumber Sholud Be Represented By Integers')
    elif (tb0.get().isnumeric() or len(tb0.get())==0)==False:
        messagebox.showinfo('Info','ID Sholud Be Represented By Integers')
    elif (tb3.get().isnumeric() or len(tb3.get())==0)==False:
        messagebox.showinfo('Info','Salary Sholud Be Represented By Integers')
    elif (tb4.get().isnumeric() or len(tb4.get())==0)==False:
        messagebox.showinfo('Info','MobileNumber Sholud Be Represented By Integers')
    elif len(tb0.get())==0 or len(tb1.get())==0  or len(tb2.get())==0 or len(tb3.get())==0 or len(tb4.get())==0:
        messagebox.showinfo('Info','Some Fields Are Empty.... Fill Every Detail Correctly')

g=[0,0,0,0,0,0,0,0]

def rem_sel_record():
    x=tree.selection()
    for i in x:
        b=tree.item(i)
        c=b.get('values')
        qry='delete from entry where id=%s'
        dat=[c[0]]
        mycursor.execute(qry,dat)
        mycon.commit()
        tree.delete(i)

def ed():
    def edit():
        i=ent1.get()
        n=ent2.get()
        p=ent3.get()
        s=ent4.get()
        m=ent5.get()
        tree.item(x,text='',values=(i,n,p,s,m))
        qry='update entry set id=%s,name=%s,position=%s,salary=%s,mobile=%s where id=%s'
        dat=[i,n,p,s,m,y]
        mycursor.execute(qry,dat)
        mycon.commit()
        newwin.destroy()
    x=tree.selection()
    if len(x)==0:
        messagebox.showinfo('Info','Please Select An Entry and Click Edit')
    elif len(x)>1:
        messagebox.showinfo('Info','Select A Single Entry and Click Edit')
    else:
        b=tree.item(x)
        c=b.get('values')
        global y
        y=c[0]
        newwin=Toplevel(win)
        newwin.geometry('500x500+420+120')
        lbr=Label(newwin,text='Update Information',font=('arialblack',20,'bold'))
        lbr.place(x=120,y=10)
        lbl1=Label(newwin,text='Id',font=('arialblack',15))
        lbl1.place(x=50,y=90)
        ent1=Entry(newwin,font=('arialblack',15))
        ent1.insert(0,c[0])
        ent1.place(x=220,y=90)
        lbl2=Label(newwin,text='Name',font=('arialblack',15))
        lbl2.place(x=50,y=155)
        ent2=Entry(newwin,font=('arialblack',15))
        ent2.insert(0,c[1])
        ent2.place(x=220,y=155)
        lbl3=Label(newwin,text='Position',font=('arialblack',15))
        lbl3.place(x=50,y=220)
        ent3=Entry(newwin,font=('arialblack',15))
        ent3.insert(0,c[2])
        ent3.place(x=220,y=220)
        lbl4=Label(newwin,text='Salary',font=('arialblack',15))
        lbl4.place(x=50,y=285)
        ent4=Entry(newwin,font=('arialblack',15))
        ent4.insert(0,c[3])
        ent4.place(x=220,y=285)
        lbl5=Label(newwin,text='MobileNumber',font=('arialblack',15))
        lbl5.place(x=50,y=350)
        ent5=Entry(newwin,font=('arialblack',15))
        ent5.insert(0,c[4])
        ent5.place(x=220,y=350)
        btt1=Button(newwin,text='Save',font=('arialblack',15,'bold'),width=5,command=edit)
        btt1.place(x=210,y=420)
    

   
add=tkinter.Button(win,text='Add New Entry',font=('arialblack',15,'bold'),width=15,fg='black',bg='blue',command=add_record)
add.place(x=440,y=465)

rem_sel=tkinter.Button(win,text='Remove Selected Entry',font=('arialblack',15,'bold'),width=20,fg='gold',bg='red',command=rem_sel_record)
rem_sel.place(x=680,y=465)

ed=tkinter.Button(win,text='Edit Selected Entry',font=('arialblack',15,'bold'),width=20,fg='black',bg='yellow',command=ed)
ed.place(x=410,y=550)

def rem_all():
    x=tree.get_children()
    mycursor.execute('truncate table entry')
    mycon.commit()
    for i in x:
        tree.delete(i)

def selec():
    a=tree.get_children()
    tree.selection_remove(a)

bt3=Button(win,text='Deselect All',font=('courier',15,'bold'),background='green',command=selec,width=20)
bt3.place(x=410,y=630)

rem_all=tkinter.Button(win,text='Remove All Entry',font=('arialblack',15,'bold'),width=20,fg='white',bg='black',command=rem_all)
rem_all.place(x=680,y=550)

def ex():
    messagebox.showinfo('Info','Feel Free To Update Entries')
    win.destroy()

bt1=Button(win,text='Exit',font=('helvetica',15,'bold'),background='aqua',command=ex,width=15)
bt1.place(x=700,y=630)


win.mainloop()


