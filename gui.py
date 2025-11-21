from PySide6.QtWidgets import QApplication, QWidget, QPushButton
from logger import get_logger

log = get_logger(__name__)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Youtube AI video summarizer")
        log.debug("MainWindow initialized")
