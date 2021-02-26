from tkinter import*
from subprocess import call
from PIL import ImageTk,Image
import sqlite3 as s


# DATABASE FOR LOGIN
try:
    client=s.connect("C://Users//Hackers world//Desktop//projects//healthprediction//register.db")
    cu=client.cursor()
    cu.execute("create table adddisease(disease_name varchar(50),sym1 varchar(80),sym2 varchar(80),sym3 varchar(80),sym4 varchar(80),sym5 varchar(80),sym6 varchar(80)")
except:
    pass


cu.execute("select * from adddisease")
a=list(cu.fetchall())


mydict={}
for i in range(1,(len(a)+1)):
    b=list(a[i-1])
    b=[j.replace('\\n','') for j in b]
    mydict[str(b[0])]=[str(b[1]),str(b[2]),str(b[3]),str(b[4]),str(b[5]),str(b[6])]
print(mydict)



# FUNCTIONS
def button():
    for k, v in mydict.items():
        if  e1.get() and e2.get() and e3.get() and e4.get() in v:
            print(k)
        elif  e1.get() and e2.get() and e3.get() in v:
            print(k)
        elif  e1.get() and e2.get() in v:
            print(k)
        elif  e1.get() in v:
            print(k)
    text.insert(END,k)
def back():
    scr.destroy()
    call(['python','diseasetypes.py'])
    
# gui_stuff------------------------------------------------------------------------------------
scr = Tk(className=' Added Disease Predictor')
scr.geometry('450x540')
scr.maxsize(540,450)
scr.minsize(540,450)

# FOR BACKGROUND IMAGE
i=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\magni.png'))
l=Label(scr,image=i)
l.pack()

# LABEL
l1=Label(scr,text='symptom 1')
l2=Label(scr,text='symptom 2')
l3=Label(scr,text='symptom 3')
l4=Label(scr,text='symptom 4')
l1.place(x=100,y=0)
l2.place(x=100,y=25)
l3.place(x=100,y=50)
l4.place(x=100,y=75)

# ENTRY
e1=Entry(scr,width=50,bg='cyan')
e1.place(x=200,y=0)
e2=Entry(scr,width=50,bg='cyan')
e2.place(x=200,y=25)
e3=Entry(scr,width=50,bg='cyan')
e3.place(x=200,y=50)
e4=Entry(scr,width=50,bg='cyan')
e4.place(x=200,y=75)


# TEXT ENTRY
text=Text(scr,width=37,height=10)
text.place(x=200,y=120)

# BUTTON
b=Button(scr,text='PREDICT',command=button,font=('Time',15,'bold'),bg='darkcyan',fg='white')
b.place(x=200,y=300)
b1=Button(scr,text='BACK',command=back,font=('Time',15,'bold'),bg='darkcyan',fg='white')
b1.place(x=350,y=300)
scr.mainloop()