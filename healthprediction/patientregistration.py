from tkinter import *
from subprocess import call
from subprocess import call
from PIL import ImageTk,Image
import sqlite3 as s
from tkinter import messagebox

scr=Tk(className='Patient Registeration')

# FOR BACKGROUND IMAGE
i=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\bgimage.jpg'))
l=Label(scr,image=i)
l.pack()

#for screen size
scr.geometry("{0}x{1}+0+0".format(scr.winfo_screenwidth(), scr.winfo_screenheight()))

# DATABASE FOR REGISTER
try:
    client=s.connect("C://Users//Hackers world//Desktop//projects//healthprediction//register.db")
    cu=client.cursor()
    cu.execute("create table pregister(name varchar(50),email varchar(80),phone int,password varchar(20),confirmpassword varchar(20))")
except:
    pass

# login button function to redirect to the dashboard
def register():
        if en3.get()==en4.get():
            cu.execute("insert into pregister values(%r,%r,%d,%r,%r)"%(en.get(),en1.get(),int(en2.get()),en3.get(),en4.get()))
            client.commit()
            scr.destroy()
            call(['python','patientlogin.py'])
        else:
            messagebox.showinfo('Error','password does not match')

def destroy():
    scr.destroy()
    call(['python','home.py'])




a=Label(scr,text='Name       ',fg='black',font=('Time',24,'bold'))
a1=Label(scr,text='Email       ',fg='black',font=('Time',24,'bold'))
a2=Label(scr,text='Phone      ',fg='black',font=('Time',24,'bold'))
a3=Label(scr,text='Password',fg='black',font=('Time',24,'bold'))
a4=Label(scr,text='Confirm   ',fg='black',font=('Time',24,'bold'))
en=Entry(scr,font=('default',24),fg='blue',bd=5)
en1=Entry(scr,font=('default',24),fg='blue',bd=5)
en2=Entry(scr,font=('default',24),fg='blue',bd=5)
en3=Entry(scr,font=('default',24),fg='blue',bd=5,show='*')
en4=Entry(scr,font=('default',24),fg='blue',bd=5,show='*')
bu=Button(scr,text=' REGISTER ',font=('default',32),bg='red',fg='White',command=register)
exitb=Button(scr,text='BACK',font=('default',32),bg='green',fg='White',command=destroy)
exitb.place(x=890,y=600)
a5=Label(scr,text='PATIENT REGISTER',width=45,bg='black',fg='yellow',font=('Arial Black',32,'bold'))
a5.place(x=0,y=0)
a.place(x=300,y=130)
a1.place(x=300,y=230)
a2.place(x=300,y=330)
a3.place(x=300,y=430)
a4.place(x=300,y=530)
en.place(x=600,y=130)
en1.place(x=600,y=230)
en2.place(x=600,y=330)
en3.place(x=600,y=430)
en4.place(x=600,y=530)
bu.place(x=600,y=600)


scr.mainloop()
