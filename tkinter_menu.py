import tkinter

window=tkinter.Tk()
window.title("CheckButton 연습")
window.geometry("400x280")
window.resizable(False,False)

def close():
    window.quit()
    window.destroy()
    
Menubar = tkinter.Menu(window)

menu_1 = tkinter.Menu(Menubar,tearoff=0)
menu_1.add_command(label="하위 메뉴 1-1")
menu_1.add_separator()
menu_1.add_separator()
menu_1.add_command(label="하위 메뉴 1-2")
menu_1.add_separator()
menu_1.add_command(label="종 료",command=close)
Menubar.add_cascade(label="상위 메뉴 1",menu=menu_1)

menu_2 = tkinter.Menu(Menubar,tearoff=0,selectcolor='red')
menu_2.add_radiobutton(label="하위 메뉴 2-1",state='disable')
menu_2.add_radiobutton(label="하위 메뉴 2-2")
menu_2.add_radiobutton(label="하위 메뉴 2-3")
Menubar.add_cascade(label='상위 메뉴 2',menu=menu_2)

menu_3 = tkinter.Menu(Menubar,tearoff=0)
menu_3.add_checkbutton(label="하위 메뉴 3-1")
menu_3.add_checkbutton(label="하위 메뉴 3-2")
Menubar.add_cascade(label="상위 메뉴 3",menu=menu_3)
window.config(menu=Menubar)

window.mainloop()