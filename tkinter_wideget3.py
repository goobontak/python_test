import tkinter

window =  tkinter.Tk()
w = 400
h = 200
p_x = 700
p_y = 100
window.geometry("{}x{}+{}+{}".format(w,h,p_x,p_y))
window.resizable(False,False)
window.title("Widget 연습_2")
a=1
for col in range(4):
    frame=tkinter.Frame(window)
    frame.pack(side="top")
    for x in range(7):
        if(a%2==0):     
            bt=tkinter.Label(frame,text=str(x+1),width=5,height=2)
            bt.pack(side="left",padx=5,pady=5)
            a=3
        else:
            bt1=tkinter.Button(frame,text=str(x+1),width=5,height=2)
            bt1.pack(side="left",padx=5,pady=5)
            a=2
window.mainloop()