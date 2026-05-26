import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import os
from app_config import FONT, FONT_BOLD, FONT_TITLE
from db import get_categories, get_products, get_suppliers

def _go_to_login():
    from ui_login import show_login
    show_login(app_ref)

def _open_product_form(title, prod_id=None, data=None):
    from ui_product import show_product_form
    show_product_form(app_ref, title=title, prod_id=prod_id, data=data)

app_ref = None

def show_shop(app, search="", category="Все категории", supplier="Все поставщики", sort_order="Без сортировки", guest=False):
    global app_ref
    app_ref = app

    selected_item = None
    selected_card = None

    root = app["root"]
    cursor = app["cursor"]
    user = app.get("user")

    role = "Гость" if guest else (user["role"] if user else "Гость")
    fio_display = "Гость" if guest else user["fio"]
    is_privileged = role in ["Менеджер", "Администратор"]

    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("1200x750")
    root.minsize(900, 600)
    root.configure(bg="#FFFFFF")
    root.title("Каталог товаров")

    # Шапка
    header = tk.Frame(root, bg="#7FFF00", height=110)
    header.pack(fill="x", side="top")
    header.pack_propagate(False)
    tk.Label(header, text="ООО «Обувь» — Каталог товаров", font=FONT_TITLE, bg="#7FFF00").place(x=20, y=35)
    tk.Label(header, text=f"{fio_display} ({role})", font=FONT_BOLD, bg="#7FFF00").place(relx=1.0, y=55, anchor="e", x=-20)

    # Панель фильтров
    control_frame = tk.Frame(root, bg="#FFFFFF")
    if is_privileged:
        control_frame.pack(fill="x", padx=30, pady=10)

    search_var = tk.StringVar(value=search)
    cat_var = tk.StringVar(value=category)
    sup_var = tk.StringVar(value=supplier)
    sort_var = tk.StringVar(value=sort_order)

    if is_privileged:
        tk.Label(control_frame, text="Поиск:", font=FONT_BOLD, bg="#FFFFFF").pack(side="left", padx=(0, 5))
        search_entry = ttk.Entry(control_frame, textvariable=search_var, width=40, font=FONT)
        search_entry.pack(side="left", padx=10)

        tk.Label(control_frame, text="Категория:", font=FONT_BOLD, bg="#FFFFFF").pack(side="left", padx=(20, 5))
        cats = ["Все категории"] + get_categories(cursor)
        cat_combo = ttk.Combobox(control_frame, textvariable=cat_var, values=cats, state="readonly", width=25, font=FONT)
        cat_combo.pack(side="left", padx=10)

        tk.Label(control_frame, text="Поставщик:", font=FONT_BOLD, bg="#FFFFFF").pack(side="left", padx=(20, 5))
        sups = ["Все поставщики"] + get_suppliers(cursor)
        sup_combo = ttk.Combobox(control_frame, textvariable=sup_var, values=sups, state="readonly", width=25, font=FONT)
        sup_combo.pack(side="left", padx=10)

        tk.Label(control_frame, text="Количество на складе:", font=FONT_BOLD, bg="#FFFFFF").pack(side="left", padx=(20, 5))
        sort_values = ["Без сортировки", "По возраст.", "По убыв."]
        sort_combo = ttk.Combobox(control_frame, textvariable=sort_var, values=sort_values, state="readonly", width=15, font=FONT)
        sort_combo.pack(side="left", padx=10)

    # Область с карточками
    list_outer = tk.Frame(root, bg="#FFFFFF")
    list_outer.pack(fill="both", expand=True, padx=30, pady=(10 if is_privileged else 20, 10))

    canvas = tk.Canvas(list_outer, bg="#FFFFFF", highlightthickness=0, bd=0)
    scrollbar = ttk.Scrollbar(list_outer, orient="vertical", command=canvas.yview)
    cards_container = tk.Frame(canvas, bg="#FFFFFF")

    canvas_window = canvas.create_window((0, 0), window=cards_container, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    # Обработчик прокрутки колесиком
    def _on_mousewheel(event):
        if event.delta:
            delta = -int(event.delta / 120)
        elif hasattr(event, 'num'):
            delta = 1 if event.num == 5 else -1
        else:
            delta = -1
        canvas.yview_scroll(delta, "units")
        return "break"

    for w in (canvas, cards_container):
        w.bind("<MouseWheel>", _on_mousewheel)
        w.bind("<Button-4>", _on_mousewheel)
        w.bind("<Button-5>", _on_mousewheel)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Синхронизация размеров при изменении окна
    def _on_canvas_resize(event):
        canvas.itemconfig(canvas_window, width=event.width)
        _update_scrollregion()

    def _on_container_resize(event):
        _update_scrollregion()

    def _update_scrollregion():
        bbox = canvas.bbox("all")
        if bbox:
            canvas.configure(scrollregion=bbox)

    canvas.bind("<Configure>", _on_canvas_resize)
    cards_container.bind("<Configure>", _on_container_resize)
    canvas.bind("<MouseWheel>", _on_mousewheel)
    canvas.bind("<Enter>", lambda e: canvas.bind_all("<MouseWheel>", _on_mousewheel))
    canvas.bind("<Leave>", lambda e: canvas.unbind_all("<MouseWheel>"))

    def update_list():
        nonlocal selected_item, selected_card
        selected_item = None
        selected_card = None

        for widget in cards_container.winfo_children():
            widget.destroy()

        if is_privileged:
            search_text = search_var.get().strip()
            category_filter = cat_var.get()
            supplier_filter = sup_var.get()
            sort_mode = sort_var.get()
            db_sort = "asc" if sort_mode == "По возраст." else ("desc" if sort_mode == "По убыв." else "")
        else:
            search_text = ""
            category_filter = "Все категории"
            supplier_filter = "Все поставщики"
            db_sort = ""

        rows = get_products(cursor, search=search_text, category=category_filter, supplier=supplier_filter, sort_order=db_sort)
        if not rows:
            tk.Label(cards_container, text="Товары не найдены", font=FONT_TITLE, bg="#FFFFFF", fg="#555555").pack(pady=50)
            return

        # Рекурсивная привязка события ко всем дочерним виджетам
        def bind_recursive(widget, event, callback):
            widget.bind(event, callback)
            for child in widget.winfo_children():
                bind_recursive(child, event, callback)

        for row in rows:
            product_id, product_name, category_name, description, manufacturer, supplier_name, price, quantity, discount, image_path, article, unit = row
            product_name = product_name or "Без названия"
            price = float(price or 0)
            quantity = int(quantity or 0)
            discount = int(discount or 0)

            if discount > 15:
                card_bg, text_color = "#2E8B57", "#FFFFFF"
            else:
                card_bg, text_color = "#FFFFFF", "#000000"

            card = tk.Frame(cards_container, bg=card_bg, relief="solid", bd=1, highlightthickness=0, takefocus=0)
            card.pack(fill="x", expand=False, pady=4, padx=0, ipady=10)

            def select_card(event=None, c=card, r=row, p=product_id):
                nonlocal selected_item, selected_card
                if selected_card == c:
                    return
                if selected_card is not None:
                    selected_card.config(relief="solid", bd=1, highlightthickness=0)
                selected_item = r
                selected_card = c
                c.config(relief="solid", bd=3, highlightthickness=2, highlightbackground="#00FA9A")

            # Фото
            photo_outer = tk.Frame(card, bg=card_bg, relief="solid", bd=2, padx=8, pady=8)
            photo_outer.pack(side="left", padx=(10, 15), pady=8)

            photo_inner = tk.Frame(photo_outer, width=140, height=180, bg="#F5F5F5")
            photo_inner.pack()
            photo_inner.pack_propagate(False)

            if image_path and os.path.exists(image_path):
                try:
                    img = Image.open(image_path)
                    img.thumbnail((130, 170), Image.Resampling.LANCZOS)
                    photo = ImageTk.PhotoImage(img)
                    tk.Label(photo_inner, image=photo, bg="#F5F5F5").pack(expand=True)
                    photo_inner.image = photo
                except Exception:
                    tk.Label(photo_inner, text="Нет фото", font=FONT, fg="#888888", bg="#F5F5F5").pack(expand=True)
            else:
                tk.Label(photo_inner, text="Нет фото", font=FONT, fg="#888888", bg="#F5F5F5").pack(expand=True)

            # Информация
            info_fr = tk.Frame(card, bg=card_bg)
            info_fr.pack(side="left", fill="both", expand=True, padx=10)

            tk.Label(info_fr, text=f"{category_name} | {product_name}", font=("Times New Roman", 16, "bold"), bg=card_bg, fg=text_color, anchor="w").pack(anchor="w")

            if description:
                tk.Label(info_fr, text=(description[:180] + "...") if len(description) > 180 else description, font=FONT, bg=card_bg, fg=text_color, anchor="w", wraplength=600, justify="left").pack(anchor="w", pady=(0, 5))

            price_fr = tk.Frame(info_fr, bg=card_bg)
            price_fr.pack(anchor="w", pady=(0, 5))
            if discount > 0:
                tk.Label(price_fr, text="Цена:", font=FONT, bg=card_bg, fg=text_color).pack(side="left")
                old_lbl = tk.Label(price_fr, text=f" {price:.2f} ₽", font=FONT, fg="red", bg=card_bg)
                old_lbl.pack(side="left")
                old_lbl.config(font=(FONT[0], FONT[1], "overstrike"))
                tk.Label(price_fr, text=f" {price * (1 - discount / 100):.2f} ₽", font=("Times New Roman", 18, "bold"), fg=text_color, bg=card_bg).pack(side="left")
            else:
                tk.Label(price_fr, text=f"Цена: {price:.2f} ₽", font=("Times New Roman", 18, "bold"), fg=text_color, bg=card_bg).pack(anchor="w")

            tk.Label(info_fr, text=f"Производитель: {manufacturer or 'Не указан'}", font=FONT, bg=card_bg, fg=text_color, anchor="w").pack(anchor="w", pady=(0, 2))
            tk.Label(info_fr, text=f"Поставщик: {supplier_name or 'Не указан'}", font=FONT, bg=card_bg, fg=text_color, anchor="w").pack(anchor="w", pady=(0, 2))
            tk.Label(info_fr, text=f"Ед.: {unit or 'шт.'}", font=FONT, bg=card_bg, fg=text_color, anchor="w").pack(anchor="w", pady=(0, 2))

            qty_bg = "#ADD8E6" if quantity == 0 and discount <= 15 else card_bg
            tk.Label(info_fr, text=f"На складе: {quantity}", font=FONT_BOLD,
                     fg="#000000" if qty_bg == "#ADD8E6" else text_color,
                     bg=qty_bg, anchor="w", justify="left").pack(anchor="w", pady=(3, 0), fill="x")

            if discount > 0:
                disc_outer = tk.Frame(card, bg=card_bg, relief="solid", bd=2, padx=15, pady=15)
                disc_outer.pack(side="right", padx=10, pady=8)

                disc_bg = "#FFFFFF" if discount <= 15 else "#1C6B3A"
                disc_fg = "#000000" if discount <= 15 else "#FFFFFF"

                disc_inner = tk.Frame(disc_outer, width=120, height=140, bg=disc_bg)
                disc_inner.pack()
                disc_inner.pack_propagate(False)

                tk.Label(disc_inner, text="Действующая\nскидка:", font=("Times New Roman", 12, "bold"),
                         fg=disc_fg, bg=disc_bg, justify="center").pack(pady=(10, 0))
                tk.Label(disc_inner, text=f"{discount}%", font=("Times New Roman", 28, "bold"),
                         fg=disc_fg, bg=disc_bg, justify="center").pack(expand=True)

            # Привязка событий выделения и редактирования
            bind_recursive(card, "<Button-1>", select_card)

            if role == "Администратор":
                def open_edit(event=None, p=product_id, r=row):
                    _open_product_form("Редактировать товар", prod_id=p, data=r)
                bind_recursive(card, "<Double-Button-1>", open_edit)

    # Нижняя панель
    bottom_frame = tk.Frame(root, bg="#FFFFFF")
    bottom_frame.pack(fill="x", pady=15)

    if role == "Администратор":
        tk.Button(bottom_frame, text="Добавить товар", command=lambda: _open_product_form("Добавить новый товар"),
                  bg="#00FA9A", fg="black", font=FONT_BOLD, width=20).pack(side="left", padx=50)

        def delete_selected():
            nonlocal selected_item, selected_card
            if selected_item is None:
                messagebox.showwarning("Внимание", "Выберите товар для удаления (кликните по карточке).")
                return

            prod_id = selected_item[0]
            prod_name = selected_item[1]

            if messagebox.askyesno("Подтверждение удаления", f"Вы действительно хотите удалить товар\n'{prod_name}'?\n\nЭто действие нельзя отменить.", icon='warning'):
                try:
                    from db import delete_product
                    delete_product(cursor, app["conn"], prod_id)
                    messagebox.showinfo("Успех", f"Товар '{prod_name}' успешно удалён!")
                    selected_item = None
                    selected_card = None
                    update_list()
                except Exception as e:
                    messagebox.showerror("Ошибка удаления", str(e))

        tk.Button(bottom_frame, text="Удалить товар", command=delete_selected,
                  bg="#FF0000", fg="white", font=FONT_BOLD, width=20).pack(side="left", padx=20)

    tk.Button(bottom_frame, text="Назад", command=_go_to_login,
              bg="#FFFFFF", fg="black", font=FONT_BOLD, width=20, relief="groove").pack(side="right", padx=100)

    if is_privileged:
        search_entry.bind("<KeyRelease>", lambda e: update_list())
        cat_combo.bind("<<ComboboxSelected>>", lambda e: update_list())
        sup_combo.bind("<<ComboboxSelected>>", lambda e: update_list())
        sort_combo.bind("<<ComboboxSelected>>", lambda e: update_list())

    update_list()