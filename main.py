import time
from tkinter import *

with open("vocabularies.dat") as words:
    content = words.read()

mywin = Tk()
left = (mywin.winfo_screenwidth()//2)
top = (mywin.winfo_screenheight()//2)
WINDOWS_WIDTH = 650
WINDOWS_HEIGHT = 600

mywin.geometry(f"{WINDOWS_WIDTH}x{WINDOWS_HEIGHT}+{left - (WINDOWS_WIDTH // 2)}+{top - (WINDOWS_HEIGHT// 2)}")
mywin.title("English Review")
mywin.config(background = "#333333")
mywin.mainloop()