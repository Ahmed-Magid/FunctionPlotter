from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from pyqtgraph import PlotWidget

from mathematics.FunctionManager import FunctionManager
from utils.Validator import Validator
from views.AlertBox import AlertBox
from views.InstructionsDialog import InstructionsDialog


class MainView(QMainWindow):
    def __init__(self):
        super(MainView, self).__init__()
        self.functionManager = FunctionManager()
        self.validator = Validator()
        self.setObjectName("MainWindow")
        self.resize(1155, 745)
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1155, 745))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(self.verticalLayoutWidget)
        self.frame.setEnabled(True)
        self.frame.setMinimumSize(QtCore.QSize(0, 80))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.frame.setObjectName("frame")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.frame)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1155, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.fXLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.fXLabel.setFont(font)
        self.fXLabel.setStyleSheet("")
        self.fXLabel.setObjectName("fXLabel")
        self.horizontalLayout_2.addWidget(self.fXLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.functionField = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.functionField.setFont(font)
        self.functionField.setStyleSheet("")
        self.functionField.setObjectName("functionField")
        self.horizontalLayout_2.addWidget(self.functionField, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.fromLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.fromLabel.setFont(font)
        self.fromLabel.setStyleSheet("")
        self.fromLabel.setObjectName("fromLabel")
        self.horizontalLayout_2.addWidget(self.fromLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.minimumDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.minimumDoubleSpinBox.setFont(font)
        self.minimumDoubleSpinBox.setStyleSheet("")
        self.minimumDoubleSpinBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.minimumDoubleSpinBox.setMinimum(-2147483648.0)
        self.minimumDoubleSpinBox.setMaximum(2147483647.0)
        self.minimumDoubleSpinBox.setObjectName("minimumDoubleSpinBox")
        self.horizontalLayout_2.addWidget(self.minimumDoubleSpinBox)
        self.toLabel = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.toLabel.setFont(font)
        self.toLabel.setStyleSheet("")
        self.toLabel.setObjectName("toLabel")
        self.horizontalLayout_2.addWidget(self.toLabel, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.maximumDoubleSpinBox = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.maximumDoubleSpinBox.setFont(font)
        self.maximumDoubleSpinBox.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.maximumDoubleSpinBox.setMinimum(-2147483648.0)
        self.maximumDoubleSpinBox.setMaximum(2147483647.0)
        self.maximumDoubleSpinBox.setObjectName("maximumDoubleSpinBox")
        self.horizontalLayout_2.addWidget(self.maximumDoubleSpinBox)
        self.plotButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.plotButton.clicked.connect(self.plotFunction)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.plotButton.setFont(font)
        self.plotButton.setStyleSheet("padding:5;\n"
                                      "margin:5")
        self.plotButton.setObjectName("plotButton")
        self.horizontalLayout_2.addWidget(self.plotButton, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.changeColorButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.changeColorButton.clicked.connect(self.changeColor)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.changeColorButton.setFont(font)
        self.changeColorButton.setStyleSheet("padding:5;\n"
                                             "margin:5")
        self.changeColorButton.setObjectName("changeColorButton")
        self.horizontalLayout_2.addWidget(self.changeColorButton)
        self.instructionsButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.instructionsButton.clicked.connect(self.openInstructionsDialog)
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(16)
        self.instructionsButton.setFont(font)
        self.instructionsButton.setStyleSheet("padding:5;\n"
                                              "margin:5")
        self.instructionsButton.setObjectName("instructionsButton")
        self.horizontalLayout_2.addWidget(self.instructionsButton)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignTop)
        self.plotter = PlotWidget(self.verticalLayoutWidget)
        self.plotter.setMinimumSize(QtCore.QSize(0, 700))
        self.color = QtGui.QColor('#282c34')
        self.plotter.setBackground(self.color)
        self.plotter.showGrid(x=True, y=True, alpha=0.5)
        self.plotter.setObjectName("plotter")
        self.verticalLayout.addWidget(self.plotter)

        self.setCentralWidget(self.centralwidget)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "Function Plotter"))
        self.fXLabel.setText(_translate("MainWindow", "f(x) = "))
        self.fromLabel.setText(_translate("MainWindow", "From"))
        self.toLabel.setText(_translate("MainWindow", "To"))
        self.plotButton.setText(_translate("MainWindow", "Plot Function"))
        self.changeColorButton.setText(_translate("MainWindow", "Change Color"))
        self.instructionsButton.setText(_translate("MainWindow", "Instructions"))

    def plotFunction(self):
        function = self.functionField.text()
        try:
            self.validator.isValidFunction(function)
        except SyntaxError as error:
            AlertBox(error.msg)
            return
        formalFunction = self.functionManager.prepareFunction(function)

        minValue = self.minimumDoubleSpinBox.value()
        maxValue = self.maximumDoubleSpinBox.value()
        if maxValue <= minValue:
            AlertBox("Max value must be larger than min value.")
            return
        xCoordinates, yCoordinates = self.functionManager.generateCoordinates(formalFunction, minValue, maxValue)
        self.reloadPlotter()
        self.plotter.plot(xCoordinates, yCoordinates)

    def changeColor(self):
        color = QtWidgets.QColorDialog.getColor()
        if color.isValid():
            self.color = color
            self.plotter.setBackground(self.color)

    def reloadPlotter(self):
        self.verticalLayout.removeWidget(self.plotter)
        self.plotter = PlotWidget(self.verticalLayoutWidget)
        self.plotter.setMinimumSize(QtCore.QSize(0, 700))
        self.plotter.setBackground(self.color)
        self.plotter.showGrid(x=True, y=True, alpha=0.5)
        self.plotter.setObjectName("plotter")

        self.verticalLayout.addWidget(self.plotter)

    def openInstructionsDialog(self):
        instructionsDialog = InstructionsDialog()
        instructionsDialog.show()
