# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_widget_main(object):
    def setupUi(self, widget_main):
        if not widget_main.objectName():
            widget_main.setObjectName(u"widget_main")
        widget_main.resize(925, 521)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(widget_main.sizePolicy().hasHeightForWidth())
        widget_main.setSizePolicy(sizePolicy)
        widget_main.setStyleSheet(u"QPushButton {\n"
"  background-color: rgb(127, 255, 0);\n"
"  color: black;\n"
"}\n"
"QPushButton:hover {\n"
"  background-color: rgb(0, 250, 154);\n"
"  color: black;\n"
"}\n"
"QPushButton:pressed {\n"
"  background-color: rgb(0, 250, 154);\n"
"  color: black;\n"
"}\n"
"\n"
"QWidget {\n"
"  background-color: rgb(255, 255, 255);\n"
"  color: black;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(widget_main)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget_header = QWidget(widget_main)
        self.widget_header.setObjectName(u"widget_header")
        self.horizontalLayout = QHBoxLayout(self.widget_header)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_logo = QLabel(self.widget_header)
        self.label_logo.setObjectName(u"label_logo")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_logo.sizePolicy().hasHeightForWidth())
        self.label_logo.setSizePolicy(sizePolicy1)
        self.label_logo.setMaximumSize(QSize(30, 30))
        self.label_logo.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_logo)

        self.comboBox = QComboBox(self.widget_header)
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setAutoFillBackground(False)

        self.horizontalLayout.addWidget(self.comboBox)

        self.comboBox_2 = QComboBox(self.widget_header)
        self.comboBox_2.setObjectName(u"comboBox_2")
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.comboBox_2)

        self.lineEdit_search = QLineEdit(self.widget_header)
        self.lineEdit_search.setObjectName(u"lineEdit_search")

        self.horizontalLayout.addWidget(self.lineEdit_search)

        self.label_username = QLabel(self.widget_header)
        self.label_username.setObjectName(u"label_username")
        sizePolicy.setHeightForWidth(self.label_username.sizePolicy().hasHeightForWidth())
        self.label_username.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.label_username, 0, Qt.AlignmentFlag.AlignRight)

        self.pushButton_exit = QPushButton(self.widget_header)
        self.pushButton_exit.setObjectName(u"pushButton_exit")
        sizePolicy.setHeightForWidth(self.pushButton_exit.sizePolicy().hasHeightForWidth())
        self.pushButton_exit.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        self.pushButton_exit.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton_exit)


        self.verticalLayout.addWidget(self.widget_header)

        self.widget = QWidget(widget_main)
        self.widget.setObjectName(u"widget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy2)
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.scrollArea = QScrollArea(self.widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QWidget {\n"
"	background-color:  rgb(127, 255, 0);\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 885, 419))
        self.scrollAreaWidgetContents.setStyleSheet(u".scrollArea {  \n"
"background-color: rgb(127, 255, 0);\n"
"}\n"
"")
        self.verticalLayout_card = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_card.setSpacing(4)
        self.verticalLayout_card.setObjectName(u"verticalLayout_card")
        self.verticalLayout_card.setContentsMargins(0, 0, 0, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.widget)

        self.widget_bottom = QWidget(widget_main)
        self.widget_bottom.setObjectName(u"widget_bottom")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_bottom)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pushButton_add = QPushButton(self.widget_bottom)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_add)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButton_clear = QPushButton(self.widget_bottom)
        self.pushButton_clear.setObjectName(u"pushButton_clear")
        self.pushButton_clear.setFont(font)

        self.horizontalLayout_2.addWidget(self.pushButton_clear)


        self.verticalLayout.addWidget(self.widget_bottom)


        self.retranslateUi(widget_main)

        QMetaObject.connectSlotsByName(widget_main)
    # setupUi

    def retranslateUi(self, widget_main):
        widget_main.setWindowTitle(QCoreApplication.translate("widget_main", u"Form", None))
        self.label_logo.setText("")
#if QT_CONFIG(tooltip)
        self.lineEdit_search.setToolTip(QCoreApplication.translate("widget_main", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lineEdit_search.setText("")
        self.lineEdit_search.setPlaceholderText(QCoreApplication.translate("widget_main", u"\u041f\u043e\u0438\u0441\u043a", None))
        self.label_username.setText(QCoreApplication.translate("widget_main", u"username", None))
        self.pushButton_exit.setText(QCoreApplication.translate("widget_main", u"\u0412\u044b\u0445\u043e\u0434", None))
        self.pushButton_add.setText(QCoreApplication.translate("widget_main", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0442\u043e\u0432\u0430\u0440", None))
        self.pushButton_clear.setText(QCoreApplication.translate("widget_main", u"\u041d\u0430\u0437\u0430\u0434", None))
    # retranslateUi

