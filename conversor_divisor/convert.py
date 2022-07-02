import re
from os import path
from pathlib import Path
from subprocess import DEVNULL, PIPE, Popen
from typing import Callable, List, Text

from conversor_divisor.settings import PLATFORM, Settings


class Convert:
    """Classe para conversão e divisão de arquivos de mídia."""

    def __init__(
        self,
        media: List[Path] = None,
        output: Path = None,
        process_signal: Callable = None,
        progress_signal: Callable = None,
        error_signal: Callable = None,
        error_signal_warm: Callable = None,
        done_signal: Callable = None,
        line_input_file_signal: Callable = None,
        low: bool = None,
        audio_only: bool = None,
        split: bool = True,
        split_only: bool = None,
    ):
        """Inicialização do obj.

        :param media: lista ou string com o diretório da mídeia
        :param output: int - path de destino da mídia
        :param process_signal: callable - sinal do processo em execução
        :param progress_signal: callable - sinal do progresso do processo em execução
        :param error_signal: callable - sinal de erro na execução do processo
        :param error_signal_warm: callable - sinal de erro na execução de uma lista de processos
        :param done_signal: callable - sinal para conclusão do processo
        :param line_input_file_signal: callable - sinal para atualização de progresso de várias mídias.
        :param low: bool - vídeo em baixa qualidade
        :param audio_only: bool - rip de áudio ou conversão de áudios
        :param split: bool - realizer a divisão após a conversão
        :param split_only: bool - somente a divisão
        """
        self.media = media
        self.output = output
        self.process_signal = process_signal
        self.progress_signal = progress_signal
        self.error_signal = error_signal
        self.error_signal_warm = error_signal_warm
        self.done_signal = done_signal
        self.line_input_file_signal = line_input_file_signal
        self.low = low
        self.audio_only = audio_only
        self.split = split
        self.split_only = split_only
        s = Settings()
        self.settings = s.read()
        self.ffmpeg_binary = 'ffmpeg'
        self.mp4box_binary = 'MP4box'

        if PLATFORM == 'win32':
            self.handbrake_binary = (
                Path(__file__)
                .parent
                .joinpath('HandBrakeCLI', 'HandBrakeCLI.exe')
                .absolute()
            )
            self.ffmpeg_binary = (
                Path(__file__).parent.joinpath('FFmpeg', 'bin', 'ffmpeg.exe').absolute()
            )
            self.mp4box_binary = (
                Path(__file__).parent.joinpath('MP4Box', 'mp4box.exe').absolute()
            )

    def _subprocess(self, *args, **kwargs):
        """Método para execução de subprocessos."""

        kwargs['bufsize'] = 1
        kwargs['stdout'] = PIPE
        kwargs['stderr'] = PIPE
        if PLATFORM == 'win32':
            from subprocess import CREATE_NEW_PROCESS_GROUP

            kwargs['creationflags'] = CREATE_NEW_PROCESS_GROUP
            kwargs['shell'] = True
        process = Popen(args, **kwargs)
        return process

    def handbrake(self, media: Path) -> Path:

        output = self.output.joinpath(f'convertido_{media.stem}.mp4')
        args = [
            self.handbrake_binary,
            '-i',
            media.absolute(),
            '-o',
            output.absolute(),
        ]
        if self.low:
            args = [
                self.handbrake_binary,
                '-i',
                media.absolute(),
                '-w',
                f"{self.settings['convert']['resolution'].split('x')[0]}" '-l',
                f"{self.settings['convert']['resolution'].split('x')[1]}" '-e',
                'mpeg4',
                '--rate',
                '30',
                '--vb',
                '100',
                '--mixdown',
                'mono',
                '--aencoder',
                'av_aac',
                '--ab',
                '48',
                '-o',
                output.absolute(),
            ]
        try:
            process = self._subprocess(*args, encoding='utf-8', text=True)
            self.process_signal.emit(process)
            re_error = re.compile('work result = [1-9]')
            for t in process.stderr:
                error = re_error.findall(t)
                if error:
                    _ = Popen(
                        ['tskill', 'HandBrakeCLI'],
                        stdout=DEVNULL,
                        stderr=DEVNULL,
                    )
                    return process.returncode
            return output
        except Exception as e:
            return e

    def _bar_ffmpeg(self, stdout: Text) -> None:
        """Método para progress bar.

        :param stdout: stantard output do processo ffmpeg.
        :return: None
        """

        regex_total_time = re.compile(
            r'\sDuration:\s[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{2}'
        )
        regex_elapsed_time = re.compile(
            r'time=\s?[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{2}'
        )

        def get_sec(time_str):
            h, m, s = time_str.split(':')
            return int(h) * 3600 + int(m) * 60 + int(float(s))

        time_duration = 0
        elapsed_time = 0
        for line in stdout:
            _total_time = regex_total_time.findall(line)
            if _total_time:
                time_duration = get_sec(_total_time[0].split()[1])
            _elapsed_time = regex_elapsed_time.findall(line)
            if _elapsed_time:
                elapsed_time = get_sec(_elapsed_time[0].split('=')[1])
            try:
                self.progress_signal.emit(
                    int(elapsed_time / time_duration * 100)
                )
            except ZeroDivisionError:
                pass

    def ffmpeg(self, media: Path) -> Path:
        """Método ffmpeg para conversão de mídia.

        :param media: midia a ser convertida
        :return: Any
        """
        output = self.output.joinpath(f'convertido_{media.stem}.mp3')
        args = [
            self.ffmpeg_binary,
            '-i',
            media.absolute(),
            '-acodec',
            'libmp3lame',
            '-max_muxing_queue_size',
            '9999',
            output.absolute(),
            '-y',
        ]
        if not self.audio_only:
            output = self.output.joinpath(f'convertido_{media.stem}.mp4')
            args = [
                self.ffmpeg_binary,
                '-i',
                media.absolute(),
                '-preset',
                'fast',
                '-max_muxing_queue_size',
                '9999',
                output.absolute(),
                '-y',
            ]
            if self.low:
                args = [
                    self.ffmpeg_binary,
                    '-i',
                    media.absolute(),
                    '-s',
                    f"{self.settings['convert']['resolution']}",
                    '-preset',
                    'fast',
                    '-r',
                    '30',
                    '-b:v',
                    '100000',
                    '-ar',
                    '44100',
                    '-ac',
                    '1',
                    '-max_muxing_queue_size',
                    '9999',
                    output.absolute(),
                ]
        try:
            process = self._subprocess(*args, encoding='utf-8', text=True)
            self.process_signal.emit(process)
            self._bar_ffmpeg(process.stderr)
            process.wait()
            if process.returncode:
                return process.returncode
            return output
        except Exception as e:
            return e

    def _bar_mp4box(self, media: Path, stdout: Text) -> None:
        """Método para progress bar.

        :param media: media a ser dividida
        :param stdout: standart output do processo de divisão.

        :return: None
        """

        regex_import_iso = re.compile(
            r'^Importing ISO File:\s*\|\S*\s*\|\s\([0-9]{2}'
        )
        regex_splitting = re.compile(r'^Splitting:\s*\|\S*\s*\|\s\([0-9]{2}')
        regex_iso_file = re.compile(
            r'^ISO File Writing:\s*\|\S*\s*\|\s\([0-9]{2}'
        )
        file_size = int(path.getsize(media.absolute())) / 1024
        total_size = 294 + 100 * (file_size / 30720)

        count = 0
        for line in stdout:
            import_iso = regex_import_iso.findall(line)
            split_file = regex_splitting.findall(line)
            iso_file = regex_iso_file.findall(line)
            if import_iso:
                self.progress_signal.emit(int(count / total_size * 100))
                count += 1
            elif split_file:
                self.progress_signal.emit(int(count / total_size * 100))
                count += 1
            elif iso_file:
                if int(count / total_size * 100) <= 100:
                    self.progress_signal.emit(int(count / total_size * 100))
                    count += 1

    def mp4box(self, media: Path) -> None:
        """Método para divisão de arquivos de vídeo.

        :param media: media a ser dividida
        :return: None
        """
        size_media = None
        if media.suffix == '.mp3':
            size_media = self.settings['split']['a_split_size_b']
            split_size_kilobytes = self.settings['split']['a_split_size_kb']
        else:
            size_media = self.settings['split']['v_split_size_b']
            split_size_kilobytes = self.settings['split']['v_split_size_kb']

        if int(path.getsize(media.absolute())) <= size_media:
            return 'minimum_size'

        try:
            args = [
                self.mp4box_binary,
                '-add',
                media.absolute(),
                '-split-size',
                f'{split_size_kilobytes}',
                self.output.joinpath(f'div_{media.name}'),
            ]
            process = self._subprocess(*args, universal_newlines=True)
            self.process_signal.emit(process)
            self._bar_mp4box(media=media, stdout=process.stderr)
            process.wait()
            if process.returncode:
                return process.returncode
            return
        except Exception as e:
            return e

    def _execute(self, media: Path) -> None:
        """Método para execução da conversão ou divisão.

        :param media: media a ser processada
        :return: None
        """
        convert_result = self.ffmpeg(media=media)
        if not isinstance(convert_result, Path):
            if self.audio_only or PLATFORM != 'win32':
                return 1
            convert_result = self.handbrake(media=media)
            if not isinstance(convert_result, Path):
                return 1
        if self.split:
            mp4box_result = self.mp4box(media=convert_result)
            if not mp4box_result:
                convert_result.unlink()
            elif mp4box_result == 'minimum_size':
                return
            elif mp4box_result:
                return 2

    def convert_or_split(self) -> None:
        """Método para conversão e divisão de mídias."""

        if self.split_only:
            mp4box_result = self.mp4box(media=self.media)
            if mp4box_result == 'minimum_size':
                self.done_signal.emit('Mídia já está em tamanho apropriado!')
                return
            elif mp4box_result:
                self.error_signal.emit(
                    'Ocorreu um erro no processo de divisão.'
                )
                return
            elif not mp4box_result:
                self.done_signal.emit('Divisão Concluída.')
                return
        if isinstance(self.media, list):
            count = 1
            for media in self.media:
                self.line_input_file_signal.emit(
                    f'Convertendo {count} de {len(self.media)}'
                )
                result_execute = self._execute(media=Path(media))
                if result_execute:
                    self.error_signal_warm.emit(
                        f'Erro ao processar a mídia: {Path(media).name}'
                    )
                    continue
                count += 1
            self.done_signal.emit(
                f'{count - 1} Conversões e/ou Divisões Concluídas.'
            )
        else:
            execute_result = self._execute(media=self.media)
            if execute_result == 1:
                self.error_signal.emit('Erro no processo de conversão.')
            elif execute_result == 2:
                self.error_signal.emit(
                    'Ocorreu um erro no processo de divisão.'
                )
            else:
                self.done_signal.emit('Conversão e/ou Divisão Concluída.')
