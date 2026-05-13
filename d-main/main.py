import os
import sys

from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QDialog, QMessageBox, QWidget
from sqlalchemy import func, or_, select

from db import session, Product, User, Supplier, Name, Category, Manufacturer, Unit, Role, OrderItem, _load_lookup
from ui.edit import Ui_widget_edit
from ui.item_card import Ui_widget_card
from ui.login import Ui_widget_login
from ui.main import Ui_widget_main

PROJECT_DIR = os.path.dirname(__file__)
ASSET_ICON_ICO = os.path.join(PROJECT_DIR, "assets", "Icon.ico")
ASSET_ICON_PNG = os.path.join(PROJECT_DIR, "assets", "Icon.png")
ASSET_PLACEHOLDER_PNG = os.path.join(PROJECT_DIR, "assets", "picture.png")


class MainUi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_widget_main()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(ASSET_ICON_ICO))
        self.setWindowTitle("Каталог товаров")
        self.ui.label_logo.setPixmap(QPixmap(ASSET_ICON_PNG))


class LoginUi(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_widget_login()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(ASSET_ICON_ICO))
        self.setWindowTitle("Авторизация")
        self.ui.label_logo.setPixmap(QPixmap(ASSET_ICON_PNG))


class CardUi(QWidget):
    def __init__(self, item, name_title, category_title, manufacturer_title,
                 supplier_title, unit_title, on_double_click=None):
        super().__init__()
        self.ui = Ui_widget_card()
        self.ui.setupUi(self)
        self.item = item
        self.name_title = name_title
        self.category_title = category_title
        self.manufacturer_title = manufacturer_title
        self.supplier_title = supplier_title
        self.unit_title = unit_title
        self._on_double_click = on_double_click

    def mouseDoubleClickEvent(self, event):
        if self._on_double_click:
            self._on_double_click(self.item)


class EditUi(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_widget_edit()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon(ASSET_ICON_ICO))


class App:
    def __init__(self):
        self.main = MainUi()
        self.login = LoginUi()
        self.edit_window = None
        self._current_role = None
        self.login.ui.pushButton_exit.clicked.connect(sys.exit)
        self.login.ui.pushButton_guest.clicked.connect(self.open_main)
        self.login.ui.pushButton_login.clicked.connect(self.auth)

    def auth(self):
        login = self.login.ui.lineEdit_login.text()
        password = self.login.ui.lineEdit_password.text()
        user = session.query(User).filter(
            User.login == login, User.password == password
        ).first()
        if user:
            roles = _load_lookup(Role)
            role_title = roles.get(user.role_id, "")
            self.open_main(username=user.full_name, role=role_title)
        else:
            QMessageBox.warning(
                self.login,
                "Ошибка",
                "Неверный логин или пароль.\nПроверьте введённые данные.",
            )

    def open_main(self, username="Гость", role=None):
        if role is None:
            role = "__guest__"
        self._current_role = role
        ui = self.main.ui
        self.login.hide()
        if role == "__guest__":
            ui.label_username.setText("Гость")
        else:
            ui.label_username.setText(username)
        ui.pushButton_exit.clicked.connect(self.open_login)
        ui.pushButton_clear.clicked.connect(self.open_login)
        ui.lineEdit_search.textChanged.connect(self.sort_products)
        ui.comboBox.currentIndexChanged.connect(self.sort_products)
        ui.comboBox_2.currentIndexChanged.connect(self.sort_products)
        if role == "Администратор":
            ui.pushButton_add.show()
            ui.pushButton_add.clicked.connect(lambda: self.open_edit(None))
        else:
            ui.pushButton_add.hide()
        if role not in ("Менеджер", "Администратор"):
            ui.lineEdit_search.hide()
            ui.comboBox.hide()
            ui.comboBox_2.hide()
        self._load_all_products()
        self.load_suppliers()
        self.load_sorting()
        self.main.show()

    def _build_query(self):
        return (
            session.query(Product, Name, Category, Manufacturer, Supplier, Unit)
            .join(Name, Product.name_id == Name.id)
            .join(Category, Product.category_id == Category.id)
            .join(Manufacturer, Product.manufacturer_id == Manufacturer.id)
            .join(Supplier, Product.supplier_id == Supplier.id)
            .join(Unit, Product.unit_id == Unit.id)
        )

    def _load_all_products(self):
        self.load_items(self._build_query())

    def add_item_card(self, product, name, category, manufacturer, supplier, unit):
        is_admin = self._current_role == "Администратор"
        on_dc = (lambda p: self.open_edit(p)) if is_admin else None
        card = CardUi(
            product,
            name.title.strip(),
            category.title.strip(),
            manufacturer.title.strip(),
            supplier.title.strip(),
            unit.title.strip(),
            on_double_click=on_dc,
        )
        price = float(product.price or 0)
        discount = float(product.discount or 0)
        count = product.stock_quantity or 0
        card.ui.label_category_plus_name.setText(
            f"Категория товара: {category.title.strip()} | Наименование товара: {name.title.strip()}"
        )
        card.ui.label_manufacturer.setText(f"Производитель: {manufacturer.title.strip()}")
        card.ui.label_count.setText(f"Количество на складе: {count}")
        card.ui.label_1.setText(f"Единица измерения: {unit.title.strip()}")
        card.ui.label_2.setText(f"Поставщик: {supplier.title.strip()}")
        card.ui.label_description.setText(f"Описание товара: {product.description or ''}")
        card.ui.label_discount.setText(f"Скидка: {discount:.0f}%")
        if discount:
            new_price = round(price * (1 - discount / 100), 2)
            card.ui.label_price.setText(
                f"Цена: <span style='color:red;text-decoration:line-through;'>{price:.2f} ₽</span> {new_price:.2f} ₽"
            )
        else:
            card.ui.label_price.setText(f"Цена: {price:.2f} ₽")
        if count == 0:
            card.ui.label_count.setStyleSheet("background:#87CEFA;")
        if discount > 15:
            card.setStyleSheet("background:#2E8B57;")
        else:
            card.setStyleSheet("background:#FFFFFF;")
        card.ui.label_image.setPixmap(QPixmap(ASSET_PLACEHOLDER_PNG))
        if product.photo and os.path.isfile(product.photo):
            card.ui.label_image.setPixmap(QPixmap(product.photo))
        self.main.ui.verticalLayout_card.addWidget(card)

    def clear_products(self):
        layout = self.main.ui.verticalLayout_card
        while layout.count():
            w = layout.takeAt(0)
            if w and w.widget():
                w.widget().deleteLater()

    def load_items(self, query):
        self.clear_products()
        for row in query.all():
            self.add_item_card(*row)
        self.main.ui.verticalLayout_card.addStretch()

    def load_suppliers(self):
        self.main.ui.comboBox.clear()
        self.main.ui.comboBox.addItem("Все поставщики", 0)
        for s in session.query(Supplier).all():
            self.main.ui.comboBox.addItem(s.title.strip(), s.id)

    def load_sorting(self):
        self.main.ui.comboBox_2.clear()
        self.main.ui.comboBox_2.addItems(["Без сортировки", "Количество ↑", "Количество ↓"])
        for i in range(3):
            self.main.ui.comboBox_2.setItemData(i, i)

    def sort_products(self):
        query = self._build_query()
        supplier_id = self.main.ui.comboBox.currentData()
        if supplier_id:
            query = query.filter(Product.supplier_id == supplier_id)
        sort_type = self.main.ui.comboBox_2.currentData()
        if sort_type == 1:
            query = query.order_by(Product.stock_quantity.asc())
        elif sort_type == 2:
            query = query.order_by(Product.stock_quantity.desc())
        search_text = self.main.ui.lineEdit_search.text().strip()
        if search_text:
            query = query.filter(
                or_(
                    Name.title.ilike(f"%{search_text}%"),
                    Category.title.ilike(f"%{search_text}%"),
                    Product.description.ilike(f"%{search_text}%"),
                    Manufacturer.title.ilike(f"%{search_text}%"),
                    Supplier.title.ilike(f"%{search_text}%"),
                )
            )
        self.load_items(query)

    def open_login(self):
        self.main.hide()
        self.clear_products()
        self.login.show()

    def open_edit(self, item):
        if self.edit_window is not None and self.edit_window.isVisible():
            self.edit_window.raise_()
            return
        self.edit_window = EditUi(self.main)
        ui = self.edit_window.ui
        # Заполнение справочников
        def fill_combo(combo, cls):
            combo.clear()
            for r in session.query(cls).all():
                combo.addItem(r.title.strip(), r.id)
        fill_combo(ui.comboBox_name, Name)
        fill_combo(ui.comboBox_category, Category)
        fill_combo(ui.comboBox_manufacturer, Manufacturer)
        fill_combo(ui.comboBox_supplier, Supplier)
        fill_combo(ui.comboBox_unit, Unit)
        if item is None:
            self.edit_window.setWindowTitle("Добавление товара")
            ui.label_id.hide()
            ui.pushButton_delete.hide()
            ui.label_photo.setPixmap(QPixmap(ASSET_PLACEHOLDER_PNG))
            ui.pushButton_save.clicked.connect(lambda: self.save_item(None))
        else:
            self.edit_window.setWindowTitle("Редактирование товара")
            ui.label_id.setText(f"ID: {item.id}")
            # Установить текущие значения в combobox
            for combo, fk_id in [
                (ui.comboBox_name, item.name_id),
                (ui.comboBox_category, item.category_id),
                (ui.comboBox_manufacturer, item.manufacturer_id),
                (ui.comboBox_supplier, item.supplier_id),
                (ui.comboBox_unit, item.unit_id),
            ]:
                idx = combo.findData(fk_id)
                if idx >= 0:
                    combo.setCurrentIndex(idx)
            ui.plainTextEdit_description.setPlainText(item.description or "")
            ui.doubleSpinBox_price.setValue(float(item.price or 0))
            ui.spinBox_quantity.setValue(item.stock_quantity or 0)
            ui.doubleSpinBox_discount.setValue(float(item.discount or 0))
            photo = item.photo
            if photo and os.path.isfile(photo):
                ui.label_photo.setPixmap(QPixmap(photo))
            else:
                ui.label_photo.setPixmap(QPixmap(ASSET_PLACEHOLDER_PNG))
            ui.pushButton_save.clicked.connect(lambda: self.save_item(item))
            ui.pushButton_delete.clicked.connect(lambda: self.delete_item(item))
        ui.pushButton_back.clicked.connect(self.edit_window.close)
        self.edit_window.show()

    def save_item(self, item):
        ui = self.edit_window.ui
        name_id = ui.comboBox_name.currentData()
        if name_id is None:
            QMessageBox.warning(self.edit_window, "Ошибка", "Выберите наименование товара.")
            return
        price = ui.doubleSpinBox_price.value()
        quantity = ui.spinBox_quantity.value()
        discount = ui.doubleSpinBox_discount.value()
        if item is None:
            max_id = session.query(func.max(Product.id)).scalar() or 0
            new_id = max_id + 1
            new_item = Product(
                id=new_id,
                article=str(new_id),
                name_id=name_id,
                category_id=ui.comboBox_category.currentData(),
                description=ui.plainTextEdit_description.toPlainText().strip() or None,
                manufacturer_id=ui.comboBox_manufacturer.currentData(),
                supplier_id=ui.comboBox_supplier.currentData(),
                price=price,
                unit_id=ui.comboBox_unit.currentData(),
                stock_quantity=quantity,
                discount=discount,
                photo=None,
            )
            session.add(new_item)
        else:
            item.name_id = name_id
            item.category_id = ui.comboBox_category.currentData()
            item.description = ui.plainTextEdit_description.toPlainText().strip() or None
            item.manufacturer_id = ui.comboBox_manufacturer.currentData()
            item.supplier_id = ui.comboBox_supplier.currentData()
            item.price = price
            item.unit_id = ui.comboBox_unit.currentData()
            item.stock_quantity = quantity
            item.discount = discount
        session.commit()
        self.edit_window.close()
        self.sort_products()

    def delete_item(self, item):
        reply = QMessageBox.question(
            self.edit_window,
            "Подтверждение удаления",
            f"Вы уверены, что хотите удалить этот товар?",
        )
        if reply != QMessageBox.StandardButton.Yes:
            return
        cnt = session.query(func.count(OrderItem.id)).filter(
            OrderItem.product_id == item.id
        ).scalar()
        if cnt > 0:
            QMessageBox.warning(
                self.edit_window,
                "Удаление невозможно",
                f"Товар присутствует в {cnt} заказе(-ах).\nУдаление запрещено.",
            )
            return
        session.delete(item)
        session.commit()
        self.edit_window.close()
        self.sort_products()


if __name__ == "__main__":
    app = QApplication()
    application = App()
    application.login.show()
    app.exec()
