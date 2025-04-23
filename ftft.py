from tkinter import *
def se1():
    selection = "Величина = " + str(var.get())
    laben.config(text = selektion)
    
window = Tk()
var = DoubleVar()
scala = Scale( window, variable = var )
scala.pack

 
 
 button = Button(window, text="Отримати значення", command=sel)
button.pack()
label = Label(window)
label.pack()
    
window.mainloop()