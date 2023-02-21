import tkinter as tk
 
window = tk.Tk()
window.title("계산기")
window.geometry("1500x1500")
img = tk.PhotoImage(file="C:\python\전철 노선도.png")
bg_img = tk.Label(image=img)
bg_img.pack(expand="True",fill="both")

num_ac = tk.Radiobutton(width=1,height=1,text="hi")
num_ac.place(x=100,y=100)
window.mainloop()