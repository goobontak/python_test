import tkinter

window=tkinter.Tk()
window.title("Canvas 연습") 
window.geometry("1000x800+10+10")

canvas=tkinter.Canvas(window,relief="solid",bd=2,width=900,height=900)


face1 = canvas.create_oval(300,50,600,350,fill="deepskyblue",width=3)
face2=canvas.create_oval(320,140,580,340,fill="white",width=2)
eye1 = canvas.create_oval(390,90,450,175,fill="white",width=2)
eye1_1=canvas.create_oval(430,130,440,150,fill="white",width=3)
eye2 = canvas.create_oval(450,90,510,175,fill="white",width=2)
eye1_1=canvas.create_oval(460,130,470,150,fill="white",width=3)
nose_line=canvas.create_line(450,180,450,280,width=3)
nose = canvas.create_oval(430,170,470,200,fill="red",width=2)
mouse = canvas.create_arc(350,180,550,280,style="arc",start=227,width=3)
sp1 = canvas.create_line(340,190,415,200,width=3)
sp1_1 = canvas.create_line(485,200,560,190,width=3)
sp2 = canvas.create_line(335,215,415,210,width=3)
sp2_1 = canvas.create_line(485,210,565,215,width=3)
sp3 = canvas.create_line(340,235,415,220,width=3)
sp3_3 = canvas.create_line(485,220,560,235,width=3)


canvas.pack()

window.mainloop()