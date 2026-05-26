import pyodbc
from tkinter import messagebox
import sys

# Настройки подключения
SERVER = "KLABSQLW19S1,49172"
DATABASE = "MagazWord" # надо поменять на свой бд

# Настройки шрифтов
FONT = ("Times New Roman", 12) # надо поменять на шрифт из тз
FONT_BOLD = ("Times New Roman", 12, "bold") # надо поменять на шрифт из тз
FONT_TITLE = ("Times New Roman", 18, "bold") # надо поменять на шрифт из тз

def get_connection():
    drivers = [d for d in pyodbc.drivers() if "SQL Server" in d]
    if not drivers:
        messagebox.showerror("Ошибка", "Не найден системный драйвер для SQL Server")
        sys.exit(1)

    try:
        conn_str = (
            f"Driver={{{drivers[-1]}}};"
            f"Server={SERVER};"
            f"Database={DATABASE};"
            "Trusted_Connection=yes;"
            "Encrypt=no;"
        )
        return pyodbc.connect(conn_str)
    except pyodbc.Error as e:
        messagebox.showerror("Ошибка подключения", str(e))
        sys.exit(1)