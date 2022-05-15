from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QDialog


class InstructionsDialog(QDialog):
    def __init__(self):
        super(InstructionsDialog, self).__init__()
        self.setObjectName("InstructionsDialog")
        self.resize(400, 140)
        self.verticalLayoutWidget = QtWidgets.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 400, 140))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.instructionsLabel = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.instructionsLabel.setFont(font)
        self.instructionsLabel.setStyleSheet("margin-top: 20")
        self.instructionsLabel.setObjectName("instructionsLabel")
        self.verticalLayout.addWidget(self.instructionsLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.okButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.okButton.setMinimumSize(QtCore.QSize(100, 0))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.okButton.setFont(font)
        self.okButton.setStyleSheet("padding: 5;")
        self.okButton.setObjectName("okButton")
        self.okButton.clicked.connect(lambda: self.close())
        self.verticalLayout.addWidget(self.okButton, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("InstructionsDialog", "Instructions"))
        self.instructionsLabel.setText(_translate("InstructionsDialog", "Available Operators: + - / * ^ ()\n"
                                                                        "\n"
                                                                        "Enter a valid function format, eg. 5*x^3 + 2*x"))
        self.okButton.setText(_translate("InstructionsDialog", "OK"))