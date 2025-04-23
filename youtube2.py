from tkinter import *

root = Tk()
root.title('YouTube')
root.geometry('900x700')
root['bg'] = '#f1f1f1'

header = Frame(root, bg='#ff0000', height=80, width=900)
header.place(x=0, y=0)

logo = Label(header, text="YouTube", font=("Arial", 30, "bold"), bg='#ff0000', fg='white')
logo.place(x=20, y=20)

search_bar = Entry(root, font=("Arial", 14), width=50)
search_bar.place(x=150, y=25)

search_button = Button(root, text="🔍", font=("Arial", 14), bg='lightgray', fg='black', width=3)
search_button.place(x=650, y=20)

video_list_frame = Frame(root, bg='#f1f1f1', width=900)
video_list_frame.place(x=0, y=100)

for i in range(6):
    video_frame = Frame(video_list_frame, bg='white', width=260, height=200, bd=1, relief=SOLID)
    video_frame.grid_propagate(False)
    video_frame.grid(row=i // 3, column=i % 3, padx=10, pady=10)

    video_thumbnail = Label(video_frame, text="Тех. Відео", font=("Arial", 12, "bold"), bg='gray', fg='white', width=26, height=10)
    video_thumbnail.pack()

    video_title = Label(video_frame, text=f"Відео {i + 1}", font=("Arial", 12), bg='white', fg='black', wraplength=250)
    video_title.pack()

    video_details = Label(video_frame, text="2 год 30 хв | 1M переглядів", font=("Arial", 10), bg='white', fg='gray')
    video_details.pack()

    comments_frame = Frame(video_frame, bg='white', width=250, height=40)
    comments_frame.pack(fill=X, padx=5, pady=5)

    comment_label = Label(comments_frame, text="Коментарі: 12", font=("Arial", 9), bg='white', fg='blue')
    comment_label.place(x=5, y=5)

sidebar = Frame(root, bg='#f1f1f1', width=250)
sidebar.place(x=0, y=100, height=600)

sidebar_header = Label(sidebar, text="Список категорій", font=("Arial", 14), bg='#f1f1f1', fg='black')
sidebar_header.place(x=10, y=10)

categories = ['Музика', 'Фільми', 'Спорт', 'Ігри', 'Новини', 'Технології']
for idx, category in enumerate(categories):
    category_button = Button(sidebar, text=category, font=("Arial", 12), bg='#ffffff', fg='black', width=20, anchor='w')
    category_button.place(x=10, y=50 + idx * 40)

root.mainloop()