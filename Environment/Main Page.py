#Main file for Creating Window
import tkinter as tk
from tkinter import ttk

# Create Instance
win = tk.Tk()
w = 600
h = 50
ws = win.winfo_screenwidth()
hs = win.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
win.geometry('%dx%d+%d+%d' % (w, h, x, y))
win.title("Project Schedule")



# Start GUI
win.mainloop()