import sys
from signal import SIGTERM
from PySide2 import QtGui, QtWidgets
from pathlib import Path
from ui_cd import Ui_MainWindow
import ui_functions
from worker import Worker
from convert import Convert


_sigterm = SIGTERM
_windows = (sys.platform == 'win32')


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.not_split = False
        self.process_in_progress = None
        self.process_split_in_progress = None
        self.input_file = None
        self.output_path = Path.home()
        self.input_file_split = None
        self.split = None
        self.low = False
        self.worker = None
        self.worker_split = None

        # menu
        self.button_toggle.clicked.connect(
            lambda: ui_functions.toggle_menu(self, 150, True)
        )
        # pages
        self.button_page_1.clicked.connect(self.change_page_1)
        self.button_page_2.clicked.connect(self.change_page_2)
        self.button_settings.clicked.connect(self.change_page_3)
        # button_start
        self.button_start.clicked.connect(self.make_convert_split)
        self.button_start_split.clicked.connect(self.make_split)
        # button_stop
        self.button_stop.clicked.connect(self.stop_process)
        self.button_stop_split.clicked.connect(self.stop_process_split)
        # button_checkbox_split
        self.check_box_split.clicked.connect(self.change_not_split)
        # buttons_source_files
        self.button_source_file.clicked.connect(
            lambda: ui_functions.get_file_video(self)
        )
        self.button_source_file_split.clicked.connect(
            lambda: ui_functions.get_file_video_split(self)
        )
        # button_output
        self.button_output_file.clicked.connect(
            lambda: ui_functions.get_path_output_name(self)
        )
        self.button_output_file_split.clicked.connect(
            lambda: ui_functions.get_path_output_name_split(self)
        )
        # button_open_folder
        self.button_open_folder.clicked.connect(
            lambda: ui_functions.open_ouput_folder(self)
        )
        self.button_open_folder_split.clicked.connect(
            lambda: ui_functions.open_ouput_folder(self)
        )
        # button_radios_quality
        self.radio_button_low.clicked.connect(self.change_quality_low)
        self.radio_button_normal.clicked.connect(self.change_quality_normal)
        # config init
        ui_functions.config_init(self)
        ui_functions.config_init_split(self)

    def change_not_split(self):
        if self.check_box_split.isChecked():
            self.not_split = True
        else:
            self.not_split = False

    def set_process(self, obj_proc):
        self.process_in_progress = obj_proc

    def set_process_split(self, obj_proc):
        self.process_split_in_progress = obj_proc

    def stop_process(self):
        if _windows:
            from signal import CTRL_BREAK_EVENT
            _sigterm = CTRL_BREAK_EVENT
        self.process_in_progress.send_signal(_sigterm)
        self.worker.terminate()
        ui_functions.config_init(self)
        self.popup_done("Conversão e/ou Cancelada")

    def stop_process_split(self):
        if _windows:
            from signal import CTRL_BREAK_EVENT
            _sigterm = CTRL_BREAK_EVENT
        self.process_split_in_progress.send_signal(_sigterm)
        self.worker_split.terminate()
        ui_functions.config_init_split(self)
        self.popup_done("Divisão Cancelada.")

    def change_quality_low(self):
        self.low = True

    def change_quality_normal(self):

        self.low = False

    def make_split(self):

        self.worker_split = Worker()
        self.worker_split.args = (self.input_file_split, self.output_path)
        self.worker_split.signal.process_signal.connect(self.set_process_split)
        self.worker_split.signal.progress_signal.connect(
            self.progress_bar_split.setValue
        )
        self.worker_split.signal.error_signal.connect(self.popup_error)
        self.worker_split.signal.done_signal.connect(self.popup_done)
        self.worker_split.kwargs["just_divide"] = self.split
        self.worker_split._class = Convert
        ui_functions.processing_split(self)
        self.worker_split.start()

    def make_convert_split(self):

        self.worker = Worker()
        self.worker.args = (self.input_file, self.output_path)
        self.worker.signal.process_signal.connect(self.set_process)
        self.worker.signal.progress_signal.connect(self.progress_bar.setValue)
        self.worker.signal.error_signal.connect(self.popup_error)
        self.worker.signal.done_signal.connect(self.popup_done)
        self.worker.kwargs["low"] = self.low
        self.worker.kwargs["not_split"] = self.not_split
        self.worker.kwargs["just_divide"] = self.split
        self.worker._class = Convert
        ui_functions.processing_cd(self)
        self.worker.start()

    def change_page_1(self):
        if self.frame_left_menu.minimumWidth() == 150:
            ui_functions.toggle_menu(self, 150, True)
        self.stackedWidget.setCurrentWidget(self.page_1)

    def change_page_2(self):
        if self.frame_left_menu.minimumWidth() == 150:
            ui_functions.toggle_menu(self, 150, True)
        self.stackedWidget.setCurrentWidget(self.page_2)

    def change_page_3(self):
        if self.frame_left_menu.minimumWidth() == 150:
            ui_functions.toggle_menu(self, 150, True)
        self.stackedWidget.setCurrentWidget(self.page_3)

    def popup_done(self, msg):

        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Conversor & Divisor")
        msg_box.setText(msg)
        msg_box.setWindowIcon(QtGui.QIcon(u":/MainIcon/main_icone"))
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        if msg == "Divisão Concluída.":
            ui_functions.config_init_split(self)
        elif msg == "Divisão Cancelada.":
            ui_functions.config_init_split(self)
        elif msg == "Conversão e/ou Cancelada":
            ui_functions.config_init(self)
        elif (
            msg == "Conversões e/ou Divisões Concluídas."
            or msg == "Conversão e/ou Divisão Concluída."
        ):
            ui_functions.config_init(self)
        elif msg == "Video já está em tamanho apropriado!":
            ui_functions.config_init_split(self)
        msg_box.exec_()

    def popup_error(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Conversor & Divisor")
        msg_box.setText(msg)
        msg_box.setWindowIcon(QtGui.QIcon(u":/MainIcon/main_icone"))
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        ui_functions.config_init(self)
        msg_box.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
