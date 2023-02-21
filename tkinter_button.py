import tkinter as tk

'''
button 옵션
overrelief = 마우스 올렸을떄 테두리 모양
repeatdelay = 버튼 눌렀을때 부터 실행까지 대기시간
repeatinterval = 버튼 눌렀을때 부터 실행까지 반복시간


button 서식
state = 버튼 상태(normal,active,disabled(비활성화))
activebackground = active 상태일떄 배경색
activeforeground = active 상태일때 문자열 색
disabledbackground = active 상태일떄 배경색
disabledforground = active 상태일때 문자열 색
hightlightcolor = 버튼 선택시 색깔 / hightlightbackground = 버튼 선택되지 않았을떄 색
hightlightthickness = 버튼 선택시 두께

'''
button = tk.Tk()
button.title("button 연습")
button.geometry('600x500+600+200')
button.resizable(False,False)

label = tk.Label(button,text=1)
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

bt= tk.Button(button,width=15,text="숫자 증가",command=cntup,overrelief='solid',repeatdelay=2000,repeatinterval=100)
bt1= tk.Button(button,width=15,text="숫자 감소",command=cntdown)
bt2= tk.Button(button,width=15,text="숫자 초기화",command=cntreset,activebackground='skyblue')
bt3= tk.Button(button,width=15,text="숫자 초기화",command=label.config(background='red'))


bt.pack()
bt1.pack()
bt2.pack()
bt3.pack()











button.mainloop()