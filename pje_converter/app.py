from ui_pje_converter import Ui_PjeConverter
from PyQt5 import QtCore, QtGui, QtWidgets
from converter import converter_and_split
from pathlib import Path
from threading import Thread


class MainWindow(QtWidgets.QMainWindow, Ui_PjeConverter):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.search_file_button.clicked.connect(self.get_file_name)
        self.start_progress_button.clicked.connect(self.make_convert)
        self.action_abrir.triggered.connect(self.get_file_name)
        self.actionSobre.triggered.connect(self.about)

    def make_convert(self):
        converter_and_split(
            self.input_file,
            self.progressBar.setValue,
            self.start_progress_button.setText)

    def get_file_name(self):
        home = Path.home()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Procurar Arquivo de Video", r"%s" % home, )
        self.input_file.setText(file_name)

    def about(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("PJe Converter")
        msg_box.setText("Desenvolvido por Haddly Trindade\n Email: haddtrindade@gmail.com")
        msg_box.exec_()

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    PjeConverter = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())