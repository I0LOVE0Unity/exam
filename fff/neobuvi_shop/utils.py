import tkinter as tk
from PIL import Image, ImageTk
import os

def clear_all(root):
    """Удаляет все виджеты из контейнера"""
    for widget in root.winfo_children():
        widget.destroy()

def calc_price(price, discount):
    """Возвращает цену со скидкой, округлённую до сотых"""
    if discount > 0:
        return round(price * (1 - discount / 100), 2)
    return round(price, 2)

def setup_placeholder(entry, placeholder, font):
    """Добавляет текст-подсказку в поле ввода"""
    entry.insert(0, placeholder)
    entry.config(fg="gray")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg="gray")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def load_image(label, image_path, max_size=(300, 200)):
    """Загружает и масштабирует изображение для метки"""
    if image_path and os.path.exists(image_path):
        try:
            image = Image.open(image_path)
            image.thumbnail(max_size, Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(image)
            label.config(image=photo, text="")
            label.image = photo
            return True
        except Exception as error:
            print(f"Ошибка загрузки изображения {image_path}: {error}")
            label.config(text="Ошибка загрузки", fg="red")
            return False
    label.config(text="Нет изображения", fg="gray")
    return False