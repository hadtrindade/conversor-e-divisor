from pathlib import Path
from subprocess import Popen

from PySide2 import QtCore, QtWidgets

from conversor_divisor.settings import PLATFORM, Settings


def config_init(app: object) -> None:
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


def config_init_split(app: object) -> None:
    """Factory para inicialização do app modo dividir."""

    app.button_start_split.setDisabled(True)
    app.button_source_file_split.setEnabled(True)
    app.button_output_file_split.setDisabled(True)
    app.button_stop_split.hide()
    app.line_edit_input_file_split.hide()
    app.line_edit_output_file_split.setDisabled(True)
    app.progress_bar_split.setValue(0)
    app.progress_bar_split.hide()


def processing_cd(app: object) -> None:
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


def processing_split(app: object) -> None:
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


def toggle_menu(app: object, max_width: int, enable: bool) -> None:

    """Factory para animação do manu."""
    if enable:
        width = app.frame_left_menu.width()
        max_extend = max_width
        standard = 70
        if width == standard:
            width_extended = max_extend
            app.button_toggle.setText(' Menu')
            app.button_page_1.setText(' Converter e Dividir')
            app.button_page_2.setText(' Dividir')
            app.button_settings.setText(' Opções')
        else:
            width_extended = standard
            app.button_toggle.setText('')
            app.button_page_1.setText('')
            app.button_page_2.setText('')
            app.button_settings.setText('')

        app.animation = QtCore.QPropertyAnimation(
            app.frame_left_menu, b'minimumWidth'
        )
        app.animation.setDuration(400)
        app.animation.setStartValue(width)
        app.animation.setEndValue(width_extended)
        app.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        app.animation.start()


def open_output_convert(app: object) -> None:
    """Factory para abrir destino das mídias."""
    if PLATFORM == 'win32':
        from os import startfile

        startfile(app.output_convert, 'Open')
    elif PLATFORM == 'darwin':
        Popen(['open', f'{app.output_convert}'])
    else:
        Popen(['xdg-open', f'{app.output_convert}'])


def open_output_split(app: object) -> None:
    """Factory para abrir destino das mídias."""
    if PLATFORM == 'win32':
        from os import startfile

        startfile(app.output_split, 'Open')
    elif PLATFORM == 'darwin':
        Popen(['open', f'{app.output_split}'])
    else:
        Popen(['xdg-open', f'{app.output_split}'])


def get_media_convert(app: object) -> None:
    """Factory para buscar as mídias."""

    files = """Video Files (*.mp4 *.mkv *.flv *.swf *.avchd *.mov
            *.qt *.avi *.wmv *.m4v *.mpeg *.rmvb *.vob)"""
    if app.audio_only:
        files = """Audio Files (*.mp3 *.wav *.flac *.aac *.wma *.ogg
                *.alac *.aiff *.ape *.ac3)"""
    app.split = False
    media, _ = QtWidgets.QFileDialog.getOpenFileNames(
        None,
        'Procurar Arquivo de Mídia',
        r'%s' % app.current_directory_convert,
        f'{files};;All Files (*)',
    )

    if not media:
        return

    if len(media) == 1:
        app.media_convert = Path(media[0])
        app.output_convert = app.media_convert.parent.absolute()
        app.current_directory_convert = str(
            app.media_convert.parent.absolute()
        )
        app.line_edit_input_file.setText(app.media_convert.name)
        app.line_edit_input_file.setToolTip(str(app.media_convert.absolute()))
        app.line_edit_output_file.setText(str(app.output_convert.stem))
        app.line_edit_output_file.setToolTip(str(app.output_convert))
        app.line_edit_input_file.setVisible(True)
        app.line_edit_output_file.setVisible(True)
        app.button_start.setEnabled(True)
        app.button_output_file.setEnabled(True)
        app.button_open_folder.setVisible(True)
        app.line_edit_input_file.setDisabled(True)
        app.line_edit_output_file.setDisabled(True)

    else:
        app.media_convert = media
        app.output_convert = Path(media[0]).parent.absolute()
        app.current_directory_convert = str(app.output_convert)
        app.line_edit_input_file.setText(f'Mídias a converter: {len(media)}')
        app.line_edit_input_file.setToolTip(
            ''.join([f'{file}\n' for file in media])
        )
        app.line_edit_output_file.setText(str(app.output_convert.stem))
        app.line_edit_output_file.setToolTip(str(app.output_convert))
        app.line_edit_input_file.setVisible(True)
        app.line_edit_output_file.setVisible(True)
        app.button_start.setEnabled(True)
        app.button_output_file.setEnabled(True)
        app.button_open_folder.setVisible(True)
        app.line_edit_input_file.setDisabled(True)
        app.line_edit_output_file.setDisabled(True)


def get_output_convert(app: object) -> None:
    """Factory para busca do path de saída das conversões."""

    output = QtWidgets.QFileDialog.getExistingDirectory(
        None,
        'Procurar Diretório de Destino.',
        r'%s' % app.current_directory_convert,
    )
    if output:
        app.output_convert = Path(output)
        app.line_edit_output_file.setText(app.output_convert.stem)
        app.line_edit_output_file.setToolTip(
            str(app.output_convert.absolute())
        )


def get_media_split(app: object) -> None:
    """Factory para busca de vídeo para divisão."""
    app.split = True
    media, _ = QtWidgets.QFileDialog.getOpenFileName(
        None,
        'Procurar Arquivo de Video',
        r'%s' % app.current_directory_split,
        'Media Files (*.mp4 *mp3)',
    )

    if not media:
        return
    app.media_split = Path(media)
    app.output_split = app.media_split.parent.absolute()
    app.current_directory_split = app.media_split.parent.absolute()
    app.line_edit_input_file_split.setText(app.media_split.name)
    app.line_edit_input_file_split.setToolTip(str(app.media_split.absolute()))
    app.button_start_split.setEnabled(True)
    app.button_output_file_split.setEnabled(True)
    app.line_edit_output_file_split.setText(app.output_split.stem)
    app.line_edit_output_file_split.setToolTip(str(app.output_split))
    app.line_edit_output_file_split.setVisible(True)
    app.line_edit_input_file_split.setVisible(True)
    app.line_edit_input_file_split.setDisabled(True)
    app.line_edit_output_file_split.setDisabled(True)


def get_output_split(app: object) -> None:
    """Factory para busca de path de saida."""
    output = QtWidgets.QFileDialog.getExistingDirectory(
        None,
        'Procurar Diretório de Destino.',
        r'%s' % app.current_directory_split,
    )
    if output:
        app.output_split = Path(output)
        app.line_edit_output_file_split.setText(app.output_split.stem)
        app.line_edit_output_file_split.setToolTip(str(app.output_split))
        app.line_edit_output_file_split.setDisabled(True)


def set_settings(app: object) -> None:
    """Factory para escrita  de configurações."""
    size_value_v = app.spinBox_split_size.text()
    value_kilobytes_v = int(size_value_v) * 1024
    value_bytes_v = value_kilobytes_v * 1024
    size_value_a = app.spinBox_split_size_audio.text()
    value_kilobytes_a = int(size_value_a) * 1024
    value_bytes_a = value_kilobytes_a * 1024

    s = Settings()
    s.write(
        'split',
        v_split_size_b=value_bytes_v,
        v_split_size_kb=value_kilobytes_v,
        v_split_size_mb=int(size_value_v),
        a_split_size_b=value_bytes_a,
        a_split_size_kb=value_kilobytes_a,
        a_split_size_mb=int(size_value_a),
    )
    resolution_value = app.resolution_settings.currentText()
    resolution_index_value = app.resolution_settings.currentIndex()
    s.write(
        'convert',
        resolution=resolution_value,
        resolution_index=resolution_index_value,
    )
    app.popup_done('Configurações Aplicadas')
