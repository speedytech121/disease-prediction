from tkinter import*
from subprocess import call
import sqlite3 as s 
from tkinter import messagebox
from PIL import ImageTk,Image


patientloginscr=Tk(className=' Patient Login')
patientloginscr.geometry('300x180')
patientloginscr.maxsize(width=300,height=180)

# FOR BACKGROUND IMAGE
i=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\3.jpg'))
l=Label(patientloginscr,image=i)
l.pack()


# DATABASE FOR LOGIN
try:
    client=s.connect("C://Users//Hackers world//Desktop//projects//healthprediction//register.db")
    cu=client.cursor()
    cu.execute("create table pregister(name varchar(50),email varchar(80),phone int,password varchar(20),confirmpassword varchar(20))")
except:
    pass

def diseasetype():
        cu.execute("select count(*) from pregister where Name=%r and Password=%r"%(id_t.get(),pswd_t.get()))
        a=cu.fetchall()
        if a[0][0]==1:
            messagebox.showinfo('Successful','Login Sucessfull')
            patientloginscr.destroy()
            call(["python","diseasetypes.py"])
        else:
            messagebox.showinfo('not found','Username or Password not found')


def destroy():
    patientloginscr.destroy()
    call(['python','home.py'])


# LABELS
heading=Label(master=patientloginscr,text='PATIENT   LOGIN',bg='darkcyan',fg='white')
id=Label(master=patientloginscr,text='User_Id    ',relief=FLAT,bd=2, bg='darkcyan',fg='white')
pswd=Label(master=patientloginscr,text='Password',relief=FLAT,bd=2,bg='darkcyan',fg='white')
heading.place(x=0,y=0,width=300)
id.place(x=25,y=45)
pswd.place(x=25,y=75)

# ENTRY BOX
id_t=Entry(master=patientloginscr,width=30)
pswd_t=Entry(master=patientloginscr,show="*",width=30)
id_t.place(x=90,y=45)
pswd_t.place(x=90,y=75)

# LOGIN BUTTON
login=Button(master=patientloginscr,text='LOGIN',bg='darkcyan',fg='white',command=diseasetype)
login.place(x=90,y=100)
exitb=Button(master=patientloginscr,text='BACK',bg='darkcyan',fg='white',command=destroy)
exitb.place(x=150,y=100)




patientloginscr.mainloop()

