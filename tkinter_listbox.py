import tkinter as inter
from tkinter import ttk
'''
insert(index,"내용") = 추가 / delete(start,end) = start ~ end 까지 삭제
size() = 항목 개수 반환 / acivate(index) = index 위치 항목을 선택
curselection() = 선택된 항목을 튜플로 반환 / get(start,end) = start ~ end 까지 튜플로 반환
xview() 가로 스크롤 연결 / yview() = 세로 스크롤 변경
xview_scroll(숫자,문자) = 스크롤 속성 설정
listvariable = 리스트박스에 표시할 문자열 변수
xscrollcommand = 가로스크롤 위젯 적용
yscrollcommand = 세로스크롤 위젯 적용
cursor = 마우스 커서 모양 (arrow,circle,clock,crosshair 등등등)



'''
new = inter.Tk()
new.title("Listbox 연습")
new.geometry('700x400')

listbox=inter.Listbox(new,selectmode ='extended',height=0,cursor="crosshair")
listbox.insert(0,'1번')
listbox.insert(1,'2번')
listbox.insert(2,'4번')
listbox.insert(3,'5번')
listbox.insert(4,'그만해')
listbox.insert(5,'3번')
listbox.yview_scroll(5,"units")
listbox.pack()

number_entry = ttk.Entry(new, width=20)
number_entry.grid(row=0, columnspan=1)
button1 = ttk.Button(new, text="1", command=lambda:print("button 1"))
button1.grid(row=1, column=0)

number_entry.pack()
button1.pack()

new.mainloop()