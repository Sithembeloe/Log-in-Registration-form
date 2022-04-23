
import bcrypt
from sqlite3 import connect
import tkinter
from tkinter import *
from tkinter import messagebox
import pyttsx3
import ast
from pymongo import MongoClient

from dotenv import load_dotenv
import os
load_dotenv('.env') 

client = MongoClient()



mongoURL = os.environ.get("DR_Url")

connection = MongoClient(mongoURL)

db = connection.TKDB

collection = {
	"users": db.users
	}

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg="#fff")
root.resizable(False,False)

def Signin():
    mainUser = None
    Name = user.get()
    Password = code.get()

    User = collection["users"].find({"Name": Name})

    for i in User:
        mainUser = i

    print(mainUser["Name"])

    password = mainUser["Password"].encode('utf-8')

    # print(r.keys())
    # print(r.values())
    name = mainUser["Name"]
    passwordCorrect = bcrypt.checkpw(Password.encode(), password)

    if(name and passwordCorrect):
        speak('Welcome back! {}'.format(name))
        root.destroy()
    #     # import Main1

    else:
        speak('Invalid Name or Password!')
        messagebox.showerror('Invalid', 'Invalid Name or Password')
        speak('if you are a new user, please click signup button below...or try again!')

#########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def signup_command():
    window = Toplevel(root)

    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)


    def speak(audio):
        engine.say(audio)
        engine.runAndWait()

    # window = Tk()
    window.title("Registration Form")
    window.geometry('925x1000+300+200')
    window.configure(bg='#fff')
    window.resizable(False,False)


    def signup():
       
        Name=user.get()
        Gender=Gender1.get()
        Email=Email1.get()
        Password=code.get()
        confirm_password=confirm_code.get()
        

        if Password==confirm_password:
            try:
                #Encode your password and hash it:
                Password = Password.encode('utf-8')
                Password = bcrypt.hashpw(Password, bcrypt.gensalt())
                Password = Password.decode('utf-8')

                print(Password)

                #Create a user array for that goes into MongoDB:
                User = {"Name":Name, "Gender": Gender, "Email": Email, "Password": Password}
                collection["users"].insert_one(User)
                messagebox.showinfo('Signup','Successfully signed up')
                window.destroy()

            except:
                messagebox.showinfo('Something went wrong')
                

        # else:
        #     messagebox.showerror('Invalid','both entered Password do not match!')

    def sign():
        window.destroy()





    img = PhotoImage(file='mark.png')
    Label(window,image=img, border=0,bg='white').place(x=70,y=110)

    frame=Frame(window,width=350,height=590,bg='#fff')
    frame.place(x=480,y=10)

    heading=Label(frame,text='Sign up',fg="#540000",bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
    heading.place(x=100,y=5)

    ######-----------------------------------------------------------------
    def on_enter(e):
        user.delete(0,'end')
    def on_leave(e):
        if user.get()=='':
            user.insert(0,'Name')

    user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    user.place(x=30,y=80)
    user.insert(0, 'Name')
    user.bind("<FocusIn>",on_enter)
    user.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)


    ######-----------------------------------------------------------------

    def on_enter(e):
        signup()
        Name = user.get()
        if Name == 'Name':
            speak("Please enter a Valid name")

        else:
            speak(f"welcome {Name}")
        Gender1.delete(0,'end')
        signup()
        Gender = Gender1.get()
        speak('...')
        speak('Under Gender, Please choose between male or female')
    def on_leave(e):
        if Gender1.get()=='':
            Gender1.insert(0,'Gender e.g(Male or Female)')

    Gender1 = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    Gender1.place(x=30,y=150)
    Gender1.insert(0, 'Gender e.g(Male or Female)')
    Gender1.bind("<FocusIn>",on_enter)
    Gender1.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

    ######-------------------------------------------------------------------

    def on_enter(e):
        signup()
        Email = Email1.get()
        speak("before you enter an email address, please make sure to you enter a correct email address")
        Email1.delete(0,'end')
    def on_leave(e):
        if Email1.get()=='':
            Email1.insert(0,'Email')

    Email1 = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    Email1.place(x=30,y=220)
    Email1.insert(0, 'Email')
    Email1.bind("<FocusIn>",on_enter)
    Email1.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=247)

    ######-----------------------------------------------------------------

    def on_enter(e):
        signup()
        Email = Email1.get()
        if Email == 'Email':
            speak("Please!, enter the valid email address")

        code.delete(0,'end')
    def on_leave(e):
        signup()
        Password = code.get()
        if Password == 'Password':
            speak("sorry, I can't take password as your password, please choose a different password")

        else:
            speak('before you type in confirmation password, make sure to duble check your password if they match')
            speak("if they don't, this registration window will not close until you have matched your password!")
        if code.get()=='':
            code.insert(0,'Password')

    code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    code.place(x=30,y=290)
    code.insert(0, 'Password')
    code.bind("<FocusIn>",on_enter)
    code.bind("<FocusOut>", on_leave)


    Frame(frame,width=295,height=2,bg='black').place(x=25,y=317)

    ######-----------------------------------------------------------------

    def on_enter(e):
        confirm_code.delete(0, 'end')
    def on_leave(e):
        if confirm_code.get()=='':
            confirm_code.insert(0,'Confirm Password')

    confirm_code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
    confirm_code.place(x=30,y=360)
    confirm_code.insert(0, 'Confirm Password')
    confirm_code.bind("<FocusIn>",on_enter)
    confirm_code.bind("<FocusOut>", on_leave)

    Frame(frame,width=295,height=2,bg='black').place(x=25,y=387)

    ####------------------------------------------------------------

    Button(frame,width=39,pady=8,text='Sign up',bg='#540000',fg='white',border=0,command=signup).place(x=40,y=420)
    label=Label(frame,text='I have an account', fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
    label.place(x=90,y=480)

    singin=Button(frame,width=7,text='Sign in',border=0,bg='white',cursor='hand2',fg='#540000',command=sign)
    singin.place(x=200,y=480)



    window.mainloop()


#########@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@



img = PhotoImage(file='mark.png')
Label(root,image=img,bg='white').place(x=50,y=50)

frame = Frame(root,width=350,height=350,bg='white')
frame.place(x=480,y=70)

heading = Label(frame,text='Sign in',fg='#540000',bg='white',font=('Microsoft Yahei UI Light',23,'bold'))
heading.place(x=100,y=5)

#############_______________________________________________________________

def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Name')
user = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Name')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

#######__________________________________________________________________

def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name = code.get()
    if name == '':
        code.insert(0, 'Password')

code = Entry(frame,width=25,fg='black',border=0,bg='white',font=('Microsoft Yahei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

############_______________________________________________________________________

Button(frame,width=39,pady=7,text='Sign in',bg='#540000',fg='white',border=0,command=Signin).place(x=35,y=204)
label = Label(frame,text="Don't have an acoount?",fg='black',bg='white',font=('Microsoft Yahei UI Light',9))
label.place(x=75,y=270)

Button(frame,width=6,text='Sign up',border=0,bg='white',cursor='hand2',fg='#540000', command=signup_command).place(x=215,y=270)

root.mainloop()