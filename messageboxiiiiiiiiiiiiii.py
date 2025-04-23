import tkinter
import tkinter.messagebox

window = tkinter.Tk()
str_var = tkinter.StringVar()

def button_click():
    s = str_var.get()
    slova = s.split()
    count = len(slova)
    if count == 1:
        tkinter.messagebox.showinfo("Результат", "Це одне слово")
    else:
         tkinter.messagebox.showinfo("Результат", f"Текст складається з {count} слів")

label = tkinter.Label(window, text="Введіть текст")
label.pack()

edit = tkinter.Entry(window, textvariable=str_var)
edit.pack()

button = tkinter.Button(window, text="Перевірити", command=button_click)
button.pack()

window.mainloop()