import tkinter as tk
import time

# tkinter 윈도우 생성
window = tk.Tk()

# 라벨 생성
label = tk.Label(window, font=("Arial", 30))

# 라벨 배치
label.pack()

# 현재 시간을 표시하는 함수
def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.configure(text=current_time+60)
    
    
 

# 시간 업데이트 시작
update_time()


search_button = tk.Button(window, text="검색", command=update_time, width=5, height=2)
search_button.place(x=540, y=120)

# tkinter 이벤트 루프 실행
window.mainloop()