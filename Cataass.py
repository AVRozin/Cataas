from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_img(url):
    try:
        resp = requests.get(url)
        image_data = BytesIO(resp.content)
        img = Image.open(image_data)

        img.thumbnail((600, 480), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f'Ошибка при загрузке файла {e}')


def set_img():
    img = load_img(url)
    if img:
        label.config(image=img)
        label.image = img


def exit():
    w.destroy()


w = Tk()
w.title = ('Коты')
w.geometry('700x500')

label = Label()
label.pack()

menu_bar = Menu(w)
w.config(menu = menu_bar)
file_menu = Menu(menu_bar, tearoff 0)
menu_bar.add_cascade(label = 'Файл', menu = file_menu)
file_menu.add_command(label = 'Загрузить фото', command = set_img)
file_menu.add_separator()
file_menu.add_command(label = 'Выход', command = exit)

# update_button = Button(text = 'Новый кот', command = set_img)
# update_button.pack()

Button(text = 'Закрыть', command = w.destroy).pack()


url = 'https://cataas.com/cat'
img = load_img(url)

set_img()

w.mainloop()
