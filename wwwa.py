# Завдання 1
# from tkinter import *
# 
# def sel():
#     sum_num=0
#     for i in range(1, int(var.get())+1):
#         sum_num += i
#     selection = "Відповідь = " + str(sum_num)
#     label.config(text = selection)
# 
# window = Tk()
# var = DoubleVar()
# scale = Scale(window, variable = var )
# scale.pack()
# 
# button = Button(window, text = 'Отримати суму чисел',command=sel)
# button.pack()
# 
# label = Label(window)
# label.pack()
# window.mainloop()

# Завдання 2
# from tkinter import *
# 
# def sel():
#     d=1
#     for i in range(2, int(var.get())+1,2):
#         d=d*i
#     selection = "Відповідь = " + str(d)
#     label.config(text = selection)
# 
# window = Tk()
# var = DoubleVar()
# scale = Scale( window, from_=0, to=10, variable = var )
# scale.pack()
# 
# button = Button(window, text = 'Отримати добуток парених чисел', command=sel)
# button.pack()
# 
# label = Label(window)
# label.pack()
# window.mainloop()

# Завдання 3
# from tkinter import *
# 
# def sel():
#     sum_num=0
#     for i in range(0, int(var.get())+1,5):
#         sum_num += i
#     selection = "Відповідь = " + str(sum_num)
#     label.config(text = selection)
# 
# window = Tk()
# var = DoubleVar()
# scale = Scale( window, variable = var )
# scale.pack()
# 
# button = Button(window, text = 'Отримати суму чисел, які кратні 5', command=sel)
# button.pack()
# 
# label = Label(window)
# label.pack()
# window.mainloop()

# Завдання 4
from tkinter import *

def sel():
    k = 0
    max_num = int(var.get())
    for i in range(0, max_num + 1):
        if i % 3 == 0:
            k += 1
    selection = f"Відповідь = {k}"
    label.config(text=selection)

window = Tk()

var = IntVar()
scale = Scale(window, variable=var, from_=0, to=100, orient=VERTICAL)
scale.pack(side=TOP, anchor="w", padx=10, pady=10)

button = Button(window, text='Отримати кількість чисел, які діляться на 3', command=sel, bg='lightblue', font=("Arial", 16))
button.pack(side=TOP, pady=50)

label = Label(window, text="Результат з'явиться тут", font=("Arial", 14))
label.pack()

window.mainloop()
