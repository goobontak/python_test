# entry = js(intputbox)
import tkinter
from math import *
'''
Entry 옵션
insert(index,"문자열") - index 위치에 문자열 추가 / delete(start_index,end_index) - start ~ end 문자열 삭제
get() - Entry 문자열 가져오기 / index(index) - index 위치 번호 / icursor(index) - index 앞에 커서 위치
select_adjust(index) - index위치까지 블럭 / select_range(start,end) - start ~ end 까지 블록 처리
select_cleart() - 블록처리 해제

Entry 서식
show - entry 표시되는 문자 수 /textbariable = 문자열 가져올 변수 / justify = 정렬
inserwidth - entry 키보드 커서 너비 / insertborderwidth = entry 키보드 커서 테두리 두께
insertbackground = 키보드 색상
selectbackground = 블록 배경 색상 / selectforeground = 블록
insertontime = 깜박임 보이는 시간 / insertofftime = 깜박임이 보이지 않는시간
takefocus = tab 으로 이동 허용 여부 [Ture,False]\
    
'''

window = tkinter.Tk()
window.title("entry 연습")
window.geometry("640x600")

def calc(event):
    label.config(text='결과'+str(eval(entry.get())))
entry = tkinter.Entry(window,insertwidth=14,insertbackground='red',selectbackground='yellow',selectforeground='blue')
entry.bind("<Return>",calc)
entry.pack()

label = tkinter.Label(window)
label.pack()
window.mainloop()
