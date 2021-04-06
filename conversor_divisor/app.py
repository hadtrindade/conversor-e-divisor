import sys
from signal import SIGTERM
from PySide2 import QtGui, QtWidgets
from pathlib import Path
from conversor_divisor.ui_cd import Ui_MainWindow
from conversor_divisor import __version__, __author__
from conversor_divisor import ui_functions
from conversor_divisor.worker import Worker
from conversor_divisor.convert import Convert
from conversor_divisor.settings import Settings


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.not_split = None
        self.process_in_progress = None
        self.process_split_in_progress = None
        self.input_file_convert = None
        self.input_file_split = None
        self.output_path_convert = Path.home()
        self.output_path_split = Path.home()
        self.current_directory_convert = Path.home()
        self.current_directory_split = Path.home()
        self.input_file_split = None
        self.low = True
        self.audio_only = None
        self.worker = None
        self.worker_split = None
        self._signal_sigterm = SIGTERM
        self._platform_ms_win = sys.platform == "win32"
        self.settings = Settings()

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
        # button_checkbox_audio
        self.check_box_audio.clicked.connect(self.change_mode_audio)
        # buttons_source_files
        self.button_source_file.clicked.connect(
            lambda: ui_functions.get_media(self)
        )
        self.button_source_file_split.clicked.connect(
            lambda: ui_functions.get_file_media_split(self)
        )
        # button_output
        self.button_output_file.clicked.connect(
            lambda: ui_functions.get_path_output_convert(self)
        )
        self.button_output_file_split.clicked.connect(
            lambda: ui_functions.get_path_output_split(self)
        )
        # button_open_folder
        self.button_open_folder.clicked.connect(
            lambda: ui_functions.open_output_folder_convert(self)
        )
        self.button_open_folder_split.clicked.connect(
            lambda: ui_functions.open_output_folder_split(self)
        )
        # button_radios_quality
        self.radio_button_low.clicked.connect(self.change_quality_low)
        self.radio_button_normal.clicked.connect(self.change_quality_normal)
        # config init
        ui_functions.config_init(self)
        ui_functions.config_init_split(self)
        # Infos
        self.label_version.setText(__version__)
        self.label_author.setText(f"Desenvolvido por {__author__}")

        # Set settings
        try:
            self.spinBox_split_size.setValue(
                self.settings.read_settings()["settings_split"][
                    "split_size_mb_v"
                ]
            )
            self.spinBox_split_size_audio.setValue(
                self.settings.read_settings()["settings_split"][
                    "split_size_mb_a"
                ]
            )
            self.resolution_settings.setCurrentIndex(
                self.settings.read_settings()["settings_convert"][
                    "resolution_index_value"
                ]
            )
        except KeyError:
            self.settings.writer_settings(
                setting="settings_split",
                **self.settings.default_settings["settings_split"],
            )
            self.settings.writer_settings(
                setting="settings_convert",
                **self.settings.default_settings["settings_convert"],
            )
        self.pushButton_apply_settings.clicked.connect(self.change_settings)

    def change_settings(self):
        ui_functions.set_settings(self)

    def change_not_split(self):
        if self.check_box_split.isChecked():
            self.not_split = True
        else:
            self.not_split = False

    def change_mode_audio(self):
        if self.check_box_audio.isChecked():
            self.audio_only = True
            self.radio_button_low.hide()
            self.radio_button_normal.hide()
        else:
            self.audio_only = False
            self.radio_button_normal.setVisible(True)
            self.radio_button_low.setVisible(True)

    def set_process(self, obj_proc):
        self.process_in_progress = obj_proc

    def set_process_split(self, obj_proc):
        self.process_split_in_progress = obj_proc

    def stop_process(self):
        if self._platform_ms_win:
            from subprocess import Popen, DEVNULL

            _ = Popen(["tskill", "ffmpeg"], stdout=DEVNULL, stderr=DEVNULL)
            _ = Popen(
                ["tskill", "HandBrakeCLI"], stdout=DEVNULL, stderr=DEVNULL
            )
        else:
            self.process_in_progress.send_signal(self._signal_sigterm)
        self.worker.terminate()
        ui_functions.config_init(self)
        self.popup_done("Conversão e/ou Cancelada")

    def stop_process_split(self):
        if self._platform_ms_win:
            from subprocess import Popen

            Popen(["tskill", "mp4box"])
        else:
            self.process_split_in_progress.send_signal(self._signal_sigterm)
        self.worker_split.terminate()
        ui_functions.config_init_split(self)
        self.popup_done("Divisão Cancelada.")

    def change_quality_low(self):
        self.low = True

    def change_quality_normal(self):

        self.low = False

    def make_split(self):

        self.worker_split = Worker()
        self.worker_split.args = (
            self.input_file_split,
            self.output_path_split,
        )
        self.worker_split.signal.process_signal.connect(self.set_process_split)
        self.worker_split.signal.progress_signal.connect(
            self.progress_bar_split.setValue
        )
        self.worker_split.signal.error_signal.connect(self.popup_error_split)
        self.worker_split.signal.done_signal.connect(self.popup_done)
        self.worker_split.kwargs["split_only"] = True
        self.worker_split._class = Convert
        ui_functions.processing_split(self)
        self.worker_split.start()

    def make_convert_split(self):

        self.worker = Worker()
        self.worker.args = (self.input_file_convert, self.output_path_convert)
        self.worker.signal.line_input_file_signal.connect(
            self.line_edit_input_file.setText
        )
        self.worker.signal.process_signal.connect(self.set_process)
        self.worker.signal.progress_signal.connect(self.progress_bar.setValue)
        self.worker.signal.error_signal.connect(self.popup_error)
        self.worker.signal.error_signal_warm.connect(self.popup_error_warm)
        self.worker.signal.done_signal.connect(self.popup_done)
        self.worker.kwargs["low"] = self.low
        self.worker.kwargs["audio_only"] = self.audio_only
        self.worker.kwargs["not_split"] = self.not_split
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
        msg_box.setWindowIcon(QtGui.QIcon(":/MainIcon/img/main_icone"))
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        if msg == "Divisão Concluída.":
            ui_functions.config_init_split(self)
        elif msg == "Divisão Cancelada.":
            ui_functions.config_init_split(self)
        elif msg == "Conversão e/ou Cancelada":
            ui_functions.config_init(self)
        elif (
            "Conversões e/ou Divisões Concluídas." in msg
            or msg == "Conversão e/ou Divisão Concluída."
        ):
            ui_functions.config_init(self)
        elif msg == "Mídia já está em tamanho apropriado!":
            ui_functions.config_init_split(self)
        msg_box.exec_()

    def popup_error(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Conversor & Divisor")
        msg_box.setText(msg)
        msg_box.setWindowIcon(QtGui.QIcon(":/MainIcon/main_icone"))
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        ui_functions.config_init(self)
        msg_box.exec_()

    def popup_error_warm(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Conversor & Divisor")
        msg_box.setText(msg)
        msg_box.setWindowIcon(QtGui.QIcon(":/MainIcon/main_icone"))
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.exec_()

    def popup_error_split(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Conversor & Divisor")
        msg_box.setText(msg)
        msg_box.setWindowIcon(QtGui.QIcon(":/MainIcon/main_icone"))
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        ui_functions.config_init_split(self)
        msg_box.exec_()


def start_app():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    start_app()
