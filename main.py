from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import QApplication
from PySide2.QtWidgets import QFileDialog


class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('myui.ui')

        self.ui.encodeButton.clicked.connect(self.encodeFun)
        self.ui.decodeButton.clicked.connect(self.decodeFun)

    def encodeFun(self):
        info = self.ui.originText.toPlainText()
        print('待加密的文本为 ' + info)
        self.ui.originTextDebug.setText('待加密的文本为 ' + info)
        # self.ui.label = int(info) + 1

    def decodeFun(self):
        info = self.ui.encodedText.toPlainText()
        print('待解密的文本为 ' + info)
        self.ui.encodedTextDebug.setText('待解密的文本为 ' + info)

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()
