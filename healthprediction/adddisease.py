from tkinter import*
from subprocess import call
from PIL import ImageTk,Image
from tkinter import messagebox
import sqlite3 as s

scr=Tk(className='Add Disease')


# DATABASE FOR REGISTER
try:
    client=s.connect("C://Users//Hackers world//Desktop//projects//healthprediction//register.db")
    cu=client.cursor()
    cu.execute("create table adddisease(disease_name varchar(50),sym1 varchar(80),sym2 varchar(80),sym3 varchar(80),sym4 varchar(80),sym5 varchar(80),sym6 varchar(80)")
except:
    pass


# FOR BACKGROUND IMAGE
i=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\addis.png'))
l=Label(scr,image=i)
l.pack()

#for screen size
scr.geometry("{0}x{1}+0+0".format(scr.winfo_screenwidth(), scr.winfo_screenheight()))


def register():
        cu.execute("insert into adddisease values(%r,%r,%r,%r,%r,%r,%r)"%(e1.get("1.0","end"),e2.get("1.0","end"),e3.get("1.0","end"),e4.get("1.0","end"),e5.get("1.0","end"),e6.get("1.0","end"),e7.get("1.0","end")))
        client.commit()
        messagebox.showinfo('SUCCESS','Disease successfuly added')
        scr.destroy()
        call(['python','adminpage.py'])


# entry box
e1=Text(scr,relief=RIDGE,height=2,width=45,bg='lightcyan')

e2=Text(scr,relief=RIDGE,height=2,width=45,bg='yellow')
e3=Text(scr,relief=RIDGE,height=2,width=45,bg='yellow')
e4=Text(scr,relief=RIDGE,height=2,width=45,bg='yellow')
e5=Text(scr,relief=RIDGE,height=2,width=45,bg='yellow')
e6=Text(scr,relief=RIDGE,height=2,width=45,bg='yellow')
e7=Text(scr,relief=RIDGE,height=2,width=45,bg='yellow')

e1.place(x=10,y=200)
e2.place(x=500,y=200)
e3.place(x=930,y=200)
e4.place(x=500,y=400)
e5.place(x=930,y=400)
e6.place(x=500,y=600)
e7.place(x=930,y=600)

b=Button(scr,text='ADD',width=5,bg='red',fg='white',font=('Time',15,'bold'),command=register)
b.place(x=930,y=690)

scr.mainloop()
