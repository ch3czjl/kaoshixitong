# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\python\PyQt5-master\zhangjl\aotuexcel.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import random
import smtplib
# 发送字符串的邮件
from email.mime.text import MIMEText
# 处理多种形态的邮件主体我们需要 MIMEMultipart 类
from email.mime.multipart import MIMEMultipart
# 处理图片需要 MIMEImage 类
from email.mime.image import MIMEImage

df = pd.read_excel('chuntiku.xlsx')
data = df.values
datalist = list(data)
global score
global sendlist
global sendAnswerlabel
sendlist = []
score = 0
sendAnswerlabel = []


class Ui_Form0(object):
    def setupUi(self, Form0):
        Form0.setObjectName("Form0")
        Form0.resize(1106, 895)
        self.gridLayoutWidget = QtWidgets.QWidget(Form0)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(220, 10, 881, 881))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout.setObjectName("MaingridLayout")
        self.label_3 = QtWidgets.QLabel(Form0)
        self.label_3.setGeometry(QtCore.QRect(11, 11, 36, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(Form0)
        self.label_2.setGeometry(QtCore.QRect(11, 37, 60, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form0)
        self.comboBox.setGeometry(QtCore.QRect(77, 37, 62, 20))
        self.comboBox.setEditable(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(Form0)
        self.label.setGeometry(QtCore.QRect(11, 63, 36, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form0)
        self.lineEdit.setGeometry(QtCore.QRect(77, 11, 133, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.comboBox_2 = QtWidgets.QComboBox(Form0)
        self.comboBox_2.setGeometry(QtCore.QRect(77, 63, 50, 20))
        self.comboBox_2.setEditable(True)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.layoutWidget = QtWidgets.QWidget(Form0)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 170, 121, 571))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_5)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_7)

        self.retranslateUi(Form0)
        QtCore.QMetaObject.connectSlotsByName(Form0)

    def retranslateUi(self, Form0):
        _translate = QtCore.QCoreApplication.translate
        Form0.setWindowTitle(_translate("Form0", "赛尔通信运行部上海维护区考试系统V1.0.0"))
        self.label_3.setText(_translate("Form0", "姓名："))
        self.label_2.setText(_translate("Form0", "入职年限："))
        self.comboBox.setItemText(0, _translate("Form0", "1年内"))
        self.comboBox.setItemText(1, _translate("Form0", "1至3年"))
        self.comboBox.setItemText(2, _translate("Form0", "3至5年"))
        self.label.setText(_translate("Form0", "设备："))
        self.comboBox_2.setItemText(0, _translate("Form0", "中兴"))
        self.comboBox_2.setItemText(1, _translate("Form0", "华为"))
        self.pushButton.setText(_translate("Form0", "开始考试"))
        self.pushButton_2.setText(_translate("Form0", "第二页"))
        self.pushButton_3.setText(_translate("Form0", "第三页"))
        self.pushButton_4.setText(_translate("Form0", "第四页"))
        self.pushButton_5.setText(_translate("Form0", "第五页"))
        self.pushButton_7.setText(_translate("Form0", "提交试卷"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form0 = QtWidgets.QWidget()
    ui = Ui_Form0()
    ui.setupUi(Form0)
    Form0.show()
    sys.exit(app.exec_())

