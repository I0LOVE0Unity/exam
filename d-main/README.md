:: 1. Создать и активировать venv (в cmd!)
python -m venv .venv
.venv\Scripts\activate.bat

:: 2. Обновить pip
pip install --upgrade pip

:: 3. Установить PySide6 со всем
pip install PySide6 PySide6-Essentials PySide6-Addons

:: 4. Проверить что всё встало
pip list | findstr PySide

:: 5. Проверить инструменты
pyside6-designer
pyside6-uic --version
winget install Python.Python.3.14 --scope user
pip install PySide6==6.10.2 SQLAlchemy==2.0.38 pyodbc==5.3.0 pymssql==2.3.13
ODBC Driver 17 for SQL Server
host="ILABSQLW19S1", port=49172
pyside6-uic ui/login.ui -o ui/login.py  pyside6-designer

## БД

**Справочники** (`category` `manufacturer` `name` `role` `status` `supplier` `unit`):

id      int
title   nvarchar


**product**

id               int
article          nvarchar
name_id          int        → name
unit_id          int        → unit
price            decimal
supplier_id      int        → supplier
manufacturer_id  int        → manufacturer
category_id      int        → category
discount         decimal   *
stock_quantity   int
description      nvarchar  *
photo            nvarchar  *


**user**

id         int
role_id    int       → role
full_name  nvarchar
login      nvarchar
password   nvarchar


**order**

id               int
order_date       datetime
delivery_date    datetime  *
pickup_point_id  int       → pickup_point
user_id          int       → user
code             nvarchar  *
status_id        int       → status


**order_item**

id          int
order_id    int  → order
product_id  int  → product
quantity    int


**pickup_point**

id       int
address  nvarchar