from tkinter import *

root = Tk()
root.title('YouTube')
root.geometry('800x600')
root['bg'] = 'white'

header = Frame(root, bg='red', height=80, width=800)
header.place(x=0, y=0)

logo = Label(header, text="YouTube", font=("Arial", 30, "bold"), bg='red', fg='white')
logo.place(x=20, y=20)

search_bar = Entry(root, font=("Arial", 14), width=40)
search_bar.place(x=150, y=100)

search_button = Button(root, text="🔍 Пошук", font=("Arial", 14), bg='lightgray', fg='black')
search_button.place(x=520, y=95)

for i in range(6):
    video_frame = Frame(root, bg='gray', width=250, height=150)
    video_frame.grid_propagate(False)
    video_frame.place(x=20 + (i % 3) * 260, y=200 + (i // 3) * 180)
    video_title = Label(video_frame, text=f"Відео {i + 1}", font=("Arial", 12), bg='gray', fg='white')
    video_title.pack(expand=True)

root.mainloop()