from ui_pje_converter import Ui_PjeConverter
from PyQt5 import QtWidgets
from PyQt5.QtCore import (QRunnable, QThread, 
                          QThreadPool, QObject, 
                          pyqtSignal, pyqtSlot
                          )
from converter import converter_and_split
from pathlib import Path
from threading import Thread


class WokerSignal(QObject):

    progress = pyqtSignal(int)
    button = pyqtSignal(object)
    done  = pyqtSignal(object)


class Worker(QRunnable):
    def __init__(self, func, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signals = WokerSignal()
    
        self.kwargs['progress_bar'] = self.signals.progress
        self.kwargs['button'] = self.signals.button
        self.kwargs['done'] = self.signals.done

    @pyqtSlot()
    def run(self):
        self.func(*self.args, **self.kwargs)


class MainWindow(QtWidgets.QMainWindow, Ui_PjeConverter):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.thread_pool = QThreadPool()

        self.search_file_button.clicked.connect(self.get_file_name)
        self.start_progress_button.clicked.connect(self.make_convert)
        self.action_abrir.triggered.connect(self.get_file_name)
        self.actionSobre.triggered.connect(self.about)

    def make_convert(self):
        worker = Worker(
            converter_and_split,
            self.input_file,
            )
        worker.signals.progress.connect(self.progressBar.setValue)
        worker.signals.button.connect(self.start_progress_button.setText)
        worker.signals.done.connect(self.done_popup)
        self.thread_pool.start(worker)

    def get_file_name(self):
        home = Path.home()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
            None, "Procurar Arquivo de Video", r"%s" % home, )
        self.input_file.setText(file_name)

    def done_popup(self, s):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("PJe Converter")
        msg_box.setText(
            "Processo Concluído.\nVideos Convertivos e/ou Dividos"
            "\nestão no mesmo local do video original"
            )
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.exec_()

    def about(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("PJe Converter")
        msg_box.setText("Desenvolvido por Haddly Trindade\nEmail: haddtrindade@gmail.com")
        msg_box.exec_()

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    PjeConverter = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())