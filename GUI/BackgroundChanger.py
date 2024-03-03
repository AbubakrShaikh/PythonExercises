from tkinter import *

def red_change():
    window.configure(bg='red')

def blue_change():
    window.configure(bg='blue')


window = Tk()

red_btn = Button(window, text="Change to Red", command=red_change)
btn.pack()

blue_btn = Button(window, text="Change to Red", command=blue_change)
btn.pack()

window. mainloop()
