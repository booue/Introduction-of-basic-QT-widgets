import sys
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QPushButton


class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        button = QPushButton("OK", self) ## 界面中设置一个Button

        self.resize(800, 600)
        button.clicked.connect(self.onOKClicked)

    def onOKClicked(self):
        # button = QMessageBox.question(self, "MessageBox Title", "是否确定关闭？", QMessageBox.Ok | QMessageBox.Cancel, QMessageBox.Ok)
        # if button == QMessageBox.Ok:
        #     print("select Ok Button")

        '''借助于性质函数进行实例化'''
        # msgBox = QMessageBox() # 实例化
        # msgBox.setText("The document has been modified.") # 窗口信息显示
        # msgBox.exec() # 窗口调用

        msgBox = QMessageBox()
        ## 显示信息
        msgBox.setText("The document has been modified.")
        msgBox.setInformativeText("Do you want to save your changes?")
        ## 小界面中设置Button
        msgBox.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
        msgBox.setDefaultButton(QMessageBox.Save)
        
        # 设置详细信息的显示，会自动添加Button按钮
        msgBox.setDetailedText("这是一个测试用例\n用于测试setDetailedText的具体用法")

        ## ret本质上会返回用户选择的按钮
        ret = msgBox.exec()
        print(ret == QMessageBox.Save)
        

        '''借助于静态函数进行实例化'''
        # ## warning的弹出框
        # ret = QMessageBox.warning(self, "Warning Message",
        #                        "The document has been modified.\n Do you want to save your changes?",
        #                        QMessageBox.Save | QMessageBox.Discard
        #                        | QMessageBox.Cancel,
        #                        QMessageBox.Save)
        
        # ## information的弹出框
        # ret = QMessageBox.information(self, "Information Message",
        #                        "The document has been modified.\n Do you want to save your changes?",
        #                        QMessageBox.Save | QMessageBox.Discard
        #                        | QMessageBox.Cancel,
        #                        QMessageBox.Save)
        
        # # ## question的弹出框 
        # ret = QMessageBox.question(self, "Question Message",
        #                        "The document has been modified.\n Do you want to save your changes?",
        #                        QMessageBox.Save | QMessageBox.Discard
        #                        | QMessageBox.Cancel,
        #                        QMessageBox.Save)
        
        # ## critical的弹出框
        # ret = QMessageBox.critical(self, "critical Message",
        #                        "The document has been modified.\n Do you want to save your changes?",
        #                        QMessageBox.Save | QMessageBox.Discard
        #                        | QMessageBox.Cancel,
        #                        QMessageBox.Save)
        # print(type(ret))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())