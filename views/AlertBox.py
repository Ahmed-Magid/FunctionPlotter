from PyQt5.QtWidgets import QMessageBox


class AlertBox(QMessageBox):
    def __init__(self, message):
        """
        Represents an error dialog.
        :param message: The error message to be displayed.
        """
        super(QMessageBox, self).__init__()
        self.critical(self, "Error", message)
