import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import os
from app_config import FONT, FONT_BOLD, FONT_TITLE

def _get_list(cursor, query):
    return [row[0].strip() for row in cursor.execute(query).fetchall() if row[0]]

def show_product_form(app, title="Новый товар", prod_id=None, data=None):
    if app.get("product_form_open", False):
        messagebox.showwarning("Внимание", "Окно редактирования товара уже открыто.")
        return

    root = app["root"]
    cursor = app["cursor"]
    conn = app["conn"]

    for widget in root.winfo_children():
        widget.destroy()

    root.geometry("950x700")
    root.minsize(800, 600)
    root.configure(bg="#FFFFFF")
    root.title(title)
    app["product_form_open"] = True

    # Шапка
    header = tk.Frame(root, bg="#7FFF00", height=80)
    header.pack(fill="x", side="top")
    header.pack_propagate(False)
    tk.Label(header, text=title, font=FONT_TITLE, bg="#7FFF00").pack(pady=20)

    # Область прокрутки
    canvas_frame = tk.Frame(root, bg="#FFFFFF")
    canvas_frame.pack(fill="both", expand=True, padx=15, pady=10)

    canvas = tk.Canvas(canvas_frame, bg="#FFFFFF", highlightthickness=0, bd=0)
    scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)
    form_frame = tk.Frame(canvas, bg="#FFFFFF")

    canvas_window = canvas.create_window((0, 0), window=form_frame, anchor="nw")
    canvas.configure(yscrollcommand=scrollbar.set)

    def on_canvas_resize(event):
        canvas.itemconfig(canvas_window, width=event.width)

    def on_frame_resize(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    canvas.bind("<Configure>", on_canvas_resize)
    form_frame.bind("<Configure>", on_frame_resize)

    def on_mousewheel(event):
        canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        return "break"

    canvas.bind("<Enter>", lambda e: root.bind_all("<MouseWheel>", on_mousewheel))
    canvas.bind("<Leave>", lambda e: root.unbind_all("<MouseWheel>"))

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Левая панель: фото и кнопки
    left_panel = tk.Frame(form_frame, bg="#FFFFFF", width=260)
    left_panel.pack(side="left", fill="y", padx=(0, 15))
    left_panel.pack_propagate(False)

    tk.Label(left_panel, text="Фото товара", font=FONT_BOLD, bg="#FFFFFF").pack(anchor="w", pady=(0, 5))
    photo_border = tk.Frame(left_panel, bg="#FFFFFF", relief="solid", bd=1, padx=6, pady=6)
    photo_border.pack(pady=5, fill="x")
    photo_frame = tk.Frame(photo_border, width=240, height=180, bg="#E0E0E0")
    photo_frame.pack()
    photo_frame.pack_propagate(False)
    photo_label = tk.Label(photo_frame, bg="#E0E0E0", text="Нет изображения", fg="gray", font=FONT)
    photo_label.place(relx=0.5, rely=0.5, anchor="center")

    state = {"current_path": data[9] if data and len(data) > 9 else None}

    def update_photo_display(path):
        if path and os.path.exists(path):
            try:
                img = Image.open(path)
                img.thumbnail((240, 180), Image.Resampling.LANCZOS)
                tk_img = ImageTk.PhotoImage(img)
                photo_label.config(image=tk_img, text="")
                photo_label.image = tk_img
            except Exception:
                photo_label.config(image="", text="Ошибка загрузки")
        else:
            photo_label.config(image="", text="Нет изображения")

    def choose_photo():
        file_path = filedialog.askopenfilename(filetypes=[("Изображения", "*.png *.jpg *.jpeg *.bmp")])
        if not file_path:
            return
        photos_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "photos")
        os.makedirs(photos_dir, exist_ok=True)
        ext = os.path.splitext(file_path)[1]
        new_name = f"prod_{prod_id or 'new'}_{len(os.listdir(photos_dir))}{ext}"
        new_path = os.path.join(photos_dir, new_name)
        if state["current_path"] and os.path.exists(state["current_path"]):
            try:
                os.remove(state["current_path"])
            except Exception:
                pass
        try:
            img = Image.open(file_path)
            img.thumbnail((300, 200), Image.Resampling.LANCZOS)
            img.save(new_path)
            state["current_path"] = new_path
            update_photo_display(new_path)
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

    update_photo_display(state["current_path"])
    tk.Button(left_panel, text="Загрузить / Заменить фото", command=choose_photo,
              bg="#00FA9A", fg="black", font=FONT_BOLD, width=22).pack(pady=10, fill="x")
    tk.Label(left_panel, text="Рекомендуемый размер: 300x200 px", font=FONT, fg="gray", bg="#FFFFFF", wraplength=240, justify="center").pack(pady=5)

    tk.Frame(left_panel, height=1, bg="#CCCCCC").pack(fill="x", pady=15, padx=10)

    # Правая панель: форма
    right_panel = tk.Frame(form_frame, bg="#FFFFFF")
    right_panel.pack(side="left", fill="both", expand=True)

    d = data if data else (None, "", "", "", "", "", 0.0, 0, 0, None, "", "")
    is_editing = prod_id is not None
    widgets = {}

    if is_editing and prod_id is not None:
        tk.Label(right_panel, text="ID товара:", font=FONT_BOLD, bg="#FFFFFF", anchor="w").pack(anchor="w", pady=(10, 2))
        id_var = tk.StringVar(value=str(int(prod_id)))
        tk.Entry(right_panel, textvariable=id_var, state="readonly", bg="#E8E8E8", fg="#000000", font=FONT, justify="center", relief="solid", bd=1).pack(fill="x", padx=15, pady=(0, 8))

    def create_input(label_text, widget_type, key, placeholder, current_value):
        tk.Label(right_panel, text=label_text, font=FONT_BOLD, bg="#FFFFFF", anchor="w").pack(anchor="w", pady=(10, 2))
        if widget_type == "entry":
            entry = tk.Entry(right_panel, font=FONT, relief="solid", bd=1)
            entry.pack(fill="x", padx=15, pady=(0, 8))
            value = str(current_value) if current_value is not None else ""
            if is_editing and value:
                entry.insert(0, value)
                entry.config(fg="black")
            else:
                entry.insert(0, placeholder)
                entry.config(fg="gray")
                entry.bind("<FocusIn>", lambda e, w=entry: (w.delete(0, tk.END), w.config(fg="black")) if w.get() == placeholder else None)
                entry.bind("<FocusOut>", lambda e, w=entry: (w.insert(0, placeholder), w.config(fg="gray")) if not w.get() else None)
            widgets[key] = entry
        elif widget_type == "text":
            text_box = tk.Text(right_panel, height=4, font=FONT, wrap="word", relief="solid", bd=1)
            text_box.pack(fill="x", padx=15, pady=(0, 8))
            if is_editing and current_value:
                text_box.insert("1.0", current_value)
                text_box.config(fg="black")
            else:
                text_box.insert("1.0", placeholder)
                text_box.config(fg="gray")
                text_box.bind("<FocusIn>", lambda e, w=text_box: (w.delete("1.0", "end"), w.config(fg="black")) if w.get("1.0", "end-1c") == placeholder else None)
                text_box.bind("<FocusOut>", lambda e, w=text_box: (w.insert("1.0", placeholder), w.config(fg="gray")) if not w.get("1.0", "end-1c").strip() else None)
            widgets[key] = text_box

    # Категория
    tk.Label(right_panel, text="Категория товара:", font=FONT_BOLD, bg="#FFFFFF", anchor="w").pack(anchor="w", pady=(10, 2))
    cat_opts = _get_list(cursor, "SELECT название_категории FROM Категория ORDER BY название_категории")
    cat_var = tk.StringVar()
    ttk.Combobox(right_panel, textvariable=cat_var, values=cat_opts, state="readonly", font=FONT).pack(fill="x", padx=15, pady=(0, 8))
    current_cat = str(d[2]).strip() if d[2] is not None else ""
    cat_var.set(current_cat if is_editing and current_cat in cat_opts else "")
    widgets["category"] = cat_var

    create_input("Описание товара:", "text", "desc", "Введите описание...", d[3])

    # Производитель (текстовое поле)
    tk.Label(right_panel, text="Производитель:", font=FONT_BOLD, bg="#FFFFFF", anchor="w").pack(anchor="w", pady=(10, 2))
    man_var = tk.StringVar()
    entry_man = tk.Entry(right_panel, textvariable=man_var, font=FONT, relief="solid", bd=1)
    entry_man.pack(fill="x", padx=15, pady=(0, 8))
    current_man = str(d[4]).strip() if d[4] is not None else ""
    man_var.set(current_man if is_editing else "")
    widgets["manufacturer"] = man_var   # или entry_man, но man_var тоже подойдёт

    # Поставщик
    tk.Label(right_panel, text="Поставщик:", font=FONT_BOLD, bg="#FFFFFF", anchor="w").pack(anchor="w", pady=(10, 2))
    sup_opts = _get_list(cursor, "SELECT название_поставщика FROM Поставщик ORDER BY название_поставщика")
    sup_var = tk.StringVar()
    ttk.Combobox(right_panel, textvariable=sup_var, values=sup_opts, state="readonly", font=FONT).pack(fill="x", padx=15, pady=(0, 8))
    current_sup = str(d[5]).strip() if d[5] is not None else ""
    sup_var.set(current_sup if is_editing and current_sup in sup_opts else "")
    widgets["supplier"] = sup_var

    create_input("Артикул:", "entry", "article", "Введите артикул", d[10])
    create_input("Наименование товара:", "entry", "name", "Введите наименование", d[1])
    create_input("Единица измерения:", "entry", "unit", "шт.", d[11])
    create_input("Цена (руб.):", "entry", "price", "0.00", d[6])
    create_input("Количество на складе:", "entry", "quantity", "0", d[7])
    create_input("Действующая скидка (%):", "entry", "discount", "0", d[8])

    def save_product():
        def get_widget_value(key, placeholder):
            w = widgets[key]
            val = w.get("1.0", tk.END).strip() if isinstance(w, tk.Text) else w.get().strip()
            return "" if val == placeholder else val

        article = get_widget_value("article", "Введите артикул")
        name = get_widget_value("name", "Введите наименование")
        category = widgets["category"].get().strip()
        desc = get_widget_value("desc", "Введите описание...")
        manufacturer = widgets["manufacturer"].get().strip()
        supplier = widgets["supplier"].get().strip()
        unit = get_widget_value("unit", "шт.") or "шт."

        try:
            price = float(get_widget_value("price", "0.00").replace(",", ".") or "0")
            if price < 0: raise ValueError("Цена не может быть отрицательной")
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))
            return

        try:
            qty = int(get_widget_value("quantity", "0") or "0")
            if qty < 0: raise ValueError("Количество не может быть отрицательным")
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))
            return

        try:
            disc = int(get_widget_value("discount", "0") or "0")
            if not (0 <= disc <= 100): raise ValueError("Скидка должна быть от 0 до 100%")
        except ValueError as e:
            messagebox.showerror("Ошибка ввода", str(e))
            return

        if not article or not name or not category:
            messagebox.showwarning("Предупреждение", "Поля 'Артикул', 'Наименование' и 'Категория' обязательны.")
            return

        product_data = {
            "category": category, "article": article, "name": name, "unit": unit,
            "price": price, "supplier": supplier, "manufacturer": manufacturer,
            "discount": disc, "quantity": qty, "description": desc,
            "photo_path": state["current_path"]
        }

        try:
            from db import save_product as db_save_product
            db_save_product(cursor, conn, prod_id, product_data)
            messagebox.showinfo("Успех", "Товар успешно сохранён!")
            app["product_form_open"] = False
            from ui_shop import show_shop
            show_shop(app)
        except Exception as e:
            messagebox.showerror("Ошибка БД", str(e))

    def go_back():
        app["product_form_open"] = False
        from ui_shop import show_shop
        show_shop(app)

    tk.Button(left_panel, text="Сохранить", command=save_product,
              bg="#00FA9A", fg="black", font=FONT_BOLD, width=20).pack(fill="x", padx=10, pady=5)
    tk.Button(left_panel, text="Назад", command=go_back,
              bg="#FFFFFF", fg="black", font=FONT_BOLD, width=20, relief="groove").pack(fill="x", padx=10, pady=5)

    root.protocol("WM_DELETE_WINDOW", lambda: [app.__setitem__("product_form_open", False), root.quit()])