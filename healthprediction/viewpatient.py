from tkinter import*
import sqlite3 as s
from PIL import ImageTk,Image
from subprocess import call
import itertools


# functions
def adminpage():
    scr.destroy()
    call(['python','adminpage.py'])

scr=Tk()

#for screen size
scr.geometry('450x740')
scr.maxsize(740,450)
scr.minsize(740,450)

try:
    client=s.connect("C://Users//Hackers world//Desktop//projects//healthprediction//register.db")
    cu=client.cursor()
    cu.execute("create table patient(name varchar(50),disease varchar(80))")
except:
    pass

# LABEL
l1=Label(scr,text='NAME',width=32,height=3,bg='darkcyan',fg='white',justify=LEFT,font=('times',15,'bold'))
l1.place(x=0,y=0)
l2=Label(scr,text='DISEASE',width=32,height=3,bg='darkcyan',fg='white',justify=LEFT,font=('times',15,'bold'))
l2.place(x=340,y=0)


# Vertical (y) Scroll Bar
scroll = Scrollbar(scr)
scroll.pack(side=RIGHT, fill=Y)

# Text Widget
eula = Text(scr,bg='#D3D3D3', wrap=NONE,width=90,height=25, yscrollcommand=scroll.set)
eula.place(x=0,y=55)

# Configure the scrollbars
scroll.config(command=eula.yview)



# ALGORITHM TO INSERT VALUES FROM DATABASE LIST
cu.execute('select * from patient')
a=list(cu.fetchall())

eula.insert(END,'\n')
for i in range(1,(len(a)+1)):
    b=list(a[i-1])
    for j in range(1):
            c=(b[j]+'\t\t\t\t\t\t\t'+b[j+1])
            eula.insert(END,str(i)+'.)  '+c+'\n')

btn=Button(master=scr,text='BACK',command=adminpage)
btn.place(x=670,y=420)

scr.mainloop()