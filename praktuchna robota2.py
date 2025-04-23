from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("пандемія")

def calculate():
    x = int(en1.get())
    y = float(en2.get()) / 100
    n = int(en3.get())

    for i in range(n):
        x += x * y

    messagebox.showinfo("результат", f"кількість інфікованих через {n} днів: {int(x)}")

Label(window, text="інфіковано людей: ").grid(row=0, column=0)
en1 = Entry(window)
en1.grid(row=0, column=1)

Label(window, text="швидкість поширення вірусу (%)").grid(row=1, column=0)
en2 = Entry(window)
en2.grid(row=1, column=1)

Label(window, text="час поширення вірусу (днів)").grid(row=2, column=0)
en3 = Entry(window)
en3.grid(row=2, column=1)

btn = Button(window, text="результат", command=calculate)
btn.grid(row=3, column=0, columnspan=2)

window.mainloop()