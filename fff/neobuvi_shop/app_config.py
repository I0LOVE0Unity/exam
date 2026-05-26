import sqlite3
from tkinter import messagebox
import sys

# Настройки подключения

DATABASE = "MagazWord.db"

# Настройки шрифтов
FONT = ("Times New Roman", 12)
FONT_BOLD = ("Times New Roman", 12, "bold")
FONT_TITLE = ("Times New Roman", 18, "bold")



def get_connection():
    """Возвращает соединение с SQLite."""
    try:
        conn = sqlite3.connect(DATABASE)
        conn.execute("PRAGMA foreign_keys = ON")
        conn.row_factory = sqlite3.Row   # доступ к столбцам по имени: row["название"]
        return conn
    except sqlite3.Error as e:
        messagebox.showerror("Ошибка подключения", f"Не удалось подключиться к SQLite:\n{e}")
        sys.exit(1)