import tkinter

window=tkinter.Tk()
window.title("CheckButton 연습")
img = tkinter.PhotoImage(file="tj.PNG")
a5 = tkinter.PhotoImage(image=img)
window.geometry("700x480",image=img)

""" 
side = 바깥쪽(top, bottom, left, right)
anchor = (center,n,e,s,w,ne,nw,se,sw)
fill = 맞춤(none,x,y,both)
expand = 사용하지 않은 부분 확보
"""
a = tkinter.Button(window,text="top")
a_1 = tkinter.Button(window,text="top-1")

a2 = tkinter.Button(window,text="bottom")
a2_1 = tkinter.Button(window,text="bottom-1")

a3 = tkinter.Button(window,text="left")
a3_1 = tkinter.Button(window,text="left-1")

a4 = tkinter.Button(window,text="right")
a4_1 = tkinter.Button(window,text="right-1")



a.pack(side="top")
a_1.pack(side="top",fill="x")
a2.pack(side="bottom")
a2_1.pack(side="bottom",anchor="e")
a3.pack(side="left")
a3_1.pack(side="left",fill="y")
a4.pack(side="right")
a4_1.pack(side="right",anchor="s")
a5.pack(expand=True,fill="both")

window.mainloop()