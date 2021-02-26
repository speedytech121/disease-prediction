from tkinter import *
from subprocess import call
from PIL import ImageTk,Image

scr=Tk(className=' Type of disease')

# FOR BACKGROUND IMAGE
i=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\diseasetype.png'))
l=Label(scr,image=i)
l.pack()



#for screen size
scr.geometry("{0}x{1}+0+0".format(scr.winfo_screenwidth(), scr.winfo_screenheight()))



def gd():
    scr.destroy()
    call(['python','viewdisease.py'])
def od():
    scr.destroy()
    call(['python','otherdisease.py'])



loadimage1 = ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\general.png'))
general =Button(image=loadimage1,width=220,height=41,command=gd)
general["bg"] = "white"
general["border"] = "5"
general.place(x=550,y=200)

loadimage2 = ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\other.png'))
other =Button(image=loadimage2,width=220,height=41,command=od)
other["bg"] = "white"
other["border"] = "5"
other.place(x=550,y=300)

scr.mainloop()