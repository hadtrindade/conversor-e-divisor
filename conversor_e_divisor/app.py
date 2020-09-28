
import sys
from PySide2 import QtCore, QtGui, QtWidgets
from subprocess import Popen, DEVNULL
from itertools import cycle
from worker import Worker
from time import sleep
from pathlib import Path
from os import path
from ui_pje_converter import Ui_MainWindow
import ui_functions
from convert import convert_or_split



class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        self.start = None
        self.stop = None
        self.not_split = False
        self.pid_process_in_progress = None
        self.input_file = None
        self.output_path = Path.home()
        self.input_file_split = None
        self.split = None
        self.low = False

        #menu
        self.button_toggle.clicked.connect(
            lambda: ui_functions.toggle_menu(self, 150, True)
            )
        #pages
        self.button_page_1.clicked.connect(self.change_page_1)
        self.button_page_2.clicked.connect(self.change_page_2)
        self.button_settings.clicked.connect(self.change_page_3)
        #button_start
        self.button_start.clicked.connect(self.make_convert_split)
        self.button_start_split.clicked.connect(self.make_split)
        #button_stop
        self.button_stop.clicked.connect(self.stop_process)
        #button_checkbox_split
        self.check_box_split.clicked.connect(self.change_not_split)
        #buttons_source_files
        self.button_source_file.clicked.connect(
            lambda: ui_functions.get_file_video(self)
            )
        self.button_source_file_split.clicked.connect(
            lambda: ui_functions.get_file_video_split(self)
            )
        #button_output
        self.button_output_file.clicked.connect(
            lambda: ui_functions.get_path_output_name(self)
            )
        self.button_output_file_split.clicked.connect(
            lambda: ui_functions.get_path_output_name_split(self)
            )
        #button_open_folder
        self.button_open_folder.clicked.connect(
            lambda: ui_functions.open_ouput_folder(self)
            )
        self.button_open_folder_split.clicked.connect(
            lambda: ui_functions.open_ouput_folder(self)
            )
        #button_radios_quality
        self.radio_button_low.clicked.connect(self.change_quality_low)
        self.radio_button_normal.clicked.connect(self.change_quality_normal)
        #thread
        self.worker = Worker(convert_or_split)
        #config init
        ui_functions.config_initial(self)
        self.progress_spinner(0)

    def change_not_split(self):
        if self.check_box_split.isChecked():
            self.not_split = True
        else:
            self.not_split = False
    
    def set_pid_process(self, pid):
        self.pid_process_in_progress = pid
    
    def stop_process(self):
        self.stop = True
        self.pid_process_in_progress.kill()
        Popen(
            ["taskkill", "/IM", "ffmpeg.exe", "/F"],
            shell=True, stdout=DEVNULL, stderr=DEVNULL
            )
        self.worker.terminate()
        ui_functions.config_initial(self)

    def change_quality_low(self):
        self.low = True

    def change_quality_normal(self):
        self.low = False

    def make_split(self):

        self.worker.args = (self.input_file_split, self.output_path, self.split)
        self.worker.signal.pid_process.connect(self.set_pid_process)
        self.worker.signal.process_done.connect(self.popup_done)
        self.worker.signal.spinner.connect(self.progress_spinner)
        self.worker.signal.error.connect(self.popup_error)
        ui_functions.config_processing(self)
        self.worker.start()


    def make_convert_split(self):

        self.worker.args = (self.input_file, self.output_path, self.split, self.not_split)
        self.worker.kwargs["low"] = self.low
        self.worker.signal.pid_process.connect(self.set_pid_process)
        self.worker.signal.process_done.connect(self.popup_done)
        self.worker.signal.spinner.connect(self.progress_spinner)
        self.worker.signal.error.connect(self.popup_error)
        ui_functions.config_processing(self)
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

    def progress_spinner(self, value):
        style_sheet = ("QFrame {"
                        "border-radius: 85px;"
                        "background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90,"
                        "stop:{stop1} rgba(217, 237, 247, 0), stop:{stop2} rgba(0, 120, 170, 255))};")
        progress = (100 - value) / 100.0
        stop1 = str(progress - 0.001)
        stop2 = str(progress)
        new_style_sheet = style_sheet.replace("{stop1}", stop1).replace("{stop2}", stop2)
        self.circular_progress.setStyleSheet(new_style_sheet)
        
    def popup_done(self, msg):
        
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Conversor & Divisor")
        if self.stop:
            msg = "Processo Cancelado"
            self.stop = False
        msg_box.setText(msg)
        msg_box.setIcon(QtWidgets.QMessageBox.Information)
        ui_functions.config_initial(self)
        msg_box.buttonClicked.connect(self.button_done_popup)
        msg_box.exec_()
    
    def popup_error(self, msg):
        msg_box = QtWidgets.QMessageBox()
        msg_box.setWindowTitle("Conversor & Divisor")
        msg_box.setText(msg)
        msg_box.setIcon(QtWidgets.QMessageBox.Critical)
        self.pid_process_in_progress.kill()
        ui_functions.config_initial(self)
        msg_box.buttonClicked.connect(self.button_done_popup)
        msg_box.exec_()

    def button_done_popup(self, arg):
        ui_functions.config_initial(self)
        self.progress_spinner(0)
        

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())