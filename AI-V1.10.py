from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

class Ui_Form(object):
    def __init__(self):
        self.current_directory = os.path.dirname(__file__)
        self.file_name = 'RD.txt'
        self.file_pic = 'pic'
        self.filet_path = os.path.join(self.current_directory, self.file_name)
        self.file_pic_path = os.path.join(self.current_directory, self.file_pic)


    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.setGeometry(200, 200, 870, 320)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 850, 300))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(30, 20, 61, 18))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(470, 20, 101, 18))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_text = QtWidgets.QLabel(self.groupBox)
        self.label_text.setGeometry(QtCore.QRect(650, 20, 61, 18))  # 设置位置和大小
        self.label_text.setText("图片显示")
        self.label_text.setObjectName("text")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(230, 15, 88, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setGeometry(QtCore.QRect(475, 160, 88, 27))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.btn2_click)
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(475, 240, 88, 27))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(QtCore.QCoreApplication.instance().quit)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(475, 120, 88, 27)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.topological)
        self.clearButton = QtWidgets.QPushButton(self.groupBox)
        self.clearButton.setText("刷新页面")
        self.clearButton.setGeometry(QtCore.QRect(475, 200, 88, 27))  # 设置按钮的位置
        self.clearButton.clicked.connect(self.clearTextEdit)
        self.textEdit = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit.setGeometry(QtCore.QRect(20, 60, 80, 211))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.groupBox)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 60, 331, 211))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_2.setReadOnly(True)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.move(460, 80)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setFixedWidth(120)
        self.pushButton.clicked.connect(self.go)
        #图片显示
        self.label_pic = QtWidgets.QLabel(self.groupBox)
        #self.label_pic.setGeometry(QtCore.QRect(520, 20, 240, 320))
        self.label_pic.setGeometry(QtCore.QRect(600, -10, 240, 320))
        self.label_pic.setStyleSheet("image: url(:/pic//01.jpg);")
        self.label_pic.setObjectName("pic")
        pix = QtGui.QPixmap(self.file_pic_path + "/01.jpg")
        pix = pix.scaled(240, 320, QtCore.Qt.KeepAspectRatio)  # 缩放图片
        self.label_pic.setPixmap(pix)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def clearTextEdit(self):
        self.textEdit.clear()
        self.textEdit_2.clear()
        self.lineEdit.clear()
        self.label_pic.clear()

    def btn2_click(self):
        if self.pushButton_2.text() != "确定输入":
            self.pushButton_2.setText("确定输入")
        else:
            self.pushButton_2.setText("修改知识库")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "动物识别系统 24组"))
        self.label.setText(_translate("Form", "输入特征"))
        self.label_2.setText(_translate("Form", "显示推理结果"))
        self.pushButton.setText(_translate("Form", "进行推理"))
        self.pushButton_2.setText(_translate("Form", "修改知识库"))
        self.pushButton_3.setText(_translate("Form", "退出程序"))
        self.pushButton_4.setText(_translate("From", "整理知识库"))

    # 将知识库做拓扑排序
    def topological(self):
        Q = []
        P = []
        ans = ""  # 排序后的结果


        for line in open(self.filet_path, 'r', encoding='utf-8'):
            line = line.strip('\n')
            if line == '':
                continue
            line = line.split(' ')
            Q.append(line[line.__len__() - 1])
            del (line[line.__len__() - 1])
            P.append(line)
        # print('P',P,'\n')
        # print('Q',Q)
        # 计算入度
        inn = []
        for i in P:
            sum = 0
            for x in i:
                if Q.count(x) > 0:  # 能找到，那么
                    sum += Q.count(x)
            inn.append(sum)
        while (1):
            x = 0
            if inn.count(-1) == inn.__len__():
                break
            for i in inn:
                if i == 0:
                    str = ' '.join(P[x])
                    ans = ans + str + " " + Q[x] + "\n"  # 写入结果
                    inn[x] = -1
                    # 更新入度
                    y = 0
                    for j in P:
                        if j.count(Q[x]) == 1:
                            inn[y] -= 1
                        y += 1
                x += 1
        print(ans)
        # 将结果写入文件
        fw = open('RD.txt', 'w', encoding= 'utf-8',buffering=1)
        fw.write(ans)
        fw.flush()
        fw.close()
    # 进行推理
    def go(self, flag=True):
        # 将产生式规则放入规则库中
        # if P then Q
        # 读取产生式文件
        self.Q = []
        self.P = []
               
        with open(self.filet_path, 'r', encoding='utf-8') as fo:
            for line in fo:
                line = line.strip('\n')
                if line == '':
                    continue
                line = line.split(' ')
                self.Q.append(line[line.__len__() - 1])
                del (line[line.__len__() - 1])
                self.P.append(line)
            fo.close()
        print("go按钮按下")
        self.lines = self.textEdit.toPlainText()
        self.lines = self.lines.split('\n')  # 分割成组
        self.DB = set(self.lines)
        print(self.DB)
        self.str = ""
        print(self.str)
        flag = True
        temp = ""
        for x in self.P:  # 对于每条产生式规则
            if ListInSet(x, self.DB):  # 如果所有前提条件都在规则库中
                self.DB.add(self.Q[self.P.index(x)])
                temp = self.Q[self.P.index(x)]
                flag = False  # 至少能推出一个结论
                self.str += "%s --> %s\n" % (x, self.Q[self.P.index(x)])
        if flag:  # 一个结论都推不出
            print("一个结论都推不出")
            for x in self.P:  # 对于每条产生式
                if ListOneInSet(x, self.DB):  # 事实是否满足部分前提
                    flag1 = False       # 默认提问时否认前提
                    for i in x:  # 对于前提中所有元素
                        if i not in self.DB:  # 对于不满足的那部分
                            btn = s.quest("是否" + i)
                            if btn == QtWidgets.QMessageBox.Ok:
                                self.textEdit.setText(self.textEdit.toPlainText() + "\n" + i)  # 确定则增加到textEdit
                                self.DB.add(i)  # 确定则增加到规则库中
                                flag1 = True    # 肯定前提
                    if flag1:  # 如果肯定前提，则重新推导
                        self.go()
                        return
        self.textEdit_2.setPlainText(self.str)
        self.pic = self.str.strip().split('>')
        pic_name = self.pic[-1].strip() + ".jpg"
        pic_path = os.path.join(self.current_directory, "pic", pic_name)
        pix = QtGui.QPixmap(pic_path)
        print(self.pic[-1].strip()+".jpg")
        pix = pix.scaled(240, 320, QtCore.Qt.KeepAspectRatio)  # 缩放图片
        self.label_pic.setPixmap(pix)
        print("----------------------")
        print(self.str)
        if flag:
            btn = s.alert("特征不在规则库中，无法推导出结论！")
        else:
            self.lineEdit.setText(temp)
# 判断list中至少有一个在集合set中
def ListOneInSet(li, se):
    for i in li:
        if i in se:
            return True
    return False
# 判断list中所有元素是否都在集合set中
def ListInSet(li, se):
    for i in li:
        if i not in se:
            return False
    return True
class SecondWindow(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(SecondWindow, self).__init__(parent)
        self.setWindowTitle("修改知识库")
        self.setGeometry(725, 200, 300, 300)
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(8, 2, 284, 286)
    # 警告没有推导结果
    def alert(self, info):
        QtWidgets.QMessageBox.move(self, 200, 200)
        QtWidgets.QMessageBox.information(self, "Information", self.tr(info))
    # 询问补充事实
    def quest(self, info):
        # 如果推理为空，需要询问用户是否要添加已知条件
        QtWidgets.QMessageBox.move(self, 200, 200)
        button = QtWidgets.QMessageBox.question(self, "Question",
         self.tr(info),   QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel,
         QtWidgets.QMessageBox.Cancel)
        return button
    def handle_click(self):
        if not self.isVisible():
            # 读取文件放到多行文本框中
            str = ""
            current_directory = os.path.dirname(__file__)
            file_name = 'RD.txt'
            file_path = os.path.join(current_directory, file_name)

            with open(file_path, 'r', encoding='utf-8')  as fo:
                for line in fo:
                    line = line.strip('\n')
                    if line == '':
                        continue
                    str = str + line + "\n"
            fo.close()
            self.textEdit.setText(str)
            self.show()
        else:
            # 输出文本框内容
            self.str = self.textEdit.toPlainText()
            print(self.str)
            # 将文本框内容写入文件
            self.fw = open('RD.txt', 'w', encoding='utf-8')
            self.fw.write(self.str)
            self.fw.close()  # 关闭文件
            self.close()  # 关闭窗口
    def handle_close(self):
        self.close()
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    s = SecondWindow()
    ui.pushButton_2.clicked.connect(s.handle_click)
    sys.exit(app.exec_())
