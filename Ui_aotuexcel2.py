# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\python\PyQt5-master\zhangjl\aotuexcel2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from Ui_aotuexcel import *
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from Ui_aotuexcel import *


def randomText(textArr):
    global randomNumber
    length = len(textArr)
    if length < 1:
        return ''
    if length == 1:
        return textArr[0]
    randomNumber = random.randint(0, length - 1)
    # textArr.del(str(textArr[randomNumber]))
    # textArr.__delattr__(str(textArr[randomNumber]))
    return textArr[randomNumber]

class Ui_Form1(object):
    def setupUi(self, Form1):
        Form1.setObjectName("Form1")
        Form1.resize(886, 900)
        self.pushButton_2 = QtWidgets.QPushButton(Form1)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 860, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayoutWidget = QtWidgets.QWidget(Form1)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 10, 881, 881))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.MaingridLayout2 = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.MaingridLayout2.setContentsMargins(0, 0, 0, 0)
        self.MaingridLayout2.setObjectName("MaingridLayout2")
        self.layoutWidget = QtWidgets.QWidget(Form1)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 39, 731, 841))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout_9.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout.addWidget(self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_2.setObjectName("checkBox_2")
        self.verticalLayout.addWidget(self.checkBox_2)
        self.checkBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.checkBox_4 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_4.setObjectName("checkBox_4")
        self.verticalLayout.addWidget(self.checkBox_4)
        self.verticalLayout_9.addLayout(self.verticalLayout)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_9.addWidget(self.label_2)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox_6 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_6.setObjectName("checkBox_6")
        self.verticalLayout_2.addWidget(self.checkBox_6)
        self.checkBox_8 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_8.setObjectName("checkBox_8")
        self.verticalLayout_2.addWidget(self.checkBox_8)
        self.checkBox_5 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_5.setObjectName("checkBox_5")
        self.verticalLayout_2.addWidget(self.checkBox_5)
        self.checkBox_7 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_7.setObjectName("checkBox_7")
        self.verticalLayout_2.addWidget(self.checkBox_7)
        self.verticalLayout_9.addLayout(self.verticalLayout_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_9.addWidget(self.label_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.checkBox_10 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_10.setObjectName("checkBox_10")
        self.verticalLayout_3.addWidget(self.checkBox_10)
        self.checkBox_12 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_12.setObjectName("checkBox_12")
        self.verticalLayout_3.addWidget(self.checkBox_12)
        self.checkBox_9 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_9.setObjectName("checkBox_9")
        self.verticalLayout_3.addWidget(self.checkBox_9)
        self.checkBox_11 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_11.setObjectName("checkBox_11")
        self.verticalLayout_3.addWidget(self.checkBox_11)
        self.verticalLayout_9.addLayout(self.verticalLayout_3)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_9.addWidget(self.label_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.checkBox_15 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_15.setObjectName("checkBox_15")
        self.verticalLayout_4.addWidget(self.checkBox_15)
        self.checkBox_13 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_13.setObjectName("checkBox_13")
        self.verticalLayout_4.addWidget(self.checkBox_13)
        self.checkBox_14 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_14.setObjectName("checkBox_14")
        self.verticalLayout_4.addWidget(self.checkBox_14)
        self.checkBox_16 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_16.setObjectName("checkBox_16")
        self.verticalLayout_4.addWidget(self.checkBox_16)
        self.verticalLayout_9.addLayout(self.verticalLayout_4)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_9.addWidget(self.label_5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.checkBox_20 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_20.setObjectName("checkBox_20")
        self.verticalLayout_5.addWidget(self.checkBox_20)
        self.checkBox_18 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_18.setObjectName("checkBox_18")
        self.verticalLayout_5.addWidget(self.checkBox_18)
        self.checkBox_19 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_19.setObjectName("checkBox_19")
        self.verticalLayout_5.addWidget(self.checkBox_19)
        self.checkBox_17 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_17.setObjectName("checkBox_17")
        self.verticalLayout_5.addWidget(self.checkBox_17)
        self.verticalLayout_9.addLayout(self.verticalLayout_5)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_9.addWidget(self.label_6)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.checkBox_24 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_24.setObjectName("checkBox_24")
        self.verticalLayout_6.addWidget(self.checkBox_24)
        self.checkBox_23 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_23.setObjectName("checkBox_23")
        self.verticalLayout_6.addWidget(self.checkBox_23)
        self.checkBox_21 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_21.setObjectName("checkBox_21")
        self.verticalLayout_6.addWidget(self.checkBox_21)
        self.checkBox_22 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_22.setObjectName("checkBox_22")
        self.verticalLayout_6.addWidget(self.checkBox_22)
        self.verticalLayout_9.addLayout(self.verticalLayout_6)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_9.addWidget(self.label_7)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.checkBox_27 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_27.setObjectName("checkBox_27")
        self.verticalLayout_7.addWidget(self.checkBox_27)
        self.checkBox_26 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_26.setObjectName("checkBox_26")
        self.verticalLayout_7.addWidget(self.checkBox_26)
        self.checkBox_28 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_28.setObjectName("checkBox_28")
        self.verticalLayout_7.addWidget(self.checkBox_28)
        self.checkBox_25 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_25.setObjectName("checkBox_25")
        self.verticalLayout_7.addWidget(self.checkBox_25)
        self.verticalLayout_9.addLayout(self.verticalLayout_7)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_9.addWidget(self.label_8)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.checkBox_32 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_32.setObjectName("checkBox_32")
        self.verticalLayout_8.addWidget(self.checkBox_32)
        self.checkBox_30 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_30.setObjectName("checkBox_30")
        self.verticalLayout_8.addWidget(self.checkBox_30)
        self.checkBox_29 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_29.setObjectName("checkBox_29")
        self.verticalLayout_8.addWidget(self.checkBox_29)
        self.checkBox_31 = QtWidgets.QCheckBox(self.layoutWidget)
        self.checkBox_31.setObjectName("checkBox_31")
        self.verticalLayout_8.addWidget(self.checkBox_31)
        self.verticalLayout_9.addLayout(self.verticalLayout_8)

        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form1", "赛尔通信运行部上海维护区考试系统V1.0.0"))
        self.pushButton_2.setText(_translate("Form1", "1/5"))

        # sendlist = []
        # score = 0
        # sendAnswerlabel = []

        randlist = randomText(data)
        if randomNumber < len(datalist):  # 消除bug：IndexError: list index out of range
            datalist.pop(randomNumber)
        self.label.setText(_translate("Form1", randlist[0]))
        self.checkBox_3.setText(_translate("Form1", randlist[2]))
        self.checkBox_2.setText(_translate("Form1", randlist[3]))
        self.checkBox.setText(_translate("Form1", randlist[4]))
        self.checkBox_4.setText(_translate("Form1", randlist[5]))
        Answerlabel = ''
        if self.checkBox.checkState():
            Answerlabel = 'A'
        if self.checkBox_2.checkState():
            Answerlabel = Answerlabel + 'B'
        if self.checkBox_3.checkState():
            Answerlabel = Answerlabel + 'C'
        if self.checkBox_4.checkState():
            Answerlabel = Answerlabel + 'D'
        if Answerlabel == randlist[1]:
            score = score + 1
        sendlist.append(randlist)
        sendAnswerlabel.append(Answerlabel)

        randlist = randomText(data)
        if randomNumber < len(datalist):  # 消除bug：IndexError: list index out of range
            datalist.pop(randomNumber)
        self.label_2.setText(_translate("Form1", randlist[0]))
        self.checkBox_6.setText(_translate("Form1", randlist[2]))
        self.checkBox_8.setText(_translate("Form1", randlist[3]))
        self.checkBox_5.setText(_translate("Form1", randlist[4]))
        self.checkBox_7.setText(_translate("Form1", randlist[5]))
        Answerlabel = ''
        if self.checkBox.checkState():
            Answerlabel = 'A'
        if self.checkBox_2.checkState():
            Answerlabel = Answerlabel + 'B'
        if self.checkBox_3.checkState():
            Answerlabel = Answerlabel + 'C'
        if self.checkBox_4.checkState():
            Answerlabel = Answerlabel + 'D'
        if Answerlabel == randlist[1]:
            score = score + 1
        sendlist.append(randlist)
        sendAnswerlabel.append(Answerlabel)

        randlist = randomText(data)
        if randomNumber < len(datalist):  # 消除bug：IndexError: list index out of range
            datalist.pop(randomNumber)
        self.label_3.setText(_translate("Form1", randlist[0]))
        self.checkBox_10.setText(_translate("Form1", randlist[2]))
        self.checkBox_12.setText(_translate("Form1", randlist[3]))
        self.checkBox_9.setText(_translate("Form1", randlist[4]))
        self.checkBox_11.setText(_translate("Form1", randlist[5]))
        Answerlabel = ''
        if self.checkBox.checkState():
            Answerlabel = 'A'
        if self.checkBox_2.checkState():
            Answerlabel = Answerlabel + 'B'
        if self.checkBox_3.checkState():
            Answerlabel = Answerlabel + 'C'
        if self.checkBox_4.checkState():
            Answerlabel = Answerlabel + 'D'
        if Answerlabel == randlist[1]:
            score = score + 1
        sendlist.append(randlist)
        sendAnswerlabel.append(Answerlabel)

        randlist = randomText(data)
        if randomNumber < len(datalist):  # 消除bug：IndexError: list index out of range
            datalist.pop(randomNumber)
        self.label_4.setText(_translate("Form1", randlist[0]))
        self.checkBox_15.setText(_translate("Form1", randlist[2]))
        self.checkBox_13.setText(_translate("Form1", randlist[3]))
        self.checkBox_14.setText(_translate("Form1", randlist[4]))
        self.checkBox_16.setText(_translate("Form1", randlist[5]))
        Answerlabel = ''
        if self.checkBox.checkState():
            Answerlabel = 'A'
        if self.checkBox_2.checkState():
            Answerlabel = Answerlabel + 'B'
        if self.checkBox_3.checkState():
            Answerlabel = Answerlabel + 'C'
        if self.checkBox_4.checkState():
            Answerlabel = Answerlabel + 'D'
        if Answerlabel == randlist[1]:
            score = score + 1
        sendlist.append(randlist)
        sendAnswerlabel.append(Answerlabel)

        randlist = randomText(data)
        if randomNumber < len(datalist):  # 消除bug：IndexError: list index out of range
            datalist.pop(randomNumber)
        self.label_5.setText(_translate("Form1", randlist[0]))
        self.checkBox_20.setText(_translate("Form1", randlist[2]))
        self.checkBox_18.setText(_translate("Form1", randlist[3]))
        self.checkBox_19.setText(_translate("Form1", randlist[4]))
        self.checkBox_17.setText(_translate("Form1", randlist[5]))
        Answerlabel = ''
        if self.checkBox.checkState():
            Answerlabel = 'A'
        if self.checkBox_2.checkState():
            Answerlabel = Answerlabel + 'B'
        if self.checkBox_3.checkState():
            Answerlabel = Answerlabel + 'C'
        if self.checkBox_4.checkState():
            Answerlabel = Answerlabel + 'D'
        if Answerlabel == randlist[1]:
            score = score + 1
        sendlist.append(randlist)
        sendAnswerlabel.append(Answerlabel)

        randlist = randomText(data)
        if randomNumber < len(datalist):  # 消除bug：IndexError: list index out of range
            datalist.pop(randomNumber)
        self.label_6.setText(_translate("Form1", randlist[0]))
        self.checkBox_24.setText(_translate("Form1", randlist[2]))
        self.checkBox_23.setText(_translate("Form1", randlist[3]))
        self.checkBox_21.setText(_translate("Form1", randlist[4]))
        self.checkBox_22.setText(_translate("Form1", randlist[5]))
        Answerlabel = ''
        if self.checkBox.checkState():
            Answerlabel = 'A'
        if self.checkBox_2.checkState():
            Answerlabel = Answerlabel + 'B'
        if self.checkBox_3.checkState():
            Answerlabel = Answerlabel + 'C'
        if self.checkBox_4.checkState():
            Answerlabel = Answerlabel + 'D'
        if Answerlabel == randlist[1]:
            score = score + 1
        sendlist.append(randlist)
        sendAnswerlabel.append(Answerlabel)

        randlist = randomText(data)
        if randomNumber < len(datalist):  # 消除bug：IndexError: list index out of range
            datalist.pop(randomNumber)
        self.label_7.setText(_translate("Form1", randlist[0]))
        self.checkBox_27.setText(_translate("Form1", randlist[2]))
        self.checkBox_26.setText(_translate("Form1", randlist[3]))
        self.checkBox_28.setText(_translate("Form1", randlist[4]))
        self.checkBox_25.setText(_translate("Form1", randlist[5]))
        Answerlabel = ''
        if self.checkBox.checkState():
            Answerlabel = 'A'
        if self.checkBox_2.checkState():
            Answerlabel = Answerlabel + 'B'
        if self.checkBox_3.checkState():
            Answerlabel = Answerlabel + 'C'
        if self.checkBox_4.checkState():
            Answerlabel = Answerlabel + 'D'
        if Answerlabel == randlist[1]:
            score = score + 1
        sendlist.append(randlist)
        sendAnswerlabel.append(Answerlabel)

        randlist = randomText(data)
        if randomNumber < len(datalist):  # 消除bug：IndexError: list index out of range
            datalist.pop(randomNumber)
        self.label_8.setText(_translate("Form1", randlist[0]))
        self.checkBox_32.setText(_translate("Form1", randlist[2]))
        self.checkBox_30.setText(_translate("Form1", randlist[3]))
        self.checkBox_29.setText(_translate("Form1", randlist[4]))
        self.checkBox_31.setText(_translate("Form1", randlist[5]))
        Answerlabel = ''
        if self.checkBox.checkState():
            Answerlabel = 'A'
        if self.checkBox_2.checkState():
            Answerlabel = Answerlabel + 'B'
        if self.checkBox_3.checkState():
            Answerlabel = Answerlabel + 'C'
        if self.checkBox_4.checkState():
            Answerlabel = Answerlabel + 'D'
        if Answerlabel == randlist[1]:
            score = score + 1
        sendlist.append(randlist)
        sendAnswerlabel.append(Answerlabel)

# class MainForm(QMainWindow, Ui_Form1):
#     def __init__(self):
#         super(MainForm, self).__init__()
#         self.setupUi(self)
#
#         self.child = ChildrenForm()#实例
#         # 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中
#         self.pushButton_2.clicked.connect(self.childShow)
#
#     def childShow(self):
#         # 添加子窗口
#         self.MaingridLayout2.addWidget(self.child)
#         self.child.show()
#
# class ChildrenForm(QWidget, Ui_Form2):
#     def __init__(self):
#         super(ChildrenForm, self).__init__()
#         self.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form1 = QtWidgets.QWidget()
    ui = Ui_Form1()
    ui.setupUi(Form1)
    Form1.show()
    sys.exit(app.exec_())

