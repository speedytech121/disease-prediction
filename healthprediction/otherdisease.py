from tkinter import *
import numpy as np
import pandas as pd
from subprocess import call
from PIL import ImageTk,Image
import sqlite3 as s

# DATABASE FOR REGISTER
try:
    client=s.connect("C://Users//Hackers world//Desktop//projects//healthprediction//register.db")
    cu=client.cursor()
    cu.execute("create table adddisease(disease_name varchar(50),sym1 varchar(80),sym2 varchar(80),sym3 varchar(80),sym4 varchar(80),sym5 varchar(80),sym6 varchar(80)")
except:
    pass

# functions
def adminpage():
    scr.destroy()
    call(['python','adminpage.py'])


# GUI TKINTER
scr=Tk(className=' Other Diseases')
#for screen size
scr.geometry('450x740')
scr.maxsize(740,450)
scr.minsize(740,450)

# FRAME
frame=Frame(scr,width=740,height=450,bg='darkcyan')
frame.place(x=0,y=0)

# LABEL
text=Label(master=scr,font=('times',17,'bold'),bg='darkcyan',fg='white',bd=0,relief=RIDGE,text="\t\t            OTHER DISEASES")
text.place(x=0,y=0)

# Vertical (y) Scroll Bar
scroll = Scrollbar(scr)
scroll.pack(side=RIGHT, fill=Y)

# Text Widget
frame1=Text(scr,bg='#D3D3D3',width=90,height=26,bd=0)
frame1.place(x=0,y=40)

# Configure the scrollbars
scroll.config(command=frame1.yview)

#for fetching all other added disease
diseases=cu.execute('select disease_name from adddisease')
a=list(diseases.fetchall())
print(a)
# for inserting disease in frame1
for i in range(1,len(a)+1):
    print(a)
    b=list(a[i-1])
    b=[j.replace('\\n','') for j in b]
    frame1.insert(END,b[0]+'\n')


btn=Button(master=scr,text='BACK',command=adminpage)
btn.place(x=670,y=420)


scr.mainloop()