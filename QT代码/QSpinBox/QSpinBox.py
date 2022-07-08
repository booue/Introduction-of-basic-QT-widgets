import sys
from PyQt5.QtWidgets import QApplication, QSpinBox, QWidget


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        
        spinBox = QSpinBox(self)
        ## SpinBox各种方法测试
        spinBox.setMinimum(10)
        spinBox.setMaximum(20)
        ## 设置调整的步长
        spinBox.setSingleStep(2)

        ## 循环操作
        spinBox.setWrapping(True)

        ## valueChanged信号函数
        spinBox.valueChanged.connect(self.onValueChanged)

    ## 将选择的数据进行返回
    def onValueChanged(self, value):
        print("current value is {0}".format(value))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())