import sys
from PyQt5.QtWidgets import QWidget,QPushButton,QApplication
from PyQt5.QtCore import QCoreApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # 创建按钮
        btn = QPushButton('退出',self)
        # 给按钮绑定操作
        # btn.clicked.connect(QCoreApplication.instance().quit)
        btn.clicked.connect(self.f)  # 整个代码的核心（绑定）

        btn.resize(btn.sizeHint())
        btn.move(50,50)

        self.setGeometry(300,300,250,150)
        self.setWindowTitle('退出按钮')
        self.show()

    def f(self):
        print('您好！')

# 测试
# 当当前模块作为主模块时，才执行下面的代码
if __name__ == "__main__":
    app = QApplication(sys.argv)
    e = Example()
    sys.exit(app.exec_())