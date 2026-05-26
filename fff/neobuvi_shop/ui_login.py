import tkinter as tk
from tkinter import messagebox
from app_config import FONT, FONT_BOLD, FONT_TITLE
from db import get_user

def clear_all(root):
    """Удаляет все виджеты с главного окна"""
    for widget in root.winfo_children():
        widget.destroy()

def setup_placeholder(entry, placeholder, font):
    """Настраивает текст-подсказку для поля ввода"""
    entry.insert(0, placeholder)
    entry.config(fg="grey")

    def on_focus_in(event):
        if entry.get() == placeholder:
            entry.delete(0, tk.END)
            entry.config(fg="black")

    def on_focus_out(event):
        if not entry.get():
            entry.insert(0, placeholder)
            entry.config(fg="grey")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)

def show_login(app):
    """Отображение окна авторизации"""
    clear_all(app["root"])

    root = app["root"]
    root.geometry("450x520")
    root.minsize(400, 500)
    root.configure(bg="#FFFFFF")
    root.title("Вход в систему")

    # Сброс состояния пользователя
    app["user"] = None

    # Шапка окна
    header_frame = tk.Frame(root, bg="#7FFF00", height=120)
    header_frame.pack(fill="x", side="top")
    header_frame.pack_propagate(False)

    tk.Label(header_frame, text="ООО «Обувь»", font=FONT_TITLE, bg="#7FFF00").pack(pady=35)

    # Метка для отображения имени пользователя после входа
    fio_label = tk.Label(header_frame, text="", font=FONT, bg="#7FFF00", fg="black")
    fio_label.place(relx=1.0, rely=0.5, anchor="e", x=-15)
    app["fio_label"] = fio_label

    # Форма ввода
    form_frame = tk.Frame(root, bg="#FFFFFF")
    form_frame.pack(expand=True, pady=(30, 0))

    login_entry = tk.Entry(form_frame, width=25, font=FONT, justify="center")
    password_entry = tk.Entry(form_frame, width=25, font=FONT, justify="center", show="*")

    setup_placeholder(login_entry, "Логин", FONT)
    setup_placeholder(password_entry, "Пароль", FONT)

    login_entry.pack(pady=12)
    password_entry.pack(pady=12)

    def do_login():
        login = login_entry.get().strip()
        password = password_entry.get().strip()

        if login == "Логин" or not login:
            messagebox.showwarning("Предупреждение", "Введите логин.")
            return
        if password == "Пароль" or not password:
            messagebox.showwarning("Предупреждение", "Введите пароль.")
            return

        # Проверка данных в БД
        user = get_user(app["cursor"], login, password)
        
        if user:
            app["user"] = user
            app["fio_label"].config(text=user["fio"])
            
            from ui_shop import show_shop
            show_shop(app, guest=False)
        else:
            messagebox.showerror("Ошибка", "Неверный логин или пароль.")

    # Кнопки управления
    btn_frame = tk.Frame(form_frame, bg="#FFFFFF")
    btn_frame.pack(pady=25)

    tk.Button(btn_frame, text="Войти", width=14, height=2, command=do_login,
              bg="#00FA9A", fg="black", font=FONT_BOLD).pack(side="left", padx=10)

    tk.Button(btn_frame, text="Гость", width=14, height=2, command=lambda: show_guest_mode(app),
              bg="#FFFFFF", fg="black", font=FONT).pack(side="left", padx=10)

    tk.Button(btn_frame, text="Выход", width=14, height=2, command=root.quit,
              bg="#FFFFFF", fg="black", font=FONT).pack(side="left", padx=10)

def show_guest_mode(app):
    """Вход в систему в роли гостя"""
    app["user"] = {"id": None, "fio": "Гость", "role": "Гость"}
    app["fio_label"].config(text="Гость")
    
    from ui_shop import show_shop
    show_shop(app, guest=True)