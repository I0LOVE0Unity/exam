# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QFrame, QHBoxLayout, QLabel, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_widget_edit(object):
    def setupUi(self, widget_edit):
        if not widget_edit.objectName():
            widget_edit.setObjectName(u"widget_edit")
        widget_edit.resize(480, 640)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        widget_edit.setFont(font)
        self.verticalLayout = QVBoxLayout(widget_edit)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_id = QLabel(widget_edit)
        self.label_id.setObjectName(u"label_id")

        self.verticalLayout.addWidget(self.label_id)

        self.widget_photo = QWidget(widget_edit)
        self.widget_photo.setObjectName(u"widget_photo")
        self.horizontalLayout_photo = QHBoxLayout(self.widget_photo)
        self.horizontalLayout_photo.setObjectName(u"horizontalLayout_photo")
        self.label_photo = QLabel(self.widget_photo)
        self.label_photo.setObjectName(u"label_photo")
        self.label_photo.setMinimumSize(QSize(150, 100))
        self.label_photo.setMaximumSize(QSize(150, 100))
        self.label_photo.setScaledContents(True)
        self.label_photo.setFrameShape(QFrame.Shape.Box)

        self.horizontalLayout_photo.addWidget(self.label_photo)

        self.pushButton_photo = QPushButton(self.widget_photo)
        self.pushButton_photo.setObjectName(u"pushButton_photo")
        self.pushButton_photo.setFont(font)
        self.pushButton_photo.setEnabled(False)

        self.horizontalLayout_photo.addWidget(self.pushButton_photo)


        self.verticalLayout.addWidget(self.widget_photo)

        self.widget_form = QWidget(widget_edit)
        self.widget_form.setObjectName(u"widget_form")
        self.formLayout = QFormLayout(self.widget_form)
        self.formLayout.setObjectName(u"formLayout")
        self.label_l_name = QLabel(self.widget_form)
        self.label_l_name.setObjectName(u"label_l_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_l_name)

        self.comboBox_name = QComboBox(self.widget_form)
        self.comboBox_name.setObjectName(u"comboBox_name")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox_name)

        self.label_l_category = QLabel(self.widget_form)
        self.label_l_category.setObjectName(u"label_l_category")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_l_category)

        self.comboBox_category = QComboBox(self.widget_form)
        self.comboBox_category.setObjectName(u"comboBox_category")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox_category)

        self.label_l_description = QLabel(self.widget_form)
        self.label_l_description.setObjectName(u"label_l_description")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_l_description)

        self.plainTextEdit_description = QPlainTextEdit(self.widget_form)
        self.plainTextEdit_description.setObjectName(u"plainTextEdit_description")
        self.plainTextEdit_description.setMaximumSize(QSize(16777215, 80))

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.plainTextEdit_description)

        self.label_l_manufacturer = QLabel(self.widget_form)
        self.label_l_manufacturer.setObjectName(u"label_l_manufacturer")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_l_manufacturer)

        self.comboBox_manufacturer = QComboBox(self.widget_form)
        self.comboBox_manufacturer.setObjectName(u"comboBox_manufacturer")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.comboBox_manufacturer)

        self.label_l_supplier = QLabel(self.widget_form)
        self.label_l_supplier.setObjectName(u"label_l_supplier")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_l_supplier)

        self.comboBox_supplier = QComboBox(self.widget_form)
        self.comboBox_supplier.setObjectName(u"comboBox_supplier")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.comboBox_supplier)

        self.label_l_price = QLabel(self.widget_form)
        self.label_l_price.setObjectName(u"label_l_price")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_l_price)

        self.doubleSpinBox_price = QDoubleSpinBox(self.widget_form)
        self.doubleSpinBox_price.setObjectName(u"doubleSpinBox_price")
        self.doubleSpinBox_price.setMinimum(0.000000000000000)
        self.doubleSpinBox_price.setMaximum(9999999.990000000223517)
        self.doubleSpinBox_price.setDecimals(2)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_price)

        self.label_l_unit = QLabel(self.widget_form)
        self.label_l_unit.setObjectName(u"label_l_unit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.label_l_unit)

        self.comboBox_unit = QComboBox(self.widget_form)
        self.comboBox_unit.setObjectName(u"comboBox_unit")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.comboBox_unit)

        self.label_l_quantity = QLabel(self.widget_form)
        self.label_l_quantity.setObjectName(u"label_l_quantity")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.label_l_quantity)

        self.spinBox_quantity = QSpinBox(self.widget_form)
        self.spinBox_quantity.setObjectName(u"spinBox_quantity")
        self.spinBox_quantity.setMinimum(0)
        self.spinBox_quantity.setMaximum(9999999)

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.spinBox_quantity)

        self.label_l_discount = QLabel(self.widget_form)
        self.label_l_discount.setObjectName(u"label_l_discount")

        self.formLayout.setWidget(8, QFormLayout.ItemRole.LabelRole, self.label_l_discount)

        self.doubleSpinBox_discount = QDoubleSpinBox(self.widget_form)
        self.doubleSpinBox_discount.setObjectName(u"doubleSpinBox_discount")
        self.doubleSpinBox_discount.setMinimum(0.000000000000000)
        self.doubleSpinBox_discount.setMaximum(100.000000000000000)
        self.doubleSpinBox_discount.setDecimals(2)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox_discount)


        self.verticalLayout.addWidget(self.widget_form)

        self.widget_buttons = QWidget(widget_edit)
        self.widget_buttons.setObjectName(u"widget_buttons")
        self.horizontalLayout_buttons = QHBoxLayout(self.widget_buttons)
        self.horizontalLayout_buttons.setObjectName(u"horizontalLayout_buttons")
        self.pushButton_save = QPushButton(self.widget_buttons)
        self.pushButton_save.setObjectName(u"pushButton_save")
        self.pushButton_save.setFont(font)

        self.horizontalLayout_buttons.addWidget(self.pushButton_save)

        self.pushButton_delete = QPushButton(self.widget_buttons)
        self.pushButton_delete.setObjectName(u"pushButton_delete")
        self.pushButton_delete.setFont(font)

        self.horizontalLayout_buttons.addWidget(self.pushButton_delete)

        self.pushButton_back = QPushButton(self.widget_buttons)
        self.pushButton_back.setObjectName(u"pushButton_back")
        self.pushButton_back.setFont(font)

        self.horizontalLayout_buttons.addWidget(self.pushButton_back)


        self.verticalLayout.addWidget(self.widget_buttons)


        self.retranslateUi(widget_edit)

        QMetaObject.connectSlotsByName(widget_edit)
    # setupUi

    def retranslateUi(self, widget_edit):
        widget_edit.setWindowTitle(QCoreApplication.translate("widget_edit", u"\u0420\u0435\u0434\u0430\u043a\u0442\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_id.setText(QCoreApplication.translate("widget_edit", u"ID: \u2014", None))
        self.label_photo.setText("")
        self.pushButton_photo.setText(QCoreApplication.translate("widget_edit", u"\u0417\u0430\u0433\u0440\u0443\u0437\u0438\u0442\u044c \u0444\u043e\u0442\u043e", None))
        self.label_l_name.setText(QCoreApplication.translate("widget_edit", u"\u041d\u0430\u0438\u043c\u0435\u043d\u043e\u0432\u0430\u043d\u0438\u0435:", None))
        self.label_l_category.setText(QCoreApplication.translate("widget_edit", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f:", None))
        self.label_l_description.setText(QCoreApplication.translate("widget_edit", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435:", None))
        self.label_l_manufacturer.setText(QCoreApplication.translate("widget_edit", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c:", None))
        self.label_l_supplier.setText(QCoreApplication.translate("widget_edit", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a:", None))
        self.label_l_price.setText(QCoreApplication.translate("widget_edit", u"\u0426\u0435\u043d\u0430 (\u20bd):", None))
        self.label_l_unit.setText(QCoreApplication.translate("widget_edit", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f:", None))
        self.label_l_quantity.setText(QCoreApplication.translate("widget_edit", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435:", None))
        self.label_l_discount.setText(QCoreApplication.translate("widget_edit", u"\u0421\u043a\u0438\u0434\u043a\u0430 (%):", None))
        self.pushButton_save.setText(QCoreApplication.translate("widget_edit", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
        self.pushButton_delete.setText(QCoreApplication.translate("widget_edit", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton_back.setText(QCoreApplication.translate("widget_edit", u"\u041d\u0430\u0437\u0430\u0434 \u043a \u043a\u0430\u0442\u0430\u043b\u043e\u0433\u0443 \u0442\u043e\u0432\u0430\u0440\u043e\u0432", None))
    # retranslateUi

