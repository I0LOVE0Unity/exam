import tkinter as tk
from app_config import get_connection
from ui_login import show_login

if __name__ == "__main__":
    connection = get_connection()
    database_cursor = connection.cursor()

    main_window = tk.Tk()
    main_window.title("ООО «Обувь»")
    main_window.configure(bg="#FFFFFF")
    main_window.geometry("1000x700")

    try:
        main_window.iconbitmap("icon.ico")
    except Exception:
        pass

    application_context = {
        "root": main_window,
        "conn": connection,
        "cursor": database_cursor,
        "user": None,
        "current_window": None
    }

    show_login(application_context)
    main_window.mainloop()