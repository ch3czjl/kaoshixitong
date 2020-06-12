# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from Ui_aotuexcel import *
from Ui_aotuexcel2 import *
from Ui_aotuexcel3 import *
from Ui_aotuexcel4 import *
from Ui_aotuexcel5 import *
from Ui_aotuexcel6 import *
import smtplib
# 发送字符串的邮件
from email.mime.text import MIMEText
# 处理多种形态的邮件主体我们需要 MIMEMultipart 类
from email.mime.multipart import MIMEMultipart
# 处理图片需要 MIMEImage 类
from email.mime.image import MIMEImage

class MainForm(QMainWindow, Ui_Form0):
    # global mingzi
    # mingzi = ''
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        
        self.pushButton.clicked.connect(self.sendmingzi)
        # 点击actionTst,子窗口就会显示在主窗口的MaingridLayout中
        self.pushButton.clicked.connect(self.childShow)

        self.pushButton_2.clicked.connect(self.closechildShow)
        self.pushButton_2.clicked.connect(self.childShow1)

        self.pushButton_3.clicked.connect(self.closechildShow1)
        self.pushButton_3.clicked.connect(self.childShow2)

        self.pushButton_4.clicked.connect(self.closechildShow2)
        self.pushButton_4.clicked.connect(self.childShow3)

        self.pushButton_5.clicked.connect(self.closechildShow3)
        self.pushButton_5.clicked.connect(self.childShow4)

        self.pushButton_7.clicked.connect(self.sendmail)

    def sendmingzi(self):
        mingzi = self.lineEdit.text()
        print(mingzi)

    def sendmail(self):
        fromaddr = 'pyma95396@163.com'  # 邮件发送方邮箱地址
        password = '92hyw1027'  # 密码(部分邮箱为授权码)
        toaddrs = ['598746155@qq.com', 'pyma95396@163.com']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
        # 设置email信息
        # ---------------------------发送字符串的邮件-----------------------------
        # 邮件内容设置
        strsenlist ='考生信息：' + mingzi + '随机到的题目如下：' + '\n' + str(sendlist) + '\n' + '你的答案是：'+ str(sendAnswerlabel) + '最后得分是： ' + str(score)
        message = MIMEText(strsenlist, 'plain', 'utf-8')
        # 邮件主题
        message['Subject'] = '考试成绩'
        # 发送方信息
        message['From'] = 'pyma95396@163.com'
        # 接受方信息
        message['To'] = '598746155@qq.com,pyma95396@163.com'
        # ---------------------------------------------------------------------


        # 登录并发送邮件
        # try:
        server = smtplib.SMTP('smtp.163.com')  # 163邮箱服务器地址，端口默认为25
        # print('1')
        server.login(fromaddr, password)
        server.sendmail(fromaddr, toaddrs, message.as_string())
        print('success')
        print(score)
        server.quit()



    def childShow(self):
        # 添加子窗口
        self.child = ChildrenForm()
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def closechildShow(self):
        self.MaingridLayout.removeWidget(self.child)
        self.child.close()

    def childShow1(self):
        # 添加子窗口
        self.child = ChildrenForm2()
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def closechildShow1(self):
        self.MaingridLayout.removeWidget(self.child)
        self.child.close()

    def childShow2(self):
        # 添加子窗口
        self.child = ChildrenForm3()
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def closechildShow2(self):
        self.MaingridLayout.removeWidget(self.child)
        self.child.close()

    def childShow3(self):
        # 添加子窗口
        self.child = ChildrenForm4()
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def closechildShow3(self):
        self.MaingridLayout.removeWidget(self.child)
        self.child.close()

    def childShow4(self):
        # 添加子窗口
        self.child = ChildrenForm5()
        self.MaingridLayout.addWidget(self.child)
        self.child.show()

    def closechildShow4(self):
        self.MaingridLayout.removeWidget(self.child)
        self.child.close()



class ChildrenForm(QWidget, Ui_Form1):
    def __init__(self):
        super(ChildrenForm, self).__init__()
        self.setupUi(self)

class ChildrenForm2(QWidget, Ui_Form2):
    def __init__(self):
        super(ChildrenForm2, self).__init__()
        self.setupUi(self)

class ChildrenForm3(QWidget, Ui_Form3):
    def __init__(self):
        super(ChildrenForm3, self).__init__()
        self.setupUi(self)

class ChildrenForm4(QWidget, Ui_Form4):
    def __init__(self):
        super(ChildrenForm4, self).__init__()
        self.setupUi(self)

class ChildrenForm5(QWidget, Ui_Form5):
    def __init__(self):
        super(ChildrenForm5, self).__init__()
        self.setupUi(self)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
