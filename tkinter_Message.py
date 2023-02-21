import tkinter

window=tkinter.Tk()
window.title("canvas 연습")
window.geometry("600x400")

canvas=tkinter.Canvas(window,relief="solid",bd=2)

line = canvas.create_line(10,10,20,20,150,30,fill='red')

canvas.pack()

window.mainloop()