import tkinter as tk

root = tk.Tk()

bg_image = tk.PhotoImage(file="tj.png")

canvas = tk.Canvas(root, width=bg_image.width(), height=bg_image.height())
canvas.create_image(1, 0, image=bg_image, anchor=tk.NW)
canvas.pack()

root.mainloop()