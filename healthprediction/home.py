from tkinter import *
from PIL import Image,ImageTk
from subprocess import call

class screen():
    # SUBPROCESS CALL FUNCTION FOR CALLING OTHER MODULE IN OPEN MODE
    def fun(self):
        self.ms.destroy()
        call(["python", "adminlogin.py"])

    def fun1(self):
        self.ms.destroy()
        call(["python", "patientlogin.py"])

    def adminregister(self):
        self.ms.destroy()
        call(["python","adminregister.py"])

    def patientregister(self):
        self.ms.destroy()
        call(["python","patientregistration.py"])



    def __init__(self):
        self.ms=Tk(className=" Health Prediction")
        self.image=Image.open("C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\dentist.png")
        self.photo=ImageTk.PhotoImage(self.image)
        self.lbl1=Label(image=self.photo)
        self.lbl1.pack()
        self.frame1 = Frame(master=self.ms, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=400, height=150, bd= 0)
        self.frame1.place(x=300,y=550)

        self.lbl4=Label(master=self.ms,text="Admin",bd=1,relief=SOLID,font=("Times", "30", "bold"))
        self.lbl4.place(x=425,y=520)
        self.btn1=Button(master=self.ms,text="Register",font=("Times", "20", "bold"),bg="red",fg="white",command=self.adminregister)
        self.btn1.place(x=320,y=600)
        self.btn2=Button(master=self.ms,text="Login",font=("Times", "20", "bold"),bg="Red",fg="white",command=self.fun)
        self.btn2.place(x=570,y=600)
        self.frame2 = Frame(master=self.ms, highlightbackground="black", highlightcolor="black", highlightthickness=1, width=400, height=150, bd= 0)
        self.frame2.place(x=800,y=550)

        self.lbl4=Label(master=self.ms,text="Patient",bd=1,relief=SOLID,font=("Times", "30", "bold"))
        self.lbl4.place(x=930,y=520)
        self.btn3=Button(master=self.ms,text="Register",font=("Times", "20", "bold"),bg="red",fg="white",command=self.patientregister)
        self.btn3.place(x=820,y=600)
        self.btn4=Button(master=self.ms,text="Login",font=("Times", "20", "bold"),bg="red",fg="white",command=self.fun1)
        self.btn4.place(x=1070,y=600)
        self.btn5=Button(master=self.ms,text="Exit",font=("Times", "20", "bold"),bg="white",fg="black",command=lambda:self.ms.destroy())
        self.btn5.place(x=1380,y=650)
        self.ms.mainloop()
scr=screen()


