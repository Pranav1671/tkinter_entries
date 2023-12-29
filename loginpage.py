from tkinter import*
from tkinter import messagebox
import mysql.connector
win=Tk()
w=win.winfo_screenwidth()
h=win.winfo_screenheight()
win.configure(width=w,height=h,bg="white")  
win.title("Login Registration")

mycon=mysql.connector.connect(host='localhost',user='root',password='pass',database='dedentry')
mycursor=mycon.cursor()

bg=PhotoImage(file="back2.png")
lb1=Label(win,image=bg)
lb1.place(x=-80,y=-30)
bg1=PhotoImage(file="profile.png")
lb2=Label(win,image=bg1)
lb2.place(x=590,y=130)

gh=[]
bh=[]
fo='select * from userlogs'
mycursor.execute(fo)
go=mycursor.fetchall()
for c in go:
    gh.append(c[0])
    bh.append(c[1])

def insert1():
    if (tb1.get() in gh) and (tb2.get() in bh):
        messagebox.showinfo("Subject Message","Your Login Succesful")
        win.destroy()
        import records
    else:
        messagebox.showinfo("Subject Message","Incorrect Username Or Password")
        
def new1():
    win.destroy()
    import signup

def clear():
    tb1.delete(0,'end')
    tb2.delete(0,'end')
    tb1.focus()

lb2=Label(text="Login Application",font=("timesnewroman",20,"bold"))
lb2.place(x=570,y=100)

lb3=Label(text="UserName",font=("timesnewroman",20,"bold"))
lb3.place(x=430,y=320)

lb4=Label(text="Password",font=("timesnewroman",20,"bold"))
lb4.place(x=430,y=420)

tb1=Entry(font=("courier",17),width=22)
tb2=Entry(win,show="*",font=("courier",17),width=22)
tb1.place(x=600,y=325)
tb2.place(x=600,y=425)

def temp_text(tb):
    tb1.delete(0,'end')

tb1.insert(0,"Enter the Username")
tb1.bind("<FocusIn>",temp_text)
tb1.place(x=600,y=325)

btt1=Button(win,text="Sign in",font=("timesnewroman",15,"bold"),width=10,bd=5,command=insert1)
btt1.place(x=620,y=490)

btt2=Button(win,text="Create Account",font=("timesnewroman",15,"bold"),width=15,bd=5,command=new1)
btt2.place(x=590,y=550)

win.mainloop()









