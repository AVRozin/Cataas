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
        return None


def open_new_window():
    tag = tag_entry.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_img(url_tag)
    if img:
        new_window = Toplevel()
        new_window.title('Картинка с котом')
        new_window.geometry('600x480')
        label = Label(new_window, image = img)
        label.image = img
        label.pack()


def exit():
    w.destroy()


w = Tk()
w.title = ('Коты')
w.geometry('700x500')

tag_entry = Entry()
tag_entry.pack()

load_button = Button(text = 'Загрузить по тегу', command = open_new_window)
load_button.pack()

menu_bar = Menu(w)
w.config(menu = menu_bar)
file_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = 'Файл', menu = file_menu)
file_menu.add_command(label = 'Загрузить фото', command = open_new_window)
file_menu.add_separator()
file_menu.add_command(label = 'Выход', command = exit)

url = 'https://cataas.com/cat'

w.mainloop()
