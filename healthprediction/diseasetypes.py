from tkinter import*
from subprocess import call
from PIL import ImageTk,Image


# FUNCTIONS
def cleancode():
    scr.destroy()
    call(['python','clean_code.py'])

def otherdisease():
    scr.destroy()
    call(['python','addedprediction.py'])



scr=Tk(className='choose disease type')

# FOR BACKGROUND IMAGE
i=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\bgimage1.jpg'))
l=Label(scr,image=i)
l.pack()

#for screen size
scr.geometry("{0}x{1}+0+0".format(scr.winfo_screenwidth(), scr.winfo_screenheight()))

label=Label(scr,text='Choose Your Disease Prediction Category',width=80,bg='darkcyan',fg='white',font=('Helvetica',24,'bold'))
label.place(x=0,y=0)




def bot():
    scr.destroy()
    call(['python','drbot.py'])


frame1=Frame(master=scr,bg='yellow',width=300,height=500,bd=0)
frame1.place(x=350,y=180)

frame2=Frame(master=scr,bg='yellow',width=300,height=500,bd=0)
frame2.place(x=790,y=180)


# FOR BACKGROUND IMAGE
i2=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\gend.png'))
l2=Label(frame1,image=i2)
l2.pack()

# FOR BACKGROUND IMAGE
i3=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\otherpng.png'))
l3=Label(frame2,image=i3)
l3.pack()


b1=Button(master=frame1,bg='red',fg='white',text='GENERAL DISEASE',font=('Time',15,'bold'),command=cleancode)
b3=Button(master=frame2,bg='red',fg='white',text='OTHER DISEASES',font=('Time',15,'bold'),command=otherdisease)
b1.place(x=35,y=430)
b3.place(x=35,y=430)


scr.mainloop()