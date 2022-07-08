## QFileDialog模块学习
import sys
from PyQt5.QtWidgets import QApplication, QFileDialog, QWidget, QPushButton



## QFileDialog用于打开和保存特定的文件
class MainWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        button = QPushButton("选择文件", self) # 创建一个Button并显示"选择文件"

        self.resize(800,600)
        button.clicked.connect(self.onOKClicked) # 点击Button函数链接至一个按钮

    def onOKClicked(self):
        
        '''Using a static function-getOpenFileName'''
        # ## getOpenFileName->三个参数：弹窗标题，初始路径，文件类型
        # ## 支持多类型选择时，中间使用分号隔开
        # ## getOpenFileName返回值为FileName
        # fname, _ = QFileDialog.getOpenFileName(self, "Open file", 'C:/Users\腻味\Desktop\ClashForWindows', "Images(*.jpg *.gif);;Text files (*.txt)") # 选择文件并将选择的文件路径进行返回
        # print(fname)

        # 测试成功
        '''creat our own QFileDialog'''
        fileNames = [] # 首先赋值为empty directory
        dialog = QFileDialog(self)
        ## 同时还包含其他Mode可供选择ExistingFile,Directory
        ## AnyFile甚至式可以选择不存在的文件，常用于设定save as的模式中
        dialog.setFileMode(QFileDialog.AnyFile)
        
        ## 指定打开的文件类型:源代码中添加tr,但查阅相关资料后发现tr可以不适用,且一般情况下不推荐使用
        # 参考文献:https://blog.csdn.net/weixin_41567783/article/details/118416484
        dialog.setNameFilter("Images (*.png *.xpm *.jpg)")
        
        ## 理论上，list仅显示文件名和文件夹列表，而Details同时显示详细信息(文件大小，修改时间等)
        # dialog.setViewMode(QFileDialog.Detail)
        # dialog.setViewMode(QFileDialog.List)

        dialog.setDirectory('C:/Users\腻味\Pictures\Saved Pictures') ## 此函数可以设计打开时的文件夹

        if dialog.exec_():
            fileNames = dialog.selectedFiles()
        print(fileNames)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWidget()
    window.resize(400, 200)
    window.show()

    sys.exit(app.exec_())