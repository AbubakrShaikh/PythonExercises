from tkinter import *

def btn_click():
	print("Button clicked")

window = Tk()
btn = Button(window, text="Click this button!", command=btn_click)
btn.pack()

window.mainloop()
