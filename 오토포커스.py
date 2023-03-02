import tkinter as tk

def set_focus(widget):
    widget.focus_set()

root = tk.Tk()

entry = tk.Entry(root)
entry.pack()

root.after(0, set_focus, entry)

root.mainloop()