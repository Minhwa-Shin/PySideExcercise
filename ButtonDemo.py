from PySide6.QtWidgets import (QApplication, QWidget, QPushButton,
                               QCheckBox, QRadioButton, QVBoxLayout, QGroupBox)
import sys

class MyForm(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self,parent)
        self.setWindowTitle("Button Demo")

        self.pushButton=QPushButton('&Ok',self)
        self.pushButton.clicked.connect(self.okButtonClicked)

        self.checkBox=QCheckBox('&Case sensitivity',self)
        self.checkBox.toggled.connect(self.onCaseSensitivity)

        box = QGroupBox("Sex",self)
        self.radioButton1=QRadioButton("Male",box)
        self.radioButton2=QRadioButton("Female",box)
        self.radioButton1.setChecked(True)

        groupBoxLayout=QVBoxLayout(box)
        groupBoxLayout.addWidget(self.radioButton1)
        groupBoxLayout.addWidget(self.radioButton2)
        self.radioButton1.toggled.connect(self.onMale)
        self.radioButton2.toggled.connect(self.onFeMale)

        mainLayout=QVBoxLayout()
        mainLayout.addWidget(self.pushButton)
        mainLayout.addWidget(self.checkBox)
        mainLayout.addWidget(box)

        self.setLayout(mainLayout)

    def okButtonClicked(self):
        print('okButtonClicked')

    def onCaseSensitivity(self,toggle):
        print('onCaseSensitivity',toggle)
        print(self.checkBox.isChecked())

    def onMale(self,toggle):
        print('onMale',toggle)

    def onFeMale(self,toggle):
        print('onFeMale',toggle)

if __name__=='__main__':
    app=QApplication(sys.argv)
    form=MyForm()
    form.show()
    app.exec()
