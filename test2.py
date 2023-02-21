import tkinter as tk

button = tk.Tk()
button.title("button 연습")
button.geometry('600x500+600+200')
button.resizable(False,False)

label = tk.Label(button,text=0)
label.pack()

count = 0
def cntup():
    global count
    count +=1
    label.config(text=count)
def cntdown():
    global count
    if count !=0:
        count-=1
    label.config(text=count)
def cntreset():
    global count
    count =0
    label.config(text=count)    

bt= tk.Button(button,width=15,text="숫자 증가",command=cntup,)
bt1= tk.Button(button,width=15,text="숫자 감소",command=cntdown)
bt2= tk.Button(button,width=15,text="숫자 초기화",command=cntreset)
bt3= tk.Button(button,width=15,text="숫자 초기화")


bt.pack()
bt1.pack()
bt2.pack()
bt3.pack()


button.mainloop()