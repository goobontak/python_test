from tkinter import *
from tkinter import ttk
 
def button_pressed(value):
    number_entry.insert("end",value)  #텍스트 창으로 숫자 전송.'end'는 오른쪽끝에 추가하라는 의미.
    print(value,"pressed")
     
root = Tk()
root.title("Calculator")
root.geometry("100x100")
 
#텍스트창의 값 저장할 변수.
entry_value = StringVar(root, value='')
 
#textvariable 속성으로 변수 설정.
number_entry = ttk.Entry(root, textvariable = entry_value, width=10)
number_entry.grid(row=0, columnspan=1)
 
button1 = ttk.Button(root, text="1", command = lambda:button_pressed('1'))
button1.grid(row=1, column=0)
 
root.mainloop()