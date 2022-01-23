from math import *
from tkinter import *
root=Tk()
root.title('Calculator 2.0')
img = PhotoImage(file='icon.ico')
root.tk.call('wm', 'iconphoto', root._w, img)
e=Entry(root,text='Enter your name please!',bg='#050505',fg='#ffffff',width=14,font=("Bahnschrift",25),border=7)
e.grid(row=0,column=0,columnspan=4,pady=6)
def buttonclick(number):
    e.insert(END,number)
    return
def deleter():
    e.delete(len(e.get())-1,END)
    return
def clearfunc():
    e.delete(0,END)
    return
def equalfunc():
    a=eval(e.get())
    e.delete(0,END)
    e.insert(0,a)
def inverser():
    a=float(e.get())*-1
    e.delete(0,END)
    e.insert(0,a)
    return
button_0=Button(root,text='0',bg='#1316e8',fg='black',padx=16,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(0))
button_1=Button(root,text='1',bg='#1316e8',fg='black',padx=19,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(1))
button_2=Button(root,text='2',bg='#1316e8',fg='black',padx=17,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(2))
button_3=Button(root,text='3',bg='#1316e8',fg='black',padx=17,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(3))
button_4=Button(root,text='4',bg='#1316e8',fg='black',padx=15.5,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(4))
button_5=Button(root,text='5',bg='#1316e8',fg='black',padx=16,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(5))
button_6=Button(root,text='6',bg='#1316e8',fg='black',padx=16,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(6))
button_7=Button(root,text='7',bg='#1316e8',fg='black',padx=17,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(7))
button_8=Button(root,text='8',bg='#1316e8',fg='black',padx=16,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(8))
button_9=Button(root,text='9',bg='#1316e8',fg='black',padx=16,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(9))
button_10=Button(root,text='+',bg='#343e78',fg='black',padx=17,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick('+'))
button_11=Button(root,text='=',bg='#343e78',fg='black',padx=18,pady=5,font = ("Bahnschrift", 20),command=equalfunc)
button_12=Button(root,text='CLEAR',bg='#c41417',fg='black',padx=73,pady=15,font = ("Bahnschrift", 13),command=clearfunc)
button_14=Button(root,text='-',bg='#343e78',fg='black',padx=18,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick('-'))
button_15=Button(root,text='×',bg='#343e78',fg='black',padx=17,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick('*'))
button_16=Button(root,text='/',bg='#343e78',fg='black',padx=20,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick('/'))
button_17=Button(root,text='+/-',bg='#32a891',fg='black',padx=5,pady=5,font = ("Bahnschrift", 20),command=inverser)
button_18=Button(root,text='.',bg='#32a891',fg='black',padx=21,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick('.'))
button_19=Button(root,text='⌫',bg='#c41417',fg='black',padx=6,pady=5,font = ("Bahnschrift", 20),command=deleter)
button_20=Button(root,text=')',bg='#1316e8',fg='black',padx=5,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(')'))
button_21=Button(root,text='(',bg='#1316e8',fg='black',padx=5,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick('('))
button_22=Button(root,text='√',bg='#343e78',fg='black',padx=12,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick('sqrt('))
button_23=Button(root,text='(',bg='#1316e8',fg='black',padx=19,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick('('))
button_24=Button(root,text=R')',bg='#1316e8',fg='black',padx=19,pady=5,font = ("Bahnschrift", 20),command=lambda:buttonclick(R')'))


button_7.grid(row=1,column=0)
button_8.grid(row=1,column=1)
button_9.grid(row=1,column=2)
button_16.grid(row=1,column=3)
button_4.grid(row=2,column=0)
button_5.grid(row=2,column=1)
button_6.grid(row=2,column=2)
button_15.grid(row=2,column=3)
button_1.grid(row=3,column=0)
button_2.grid(row=3,column=1)
button_3.grid(row=3,column=2)
button_14.grid(row=3,column=3)
button_17.grid(row=5,column=0)
button_0.grid(row=4,column=1)
button_18.grid(row=5,column=1)
button_10.grid(row=4,column=3)
button_12.grid(row=6,column=0,columnspan=3)
button_19.grid(row=5,column=2)
button_11.grid(row=6,column=3)
button_22.grid(row=5,column=3)
# button_20.grid(row=5,column=3,padx=0)
# button_21.grid(row=5,column=4,padx=0)
button_23.grid(row=4,column=0,padx=0)
button_24.grid(row=4,column=2,padx=0)


root.mainloop()