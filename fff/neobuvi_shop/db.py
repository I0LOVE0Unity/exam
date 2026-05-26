import pyodbc

def get_user(cursor, login, password):
    query = """
        SELECT a.ид_клиента, a.фио, r.название_роли
        FROM Аккаунт a
        JOIN Роль r ON a.ид_роли = r.ид_роли
        WHERE a.логин=? AND a.пароль=?
    """
    cursor.execute(query, (login, password))
    row = cursor.fetchone()
    if not row:
        return None
    return {"id": row[0], "fio": row[1], "role": row[2]}

def get_categories(cursor):
    cursor.execute("SELECT название_категории FROM Категория ORDER BY название_категории")
    return [row[0] for row in cursor.fetchall()]

def get_suppliers(cursor):
    cursor.execute("SELECT название_поставщика FROM Поставщик ORDER BY название_поставщика")
    return [row[0] for row in cursor.fetchall()]

def get_products(cursor, search="", category="Все категории", supplier="Все поставщики", sort_order=""):
    query = """
        SELECT p.ид_товара, p.наименование_товара, c.название_категории,
               p.описание_товара, p.производитель, s.название_поставщика,
               p.цена, p.количество_на_складе, p.действующая_скидка, p.фото, p.артикул, p.единица_измерения
        FROM Товар p
        JOIN Категория c ON p.ид_категории_товара = c.ид_категории_товара
        JOIN Поставщик s ON p.ид_поставщика = s.ид_поставщика
        WHERE 1=1
    """
    params = []
    
    if search:
        search_pattern = f"%{search.lower()}%"
        query += """
            AND (
                LOWER(p.наименование_товара) LIKE ? OR
                LOWER(p.артикул) LIKE ? OR
                LOWER(p.описание_товара) LIKE ? OR
                LOWER(p.производитель) LIKE ? OR
                LOWER(s.название_поставщика) LIKE ? OR
                LOWER(c.название_категории) LIKE ?
            )
        """
        params.extend([search_pattern] * 6)
    
    if category != "Все категории":
        query += " AND c.название_категории = ?"
        params.append(category)
        
    if supplier != "Все поставщики":
        query += " AND s.название_поставщика = ?"
        params.append(supplier)

    if sort_order == "По возраст.":
        query += " ORDER BY p.количество_на_складе ASC"
    elif sort_order == "По убыв.":
        query += " ORDER BY p.количество_на_складе DESC"
    else:
        query += " ORDER BY p.ид_товара ASC"

    cursor.execute(query, params)
    return cursor.fetchall()

def save_product(cursor, conn, prod_id, data_dict):
    category_title = data_dict.get("category", "")
    cursor.execute("SELECT ид_категории_товара FROM Категория WHERE название_категории = ?", (category_title,))
    category_row = cursor.fetchone()
    if not category_row:
        raise ValueError(f"Категория '{category_title}' не найдена в БД")
    category_id = category_row[0]

    supplier_name = data_dict.get("supplier", "")
    cursor.execute("SELECT ид_поставщика FROM Поставщик WHERE название_поставщика = ?", (supplier_name,))
    supplier_row = cursor.fetchone()
    if not supplier_row:
        raise ValueError(f"Поставщик '{supplier_name}' не найден в БД")
    supplier_id = supplier_row[0]

    sql_params = (
        category_id,
        data_dict.get("article", ""),
        data_dict.get("name", ""),
        data_dict.get("unit", "шт."),
        float(data_dict.get("price", 0)),
        supplier_id,
        data_dict.get("manufacturer", ""),
        int(data_dict.get("discount", 0)),
        int(data_dict.get("quantity", 0)),
        data_dict.get("description", ""),
        data_dict.get("photo_path", "")
    )

    if prod_id:
        cursor.execute("""
            UPDATE Товар SET
                ид_категории_товара=?, артикул=?, наименование_товара=?, единица_измерения=?,
                цена=?, ид_поставщика=?, производитель=?, действующая_скидка=?,
                количество_на_складе=?, описание_товара=?, фото=?
            WHERE ид_товара=?
        """, sql_params + (prod_id,))
    else:
        cursor.execute("""
            INSERT INTO Товар (
                ид_категории_товара, артикул, наименование_товара, единица_измерения,
                цена, ид_поставщика, производитель, действующая_скидка,
                количество_на_складе, описание_товара, фото
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, sql_params)
    
    conn.commit()

def delete_product(cursor, conn, prod_id):
    cursor.execute("SELECT COUNT(*) FROM Деталь_Заказа WHERE ид_товара = ?", (prod_id,))
    order_count = cursor.fetchone()[0]
    
    if order_count > 0:
        raise ValueError("Нельзя удалить товар, который присутствует в существующих заказах!")
    
    cursor.execute("DELETE FROM Товар WHERE ид_товара = ?", (prod_id,))
    conn.commit()