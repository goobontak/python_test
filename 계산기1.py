import tkinter as tk
 
window = tk.Tk()
window.title("계산기")
window.geometry("500x500")
img = tk.PhotoImage(file="ru1.png")
bg_img = tk.Label(image=img)
bg_img.pack(expand="True",fill="both")
window.resizable(False,False)
def button_pressed(value):
    fr1.insert("end",value)  #텍스트 창으로 숫자 전송.'end'는 오른쪽끝에 추가하라는 의미.
    print(value,"pressed")


bt = tk.Button(window,width=5,height=2,text="*",command= lambda:button_pressed('*'))
bt.place(x=200,y=250)
bt = tk.Button(window,width=5,height=2,text="/",command= lambda:button_pressed('/'))
bt.place(x=250,y=250)


bt = tk.Button(window,width=5,height=2,text="7",command= lambda:button_pressed('7'))
bt.place(x=150,y=300)
bt = tk.Button(window,width=5,height=2,text="8",command= lambda:button_pressed('8'))
bt.place(x=200,y=300)
bt = tk.Button(window,width=5,height=2,text="9",command= lambda:button_pressed('9'))
bt.place(x=250,y=300)
bt = tk.Button(window,width=5,height=2,text="-",command= lambda:button_pressed('-'))
bt.place(x=300,y=300)

bt = tk.Button(window,width=5,height=2,text="4",command= lambda:button_pressed('4'))
bt.place(x=150,y=350)
bt = tk.Button(window,width=5,height=2,text="5",command= lambda:button_pressed('5'))
bt.place(x=200,y=350)
bt = tk.Button(window,width=5,height=2,text="6",command= lambda:button_pressed('6'))
bt.place(x=250,y=350)
bt = tk.Button(window,width=5,height=2,text="+",command= lambda:button_pressed('+'))
bt.place(x=300,y=350)


bt = tk.Button(window,width=5,height=2,text="1",command= lambda:button_pressed('1'))
bt.place(x=150,y=400)
bt = tk.Button(window,width=5,height=2,text="2",command= lambda:button_pressed('2'))
bt.place(x=200,y=400)
bt = tk.Button(window,width=5,height=2,text="3",command= lambda:button_pressed('3'))
bt.place(x=250,y=400)


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
 
bt = tk.Button(window, text='=', width=5,height=2)  # = 버튼 추가
bt.bind('<Button-1>',calc)          # 버튼에 클릭 이벤트 추가
bt.place(x=300,y=400) 
 
bt = tk.Button(window, text='A/C', width=5,height=2)  # C버튼추가. text속성은 버튼에 표시할 문자입니다.
bt.bind('<Button-1>',clear)
window.bind('<Escape>', clear)# <Button-1> 이벤트는 마우스 왼쪽클릭 이벤트입니다.
bt.place(x=150,y=250)



window.mainloop()