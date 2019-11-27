import sys
from PyQt5.QtWidgets import QWidget, QApplication, qApp
from PyQt5.QtCore import Qt
from Ui_weather import Ui_Form
from query import *


class Weather(QWidget, Ui_Form):
    def __init__(self, parent=None):
        # 继承主窗口类
        super(Weather, self).__init__(parent)
        self.setupUi(self)
        self.initUi()

    def initUi(self):
        # 维护一个城市代码字典
        self.table = read_code()
        # 将 textEdit 设置为只读模式
        self.textEdit.setReadOnly(True)
        # 将鼠标焦点放在 lineEdit 编辑栏里
        self.lineEdit.setFocus()

    def queryWeather(self):
        # 获取 lineEdit 中的文本
        city = self.lineEdit.text()
        err_msg = ''
        try:
            code = query_code(self.table, city)
        except KeyError:
            err_msg = '请输入正确的城市名称'

        if not err_msg:
            try:
                info = query_weather(code)
            except requests.ConnectionError:
                err_msg = '请检查网络是否连接正确'

        if not err_msg:
            self.lineEdit.setFocus()
            # 设置文本
            self.textEdit.setText(info)
            # 清空文本
            self.lineEdit.clear()

        else:
            self.lineEdit.setFocus()
            self.textEdit.setText(err_msg)
            self.lineEdit.clear()

    def keyPressEvent(self, e):
        # 设置快捷键
        if e.key() == Qt.Key_Return:
            self.queryWeather()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather = Weather()
    weather.show()
    sys.exit(app.exec_())
