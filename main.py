from PyQt5.QtWidgets import QApplication

from views.MainView import MainView

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mainView = MainView()
    mainView.show()
    sys.exit(app.exec_())
