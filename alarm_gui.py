import winsound,time
from tkinter import *

root=Tk()

root.geometry('270x300')

def sound():
    for i in range(5):
        winsound.MessageBeep()
        time.sleep(2)

def insert_hours():
    alert=Label(text="After how many hours?")
    alert.grid(row=5,column=0)
    global choice
    choice=Entry(root,bd=5)
    choice.grid(row=7,column=0)
    b4=Button(root,text="SUBMIT",command=submit_hours)
    b4.grid(row=10,column=0)

def insert_minutes():
    alert=Label(text="After how many minutes?")
    alert.grid(row=5,column=0)
    global choice
    choice=Entry(root,bd=5)
    choice.grid(row=7,column=0)
    b4=Button(root,text="SUBMIT",command=submit_minutes)
    b4.grid(row=10,column=0)

def submit_seconds():
    alert=Label(root,text="Submitting your choice...").grid(row=13,column=0)

def insert_seconds():
    alert=Label(text="After how many seconds?")
    alert.grid(row=5,column=0)
    global choice
    choice=Entry(root,bd=5)
    choice.grid(row=7,column=0)
    b4=Button(root,text="SUBMIT",command=submit_seconds)
    b4.grid(row=10,column=0)

def submit_seconds():
    global var
    var=int(choice.get())
    var1=var
    time.sleep(var1)
    sound()


def submit_minutes():
    global var
    var=int(choice.get())
    var1=var*60
    time.sleep(var1)
    sound()

def submit_hours():
    global var
    var=int(choice.get())
    var1=(var*60)*60
    global beeps
    time.sleep(var1)
    sound()
    
b1=Button(root,text="Do you want to set alarm after some hours?",command=insert_hours)
b1.grid(row=0,column=0)

b2=Button(root,text="Do you want to set alarm after some minutes?",command=insert_minutes)
b2.grid(row=1,column=0)

b3=Button(root,text="Do you want to set alarm after some seconds?",command=insert_seconds)
b3.grid(row=2,column=0)



root.mainloop()
