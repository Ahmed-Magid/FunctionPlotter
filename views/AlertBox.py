from PyQt5.QtWidgets import QMessageBox


class AlertBox(QMessageBox):
    def __init__(self, message):
        super(QMessageBox, self).__init__()
        self.critical(self, "Error", message)
