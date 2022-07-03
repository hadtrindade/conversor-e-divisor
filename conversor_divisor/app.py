import sys
from pathlib import Path
from signal import SIGTERM

from PySide2 import QtGui, QtWidgets

from conversor_divisor import __author__, __version__, functions
from conversor_divisor.convert import Convert
from conversor_divisor.settings import PLATFORM, Settings
from conversor_divisor.ui import Ui_MainWindow
from conversor_divisor.worker import Worker


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.not_split = True
        self.process_in_progress = None
        self.process_split_in_progress = None
        self.media_convert = None
        self.media_split = None
        self.output_convert = Path.home()
        self.output_split = Path.home()
        self.current_directory_convert = Path.home()
        self.current_directory_split = Path.home()
        self.low = True
        self.audio_only = None
        self.worker = None
        self.worker_split = None
        self._signal_sigterm = SIGTERM
        self._platform_ms_win = PLATFORM
        self.settings = Settings()

        # menu
        self.button_toggle.clicked.connect(
            lambda: functions.toggle_menu(self, 150, True)
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
            lambda: functions.get_media_convert(self)
        )
        self.button_source_file_split.clicked.connect(
            lambda: functions.get_media_split(self)
        )
        # button_output
        self.button_output_file.clicked.connect(
            lambda: functions.get_output_convert(self)
        )
        self.button_output_file_split.clicked.connect(
            lambda: functions.get_output_split(self)
        )
        # button_open_folder
        self.button_open_folder.clicked.connect(
            lambda: functions.open_output_convert(self)
        )
        self.button_open_folder_split.clicked.connect(
            lambda: functions.open_output_split(self)
        )
        # button_radios_quality
        self.radio_button_low.clicked.connect(self.change_quality_low)
        self.radio_button_normal.clicked.connect(self.change_quality_normal)
        # config init
        functions.config_init(self)
        functions.config_init_split(self)
        # Infos
        self.label_version.setText(__version__)
        self.label_author.setText(f'Desenvolvido por {__author__}')

        # Set settings
        try:
            self.spinBox_split_size.setValue(
                self.settings.read()['split']['v_split_size_mb']
            )
            self.spinBox_split_size_audio.setValue(
                self.settings.read()['split']['a_split_size_mb']
            )
            self.resolution_settings.setCurrentIndex(
                self.settings.read()['convert']['resolution_index']
            )
        except KeyError:
            self.settings.write(
                setting='split',
                **self.settings.default_settings['split'],
            )
            self.settings.write(
                setting='convert',
                **self.settings.default_settings['convert'],
            )
        self.pushButton_apply_settings.clicked.connect(self.change_settings)

    def change_settings(self):
        functions.set_settings(self)

    def change_not_split(self):
        if self.check_box_split.isChecked():
            self.not_split = True

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
        if self._platform_ms_win == 'win32':
            from subprocess import DEVNULL, Popen
            try:
                _ = Popen(['tskill', 'ffmpeg'], stdout=DEVNULL, stderr=DEVNULL)
                _ = Popen(
                    ['tskill', 'HandBrakeCLI'], stdout=DEVNULL, stderr=DEVNULL
                )
            except FileNotFoundError:
                _ = Popen(['taskkill', '/F', '/IM', 'ffmpeg.exe'], stdout=DEVNULL, stderr=DEVNULL)
                _ = Popen(['taskkill', '/F', '/IM', 'HandBrakeCLI.exe'], stdout=DEVNULL, stderr=DEVNULL)
        else:
            self.process_in_progress.send_signal(self._signal_sigterm)
        self.worker.terminate()
        functions.config_init(self)
        self.popup_done('Conversão e/ou Cancelada')

    def stop_process_split(self):
        if self._platform_ms_win == 'win32':
            from subprocess import Popen

            Popen(['tskill', 'mp4box'])
        else:
            self.process_split_in_progress.send_signal(self._signal_sigterm)
        self.worker_split.terminate()
        functions.config_init_split(self)
        self.popup_done('Divisão Cancelada.')

    def change_quality_low(self):
        self.low = True

    def change_quality_normal(self):

        self.low = False

    def make_split(self):

        self.worker_split = Worker()
        self.worker_split.args = (
            self.media_split,
            self.output_split,
        )
        self.worker_split.signal.process_signal.connect(self.set_process_split)
        self.worker_split.signal.progress_signal.connect(
            self.progress_bar_split.setValue
        )
        self.worker_split.signal.error_signal.connect(self.popup_error_split)
        self.worker_split.signal.done_signal.connect(self.popup_done)
        self.worker_split.kwargs['split_only'] = True
        self.worker_split._class = Convert
        functions.processing_split(self)
        self.worker_split.start()

    def make_convert_split(self):

        self.worker = Worker()
        self.worker.args = (self.media_convert, self.output_convert)
        self.worker.signal.line_input_file_signal.connect(
            self.line_edit_input_file.setText
        )
        self.worker.signal.process_signal.connect(self.set_process)
        self.worker.signal.progress_signal.connect(self.progress_bar.setValue)
        self.worker.signal.error_signal.connect(self.popup_error)
        self.worker.signal.error_signal_warm.connect(self.popup_error_warm)
        self.worker.signal.done_signal.connect(self.popup_done)
        self.worker.kwargs['low'] = self.low
        self.worker.kwargs['audio_only'] = self.audio_only
        self.worker.kwargs['split'] = self.not_split
        self.worker._class = Convert
        functions.processing_cd(self)
        self.worker.start()

    def change_page_1(self):
        if self.frame_left_menu.minimumWidth() == 150:
            functions.toggle_menu(self, 150, True)
        self.stackedWidget.setCurrentWidget(self.page_1)

    def change_page_2(self):
        if self.frame_left_menu.minimumWidth() == 150:
            functions.toggle_menu(self, 150, True)
        self.stackedWidget.setCurrentWidget(self.page_2)

    def change_page_3(self):
        if self.frame_left_menu.minimumWidth() == 150:
            functions.toggle_menu(self, 150, True)
        self.stackedWidget.setCurrentWidget(self.page_3)

    def popup_done(self, msg):

        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('Conversor & Divisor')
        msg_box.setText(msg)
        msg_box.setWindowIcon(QtGui.QIcon(':/MainIcon/img/main_icone'))
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        if msg == 'Divisão Concluída.':
            functions.config_init_split(self)
        elif msg == 'Divisão Cancelada.':
            functions.config_init_split(self)
        elif msg == 'Conversão e/ou Cancelada':
            functions.config_init(self)
        elif (
            'Conversões e/ou Divisões Concluídas.' in msg
            or msg == 'Conversão e/ou Divisão Concluída.'
        ):
            functions.config_init(self)
        elif msg == 'Mídia já está em tamanho apropriado!':
            functions.config_init_split(self)
        msg_box.exec_()

    def popup_error(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('Conversor & Divisor')
        msg_box.setText(msg)
        msg_box.setWindowIcon(QtGui.QIcon(':/MainIcon/main_icone'))
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        functions.config_init(self)
        msg_box.exec_()

    def popup_error_warm(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('Conversor & Divisor')
        msg_box.setText(msg)
        msg_box.setWindowIcon(QtGui.QIcon(':/MainIcon/main_icone'))
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        msg_box.exec_()

    def popup_error_split(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle('Conversor & Divisor')
        msg_box.setText(msg)
        msg_box.setWindowIcon(QtGui.QIcon(':/MainIcon/main_icone'))
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        functions.config_init_split(self)
        msg_box.exec_()


def start_app():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    start_app()
