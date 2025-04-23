from tkinter import *

def size(val):
    label.config(font=("Arial", int(val)))

window = Tk()
window.title("Горизонтальна шкала")
window.geometry("300x150")
window.configure(bg='lightblue')

var = IntVar()
scale = Scale(window, from_=10, to=40, orient=VERTICAL, length=200, tickinterval=10,  variable=var, command=size)
scale.pack(side=LEFT)

label = Label(window, text="Tkinter", font=("Arial", 10), bg='lightblue')
label.pack()

window.mainloop()
