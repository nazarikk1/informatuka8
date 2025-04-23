import tkinter as tk
import tkinter.messagebox

def button_click():
    try:
        s = 1
        i = 1
        st = str_var.get()
        k = int(st)  
        
        while i <= 10:
            s += (i - 1) * i
            i += 2  
        
        if k <= s:
            tkinter.messagebox.showinfo("Результат", f"Встигне отримати {s}")
        else:
            tkinter.messagebox.showinfo("Результат", "Не встигне отримати!")
    except ValueError:
        tkinter.messagebox.showerror("Помилка", "Будь ласка, введіть число!")

window = tk.Tk()
window.title("Обчислення")
window.geometry("300x200")
window.configure(bg="black")

str_var = tk.StringVar()

label = tk.Label(window, text="Введіть число:", font=("Arial", 12), fg="white", bg="black")
label.pack(pady=10)

edit = tk.Entry(window, textvariable=str_var, font=("Arial", 12))
edit.pack()

button = tk.Button(window, text="Визначити", font=("Arial", 12), command=button_click, bg="gray", fg="white")
button.pack(pady=10)


window.mainloop()