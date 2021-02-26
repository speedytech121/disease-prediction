from tkinter import*
from PIL import ImageTk,Image
from subprocess import call

# SCREEN
scr=Tk(className=" AdminPage")

# FOR BACKGROUND IMAGE
i=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\bgimage.jpg'))
l=Label(scr,image=i)
l.pack()

#for screen size
scr.geometry("{0}x{1}+0+0".format(scr.winfo_screenwidth(), scr.winfo_screenheight()))

#functions
def exit():
    scr.destroy()
    call(["python","home.py"])

def viewpatient():
    scr.destroy()
    call(['python','viewpatient.py'])

def viewdisease():
    scr.destroy()
    call(['python','viewdiseasetype.py'])

def adddisease():
    scr.destroy()
    call(['python','adddisease.py'])

# MENU BUTTONS
logoutbutton=Button(master=scr,text='LOGOUT', fg='white',font=("Times", "18", "bold"),bg='darkcyan',activebackground='green',activeforeground='black',command=exit)
logoutbutton.place(width=1400,height=40,x=0,y=0)

# frame
fr=Frame(master=scr,width=1000,height=250,bd=1,relief=RIDGE)
fr.place(x=200,y=300)
fr1=Frame(master=scr,width=500,height=30,bg='#33ccff',bd=0,relief=RIDGE)
fr1.place(x=450,y=560)
fr2=Frame(master=scr,width=250,height=20,bg='#3399ff',bd=0,relief=RIDGE)
fr2.place(x=575,y=600)
fr3=Frame(master=scr,width=125,height=15,bg='#3366ff',bd=0,relief=RIDGE)
fr3.place(x=637,y=630)
fr4=Frame(master=scr,width=62,height=7,bg='#3333ff',bd=0,relief=RIDGE)
fr4.place(x=668,y=655)
fr5=Frame(master=scr,width=31,height=3,bg='#3333ff',bd=0,relief=RIDGE)
fr5.place(x=683,y=670)



# FOR BACKGROUND IMAGE
i1=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\frame.jpg'))
l1=Label(fr,image=i1)
l1.pack()

# WIDGETS(FUNCTIONS) BUTTONS
addd=Button(master=scr, text='ADD DISEASE',bg='red',fg='white',bd=2,relief=SUNKEN,font=("Times", "18", "bold"),command=adddisease)
viewdisease=Button(master=scr, text='VIEW DISEASE',bg='red',fg='white',bd=2,relief=SUNKEN,font=("Times", "18", "bold"),command=viewdisease)
viewpatient=Button(master=scr, text='VIEW PATIENT',bg='red',fg='white',bd=2,relief=SUNKEN,font=("Times", "18", "bold"),command=viewpatient)
addd.place(width=200,height=200,x=235,y=325)
viewdisease.place(width=200,height=200,x=590,y=325)
viewpatient.place(width=200,height=200,x=970,y=325)


scr.mainloop()