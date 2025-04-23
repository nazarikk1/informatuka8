from tkinter import*

def sel():
    selection = "Величина = " + str(var.get())
    label.config(text = selection)
    
window = Tk()
window.title("Горизонтальна шкала")
window.geometry("300x150")
window.configure(bg='lightblue')

var = DoubleVar()
scala = Scale(window , variable = var)
scala.pack()

button = Button(window, text="Отримати значення", command=sel)
button.pack()
button.configure(bg='lightblue')


label = Label(window)
label.pack()
label.configure(bg='lightblue')

window.mainloop()