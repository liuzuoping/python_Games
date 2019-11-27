import math
import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, qApp, QMessageBox
from PyQt5.QtCore import Qt
from sample import Ui_Form


# 继承至界面文件的主窗口类
class MyMainWindow(QMainWindow, Ui_Form):
    # 生成随机数的右界
    random_choice = [i * 100 for i in range(1, 20)]

    def __init__(self, parent=None):
        # 继承主窗口类
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        # 随机数的右界
        self.guess_range = None
        # 生成的随机数
        self.guess_num = None
        # 提示范围的左界
        self.left = None
        # 提示范围的右界
        self.right = None
        # 产生随机数
        self.random_num()
        # 初始化功能
        self.initUi()

    def init_range(self):
        # 为随机数的左右界赋值
        self.left = 1
        self.right = self.guess_range

    @property
    def _random_range(self):
        # 随机产生随机数的右界
        return random.choice(self.random_choice)

    def random_num(self):
        self.guess_range = self._random_range
        # 产生随机数
        self.guess_num = random.randint(1, self.guess_range)
        self.init_range()

    def initUi(self):
        # 提示数值范围
        self.label.setText('数值的范围是：{}-{}'.format(self.left, self.right))
        # 按下按钮一，运行 self.guess 函数
        self.pushButton.clicked.connect(self.guess)
        # 按下按钮二，运行 quit 函数
        self.pushButton_2.clicked.connect(qApp.quit)
        # 按下按钮三，运行 self.reset 函数
        self.pushButton_3.clicked.connect(self.reset)

    def guess(self):
        # text 接受文本框中的文本
        text = self.lineEdit.text()
        # 异常处理
        # 可处理数值型字符串，其他输入提示错误
        try:
            text = float(text)
        except:
            self.label.setText('     输入不合法')
            self.label_2.setText('数值的范围:{}-{}'.format(self.left, self.right))
            self.lineEdit.clear()
            text = ''
        # 文本不为空继续执行文件
        if text:
            num = math.floor(text)
            if self.guess_num == num:
                QMessageBox.question(self, '胜利', '恭喜你猜中了：{}'.format(self.guess_num), QMessageBox.Yes)
                self.reset()

            elif self.guess_num > num:
                if num > self.left:
                    self.left = num
                self.label.setText('数值的范围:{}-{}'.format(self.left, self.right))
                self.label_2.setText('      猜小了')

            elif self.guess_num < num:
                if num < self.right:
                    self.right = num
                self.label.setText('数值的范围:{}-{}'.format(self.left, self.right))
                self.label_2.setText('       猜大了')
            self.lineEdit.clear()

    def reset(self):
        # 重置游戏
        self.guess_range = None
        self.guess_num = None
        self.left = None
        self.right = None
        self.random_num()
        self.label.setText('')
        self.label_2.setText('')
        self.initUi()

    def keyPressEvent(self, e):
        # 设置快捷键
        if e.key() == Qt.Key_Return:
            self.guess()
        elif e.key() == Qt.Key_Escape:
            qApp.quit()
        elif e.key() == Qt.Key_R:
            self.reset()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())