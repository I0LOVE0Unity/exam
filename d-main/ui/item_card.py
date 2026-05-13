# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'item_card.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_widget_card(object):
    def setupUi(self, widget_card):
        if not widget_card.objectName():
            widget_card.setObjectName(u"widget_card")
        widget_card.resize(529, 160)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_card.sizePolicy().hasHeightForWidth())
        widget_card.setSizePolicy(sizePolicy)
        widget_card.setStyleSheet(u"	background-color: rgb(255, 255, 255);")
        self.horizontalLayout = QHBoxLayout(widget_card)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(widget_card)
        self.widget.setObjectName(u"widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy1)
        self.widget.setMinimumSize(QSize(130, 160))
        self.widget.setMaximumSize(QSize(130, 160))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_image = QLabel(self.widget)
        self.label_image.setObjectName(u"label_image")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_image.sizePolicy().hasHeightForWidth())
        self.label_image.setSizePolicy(sizePolicy2)
        self.label_image.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_image, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(widget_card)
        self.widget_2.setObjectName(u"widget_2")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        self.widget_2.setFont(font)
        self.verticalLayout = QVBoxLayout(self.widget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_category_plus_name = QLabel(self.widget_2)
        self.label_category_plus_name.setObjectName(u"label_category_plus_name")
        self.label_category_plus_name.setFont(font)

        self.verticalLayout.addWidget(self.label_category_plus_name)

        self.label_description = QLabel(self.widget_2)
        self.label_description.setObjectName(u"label_description")
        self.label_description.setFont(font)

        self.verticalLayout.addWidget(self.label_description)

        self.label_manufacturer = QLabel(self.widget_2)
        self.label_manufacturer.setObjectName(u"label_manufacturer")
        self.label_manufacturer.setFont(font)

        self.verticalLayout.addWidget(self.label_manufacturer)

        self.label_2 = QLabel(self.widget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.verticalLayout.addWidget(self.label_2)

        self.label_price = QLabel(self.widget_2)
        self.label_price.setObjectName(u"label_price")
        self.label_price.setFont(font)

        self.verticalLayout.addWidget(self.label_price)

        self.label_1 = QLabel(self.widget_2)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setFont(font)

        self.verticalLayout.addWidget(self.label_1)

        self.label_count = QLabel(self.widget_2)
        self.label_count.setObjectName(u"label_count")
        self.label_count.setFont(font)

        self.verticalLayout.addWidget(self.label_count)


        self.horizontalLayout.addWidget(self.widget_2)

        self.widget_right = QWidget(widget_card)
        self.widget_right.setObjectName(u"widget_right")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.widget_right.sizePolicy().hasHeightForWidth())
        self.widget_right.setSizePolicy(sizePolicy3)
        self.widget_right.setMinimumSize(QSize(120, 160))
        self.widget_right.setFont(font)
        self.horizontalLayout_3 = QHBoxLayout(self.widget_right)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_discount = QLabel(self.widget_right)
        self.label_discount.setObjectName(u"label_discount")
        self.label_discount.setStyleSheet(u"color: rgb(0, 0, 0);")

        self.horizontalLayout_3.addWidget(self.label_discount, 0, Qt.AlignmentFlag.AlignHCenter)


        self.horizontalLayout.addWidget(self.widget_right)


        self.retranslateUi(widget_card)

        QMetaObject.connectSlotsByName(widget_card)
    # setupUi

    def retranslateUi(self, widget_card):
        widget_card.setWindowTitle(QCoreApplication.translate("widget_card", u"Form", None))
        self.label_image.setText(QCoreApplication.translate("widget_card", u"Image", None))
        self.label_category_plus_name.setText(QCoreApplication.translate("widget_card", u"\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f \u0442\u043e\u0432\u0430\u0440\u0430 | \u0418\u043c\u044f \u0442\u043e\u0432\u0430\u0440\u0430", None))
        self.label_description.setText(QCoreApplication.translate("widget_card", u"\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0442\u043e\u0432\u0430\u0440\u0430:", None))
        self.label_manufacturer.setText(QCoreApplication.translate("widget_card", u"\u041f\u0440\u043e\u0438\u0437\u0432\u043e\u0434\u0438\u0442\u0435\u043b\u044c:", None))
        self.label_2.setText(QCoreApplication.translate("widget_card", u"\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a:", None))
        self.label_price.setText(QCoreApplication.translate("widget_card", u"\u0426\u0435\u043d\u0430:", None))
        self.label_1.setText(QCoreApplication.translate("widget_card", u"\u0415\u0434\u0438\u043d\u0438\u0446\u0430 \u0438\u0437\u043c\u0435\u0440\u0435\u043d\u0438\u044f:", None))
        self.label_count.setText(QCoreApplication.translate("widget_card", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043d\u0430 \u0441\u043a\u043b\u0430\u0434\u0435:", None))
        self.label_discount.setText(QCoreApplication.translate("widget_card", u"Скидка: 0%", None))
    # retranslateUi

