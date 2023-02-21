import tkinter
import math

ar = ""
bracket = False
buho = False
def ft(a):
    global ar
    global bracket
    global buho
    tx = str(text.cget("text"))
    if tx.rfind(" ") == -1:
        Bom = 0
    else:
        Bom = tx.rfind(" ")
        
    if a == "x!":
        text.config(text=tx+"! ")
        ar = ar[:ar.rfind(" ")+1] + str(math.factorial(int(tx[Bom:])))
    elif a == "C":
        text.config(text="0")
        ar = ""
        bracket = False
    elif a == "%":
        text.config(text=tx+"% ")
        ar = ar[:ar.rfind(" ")+1] + str(int(tx[Bom:])*0.01)
    elif a == "e" :
        text.config(text=tx+"e")
        ar = ar[:ar.rfind(" ")+1] + str(math.exp(int(tx[Bom:])))
    elif a == "ln":
        text.config(text=tx[:tx.rfind(" ")+1]+"ln("+tx[Bom:]+")")
        ar = ar[:ar.rfind(" ")+1] + str(math.log(int(tx[Bom:])))
    elif a == "sin":
        text.config(text=tx[:tx.rfind(" ")+1]+"sin("+tx[Bom:]+")")
        ar = ar[:ar.rfind(" ")+1] + str(math.sin(int(tx[Bom:])))
    elif a == "π":
        if tx == '0':
            text.config(text="")
            tx = ""
            text.config(text=tx+str(a))
            ar+="3.14"
        else:
            text.config(text=tx+"π")
            ar += "*3.14"
    elif a == "=":
        text.config(text=eval(str(ar)))
    elif a == "(":
        bracket = True
        text.config(text=tx+"(")
        ar += " ( "
    elif a == ")":
        if bracket:
            if buho == False:
                text.config(text=tx+")")
                ar += " ) "
                
def buho1(a):
    global ar
    tx = str(text.cget("text"))
    if tx.rfind(" ") == -1:
        Bom = 0
    else:
        Bom = tx.rfind(" ")
    text.config(text=tx[:tx.rfind(" ")+1]+tx[Bom:]+a)
    ar += " "+a+" "
    

def su(a):
    global ar
    tx = str(text.cget("text"))
    
    if tx == '0':
        text.config(text="")
        tx = ""
        ar = ""
    text.config(text=tx+str(a))
    ar += str(a)
    
def close():
    Calculator.quit()
    Calculator.destroy()

def new_win():    
    developer = tkinter.Toplevel()
    developer.title("Developer")
    developer.geometry("200x200")
    developer.resizable(False,False)
    text = tkinter.Label(developer,text="Develope\n코싸1 : 김영우\n코싸2 : 조정민\n코싸3 : 최윤석")
    text.pack(anchor="center")

Calculator = tkinter.Tk()
Calculator.title("계산기")
Calculator.geometry("446x300")
Calculator.resizable(False,False)


menu = tkinter.Menu(Calculator)
menu_1 = tkinter.Menu(menu,tearoff=False)
menu_1.add_command(label="Developer",command=new_win)
menu_1.add_separator()
menu_1.add_command(label="종료", command=close)
menu.add_cascade(label="도움말",menu=menu_1)

Calculator.config(menu=menu)

result = tkinter.Frame(Calculator,bg="#BBBBBB")
result.place(x=0, y=0,width=446, height=100)

text = tkinter.Label(result,text="0", relief="flat", bg="#BBBBBB",anchor="center",font=("굴림","15"))
text.pack(side="right")
button_setting = tkinter.Frame(Calculator)
button_setting.place(x=0,y=100,width=1000, height=200)
x = 89
y = 40
bg_ft = "skyblue"
bg_su = "#FAFABE"
bg_at = "#336699"
bg_at2 = "#003366"
tkinter.Button(button_setting,text="x!",command=lambda:ft("x!"),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*0,y=y*0)
tkinter.Button(button_setting,text="(",command=lambda:ft("("),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*1,y=y*0)
tkinter.Button(button_setting,text=")",command=lambda:ft(")"),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*2,y=y*0)
tkinter.Button(button_setting,text="%",command=lambda:ft("%"),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*3,y=y*0)
tkinter.Button(button_setting,text="C",command=lambda:ft("C"),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*4,y=y*0)

tkinter.Button(button_setting,text="ln",command=lambda:ft("ln"),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*0,y=y*1) 
tkinter.Button(button_setting,text="7",command=lambda:su(7),width=10, height=2, font=("굴림",11), bg=bg_su, activebackground=bg_at).place(x=x*1,y=y*1)
tkinter.Button(button_setting,text="8",command=lambda:su(8),width=10, height=2, font=("굴림",11), bg=bg_su, activebackground=bg_at).place(x=x*2,y=y*1)
tkinter.Button(button_setting,text="9",command=lambda:su(9),width=10, height=2, font=("굴림",11), bg=bg_su, activebackground=bg_at).place(x=x*3,y=y*1)
tkinter.Button(button_setting,text="/",command=lambda:buho1("/"),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*4,y=y*1)

tkinter.Button(button_setting,text="π",command=lambda:ft("π"),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*0,y=y*2)
tkinter.Button(button_setting,text="4",command=lambda:su(4),width=10, height=2, font=("굴림",11), bg=bg_su, activebackground=bg_at).place(x=x*1,y=y*2)
tkinter.Button(button_setting,text="5",command=lambda:su(5),width=10, height=2, font=("굴림",11), bg=bg_su, activebackground=bg_at).place(x=x*2,y=y*2)
tkinter.Button(button_setting,text="6",command=lambda:su(6),width=10, height=2, font=("굴림",11), bg=bg_su, activebackground=bg_at).place(x=x*3,y=y*2)
tkinter.Button(button_setting,text="×",command=lambda:buho1("*"),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*4,y=y*2)

tkinter.Button(button_setting,text="sin",command=lambda:ft("sin"),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*0,y=y*3)
tkinter.Button(button_setting,text="1",command=lambda:su(1),width=10, height=2, font=("굴림",11), bg=bg_su, activebackground=bg_at).place(x=x*1,y=y*3)
tkinter.Button(button_setting,text="2",command=lambda:su(2),width=10, height=2, font=("굴림",11), bg=bg_su, activebackground=bg_at).place(x=x*2,y=y*3)
tkinter.Button(button_setting,text="3",command=lambda:su(3),width=10, height=2, font=("굴림",11), bg=bg_su, activebackground=bg_at).place(x=x*3,y=y*3)
tkinter.Button(button_setting,text="-",command=lambda:buho1("-"),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*4,y=y*3)

tkinter.Button(button_setting,text=".",command=lambda:su("."),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*0,y=y*4)
tkinter.Button(button_setting,text="0",command=lambda:su(0),width=21, height=2, font=("굴림",11), bg=bg_su, activebackground=bg_at).place(x=x*1,y=y*4)
tkinter.Button(button_setting,text="=",command=lambda:ft("="),width=10, height=2, font=("굴림",11), bg=bg_su, activebackground=bg_at).place(x=x*3,y=y*4)
tkinter.Button(button_setting,text="+",command=lambda:buho1("+"),width=10, height=2, font=("굴림",11), bg=bg_ft, activebackground=bg_at2).place(x=x*4,y=y*4)

Calculator.mainloop()