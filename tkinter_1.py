import tkinter

window = tkinter.Tk()
window.title("tkinter 연습 ")
window.geometry("500x500+700+300") # 너비 x 높이 + x좌표 + y좌표
window.resizable(False,False)

lb = tkinter.Label(window,  text="안녕하세요.\n 오늘 시험이에요.",width=20,height=2,fg='red',relief='solid',bg="green")
lb.pack()
label= tkinter.Label(window,text="hello python",font=('궁서체',30),fg='blue',highlightthickness=5,highlightbackground='pink')
label.pack()


'''
Label 옵션
text = 내용 / textvariable = 문자열 가져올 변수
anchor = (문자,이미지)내용의 위치  /  justify = 정렬 / font = 글꼴
bitmap = 기본 이미지 / image = 임의 이미지 / compound = 문자열 + 이미지 겹치기

Label,button 서식
relief = 테두리 모양(flat,solid,sunken,raised) / bd(borderwidth) = 테두리 두께
bg(background) = 배경색 / fg(foreground) = 문자열 색 /padx = 내용 가로 여백 / pady = 내용 세로 여백
highlightthickness = 테두리 두께 / hightlightbackground = 테두리 색상

'''


btn =tkinter.Button(lb,text="ok",width=20)


window.mainloop()