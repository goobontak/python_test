import tkinter
from math import *
import tkinter as tk

def button_pressed(value):
    fr1.insert("end",value)  #텍스트 창으로 숫자 전송.'end'는 오른쪽끝에 추가하라는 의미.
    print(value,"pressed")

window=tkinter.Tk()
window.title("Frame 연습") 
window.geometry("500x500")
img = tkinter.PhotoImage(file="ru1.png")
bg_img = tkinter.Label(image=img)
bg_img.pack(expand="True",fill="both")

img0 = tkinter.PhotoImage(file="0.png")
bg_img0 = tkinter.Label(image=img0)

img1 = tkinter.PhotoImage(file="1.png")
bg_img1 = tkinter.Label(image=img1)

img2 = tkinter.PhotoImage(file="2.png")
bg_img2 = tkinter.Label(image=img2)

img3 = tkinter.PhotoImage(file="3.png")
bg_img3 = tkinter.Label(image=img3)

img4 = tkinter.PhotoImage(file="4.png")
bg_img4 = tkinter.Label(image=img4)

img5 = tkinter.PhotoImage(file="5.png")
bg_img5 = tkinter.Label(image=img5)
img6 = tkinter.PhotoImage(file="6.png")
bg_img6 = tkinter.Label(image=img6)
img7 = tkinter.PhotoImage(file="7.png")
bg_img7 = tkinter.Label(image=img7)
img8 = tkinter.PhotoImage(file="8.png")
bg_img8 = tkinter.Label(image=img8)
img9 = tkinter.PhotoImage(file="9.png")
bg_img9 = tkinter.Label(image=img9)

imgmul = tkinter.PhotoImage(file="mul.png")
bg_imgmul = tkinter.Label(image=imgmul)
imgdiv = tkinter.PhotoImage(file="div.png")
bg_imgdiv = tkinter.Label(image=imgdiv)
imgplus = tkinter.PhotoImage(file="plus.png")
bg_imgplus = tkinter.Label(image=imgplus)
imgminus = tkinter.PhotoImage(file="minus.png")
bg_imgminus = tkinter.Label(image=imgminus)

imgset = tkinter.PhotoImage(file="set.png")
bg_imgset = tkinter.Label(image=imgset)
imgequal = tkinter.PhotoImage(file="equal.png")
bg_imgequal = tkinter.Label(image=imgequal)


bt = tkinter.Button(width=40,height=35,image=imgmul,command= lambda:button_pressed('*'))
bt.place(x=200,y=250)
bt = tkinter.Button(width=40,height=35,image=imgdiv,command= lambda:button_pressed('/'))
bt.place(x=250,y=250)



bt = tkinter.Button(width=40,height=35,image=img7,command= lambda:button_pressed('7'))
bt.place(x=150,y=300)
bt = tkinter.Button(width=40,height=35,image=img8,command= lambda:button_pressed('8'))
bt.place(x=200,y=300)
bt = tkinter.Button(width=40,height=35,image=img9,command= lambda:button_pressed('9'))
bt.place(x=250,y=300)
bt = tkinter.Button(width=40,height=35,image=imgminus,command= lambda:button_pressed('-'))
bt.place(x=300,y=300)

bt = tkinter.Button(width=40,height=35,image=img4,command= lambda:button_pressed('4'))
bt.place(x=150,y=350)
bt = tkinter.Button(width=40,height=35,image=img5,command= lambda:button_pressed('5'))
bt.place(x=200,y=350)
bt = tkinter.Button(width=40,height=35,image=img6,command= lambda:button_pressed('6'))
bt.place(x=250,y=350)
bt = tkinter.Button(width=40,height=35,image=imgplus,command= lambda:button_pressed('+'))
bt.place(x=300,y=350)

bt = tkinter.Button(width=40,height=35,image=img1,command= lambda:button_pressed('1'))
bt.place(x=150,y=400)
bt = tkinter.Button(width=40,height=35,image=img2,command= lambda:button_pressed('2'))
bt.place(x=200,y=400)
bt = tkinter.Button(width=40,height=35,image=img3,command= lambda:button_pressed('3'))
bt.place(x=250,y=400)
bt0 = tkinter.Button(width=40,height=35,image=img0,command= lambda:button_pressed('0'))
bt0.place(x=300,y=400)


def calc(event):   # func함수이름을 calculate로 바꿔줬습니다. 호출하는 부분도 같이 바꿔주세요.
    value = tk.Entry.get(fr1)
    if value != '':
        result = eval(value)
        print(result)
        fr1.delete(0,tk.END)
        fr1.insert(0,result)
       
 
def clear(event):            # C 버튼과 Esc 키를 위한 함수 입니다.
    fr1.delete(0,tk.END)  # 내용 삭제
     
fr1 = tk.Entry(window, width=20)
fr1.place(x=200,y=20)
 
bt = tk.Button(window, width=40,height=35,image=imgequal)  # = 버튼 추가
bt.bind('<Button-1>',calc)          # 버튼에 클릭 이벤트 추가
bt.place(x=300,y=250) 

 
bt = tk.Button(window,width=40,height=35,image=imgset)  # C버튼추가. text속성은 버튼에 표시할 문자입니다.
bt.bind('<Button-1>',clear)           # <Button-1> 이벤트는 마우스 왼쪽클릭 이벤트입니다.
bt.place(x=150,y=250)


window.bind('<Return>', calc)
window.bind('<Escape>', clear) 

    
window.mainloop()