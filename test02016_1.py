# Entry  = js(inputbox) , 기입창

import tkinter
from math import *
window = tkinter.Tk()
window.title("Entry 연습")
window.geometry("640x480")


plma = tkinter.Button(window,text="±",height=4,width=7)
per = tkinter.Button(window,text="%",height=4,width=7)
dot = tkinter.Button(window,text=".",height=4,width=7)

num_1 = tkinter.Button(window,text="1",height=4,width=7)
num_2 = tkinter.Button(window,text="2",height=4,width=7)
num_3 = tkinter.Button(window,text="3",height=4,width=7)

num_4 = tkinter.Button(window,text="4",height=4,width=7)
num_5 = tkinter.Button(window,text="5",height=4,width=7)
num_6 = tkinter.Button(window,text="6",height=4,width=7)

num_7 = tkinter.Button(window,text="7",height=4,width=7)
num_8 = tkinter.Button(window,text="8",height=4,width=7)
num_9 = tkinter.Button(window,text="9",height=4,width=7)
num_0 = tkinter.Button(window,text="0",height=4,width=7)

plus = tkinter.Button(window,text="＋",height=4,width=7)
minus = tkinter.Button(window,text="－",height=4,width=7)
mul= tkinter.Button(window,text="×",height=4,width=7)
dive = tkinter.Button(window,text="÷",height=4,width=7)
equl = tkinter.Button(window,text="=",height=4,width=16)
re = tkinter.Button(window,text="C",height=4,width=7)

re.grid(row=1, column=0)
plma.grid(row=1, column=1)
per.grid(row=1, column=2)
plus.grid(row=1, column=3)

num_7.grid(row=2, column=0)
num_8.grid(row=2, column=1)
num_9.grid(row=2, column=2)
minus.grid(row=2, column=3)

num_4.grid(row=3, column=0)
num_5.grid(row=3, column=1)
num_6.grid(row=3, column=2)
mul.grid(row=3, column=3)

num_1.grid(row=4, column=0)
num_2.grid(row=4, column=1)
num_3.grid(row=4, column=2)
dive.grid(row=4, column=3)

num_0.grid(row=5, column=0)
equl.grid(row=5, column=1,columnspan=2)
dot.grid(row=5, column=3)

def calc(event):
    label.config(text="결과 = "+str(eval(entry.get())))
   


entry = tkinter.Entry(window,width=20,insertwidth=5,insertbackground="red",selectbackground="yellow",selectforeground="green",insertontime=1000)
entry.bind("<Return>",calc)
entry.grid(row=0,column=0,columnspan=3)

label = tkinter.Label(window)
label.grid()


window.mainloop()