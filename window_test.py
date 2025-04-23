# import tkinter
# window = tkinter.Tk ()
# var1 = tkinter.IntVar ()
# var2 = tkinter.IntVar ()
# check1 = tkinter.Checkbutton(window,
#                             text = "1 пункт",
#                             variable = var1,
#                             onvalue = 1, offvalue = 0)
# check2 = tkinter.Checkbutton(window,
#                             text = "2 пункт",
#                             variable = var2,
#                             onvalue = 1, offvalue = 0)
# check1.pack()
# check2.pack()
# window.mainloop()

# import tkinter
# window = tkinter.Tk ()
# window.geometry('300x100')
# window.title("Ви хочете додому?")
# v = tkinter.IntVar () 
# rbutton1 = tkinter.Radiobutton(window, text="Так",
#                         variable=v, value=1)
# rbutton2 = tkinter.Radiobutton(window, text="Звісно",
#                         variable=v, value=2)
# rbutton3 = tkinter.Radiobutton(window, text="Звичайно",
#                         variable=v, value=3)
# rbutton1.pack()
# rbutton2.pack()
# rbutton3.pack()
# window.mainloop()

from tkinter import *

def change():
    if var.get() == 0:
        label['bg'] = 'lightyellow'
    elif var.get() == 1:
        label['bg'] = 'lightblue'
    elif var.get() == 2:
        label['bg'] = 'lightpink'

window = Tk()
var = IntVar()
var.set(0)

red = Radiobutton(text="Пастельно-Жовтий", variable=var, value=0)
green = Radiobutton(text="Пастельно-Голубий", variable=var, value=1)
yellow = Radiobutton(text="Пастельно-Рожевий", variable=var, value=2)

button = Button(text="Змінити", command=change)
label = Label(width=20, height=10)

red.pack()
green.pack()
yellow.pack()
button.pack()
label.pack()

window.mainloop()