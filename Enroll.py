from tkinter import *
import tkinter.messagebox
from tkinter import filedialog
import random
from tkinter import ttk

studentNo = []
lname = []
fname = []
mname = []
maleFe = []
coursee = []
learnP = []
fullname = []

def call():
    res = tkinter.messagebox.askquestion('Exit', 'Do you really want to exit')
    if res == 'yes':
        windows.destroy()

def show(frame):
    frame.config(width=590, height=560)
    frame.tkraise()

def dilit():
    zx = data.focus()
    qw = data.index(zx)
    studentNo.pop(qw)
    fname.pop(qw)
    lname.pop(qw)
    mname.pop(qw)
    maleFe.pop(qw)
    coursee.pop(qw)
    learnP.pop(qw)
    fullname.pop(qw)
    data.delete(qw)

def update():
    for items in data.get_children():
        data.delete(items)
    for i in range(len(studentNo)):
        data.insert("",[i],iid=[i],values=(f"03-2223-03{studentNo[i]}", f"{lname [i]}", f"{fname [i]}", f"{mname [i]}", f"{maleFe [i]}",f"{coursee[i]}", f"{learnP[i]}\n"))

def validate():
    lastName= entry_1.get()
    firstName= entry_2.get()
    middleName = entry_5.get()
    courses= c.get()
    flexrad= var1.get()
    gender= var.get()
    pullname = (f"{lastName} {firstName} {middleName}")
    if firstName=="" or lastName=="" or courses== list1 or flexrad ==0 or gender == 0 or middleName == 0:
        tkinter.messagebox.showinfo('Alert',"Fields cannot be left empty!")
    elif pullname in fullname:
        tkinter.messagebox.showinfo('Info',"Student is already enrolled.")
    else:
        fullname.append(pullname)
        lname.append(lastName)
        fname.append(firstName)
        mname.append(middleName)
        coursee.append(courses)
        if gender==1:
            maleFe.append("MALE")
        else:
            maleFe.append("FEMALE")
        if flexrad==1:
            learnP.append("FLEX")
        else:
            learnP.append("RAD")
        x = random.randint(1000,9999)
        studentNo.append(x)
        print(firstName)
        print(fname)
        update()
        entry_2.delete(0, END)
        entry_1.delete(0,END)
        entry_5.delete(0,END)
        c.set("Select your course")
        var1.set(None)
        var.set(None)
        tkinter.messagebox.showinfo('Success',"Successfully registered!")

def clear():
   entry_2.delete(0, END)
   entry_1.delete(0,END)
   entry_5.delete(0,END)
   c.set("Select your course")
   var1.set(None)
   var.set(None)

def clearpild():
    haha.delete(0, END)
    haha1.delete(0,END)
    haha2.delete(0,END)
    haha3.set("Select your course")
    haha4.set(None)
    haha5.set(None)

def conpirm():
    var1 = random.randint(1000,9999)
    var2 = haha.get()
    var3 = haha1.get()
    var4 = haha2.get()
    var5 = haha3.get()
    var6 = haha4.get()
    var7 = haha5.get()
    if var5==1:
        var5 = "MALE"
    else:
        var5 = "FEMALE"
    if var7==1:
        var7 = "FLEX"
    else:
        var7 = "RAD"

    if var2 == "" or var3 == "" or var4 == "" or var5 ==0 or var6 == list1 or var7 == 0:
        tkinter.messagebox.showinfo('Alert',"Fields cannot be left empty!")
    else:
        zx = data.focus()
        qw = data.index(zx)
        studentNo[qw] = var1
        lname[qw] = var2
        fname[qw] = var3
        mname[qw] = var4
        maleFe[qw] = var5
        coursee[qw] = var6
        learnP[qw] = var7
        fullname[qw] = (f"{var2} {var3} {var4}")
        #for i in lb.curselection():
        #    studentNo[i] = var1
        #    lname[i] = var2
        #    fname[i] = var3
        #    mname[i] = var4
        #    maleFe[i] = var5
        #    coursee[i] = var6
        #    learnP[i] = var7
        #    fullname[i] = (f"{var2} {var3} {var4}")

        haha.delete(0, END)
        haha1.delete(0,END)
        haha2.delete(0,END)
        haha3.set("Select your course")
        haha4.set(None)
        haha5.set(None)
        for items in data.get_children():
            data.delete(items)
        for i in range(len(studentNo)):
            data.insert("",[i],iid=[i],values=(f"03-2223-03{studentNo[i]}", f"{lname [i]}", f"{fname [i]}", f"{mname [i]}", f"{maleFe [i]}",f"{coursee[i]}", f"{learnP[i]}\n"))
        tkinter.messagebox.showinfo("Sucess","Changes saved.")

def risit():
    asked = tkinter.messagebox.askquestion('Reset', 'Do you want to reset everything?')
    if asked == 'yes':
        studentNo.clear()
        fname.clear()
        lname.clear()
        mname.clear()
        maleFe.clear()
        coursee.clear()
        learnP.clear()
        fullname.clear()

        #lb.delete(0, END)

        entry_2.delete(0, END)
        entry_1.delete(0,END)
        entry_5.delete(0,END)
        c.set("Select your course")
        var1.set(None)
        var.set(None)

def save():
    #print(lname,fname,mname,maleFe,coursee,learnP)
    ask = tkinter.messagebox.askquestion('Save', 'Do you want to save and end the session?')
    if ask == 'yes':
        filez = filedialog.asksaveasfile(defaultextension=".txt")
        filez.writelines("Student ID               Last Name               Given Name                Middle Name    Gender           Course             Learning Modality\n")
        for i in range(len(studentNo)):
            filez.writelines(f"03-2223-03{studentNo[i] :<14} {lname [i]:<23} {fname [i]:<25} {mname [i]:<14} {maleFe [i]:<16} {coursee[i] :<18} {learnP[i] :<20}\n")
    else:
        pass

windows =Tk()
windows.title("Enrollment System for Freshmen")
windows.state("normal")

frame1 = Frame(windows)
frame2 = Frame(windows)
frame3 = Frame(windows)
frame4 = Frame(windows)

#FRAME 1================================================================================================================

bg = PhotoImage(file="newSize.png")
label2 = Label(frame1, image = bg)
label2.place(x=-2,y=-2)

logo1 = PhotoImage(file="display.png")
label1 = Label(frame1, image = logo1)
label1.place(x=130,y=50)

for frame in (frame1,frame2,frame3,frame4):
    frame.grid(row=1,column=1,sticky=NSEW)

button1 = PhotoImage(file="buttonE.png")
button2 = PhotoImage(file="about2.png")
button3 = PhotoImage(file="exit.png")

buttonE = Button(frame1,image=button1,command=lambda:show(frame2))
buttonE.place(x=106, y=235)
buttonR = Button(frame1,image=button2,command=lambda:show(frame3))
buttonR.place(x=106, y=285)
buttonM = Button(frame1,image=button3,command=lambda:call())
buttonM.place(x=106, y=335)

#FRAME 2===============================================================================================================

label_0 = Label(frame2, text="Registration Form",width=20,font=("bold", 20))
label_0.place(x=150,y=53)

label_1 = Label(frame2, text="Last Name:",width=20,font=("bold", 10))
label_1.place(x=130,y=130)

entry_1 = Entry(frame2)
entry_1.place(x=265,y=130)

label_2 = Label(frame2, text="Given Name:",width=20,font=("bold", 10))
label_2.place(x=130,y=180)

entry_2 = Entry(frame2)
entry_2.place(x=265,y=180)

label_5 = Label(frame2,text="Middle Name:",width=20,font=("bold",10))
label_5.place(x=130,y=230)

entry_5 = Entry(frame2)
entry_5.place(x=265,y=230)

label_3 = Label(frame2, text="Gender:",width=20,font=("bold", 10))
label_3.place(x=130,y=280)

var = IntVar()
Radiobutton(frame2, text="Male",padx = 5, variable=var, value=1).place(x=250,y=280)
Radiobutton(frame2, text="Female",padx = 20, variable=var, value=2).place(x=305,y=280)

label_4 = Label(frame2, text="Courses:",width=20,font=("bold", 10))
label_4.place(x=130,y=335)

list1 = ['BSIT','BSMLS','BSCE','BSTM','BSN','BSA']
c=StringVar()
droplist=OptionMenu(frame2,c, *list1)
droplist.config(width=15)
c.set('Select your course') 
droplist.place(x=265,y=330)

label_4 = Label(frame2, text="Learning Modality:",width=20,font=("bold", 10))
label_4.place(x=130,y=375)
var1 = IntVar()
Radiobutton(frame2, text="FLEX Learning", variable=var1,value=1).place(x=275,y=365)
Radiobutton(frame2, text="RAD Learning", variable=var1,value=2).place(x=275,y=385)

Button(frame2, text='Clear Field',width=10,bg='green',fg='white', command =lambda:clear()).place(x=189,y=430)
Button(frame2, text="Back",width=10,bg="green",fg="white",command=lambda:show(frame1)).place(x=20,y=10)
Button(frame2, text="Submit",width=10,bg = "green",fg="white",command=lambda:validate()).place(x=400,y=430)
Button(frame2, text="View Enrolled Students",width=17,bg = "green",fg="white",command=lambda:show(frame4)).place(x=270,y=430)
Button(frame2, text="Reset",width=10,bg="red",fg="white",command=lambda:risit()).place(x=108,y=430)

#FRAME 3===================================================================================================================================

img = PhotoImage(file="paynal.png")
label2 = Label(frame3, image = img)
label2.place(x=-2,y=-2)
Button(frame3,text = "Back",width=20,bg="green",fg="white",command=lambda:show(frame1)).place(x=210,y=500)

#FRAME 4===================================================================================================================================
#a = "Student No" ; b= "Last Name";d="First Name";e="Middle Name" ; f="Gender" ; g = "Course" ; h = "Learning Modality"
#texts = Label(frame4,text=f"          {a:<14} {b:<23} {d:<15} {e:<20} {f:<10} {g :<10} {h}\n").pack()
title = ("Student No.","Last Name","Given Name","Middle Name","Gender","Course","Learning Modality")
global data
data = ttk.Treeview(frame4,columns=title,show="headings",height=20)

data.column("#0",width=0,stretch=NO)
data.column("Student No.",anchor=CENTER,width=96)
data.column("Last Name",anchor=CENTER,width=100)
data.column("Given Name",anchor=CENTER,width=100)
data.column("Middle Name",anchor=CENTER,width=90)
data.column("Gender",anchor=CENTER,width=50)
data.column("Course",anchor=CENTER,width=50)
data.column("Learning Modality",anchor=CENTER,width=105)

data.heading("Student No.",text="Student No.")
data.heading("Last Name",text="Last Name")
data.heading("Given Name",text="Given Name")
data.heading("Middle Name",text="Middle Name")
data.heading("Gender",text="Gender")
data.heading("Course",text="Course")
data.heading("Learning Modality",text="Learning Modality")

data.pack()

#global listbox
#lb = Listbox(frame4,height=23, width = 97,bg="white")
#lb.pack()

Label(frame4,text="Last Name").place(x=0,y=430)
haha = Entry(frame4)
haha.place(x=100,y=430)

Label(frame4,text="Given Name").place(x=0,y=460)
haha1 = Entry(frame4)
haha1.place(x=100, y=460)

Label(frame4,text="Middle Name").place(x=0,y=490)
haha2 = Entry(frame4)
haha2.place(x=100,y=490)

Label(frame4,text="Gender").place(x=300,y=430)
haha3 = IntVar()
Radiobutton(frame4, text="Male", variable=haha3, value=1).place(x=400,y=430)
Radiobutton(frame4, text="Female", variable=haha3, value=2).place(x=450,y=430)

Label(frame4,text="Course").place(x=300,y=460)
list1 = ['BSIT','BSMLS','BSCE','BSTM','BSN','BSA']

haha4=StringVar()
droplist=OptionMenu(frame4,haha4, *list1)
droplist.config(width=15)
haha4.set('Select your course') 
droplist.place(x=400,y=458)

Label(frame4,text="Learning Modality").place(x=300,y=490)
haha5 = IntVar()
Radiobutton(frame4, text="FLEX", variable=haha5,value=1).place(x=400,y=490)
Radiobutton(frame4, text="RAD", variable=haha5,value=2).place(x=450,y=490)

Button(frame4,text = "Back",width=3,bg="green",fg="white",command=lambda:show(frame2)).place(x=0,y=533)
Button(frame4,text = "Save and End Session",width=17,bg="green",fg="white",command=lambda:save()).place(x=342,y=533)
Button(frame4,text = "Update Info",width=10,bg="green",fg="white",command=lambda:conpirm()).place(x=260,y=533)
Button(frame4,text = "Clear Field",width="10",bg="green",fg="white",command=lambda:clearpild()).place(x=178,y=533)
Button(frame4,text = "Remove",width=6,bg="red",fg="white",command=lambda:dilit()).place(x=125,y=533)

#===========================================================================================================================================
show(frame1)

windows.geometry("590x560")
windows.resizable(False,False)

icon = PhotoImage(file="iconn.png")
windows.iconphoto(True,icon)

windows.mainloop()