from tkinter import*
from subprocess import call
import sqlite3 as s
from tkinter import messagebox
from PIL import ImageTk,Image


adminloginscr=Tk(className=' Admin Login')
adminloginscr.geometry('300x180')
adminloginscr.maxsize(width=300,height=180)


# FOR BACKGROUND IMAGE
i=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\3.jpg'))
l=Label(adminloginscr,image=i)
l.pack()

# DATABASE FOR LOGIN
try:
    client=s.connect("C://Users//Hackers world//Desktop//projects//healthprediction//register.db")
    cu=client.cursor()
    cu.execute("create table aregister(name varchar(50),email varchar(80),phone int,password varchar(20),confirmpassword varchar(20))")
except:
    pass

def adminpage():
        cu.execute("select count(*) from aregister where Name=%r and Password=%r"%(id_t.get(),pswd_t.get()))
        a=cu.fetchall()
        if a[0][0]==1:
            messagebox.showinfo('Successful','Login Sucessfull')
            adminloginscr.destroy()
            call(["python","adminpage.py"])
        else:
            messagebox.showinfo('not found','Username or Password not found')




def destroy():
    adminloginscr.destroy()
    call(['python','home.py'])


# LABELS
heading=Label(master=adminloginscr,text='ADMIN    LOGIN',bg='darkcyan',fg='white')
id=Label(master=adminloginscr,text='User_Id    ',bg='darkcyan',fg='white')
pswd=Label(master=adminloginscr,text='Password',bg='darkcyan',fg='white')
heading.place(x=0,y=0,width=300)
id.place(x=25,y=45)
pswd.place(x=25,y=75)

# ENTRY BOX
id_t=Entry(master=adminloginscr,width=30)
pswd_t=Entry(master=adminloginscr,show="*",width=30)
id_t.place(x=90,y=45)
pswd_t.place(x=90,y=75)

# LOGIN BUTTON
login=Button(master=adminloginscr,text='LOGIN',bg='darkcyan',fg='white',command=adminpage)
login.place(x=90,y=100)

exitb=Button(master=adminloginscr,text='BACK',bg='darkcyan',fg='white',command=destroy)
exitb.place(x=150,y=100)



adminloginscr.mainloop()

