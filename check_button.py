import tkinter
window=tkinter.Tk()
window.title("CheckButton 연습")
window.geometry("400x180")
window.resizable(False,False)

def flash():
    Chk_bt_1.flash()
"""
Checkbutton 옵션
select() - 선택 / deselect() - 선택 해제 / toggle() - 토글(스위치)
invoke() - 체크버튼실행 / flash() - 깜빡
selectcolor - 체크버튼 배경색
onvalue - 체크버튼선택시(True)
offvalue - 체크버튼비선택시(True)
"""    

Check_var_1 = tkinter.IntVar()
Check_var_2 = tkinter.IntVar()

Chk_bt_1 = tkinter.Checkbutton(window, text="O", variable=Check_var_1, activebackground="blue")
Chk_bt_2 = tkinter.Checkbutton(window, text="△", variable=Check_var_2, selectcolor="red")
Chk_bt_3 = tkinter.Checkbutton(window, text="X", variable=Check_var_2, command=flash,bg="yellow")

Chk_bt_1.pack()
Chk_bt_2.pack()
Chk_bt_3.pack()

window.mainloop()
