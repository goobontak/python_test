import tkinter
from math import *

window=tkinter.Tk()
window.title("car")
window.geometry("650x400")
""" 
row = 행위치(가로) / column = 열위치(세로)
rowspan = 행위치조정 /  columnspan = 열위치조정
sticky = 할당된 공간 내에서 위치 조정(정렬? - w,n,e,s,nw,ne,sw,se)
"""
dis = tkinter.Entry(window, justify='right', bg = 'white',fg='red')
dis.grid(column=0, row=5, ipadx=80, ipady=30)
plma = tkinter.Button(window,text="±",height=2,width=3)
per = tkinter.Button(window,text="%",height=2,width=3)
dot = tkinter.Button(window,text=".",height=2,width=3)

num_1 = tkinter.Button(window,text="1",height=2,width=3)
num_2 = tkinter.Button(window,text="2",height=2,width=3)
num_3 = tkinter.Button(window,text="3",height=2,width=3)

num_4 = tkinter.Button(window,text="4",height=2,width=3)
num_5 = tkinter.Button(window,text="5",height=2,width=3)
num_6 = tkinter.Button(window,text="6",height=2,width=3)

num_7 = tkinter.Button(window,text="7",height=2,width=3)
num_8 = tkinter.Button(window,text="8",height=2,width=3)
num_9 = tkinter.Button(window,text="9",height=2,width=3)
num_0 = tkinter.Button(window,text="0",height=2,width=3)

plus = tkinter.Button(window,text="＋",height=2,width=3)
minus = tkinter.Button(window,text="－",height=2,width=3)
mul= tkinter.Button(window,text="×",height=2,width=3)
dive = tkinter.Button(window,text="÷",height=2,width=3)
equl = tkinter.Button(window,text="=",height=2,width=7)
re = tkinter.Button(window,text="C",height=2,width=3)

re.grid(row=0, column=0)
plma.grid(row=0, column=1)
per.grid(row=0, column=2)
dot.grid(row=4, column=3)

num_1.grid(row=3, column=0)
num_2.grid(row=3, column=1)
num_3.grid(row=3, column=2)
num_4.grid(row=2, column=0)
num_5.grid(row=2, column=1)
num_6.grid(row=2, column=2)
num_7.grid(row=1, column=0)
num_8.grid(row=1, column=1)
num_9.grid(row=1, column=2)
num_0.grid(row=4, column=0)

plus.grid(row=0, column=3)
minus.grid(row=1, column=3)
mul.grid(row=2, column=3)
dive.grid(row=3, column=3)
equl.grid(row=4, column=1,columnspan=2)
def calc(event):
    label.config(text="결과 = "+str(eval(entry.get())))
    
entry = tkinter.Entry(window,insertwidth=5,insertbackground="red",selectbackground="yellow",selectforeground="green",insertontime=1000)
entry.bind("<Return>",calc)
entry.grid()

label = tkinter.Label(window)
label.grid()





window.mainloop()