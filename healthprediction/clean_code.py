from tkinter import *
import numpy as np
import pandas as pd
from subprocess import call
from PIL import ImageTk,Image
import pyttsx3
import datetime
import speech_recognition as sr
import sqlite3 as s


# from gui_stuff import *
df=pd.read_csv("Training.csv")
tr=pd.read_csv("Testing.csv")


l1=['itching','skin rash','nodal skin eruptions','continuous sneezing','shivering','chills','joint pain','stomach pain',
'acidity','ulcers on tongue','muscle wasting','vomiting','burning micturition','spotting urination','fatigue',
'weight gain','anxiety','cold hands and feets','mood swings','weight loss','restlessness','lethargy','patches in throat',
'irregular sugar level','cough','high fever','sunken eyes','breathlessness','sweating','dehydration','indigestion',
'headache','yellowish skin','dark urine','nausea','loss of appetite','pain behind the eyes','back pain','constipation',
'abdominal pain','diarrhoea','mild fever','yellow urine','yellowing of eyes','acute liver failure','fluid overload',
'swelling of stomach','swelled lymph nodes','malaise','blurred and distorted vision','phlegm','throat irritation',
'redness of eyes','sinus pressure','runny nose','congestion','chest pain','weakness in limbs','fast heart rate',
'pain during bowel movements','pain in anal region','bloody stool',
'irritation in anus','neck pain','dizziness','cramps','bruising','obesity','swollen legs','swollen blood vessels',
'puffy face and eyes','enlarged thyroid','brittle nails','swollen extremeties','excessive hunger',
'extra marital contacts','drying and tingling lips','slurred speech','knee pain','hip joint pain','muscle weakness',
'stiff neck','swelling joints','movement stiffness','spinning movements','loss of balance','unsteadiness',
'weakness of one body side','loss of smell','bladder discomfort','foul smell of urine','continuous feel of urine',
'passage of gases','internal itching','toxic look (typhos)','depression','irritability','muscle pain',
'altered sensorium','red spots over body','belly pain','abnormal menstruation','dischromic patches',
'watering from eyes','increased appetite','polyuria','family history','mucoid sputum','rusty sputum',
'lack of concentration','visual disturbances','receiving blood transfusion','receiving unsterile injections',
'coma','stomach bleeding','distention of abdomen','history of alcohol consumption','fluid overload','blood in sputum',
'prominent veins on calf','palpitations','painful walking','pus filled pimples','blackheads','scurring','skin peeling',
'silver like dusting','small dents in nails','inflammatory nails','blister','red sore around nose','yellow crust ooze']




disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for x in range(0,len(l1)):
    l2.append(0)

# TESTING DATA df -------------------------------------------------------------------------------------
df=pd.read_csv("Training.csv")
df.columns = df.columns.str.replace('dischromic _patches', 'dischromic patches')
df.columns = df.columns.str.replace('spotting_ urination','spotting urination' )
df.columns = df.columns.str.replace('_', ' ')


df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

# print(df.head())

X= df[l1]
y = df[["prognosis"]]
np.ravel(y)
# print(y)

# TRAINING DATA tr --------------------------------------------------------------------------------
tr=pd.read_csv("Testing.csv")
tr.columns = tr.columns.str.replace('dischromic _patches', 'dischromic patches')
tr.columns = tr.columns.str.replace('spotting_ urination','spotting urination' )
tr.columns = tr.columns.str.replace('_', ' ')

tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]
np.ravel(y_test)
# ------------------------------------------------------------------------------------------------------
lst=[]
diseaselist=[]
def DecisionTree():

    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()   # empty model of the decision tree
    clf3 = clf3.fit(X,y)

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf3.predict(X_test)
    pre=(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        # print (k,)
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf3.predict(inputtest)
    predicted=predict[0]

    h='no'
    for a in range(0,len(disease)):
        if(predicted == a):
            h='yes'
            break


    if (h=='yes'):
        t1.delete("1.0", END)
        t1.insert(END, disease[a])
    else:
        t1.delete("1.0", END)
        t1.insert(END, "Not Found")
    lst.append(int(pre))
    diseaselist.append(disease[a])
    
    

def randomforest():
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=clf4.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    pre1=(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = clf4.predict(inputtest)
    predicted=predict[0]

    h='no'
    for b in range(0,len(disease)):
        if(predicted == b):
            h='yes'
            break

    if (h=='yes'):
        t2.delete("1.0", END)
        t2.insert(END, disease[b])
    else:
        t2.delete("1.0", END)
        t2.insert(END, "Not Found")
    lst.append(int(pre1))
    diseaselist.append(disease[b])

def NaiveBayes():
    try:
        client=s.connect("C://Users//Hackers world//Desktop//projects//healthprediction//register.db")
        cu=client.cursor()
        cu.execute("create table patient(name varchar(50),disease varchar(80))")
    except:
        pass

    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb=gnb.fit(X,np.ravel(y))

    # calculating accuracy-------------------------------------------------------------------
    from sklearn.metrics import accuracy_score
    y_pred=gnb.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    pre2=(accuracy_score(y_test, y_pred,normalize=False))
    # -----------------------------------------------------

    psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]
    for k in range(0,len(l1)):
        for z in psymptoms:
            if(z==l1[k]):
                l2[k]=1

    inputtest = [l2]
    predict = gnb.predict(inputtest)
    predicted=predict[0]

    h='no'
    for c in range(0,len(disease)):
        if(predicted == c):
            h='yes'
            break

    if (h=='yes'):
        t3.delete("1.0", END)
        t3.insert(END, disease[c])
    else:
        t3.delete("1.0", END)
        t3.insert(END, "Not Found")
    lst.append(int(pre2))
    diseaselist.append(disease[c])
    print(diseaselist)
    # IMPORTING COLLECTION
    import collections
    final=([item for item, count in collections.Counter(diseaselist).items() if count > 1])
    t4.insert(END,final)
    cu.execute("insert into patient values(%r,%r)"%(NameEn.get(),diseaselist[2]))
    client.commit()    
    
# gui_stuff------------------------------------------------------------------------------------

root = Tk(className=' Disease Predictor')
root.geometry('450x740')
root.maxsize(740,450)
root.minsize(740,450)



# FOR BACKGROUND IMAGE
i=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\png.png'))
l=Label(root,image=i)
l.grid(row=0,column=0)
# entry variables
Symptom1 = StringVar()
Symptom1.set(None)
Symptom2 = StringVar()
Symptom2.set(None)
Symptom3 = StringVar()
Symptom3.set(None)
Symptom4 = StringVar()
Symptom4.set(None)
Symptom5 = StringVar()
Symptom5.set(None)
Name = StringVar()

def sym1():
    Symptom1.set(None)
def sym2():
    Symptom2.set(None)
def sym3():
    Symptom3.set(None)
def sym4():
    Symptom4.set(None)
def sym5():
    Symptom5.set(None)

#logout function
def logoutfun():
    root.destroy()
    call(["python","home.py"])


# Heading
w2 = Label(root,width=62,height=1,justify='center', text=" Disease Predictor ",font=('times',15,'bold'), fg="white",bg='darkcyan')

w2.place(x=0,y=0)

# labels
NameLb = Label(root, text="Patient Name", font=('times',15,'bold'),fg="white",bg='darkcyan')
NameLb.place(x=10,y=72)


S1Lb = Label(root, text="Symptom 1    ", font=('times',15,'bold'),fg="white",bg='darkcyan')
S1Lb.place(x=10,y=118)

S2Lb = Label(root, text="Symptom 2    ", font=('times',15,'bold'),fg="white",bg='darkcyan')
S2Lb.place(x=10,y=158)

S3Lb = Label(root, text="Symptom 3    ", font=('times',15,'bold'),fg="white",bg='darkcyan')
S3Lb.place(x=10,y=198)

S4Lb = Label(root, text="Symptom 4    ",font=('times',15,'bold'), fg="white",bg='darkcyan')
S4Lb.place(x=10,y=238)

S5Lb = Label(root, text="Symptom 5    ",font=('times',15,'bold'), fg="white",bg='darkcyan')
S5Lb.place(x=10,y=278)


lrLb = Label(root, text="DecisionTree", font=('times',15,'bold'),fg="white",bg='green')
lrLb.place(x=10,y=322)

destreeLb = Label(root, text="Rand_Forest ", font=('times',15,'bold'),fg="white",bg='green')
destreeLb.place(x=10,y=362)

ranfLb = Label(root, text="NaiveBayes  ",font=('times',15,'bold'), fg="white",bg='green')
ranfLb.place(x=10,y=402)
# entries
OPTIONS = sorted(l1)

NameEn = Entry(root, textvariable=Name,width=25)
NameEn.place(x=140,y=73)

S1En = OptionMenu(root, Symptom1,*OPTIONS)
S1En.place(x=140,y=113)

S2En = OptionMenu(root, Symptom2,*OPTIONS)
S2En.place(x=140,y=153)


S3En = OptionMenu(root, Symptom3,*OPTIONS)
S3En.place(x=140,y=193)


S4En = OptionMenu(root, Symptom4,*OPTIONS)
S4En.place(x=140,y=233)


S5En = OptionMenu(root, Symptom5,*OPTIONS)
S5En.place(x=140,y=273)

# clear button for option menu
btn1=Button(root,text='CLEAR',command=sym1)
btn1.place(x=420,y=116)
btn2=Button(root,text='CLEAR',command=sym2)
btn2.place(x=420,y=156)
btn3=Button(root,text='CLEAR',command=sym3)
btn3.place(x=420,y=196)
btn4=Button(root,text='CLEAR',command=sym4)
btn4.place(x=420,y=236)
btn5=Button(root,text='CLEAR',command=sym5)
btn5.place(x=420,y=276)



dst = Button(root, text="DecisionTree ", font=('times',15,'bold'),command=DecisionTree,bg="green",fg="white")
dst.place(x=600,y=113)

rnf = Button(root, text="Randomforest", font=('times',15,'bold'),command=randomforest,bg="green",fg="white")
rnf.place(x=600,y=173)

lr = Button(root, text="NaiveBayes    ",font=('times',15,'bold'), command=NaiveBayes,bg="green",fg="white")
lr.place(x=600,y=233)

#textfileds
t1 = Text(root, height=1, width=40,bg="orange",fg="black")
t1.place(x=150,y=323)

t2 = Text(root, height=1, width=40,bg="orange",fg="black")
t2.place(x=150,y=363)

t3 = Text(root, height=1, width=40,bg="orange",fg="black")
t3.place(x=150,y=403)
fl=Label(root,text='   FINAL PREDICTION   ',font=('times',10,'bold'),bg='darkcyan',fg='black')
fl.place(x=600,y=283)
t4=Text(root,width=18,height=40)
t4.place(x=600,y=303)


# Speech recognintion

def SpeechRecog():
    
    #voices 
    engine=pyttsx3.init('sapi5')
    voices=engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)

    #for speak
    def speak (audio):
        engine.say(audio)
        engine.runAndWait()

    #wishing

    def wishme():
        speak("hello, this is disease predictor")


    # it takes microphone input from user and return string output
    def takeCommand():
        r=sr.Recognizer()
        with sr.Microphone() as source:
            speak("please tell your name.")
            print('listening...')
            r.pause_threshold=1
            audio=r.listen(source)
        try:
            print('recogninzing...')
            query=r.recognize_google(audio,language='en-in')
            print(query)
            Name.set(query)
        except Exception as e:
            print('say that again please...')
            return takeCommand()
        
        nolist=['first','second','third','fourth','fifth']
        symoptions=list(set(OPTIONS))
             
        def symptomsrec():
            r=sr.Recognizer()
            with sr.Microphone() as source:
                for i in range(len(nolist)):
                    speak('your'+ nolist[i]+ 'symptom please')
                    print('listening..')
                    r.pause_threshold=1
                    audio=r.listen(source)
                    try:
                        print('recongnizing...')
                        query=r.recognize_google(audio,language='en-in')
                        print(query)
                        if query in symoptions:
                            if i==0:
                                Symptom1.set(query)
                            if i==1:
                                Symptom2.set(query)
                            if i==2:
                                Symptom3.set(query)
                            if i==3:
                                Symptom4.set(query)
                            if i==4:
                                Symptom5.set(query)        
                    except:
                        print('say that again please...')
                            
        speak('do you want to fill your symptoms by using me.')
        r=sr.Recognizer()
        with sr.Microphone() as source:
            print('listening..')
            r.pause_threshold=1
            audio=r.listen(source)
            print('recognizing..')
            
            query1=r.recognize_google(audio,language='en-in')
            
            mainquery=[]
            mainquery.append(query1)
            if 'yes' in mainquery:
                print(mainquery)
                symptomsrec()
            else:
                pass
                



    #main function
    if __name__=="__main__":
        wishme()
        takeCommand()
        DecisionTree()
        randomforest()
        NaiveBayes()

    




#mic
mic=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\mic.jpg'))
microphone=Button(master=root,width=13,height=13,image=mic,relief='flat',command=SpeechRecog)
microphone.place(x=300,y=74)
#logout
logout=ImageTk.PhotoImage(Image.open('C:\\Users\\Hackers world\\Desktop\\projects\\healthprediction\\images\\logoutbtn.jpg'))
log_out=Button(master=root,width=41,height=41,image=logout,relief='flat',command=logoutfun)
log_out.place(x=600,y=30)

btn=Button(master=root,width=9,height=2,bg='green',fg='white',relief='flat',text='LOGOUT',font=('times',11,'bold'),command=logoutfun)
btn.place(x=645,y=30)


def reload():
    root.destroy()
    call(['python','clean_code.py'])


repeatbtn=Button(root,text='PREDICT AGAIN',bg='red',fg='white',width=18,height=2,font=('times',11,'bold'),command=reload)
repeatbtn.place(x=400,y=30)

root.mainloop()
