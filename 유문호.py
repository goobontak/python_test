import tkinter

window=tkinter.Tk()
window.title("노선도")
window.geometry("1200x800")
window.resizable(False,False)

station=["암사","천호","강동구청","몽촌토성","잠실","석촌","송파","가락시장","문정","장지","복정","산성","남한산성입구","단대오거리","신흥","수진"]

sw=0
a=0
b=0
def sumbutton(value):
    global sw
    global a
    global b
    if sw==0:
        a = value
        sw=1
        labelsum.config(text="소요 시간 : 0 분")
        labelstart.config(text="시작역: "+station[value-1])
                
    else:
        b = value
        sw=0
        labelsum.config(text="소요 시간 : "+str(abs(b-a)*4)+" 분")
        labelend.config(text="도착역: "+station[value-1])
    
        
        
def reset():
    global sw, a, b
    sw = 0
    a = 0
    b = 0
    labelsum.config(text="소요 시간")
    labelstart.config(text=" ")
    labelend.config(text=" ")
    radio1.deselect()
    radio2.deselect()
    radio3.deselect()
    radio4.deselect()
    radio5.deselect()
    radio6.deselect()
    radio7.deselect()
    radio8.deselect()
    radio9.deselect()
    radio10.deselect()
    radio11.deselect()
    radio12.deselect()
    radio13.deselect()
    radio14.deselect()
    radio15.deselect()
    radio16.deselect()  

labelsum=tkinter.Label(window,text="소요 시간")
labelsum.place(x=575,y=430)
labelstart=tkinter.Label(window,text=" ")
labelstart.place(x=580,y=390)
labelend=tkinter.Label(window,text=" ")
labelend.place(x=580,y=410)

label1 = tkinter.Label(window,text="암사")
label1.place(x=70,y=30)
label2 = tkinter.Label(window,text="천호")
label2.place(x=140,y=30)
label3 = tkinter.Label(window,text="강동구청")
label3.place(x=190,y=30)
label4 = tkinter.Label(window,text="몽촌토성")
label4.place(x=260,y=30)
label5 = tkinter.Label(window,text="잠실")
label5.place(x=350,y=30)
label6 = tkinter.Label(window,text="석촌")
label6.place(x=420,y=30)
label7 = tkinter.Label(window,text="송파")
label7.place(x=490,y=30)
label8 = tkinter.Label(window,text="가락시장")
label8.place(x=540,y=30)
label9 = tkinter.Label(window,text="문정")
label9.place(x=630,y=30)
label10 = tkinter.Label(window,text="장지")
label10.place(x=700,y=30)
label11 = tkinter.Label(window,text="복정")
label11.place(x=770,y=30)
label12 = tkinter.Label(window,text="산성")
label12.place(x=840,y=30)
label13 = tkinter.Label(window,text="남한산성입구")
label13.place(x=880,y=30)
label14 = tkinter.Label(window,text="단대오거리")
label14.place(x=960,y=30)
label15 = tkinter.Label(window,text="신흥")
label15.place(x=1050,y=30)
label16 = tkinter.Label(window,text="수진")
label16.place(x=1120,y=30)

ra1 = tkinter.IntVar()
ra2 = tkinter.IntVar()
ra3 = tkinter.IntVar()
ra4 = tkinter.IntVar()
ra5 = tkinter.IntVar()
ra6 = tkinter.IntVar()
ra7 = tkinter.IntVar()
ra8 = tkinter.IntVar()
ra9 = tkinter.IntVar()
ra10 = tkinter.IntVar()
ra11 = tkinter.IntVar()
ra12 = tkinter.IntVar()
ra13 = tkinter.IntVar()
ra14 = tkinter.IntVar()
ra15 = tkinter.IntVar()
ra16 = tkinter.IntVar()
ra17 = tkinter.IntVar()

radio1 = tkinter.Checkbutton(window,variable=ra1,command=lambda:sumbutton(1))
radio1.place(x=70,y=50)
radio2 = tkinter.Checkbutton(window,variable=ra2,command=lambda:sumbutton(2))
radio2.place(x=140,y=50)
radio3 = tkinter.Checkbutton(window,variable=ra3,command=lambda:sumbutton(3))
radio3.place(x=210,y=50)
radio4 =tkinter.Checkbutton(window,variable=ra4,command=lambda:sumbutton(4))
radio4.place(x=280,y=50)
radio5 = tkinter.Checkbutton(window,variable=ra5,command=lambda:sumbutton(5))
radio5.place(x=350,y=50)
radio6 = tkinter.Checkbutton(window,variable=ra6,command=lambda:sumbutton(6))
radio6.place(x=420,y=50)
radio7 = tkinter.Checkbutton(window,variable=ra7,command=lambda:sumbutton(7))
radio7.place(x=490,y=50)
radio8 = tkinter.Checkbutton(window,variable=ra8,command=lambda:sumbutton(8))
radio8.place(x=560,y=50)
radio9 = tkinter.Checkbutton(window,variable=ra9,command=lambda:sumbutton(9))
radio9.place(x=630,y=50)
radio10 = tkinter.Checkbutton(window,variable=ra10,command=lambda:sumbutton(10))
radio10.place(x=700,y=50)
radio11 = tkinter.Checkbutton(window,variable=ra11,command=lambda:sumbutton(11))
radio11.place(x=770,y=50)
radio12 = tkinter.Checkbutton(window,variable=ra12,command=lambda:sumbutton(12))
radio12.place(x=840,y=50)
radio13 = tkinter.Checkbutton(window,variable=ra13,command=lambda:sumbutton(13))
radio13.place(x=910,y=50)
radio14 = tkinter.Checkbutton(window,variable=ra14,command=lambda:sumbutton(14))
radio14.place(x=980,y=50)
radio15 = tkinter.Checkbutton(window,variable=ra15,command=lambda:sumbutton(15))
radio15.place(x=1050,y=50)
radio16 = tkinter.Checkbutton(window,variable=ra16,command=lambda:sumbutton(16))
radio16.place(x=1120,y=50)

resetbutton = tkinter.Button(window, text="초기화", command=reset)
resetbutton.place(x=580,y=460)

window.mainloop()