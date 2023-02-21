import tkinter

window=tkinter.Tk()
window.title("CheckButton 연습")
window.geometry("400x280")
window.resizable(False,False)
""" 
RadioButton 옵션
select() - 선택 / deselect() - 선택 해제 
invoke() - 체크버튼실행 / flash() - 깜빡
value = 값(주소,그룹) / variable = 값을 지정할 변수
"""
def check():
    label.config(text = "Radio_Var_1 = " + str(Radio_Var_1.get()) + "\n" + 
                        "Radio_Var_2 = " + str(Radio_Var_2.get()) + "\n\n" + 
                        "Total = "       + str(Radio_Var_1.get() + Radio_Var_2.get()))

Radio_Var_1 = tkinter.IntVar()
Radio_Var_2 = tkinter.IntVar()
radio1 = tkinter.Radiobutton(window, text="1번", value=3, variable=Radio_Var_1, command=check)
radio1.pack()
radio2 = tkinter.Radiobutton(window, text="2번(1번)", value=3, variable=Radio_Var_1, command=check)
radio2.pack()
radio3 = tkinter.Radiobutton(window, text="3번", value=9, variable=Radio_Var_1, command=check)
radio3.pack()
label =tkinter.Label(window, text="None", height=5)
label.pack()
radio4 = tkinter.Radiobutton(window, text="4번", value=10, variable=Radio_Var_2, command=check)
radio4.pack()
radio5 = tkinter.Radiobutton(window, text="5번", value=12, variable=Radio_Var_2, command=check)
radio5.pack()
window.mainloop()