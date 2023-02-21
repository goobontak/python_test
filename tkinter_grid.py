import tkinter

window=tkinter.Tk()
window.title("Grid 연습")
window.geometry("650x400")
""" 
row = 행위치(가로) / column = 열위치(세로)
rowspan = 행위치조정 /  columnspan = 열위치조정
sticky = 할당된 공간 내에서 위치 조정(정렬? - w,n,e,s,nw,ne,sw,se)
"""
a1 = tkinter.Button(window,text="(0, 0)")
a2 = tkinter.Button(window,text="(0, 1)")
a3 = tkinter.Button(window,text="(0, 2)")

a4 = tkinter.Button(window,text="(1, 0)")
a5 = tkinter.Button(window,text="(1, 1)")
a6 = tkinter.Button(window,text="(1, 4)")

a7 = tkinter.Button(window,text="(2, 1)")
a8 = tkinter.Button(window,text="(2, 2)")
a9 = tkinter.Button(window,text="(3, 3)")

a1.grid(row=0, column=0)
a2.grid(row=0, column=1)
a3.grid(row=0, column=2)
a4.grid(row=1, column=0)
a5.grid(row=1, column=1)
a6.grid(row=1, column=4)
a7.grid(row=2, column=1,sticky="w")
a8.grid(row=2, column=2)
a9.grid(row=3, column=3)

window.mainloop()