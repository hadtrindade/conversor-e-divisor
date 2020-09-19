from ui_pje_converter import Ui_PjeConverter
from PyQt5 import QtWidgets
from PyQt5.QtCore import (QRunnable, QThread, 
                          QObject, pyqtSignal,
                          pyqtSlot,
                          )
from converter import converter_and_split
from pathlib import Path
from os import path
from threading import Thread
from subprocess import Popen
from time import sleep


class WorkerSignals(QObject):

    progress = pyqtSignal(int)
    button = pyqtSignal(object)
    done = pyqtSignal(object)
    error = pyqtSignal(object)


class Worker(QThread):

    def __init__(self, func, *args, **kwargs):
        super(Worker,self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

        self.kwargs['progress_bar'] = self.signals.progress
        self.kwargs['button'] = self.signals.button
        self.kwargs['done'] = self.signals.done
        self.kwargs['error'] = self.signals.error

    def stop(self):
        self.terminate()

    def run(self):
        self.func(*self.args, **self.kwargs)


class MainWindow(QtWidgets.QMainWindow, Ui_PjeConverter):

    low_quality = True

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.worker = Worker(converter_and_split)

        self.search_file_button.clicked.connect(self.get_file_name)
        self.start_progress_button.clicked.connect(self.make_convert)
        self.action_abrir.triggered.connect(self.get_file_name)
        self.actionSobre.triggered.connect(self.about)
        self.output_file_button.clicked.connect(self.get_path_output_name)
        self.radio_button_normal.clicked.connect(self.set_nornal_quality)
        self.open_folder.clicked.connect(self.open_ouput_folder)
        self.stop_progress_button.setDisabled(True)
        self.stop_progress_button.clicked.connect(self.stop_task)
        self.start_progress_button.setDisabled(True)

    def set_nornal_quality(self):
        MainWindow.low_quality = False

    def open_ouput_folder(self):
        path_output_folder = self.output_file.text().replace("/","\\")
        Popen(f"explorer /open, \"{path_output_folder}\"")

    def make_convert(self):
        
        self.stop_progress_button.setEnabled(True)
        self.start_progress_button.setDisabled(True)
        self.worker.args = (self.input_file, self.output_file.text(), MainWindow.low_quality)
        self.worker.signals.progress.connect(self.progressBar.setValue)
        self.worker.signals.button.connect(self.start_progress_button.setText)
        self.worker.signals.done.connect(self.done_popup)
        self.worker.signals.error.connect(self.app_error)
        self.worker.start()

    def stop_task(self):
        self.worker.stop()
        self.popup
        self.stop_progress_button.setDisabled(True)
        self.progressBar.setValue(0)
        self.start_progress_button.setText("Iniciar")
        self.start_progress_button.setEnabled(True)
    
    def get_file_name(self):
        home = Path.home()
        file_name, _ = QtWidgets.QFileDialog.getOpenFileNames(
            None, "Procurar Arquivo de Video", r"%s" % home,
            "Video Files (*.mp4 *.mkv *.flv *.swf *.avchd *.mov *.qt *.avi *.wmv *.mpeg *.rmvb);;All Files (*)",
            )
        
        if not file_name:
            return

        if len(file_name) == 1:
            paths = path.split(file_name[0])
            ouput_path = paths[0]
            self.input_file.setPlainText(file_name[0])
            self.output_file.setText(ouput_path)
            self.start_progress_button.setEnabled(True)
        else:
            paths = path.split(file_name[0])
            ouput_path = paths[0]
            files = ""
            for i in file_name:
                files += i+"\n"
            self.input_file.setPlainText(files)
            self.output_file.setText(ouput_path)
            self.start_progress_button.setEnabled(True)
            
    def get_path_output_name(self):
        home = Path.home()
        path_output = QtWidgets.QFileDialog.getExistingDirectory(
            None, "Procurar Diretório de Destino.", r"%s" % home,)
        self.output_file.setText(path_output)

    def done_popup(self, s):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("PJe Converter")
        msg_box.setText(
            "Processo Concluído.\nVideos Convertivos e/ou Dividos"
            "\nestão no mesmo local do video original"
            )
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.buttonClicked.connect(self.button_done_popup)
        msg_box.exec_()

    def button_done_popup(self, arg):
        self.input_file.clear()
        self.progressBar.setValue(0)


    def app_error(self, arg):
        self.input_file.clear()
        self.progressBar.setValue(0)
        self.popup(arg)

    def popup(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("PJe Converter")
        msg_box.setText(msg)
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.buttonClicked.connect(self.button_done_popup)
        msg_box.exec_()

    def about(self):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("PJe Converter")
        msg_box.setText(
            "Desenvolvido por Haddly Trindade\n"
            "Email: haddtrindade@gmail.com\n"
            "github.com/hadtrindade\n"
            "Versão: 0.1.0"
            )
        msg_box.exec_()

if __name__ == "__main__":

    import sys
    app = QtWidgets.QApplication(sys.argv)
    PjeConverter = QtWidgets.QMainWindow()
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())