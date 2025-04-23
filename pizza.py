import tkinter
from tkinter import Checkbutton, BooleanVar, Button, Canvas, Label

window = tkinter.Tk()
window.title("Pizza Order / PizzaCity")
window.geometry("300x400")

def btcl():
    lab.config(text='Вартість: ' + str(var.get()) + 'грн.')

var = tkinter.IntVar()
var.set(120)

rbutton1 = tkinter.Radiobutton(window, text="Великий корж", variable=var, value=150)
rbutton1.pack()
rbutton2 = tkinter.Radiobutton(window, text="Середній корж", variable=var, value=120)
rbutton2.pack()
button = tkinter.Button(window, text="Замовити", command=btcl)
button.pack(pady=10)

cvar1 = BooleanVar()
cvar1.set(0)
cvar2 = BooleanVar()
cvar2.set(0)
cvar3 = BooleanVar()
cvar3.set(0)

chbut1 = Checkbutton(window, text="Цибуля", variable=cvar1, onvalue=1, offvalue=0, command=btcl)
chbut1.pack()
chbut2 = Checkbutton(window, text="Моцарела", variable=cvar2, onvalue=1, offvalue=0, command=btcl)
chbut2.pack()
chbut3 = Checkbutton(window, text="Бекон", variable=cvar3, onvalue=1, offvalue=0, command=btcl)
chbut3.pack()

buttton = Button(window, text="Order", command=btcl)
buttton.pack(pady=10)

lab = Label(window, text="Вартість: 0 грн.", font=("Arial", 12))
lab.pack(side="bottom", pady=10)

canvas = Canvas(window, width=300, height=100, bg="red")
canvas.pack(side="bottom")
canvas.create_oval(50, 30, 250, 130, fill="yellow", outline="black")
canvas.create_oval(90, 50, 110, 70, fill="red", outline="black")
canvas.create_oval(150, 50, 170, 70, fill="red", outline="black")  
canvas.create_oval(120, 80, 140, 100, fill="red", outline="black")  

window.mainloop()
