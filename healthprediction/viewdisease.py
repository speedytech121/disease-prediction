from tkinter import *
import numpy as np
import pandas as pd
from subprocess import call
from PIL import ImageTk,Image
import sqlite3 as s

# functions
def adminpage():
    scr.destroy()
    call(['python','adminpage.py'])


tr=pd.read_csv("Testing.csv")
disease=(list(set(tr['prognosis'])))

# GUI TKINTER
scr=Tk(className='Diseases')
#for screen size
scr.geometry('450x740')
scr.maxsize(740,450)
scr.minsize(740,450)

# FRAME
frame=Frame(scr,width=740,height=450,bg='darkcyan')
frame.place(x=0,y=0)

# LABEL
text=Label(master=scr,font=('times',17,'bold'),bg='darkcyan',fg='white',bd=0,relief=RIDGE,text="\t\t            GENERAL DISEASES")
text.place(x=0,y=0)

# Vertical (y) Scroll Bar
scroll = Scrollbar(scr)
scroll.pack(side=RIGHT, fill=Y)

# Text Widget
frame1=Text(scr,bg='#D3D3D3',width=90,height=26,bd=0)
frame1.place(x=0,y=40)

# Configure the scrollbars
scroll.config(command=frame1.yview)

for i in range(len(disease)):
    frame1.insert(END,'  '+disease[i]+'\n')




btn=Button(master=scr,text='BACK',command=adminpage)
btn.place(x=670,y=420)



scr.mainloop()