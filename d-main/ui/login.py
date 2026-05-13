# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_widget_login(object):
    def setupUi(self, widget_login):
        if not widget_login.objectName():
            widget_login.setObjectName(u"widget_login")
        widget_login.resize(291, 142)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_login.sizePolicy().hasHeightForWidth())
        widget_login.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(widget_login)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_logo = QLabel(widget_login)
        self.label_logo.setObjectName(u"label_logo")
        self.label_logo.setMinimumSize(QSize(120, 100))
        self.label_logo.setMaximumSize(QSize(200, 150))
        self.label_logo.setScaledContents(True)
        self.label_logo.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_logo, 0, Qt.AlignmentFlag.AlignHCenter)

        self.widget = QWidget(widget_login)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lineEdit_login = QLineEdit(self.widget)
        self.lineEdit_login.setObjectName(u"lineEdit_login")

        self.verticalLayout_2.addWidget(self.lineEdit_login)

        self.lineEdit_password = QLineEdit(self.widget)
        self.lineEdit_password.setObjectName(u"lineEdit_password")
        self.lineEdit_password.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_2.addWidget(self.lineEdit_password)


        self.verticalLayout.addWidget(self.widget, 0, Qt.AlignmentFlag.AlignVCenter)

        self.widget_buttons = QWidget(widget_login)
        self.widget_buttons.setObjectName(u"widget_buttons")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.widget_buttons.sizePolicy().hasHeightForWidth())
        self.widget_buttons.setSizePolicy(sizePolicy1)
        self.horizontalLayout = QHBoxLayout(self.widget_buttons)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_login = QPushButton(self.widget_buttons)
        self.pushButton_login.setObjectName(u"pushButton_login")
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        self.pushButton_login.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_login)

        self.pushButton_guest = QPushButton(self.widget_buttons)
        self.pushButton_guest.setObjectName(u"pushButton_guest")
        self.pushButton_guest.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_guest)

        self.pushButton_exit = QPushButton(self.widget_buttons)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        self.pushButton_exit.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_exit)


        self.verticalLayout.addWidget(self.widget_buttons)


        self.retranslateUi(widget_login)

        QMetaObject.connectSlotsByName(widget_login)
    # setupUi

    def retranslateUi(self, widget_login):
        widget_login.setWindowTitle(QCoreApplication.translate("widget_login", u"Form", None))
        self.label_logo.setText("")
        self.lineEdit_login.setText("")
        self.lineEdit_login.setPlaceholderText(QCoreApplication.translate("widget_login", u"\u041b\u043e\u0433\u0438\u043d", None))
        self.lineEdit_password.setText("")
        self.lineEdit_password.setPlaceholderText(QCoreApplication.translate("widget_login", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pushButton_login.setText(QCoreApplication.translate("widget_login", u"\u0412\u0445\u043e\u0434", None))
        self.pushButton_guest.setText(QCoreApplication.translate("widget_login", u"\u0413\u043e\u0441\u0442\u044c", None))
        self.pushButton_exit.setText(QCoreApplication.translate("widget_login", u"\u0412\u044b\u0445\u043e\u0434", None))
    # retranslateUi

