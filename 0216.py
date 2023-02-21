import tkinter
from math import *

window = tkinter.Tk()
window.title("entry 연습")
window.geometry("640x600")

text =tkinter.Entry(window)
text.grid(row=2,column=2,padx=5,pady=10)

count=0
def btn_click(number):
    current=text.get()
    text.delete(0,tkinter.END)
    text.insert(0,str(text) +str(number))
    
 
    return
  
bt=tkinter.Button(text="7",command=lambda:btn_click(1))
bt.place(x=200,y=200)


    
window.mainloop()
