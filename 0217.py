import tkinter as tk

#윈도우 생성
root=tk.Tk()

#전체 이름
root.title('코로나 진단키트 에측도 진단 프로그램')

#창 크기 +붙은 부분은 좌상단 떨어진 위치
root.geometry("600x500+100+100")

#함수들

def make_lab14() :
    lab14.configure(text=ent12.get())

#1행 라벨 추가
lab11=tk.Label(root,
    text="민감도",
    width=8,
    height=1,
    font=('맑은 고딕',16,'bold'),
    bg='#2F5597',
    fg='white')
lab11.grid(row=0,column=0,padx=5,pady=10)

ent12=tk.Entry(font=('맑은 고딕',16,'bold'),bg='white',width=8)
ent12.grid(row=0,column=1,padx=5,pady=10)

button13 = tk.Button(root,text='\u2192',font=('맑은 고딕',11,'bold'),bg="red",fg='white',width=4,command=make_lab14)
button13.grid(row=0,column=2,padx=5,pady=10)

lab14=tk.Label(root,width=8,height=1,font=('맑은 고딕',16,'bold'),bg='#2F5597',fg='white')
lab14.grid(row=0,column=3,padx=5,pady=10)

root.mainloop()