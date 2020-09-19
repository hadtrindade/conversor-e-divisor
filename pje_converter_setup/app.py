from os import environ, path
import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import (pyqtSignal, pyqtSlot, QRect,
                          QRunnable, QThreadPool, QObject
                          )
from main_windows import Ui_Pje_converter_setup
from next_window_pre_install import Ui_Pje_converter_setup_pre_install
from next_window_progress_bar_install import (
    Ui_Pje_converter_setup_install_progress_bar
    )
from main_window_template import Ui_Pje_converter_setup_template_window
from setup_tools import init_setup


class WokerSignal(QObject):

    progress = pyqtSignal(int)
    button_finish = pyqtSignal(object)
    error = pyqtSignal(object)


class Worker(QRunnable):
    def __init__(self, func, *args, **kwargs):
        super(Worker, self).__init__()
        self.func = func
        self.args = args
        self.kwargs = kwargs
        self.signals = WokerSignal()

        self.kwargs['progress_bar'] = self.signals.progress
        self.kwargs['button_finish'] = self.signals.button_finish
        self.kwargs['error'] = self.signals.error

    @pyqtSlot()
    def run(self):
        self.func(*self.args, **self.kwargs)


class PageWindow(QtWidgets.QMainWindow):
    goto_signal = pyqtSignal(str)

    def goto(self, name):
        self.goto_signal.emit(name)


class NextPreInstall(PageWindow, Ui_Pje_converter_setup_pre_install):

    path_default = None

    def __init__(self):
        super(NextPreInstall, self).__init__()
        self.setupUi(self)
        self.button_back.clicked.connect(self.goto_main_setup)
        self.button_next_for_install.clicked.connect(self.install_program)
        self._base_path = environ["PROGRAMFILES(X86)"]
        self._path_install = path.join(self._base_path, "PJe Converter")
        self.input_directory_install.setText(self._path_install)
        self.button_change_directory.clicked.connect(self.change_directory)
        NextPreInstall.path_default = self._path_install

    def change_directory(self):
        directory = QtWidgets.QFileDialog.getExistingDirectory(
            None,
            "Escolha um diretório para a Instalação",
            self._base_path
            )
        if not directory:
            self.input_directory_install.setText(self._path_install)
        self.input_directory_install.setText(
            path.join(directory, "PJe Converter")
            )
        NextPreInstall.path_default = directory

    def goto_main_setup(self):
        self.goto("main_setup")

    def install_program(self):
        self.goto("install_progress_bar")


class NextProgressBarInstall(
    PageWindow,
    Ui_Pje_converter_setup_install_progress_bar
    ):
    def __init__(self):
        super(NextProgressBarInstall, self).__init__()
        self.setupUi(self)
        self.thread_pool = QThreadPool()
        self.button_back_pre_install.clicked.connect(self.goto_pre_install)
        self.button_install.clicked.connect(self.install_app)
        self.button_close.hide()
        self.button_close.clicked.connect(self.close_app)

    def install_app(self):
        self.button_close.hide()
        self.button_back_pre_install.hide()
        self.button_install.setText("Instalando")
        worker = Worker(init_setup, NextPreInstall.path_default)
        worker.signals.error.connect(self.error)
        worker.signals.progress.connect(self.progress_bar_install.setValue)
        worker.signals.button_finish.connect(self.set_button_finish)
        self.thread_pool.start(worker)

    def error(self, name):
        if name == "PermissionError":
            self.popup(f"{name}, Execute o programa de Instalação\n"
                       "como administrador."
                       )

    def popup(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("PJe Installer")
        msg_box.setText(msg)
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        msg_box.buttonClicked.connect(self.button_done_popup)
        msg_box.exec_()

    def button_done_popup(self):
        sys.exit()

    def set_button_finish(self, arg):
        self.button_install.hide()
        self.button_close.setVisible(True)

    def close_app(self):
        sys.exit()

    def goto_pre_install(self):
        self.goto("pre_install")


class PjeSetupWindow(PageWindow, Ui_Pje_converter_setup):
    def __init__(self):
        super(PjeSetupWindow, self).__init__()
        self.setupUi(self)
        self.button_next.hide()
        self.button_next.clicked.connect(self.goto_next_pre_install)
        self.button_exit.clicked.connect(self.close_app)

    def close_app(self):
        sys.exit()

    def goto_next_pre_install(self):
        self.goto("pre_install")


class Window(PageWindow, Ui_Pje_converter_setup_template_window):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.stacked_widget = QtWidgets.QStackedWidget()
        self.setCentralWidget(self.stacked_widget)
        self.m_pages = {}
        self.register(PjeSetupWindow(), "main_setup")
        self.register(NextPreInstall(), "pre_install")
        self.register(NextProgressBarInstall(), "install_progress_bar")
        self.goto("main_setup")

    def register(self, widget, name):
        self.m_pages[name] = widget
        self.stacked_widget.addWidget(widget)
        if isinstance(widget, PageWindow):
            widget.goto_signal.connect(self.goto)

    @pyqtSlot(str)
    def goto(self, name):
        if name in self.m_pages:
            widget = self.m_pages[name]
            self.stacked_widget.setCurrentWidget(widget)
            self.setWindowTitle(widget.windowTitle())


if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    ui = Window()
    ui.show()
    sys.exit(app.exec_())
