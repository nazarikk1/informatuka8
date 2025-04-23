import tkinter
window = tkinter.Tk ()
var1 = tkinter.IntVar ()
var2 = tkinter.IntVar ()
check1 = tkinter.Checkbutton(window,
                             text = '1 пункт ',
                             variable = var1 ,
                             onvalue = 1, offvalue = 0)
check2 = tkinter.Checkbutton (window,
                              text = '2 пункт ',
                              variable = var2,
                              onvalue = 1, offvalue = 0)
check1.pack ()
check2.pack ()
window.mainloop ()