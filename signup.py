from tkinter import*
from tkinter import messagebox
import mysql.connector
win=Tk()
w=win.winfo_screenwidth()
h=win.winfo_screenheight()
win.configure(width=w,height=h,bg="white")  
win.title(" Sign Up")

mycon=mysql.connector.connect(host='localhost',user='root',password='pass',database='dedentry')
mycursor=mycon.cursor()
'''
mycursor.execute('drop table if exists userlogs')
mycursor.execute('create table userlogs(user varchar(20),pass varchar(20))')
'''
bg=PhotoImage(file="login1.png")
lb1=Label(win,image=bg)
lb1.place(x=-60,y=-30)


gh=[]
fo='select * from userlogs'
mycursor.execute(fo)
go=mycursor.fetchall()
for c in go:
    gh.append(c[0])

def insert1():
    if tb1.get() in gh:
        messagebox.showinfo("Subject Message","UserName Already Exists....Try Another UserName")
    elif tb1.get()!="" and tb2.get()!="":
        u=tb1.get()
        p=tb2.get()
        qry='insert into userlogs values(%s,%s)'
        dat=[u,p]
        mycursor.execute(qry,dat)
        messagebox.showinfo("Subject Message","Account Created Succesfully")
        clear()
        mycon.commit()
        win.destroy()
        import loginpage
    else:
        messagebox.showinfo("Subject Message","Empty Field !")
        
def log():
    win.destroy()
    import loginpage

def clear():
    tb1.delete(0,'end')
    tb2.delete(0,'end')
    tb1.focus()

lb2=Label(text="Sign Up",font=("timesnewroman",20,"bold"))
lb2.place(x=620,y=100)

lb3=Label(text="Enter UserName",font=("timesnewroman",20,"bold"))
lb3.place(x=570,y=190)

lb4=Label(text="Enter Password",font=("timesnewroman",20,"bold"))
lb4.place(x=570,y=350)

tb1=Entry(win,font=("courier",17),width=22)
tb2=Entry(win,show="*",font=("courier",17),width=22)
tb1.place(x=530,y=260)
tb2.place(x=530,y=410)

def temp_text1(tb):
    tb1.delete(0,'end')

tb1.insert(0,"Enter the Username")
tb1.bind("<FocusIn>",temp_text1)
tb1.place(x=530,y=260)


btt1=Button(win,text="Sign up",font=("timesnewroman",15,"bold"),width=10,bd=5,command=insert1)
btt1.place(x=615,y=480)

lb4=Label(text="Already Have An Account? Then Click Below",font=("timesnewroman",14))
lb4.place(x=500,y=540)

btt2=Button(win,text="Login",font=("timesnewroman",15,"bold"),width=15,bd=5,command=log)
btt2.place(x=590,y=580)


win.mainloop()









