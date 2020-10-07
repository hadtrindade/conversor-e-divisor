from os import path
from subprocess import Popen
from pathlib import Path
from PySide2 import QtCore, QtWidgets, QtGui


def config_initial(app):

    app.button_start.setDisabled(True)
    app.button_start_split.setDisabled(True)
    app.button_output_file.setDisabled(True)
    app.button_source_file.setEnabled(True)
    app.button_source_file_split.setEnabled(True)
    app.button_output_file_split.setDisabled(True)
    app.check_box_split.setEnabled(True)
    app.radio_button_normal.setEnabled(True)
    app.radio_button_low.setEnabled(True)
    app.button_stop.hide()
    app.line_edit_input_file.hide()
    app.line_edit_input_file_split.hide()
    app.line_edit_output_file.setDisabled(True)
    app.line_edit_output_file_split.setDisabled(True)
    app.progress_bar.setValue(0)
    app.progress_bar.hide()  


def config_processing(app):

    app.button_start.setDisabled(True)
    app.button_start_split.setDisabled(True)
    app.button_output_file.setDisabled(True)
    app.button_output_file_split.setDisabled(True)
    app.button_source_file.setDisabled(True)
    app.button_source_file_split.setDisabled(True)
    app.check_box_split.setDisabled(True)
    app.radio_button_normal.setDisabled(True)
    app.radio_button_low.setDisabled(True)
    app.button_stop.setVisible(True)
    app.line_edit_output_file.setDisabled(True)
    app.line_edit_input_file.setDisabled(True)
    app.button_open_folder_split.setVisible(True)
    app.progress_bar.setVisible(True)


def toggle_menu(app, max_width, enable):
    if enable:
        width = app.frame_left_menu.width()
        max_extend = max_width
        standard = 70
        if width == standard:
            width_extended = max_extend
            app.button_toggle.setText(" Menu")
            app.button_page_1.setText(" Converter e Dividir")
            app.button_page_2.setText(" Dividir")
            app.button_settings.setText(" Opções")
        else:
            width_extended = standard
            app.button_toggle.setText("")
            app.button_page_1.setText("")
            app.button_page_2.setText("")
            app.button_settings.setText("")

        app.animation = QtCore.QPropertyAnimation(app.frame_left_menu, b"minimumWidth")
        app.animation.setDuration(400)
        app.animation.setStartValue(width)
        app.animation.setEndValue(width_extended)
        app.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        app.animation.start()


def open_ouput_folder(app):
    try:
        path_output_folder = app.output_path.replace("/","\\")
    except TypeError:
        Popen(f"explorer /open, \"{app.output_path}\"")
    else:
        Popen(f"explorer /open, \"{path_output_folder}\"")


def get_file_video(app):
    app.split = False
    home = Path.home()
    file_name, _ = QtWidgets.QFileDialog.getOpenFileNames(
        None, "Procurar Arquivo de Video", r"%s" % home,
        "Video Files (*.mp4 *.mkv *.flv *.swf *.avchd *.mov *.qt *.avi *.wmv *.mpeg *.rmvb);;All Files (*)",
        )
    
    if not file_name:
        return

    if len(file_name) == 1:
        paths = path.split(file_name[0])
        app.input_file = file_name[0]
        app.output_path = paths[0]
        app.line_edit_input_file.setText(paths[1])
        app.line_edit_output_file.setText(app.output_path)
        app.line_edit_input_file.setVisible(True)
        app.line_edit_output_file.setVisible(True)
        app.button_start.setEnabled(True)
        app.button_output_file.setEnabled(True)
        app.button_open_folder.setVisible(True)
        app.line_edit_input_file.setDisabled(True)
        app.line_edit_output_file.setDisabled(True)

    else:
        paths = path.split(file_name[0])
        app.input_file = file_name
        app.output_path = paths[0]
        app.line_edit_input_file.setText(f"Você Adicinou {len(file_name)} Videos")
        app.line_edit_output_file.setText(app.output_path)
        app.line_edit_input_file.setVisible(True)
        app.line_edit_output_file.setVisible(True)
        app.button_start.setEnabled(True)
        app.button_output_file.setEnabled(True)
        app.button_open_folder.setVisible(True)
        app.line_edit_input_file.setDisabled(True)
        app.line_edit_output_file.setDisabled(True)


def get_path_output_name(app):
    home = Path.home()
    output_path = QtWidgets.QFileDialog.getExistingDirectory(
        None, "Procurar Diretório de Destino.", r"%s" % home,)
    app.output_path = output_path
    app.line_edit_output_file.setText(app.output_path)
    app.button_output_file.setDisabled(True)


def get_file_video_split(app):
    app.split = True
    home = Path.home()
    file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
        None, "Procurar Arquivo de Video", r"%s" % home,
        "Video Files (*.mp4 )",
        )
    
    if not file_name:
        return
    app.input_file_split = file_name 
    file = path.split(file_name)
    app.output_path = file[0]
    app.line_edit_input_file_split.setText(file[1])
    app.button_start_split.setEnabled(True)
    app.button_output_file_split.setEnabled(True)
    app.line_edit_output_file_split.setText(file[0])
    app.line_edit_output_file_split.setVisible(True)
    app.line_edit_input_file_split.setVisible(True)
    app.line_edit_input_file_split.setDisabled(True)
    app.line_edit_output_file_split.setDisabled(True)


def get_path_output_name_split(app):
    home = Path.home()
    path_dst = QtWidgets.QFileDialog.getExistingDirectory(
        None, "Procurar Diretório de Destino.", r"%s" % home,)
    app.output_path = path_dst
    app.line_edit_output_file_split.setText(app.output_path)
    app.line_edit_output_file_split.setDisabled(True)




