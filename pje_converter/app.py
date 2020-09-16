from UiPjeConverter import UiPjeConverter
from PyQt5 import QtCore, QtGui, QtWidgets
from converter import converter_and_split
from pathlib import Path


class MainWindow(QtWidgets.QMainWindow, UiPjeConverter):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.search_file_button.clicked.connect(self.get_file_name)
        self.start_progress_button.clicked.connect(self.make_convert)

    def make_convert(self):
        converter_and_split(self.input_file.text())

    def get_file_name(self):
        home = Path.home()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Procurar Arquivo de Video", r"%s" % home, "Video mp4files (*.py* .wmv *.mp4)"
        )
        self.input_file.setText(file_name)
       

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    PjeConverter = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())