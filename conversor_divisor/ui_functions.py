import sys
from os import path
from subprocess import Popen
from typing import NoReturn
from PySide2 import QtCore, QtWidgets
from conversor_divisor.settings import Settings


_windows = sys.platform == "win32"


def config_init(app: object) -> NoReturn:
    """Factory para inicialização do app modo converter e dividir."""

    app.button_start.setDisabled(True)
    app.button_output_file.setDisabled(True)
    app.button_source_file.setEnabled(True)
    app.check_box_split.setEnabled(True)
    app.check_box_audio.setEnabled(True)
    app.radio_button_normal.setEnabled(True)
    app.radio_button_low.setEnabled(True)
    app.button_stop.hide()
    app.line_edit_input_file.hide()
    app.line_edit_output_file.setDisabled(True)
    app.progress_bar.setValue(0)
    app.progress_bar.hide()


def config_init_split(app: object) -> NoReturn:
    """Factory para inicialização do app modo dividir."""

    app.button_start_split.setDisabled(True)
    app.button_source_file_split.setEnabled(True)
    app.button_output_file_split.setDisabled(True)
    app.button_stop_split.hide()
    app.line_edit_input_file_split.hide()
    app.line_edit_output_file_split.setDisabled(True)
    app.progress_bar_split.setValue(0)
    app.progress_bar_split.hide()


def processing_cd(app: object) -> NoReturn:
    """Factory para bloqueio de funções.
    Bloqueias funções do modo converter e dividir
    até que o processamento seja concluído
    """
    app.button_start.setDisabled(True)
    app.button_output_file.setDisabled(True)
    app.button_source_file.setDisabled(True)
    app.check_box_split.setDisabled(True)
    app.check_box_audio.setDisabled(True)
    app.radio_button_normal.setDisabled(True)
    app.radio_button_low.setDisabled(True)
    app.button_stop.setVisible(True)
    app.line_edit_output_file.setDisabled(True)
    app.line_edit_input_file.setDisabled(True)
    app.progress_bar.setVisible(True)


def processing_split(app: object) -> NoReturn:
    """Factory para bloqueio de funções.
    Bloqueias funções do modo dividir até
    que o processamento seja concluído
    """
    app.button_start_split.setDisabled(True)
    app.button_source_file_split.setDisabled(True)
    app.button_output_file_split.setDisabled(True)
    app.button_stop_split.setVisible(True)
    app.button_open_folder_split.setVisible(True)
    app.progress_bar_split.setVisible(True)


def toggle_menu(app: object, max_width: int, enable: bool) -> NoReturn:

    """Factory para animação do manu."""
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

        app.animation = QtCore.QPropertyAnimation(
            app.frame_left_menu, b"minimumWidth"
        )
        app.animation.setDuration(400)
        app.animation.setStartValue(width)
        app.animation.setEndValue(width_extended)
        app.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        app.animation.start()


def open_output_folder_convert(app: object) -> NoReturn:
    """Factory para abrir destino das mídias."""
    if _windows:
        from os import startfile

        startfile(app.output_path_convert, "Open")
    else:
        Popen(["xdg-open", f"{app.output_path_convert}"])


def open_output_folder_split(app: object) -> NoReturn:
    """Factory para abrir destino das mídias."""
    if _windows:
        from os import startfile

        startfile(app.output_path_split, "Open")
    else:
        Popen(["xdg-open", f"{app.output_path_split}"])


def get_media(app: object) -> NoReturn:
    """Factory para buscar as mídias."""

    files = """Video Files (*.mp4 *.mkv *.flv *.swf *.avchd *.mov
            *.qt *.avi *.wmv *.m4v *.mpeg *.rmvb *.vob)"""
    if app.audio_only:
        files = """Audio Files (*.mp3 *.wav *.flac *.aac *.wma *.ogg
                *.alac *.aiff *.ape *.ac3)"""
    app.split = False
    file_name, _ = QtWidgets.QFileDialog.getOpenFileNames(
        None,
        "Procurar Arquivo de Mídia",
        r"%s" % app.current_directory_convert,
        f"{files};;All Files (*)",
    )

    if not file_name:
        return

    if len(file_name) == 1:
        paths = path.split(file_name[0])
        app.input_file_convert = file_name[0]
        app.output_path_convert = paths[0]
        app.current_directory_convert = paths[0]
        app.line_edit_input_file.setText(paths[1])
        app.line_edit_input_file.setToolTip(file_name[0])
        app.line_edit_output_file.setText(
            path.split(app.output_path_convert)[1]
        )
        app.line_edit_output_file.setToolTip(paths[0])
        app.line_edit_input_file.setVisible(True)
        app.line_edit_output_file.setVisible(True)
        app.button_start.setEnabled(True)
        app.button_output_file.setEnabled(True)
        app.button_open_folder.setVisible(True)
        app.line_edit_input_file.setDisabled(True)
        app.line_edit_output_file.setDisabled(True)

    else:
        paths = path.split(file_name[0])
        app.input_file_convert = file_name
        app.output_path_convert = paths[0]
        app.current_directory_convert = paths[0]
        app.line_edit_input_file.setText(
            f"Mídias a converter: {len(file_name)}"
        )
        app.line_edit_input_file.setToolTip(
            "".join([f"{file}\n" for file in file_name])
        )
        app.line_edit_output_file.setText(
            path.split(app.output_path_convert)[1]
        )
        app.line_edit_output_file.setToolTip(app.output_path_convert)
        app.line_edit_input_file.setVisible(True)
        app.line_edit_output_file.setVisible(True)
        app.button_start.setEnabled(True)
        app.button_output_file.setEnabled(True)
        app.button_open_folder.setVisible(True)
        app.line_edit_input_file.setDisabled(True)
        app.line_edit_output_file.setDisabled(True)


def get_path_output_convert(app: object) -> NoReturn:
    """Factory para busca do path de saída das conversões."""

    output_path = QtWidgets.QFileDialog.getExistingDirectory(
        None,
        "Procurar Diretório de Destino.",
        r"%s" % app.current_directory_convert,
    )
    if output_path:
        app.output_path_convert = output_path
        app.line_edit_output_file.setText(
            path.split(app.output_path_convert)[1]
        )
        app.line_edit_output_file.setToolTip(app.output_path_convert)


def get_file_media_split(app: object) -> NoReturn:
    """Factory para busca de vídeo para divisão."""
    app.split = True
    file_name, _ = QtWidgets.QFileDialog.getOpenFileName(
        None,
        "Procurar Arquivo de Video",
        r"%s" % app.current_directory_split,
        "Media Files (*.mp4 *mp3)",
    )

    if not file_name:
        return
    app.input_file_split = file_name
    file = path.split(file_name)
    app.output_path_split = file[0]
    app.current_directory_split = file[0]
    app.line_edit_input_file_split.setText(file[1])
    app.line_edit_input_file_split.setToolTip(app.input_file_split)
    app.button_start_split.setEnabled(True)
    app.button_output_file_split.setEnabled(True)
    app.line_edit_output_file_split.setText(path.split(file[0])[1])
    app.line_edit_output_file_split.setToolTip(app.output_path_split)
    app.line_edit_output_file_split.setVisible(True)
    app.line_edit_input_file_split.setVisible(True)
    app.line_edit_input_file_split.setDisabled(True)
    app.line_edit_output_file_split.setDisabled(True)


def get_path_output_split(app: object) -> NoReturn:
    """Factory para busca de path de saida."""
    output_path = QtWidgets.QFileDialog.getExistingDirectory(
        None,
        "Procurar Diretório de Destino.",
        r"%s" % app.current_directory_split,
    )
    if output_path:
        app.output_path_split = output_path
        app.line_edit_output_file_split.setText(
            path.split(app.output_path_split)[1]
        )
        app.line_edit_output_file_split.setToolTip(app.output_path_split)
        app.line_edit_output_file_split.setDisabled(True)


def set_settings(app: object) -> NoReturn:
    """Factory para escrita  de configurações."""
    size_value_v = app.spinBox_split_size.text()
    value_kilobytes_v = int(size_value_v) * 1024
    value_bytes_v = value_kilobytes_v * 1024
    size_value_a = app.spinBox_split_size_audio.text()
    value_kilobytes_a = int(size_value_a) * 1024
    value_bytes_a = value_kilobytes_a * 1024

    s = Settings()
    s.writer_settings(
        "settings_split",
        split_size_bytes_v=value_bytes_v,
        split_size_kilobytes_v=value_kilobytes_v,
        split_size_mb_v=int(size_value_v),
        split_size_bytes_a=value_bytes_a,
        split_size_kilobytes_a=value_kilobytes_a,
        split_size_mb_a=int(size_value_a),
    )
    resolution_value = app.resolution_settings.currentText()
    resolution_index_value = app.resolution_settings.currentIndex()
    s.writer_settings(
        "settings_convert",
        resolution_value=resolution_value,
        resolution_index_value=resolution_index_value,
    )
    app.popup_done("Configurações Aplicadas")
