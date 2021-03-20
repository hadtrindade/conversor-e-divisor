import re
import sys
from typing import Text, NoReturn, Any, Callable
from subprocess import Popen, PIPE, DEVNULL
from os import path, getcwd, remove
from conversor_divisor.settings import Settings


_windows = sys.platform == "win32"


class Convert:
    """Classe para conversão e divisão de arquivos de mídia."""

    def __init__(
        self,
        input_file: Any = None,
        output_path: Text = None,
        process_signal: Callable = None,
        progress_signal: Callable = None,
        error_signal: Callable = None,
        done_signal: Callable = None,
        line_input_file_signal: Callable = None,
        low: bool = None,
        audio_only: bool = None,
        not_split: bool = None,
        split_only: bool = None,
    ):
        """Inicialização do obj.

        :param input_file: lista ou string com o diretório da mídeia
        :param output_path: int - path de destino da mídia
        :param process_signal: callable - sinal do processo em execução
        :param progress_signal: callable - sinal do progresso do processo em execução
        :param error_signal: callable - sinal de erro na execução do processo
        :param done_signal: callable - sinal para conclusão do processo
        :param line_input_file_signal: callable - sinal para atualização de progresso de várias mídias.
        :param low: bool - vídeo em baixa qualidade
        :param audio_only: bool - rip de áudio ou conversão de áudios
        :param not_split: bool - não realizar a divisão somente a conversão
        :param split_only: bool - somente a divisão
        """
        self.input_file = input_file
        self.output_path = output_path
        self.process_signal = process_signal
        self.progress_signal = progress_signal
        self.error_signal = error_signal
        self.done_signal = done_signal
        self.line_input_file_signal = line_input_file_signal
        self.low = low
        self.audio_only = audio_only
        self.not_split = not_split
        self.split_only = split_only
        s = Settings()
        self.settings = s.read_settings()

    def _subprocess(self, *args, **kwargs):
        """Método para execução de subprocessos."""

        kwargs["bufsize"] = 1
        kwargs["stdout"] = PIPE
        kwargs["stderr"] = PIPE
        if _windows:
            from subprocess import CREATE_NEW_PROCESS_GROUP

            kwargs["creationflags"] = CREATE_NEW_PROCESS_GROUP
            kwargs["shell"] = True
        process = Popen(args, **kwargs)
        return process

    def _bar_ffmpeg(self, std_out: Text) -> NoReturn:
        """Método para progress bar.

        :param std_out: stantard output do processo ffmpeg.
        :return: None
        """

        regex_total_time = re.compile(
            r"\sDuration:\s[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{2}"
        )
        regex_elapsed_time = re.compile(
            r"time=\s?[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{2}"
        )
        time_duration = 0
        elapsed_time = 0
        for line in std_out:
            _total_time = regex_total_time.findall(line)
            if _total_time:
                time_duration = self._get_sec(_total_time[0].split()[1])
            _elapsed_time = regex_elapsed_time.findall(line)
            if _elapsed_time:
                elapsed_time = self._get_sec(_elapsed_time[0].split("=")[1])
            try:
                self.progress_signal.emit(
                    int(elapsed_time / time_duration * 100)
                )
            except ZeroDivisionError:
                pass

    def ffmpeg(self, file_in: Text, file_out: Text) -> Any:
        """Método ffmpeg para conversão de mídia.

        :param file_in: mídia de entrada
        :param fule_out: nome da mídia de saída.
        :return: Any
        """
        binary_ffmpeg = "ffmpeg"
        input_file = file_in
        output_file = file_out
        if _windows:
            binary_ffmpeg = path.join(getcwd(), r"FFmpeg\bin\ffmpeg.exe")
            binary_handbrake = path.join(
                getcwd(), r"HandBrakeCLI\HandBrakeCLI.exe"
            )
            input_file = file_in.replace("/", "\\")
            output_file = file_out.replace("/", "\\")
        args = [
            f"{binary_ffmpeg}",
            "-i",
            f"{input_file}",
            "-preset",
            "fast",
            "-max_muxing_queue_size",
            "9999",
            f"{output_file}",
            "-y",
        ]
        if self.low:
            args = [
                f"{binary_ffmpeg}",
                "-i",
                f"{input_file}",
                "-s",
                f"{self.settings['settings_convert']['resolution_value']}",
                "-preset",
                "fast",
                "-r",
                "30",
                "-b:v",
                "100000",
                "-ar",
                "44100",
                "-ac",
                "1",
                "-max_muxing_queue_size",
                "9999",
                f"{output_file}",
                "-y",
            ]
        if self.audio_only:
            path_out, file = path.split(output_file)
            output_file = path.join(path_out, f"_{file[:-5]}.mp3")
            args = [
                f"{binary_ffmpeg}",
                "-i",
                f"{input_file}",
                "-acodec",
                "libmp3lame",
                "-max_muxing_queue_size",
                "9999",
                f"{output_file}",
                "-y",
            ]
        try:
            process = self._subprocess(*args, encoding="utf-8", text=True)
            self.process_signal.emit(process)
            self._bar_ffmpeg(process.stderr)
            process.wait()
            if process.returncode:
                args_1 = [
                    f"{binary_handbrake}",
                    "-i",
                    f"{input_file}",
                    "-w",
                    "320",
                    "-l",
                    "240",
                    "-e",
                    "mpeg4",
                    "--rate",
                    "30",
                    "--vb",
                    "100",
                    "--mixdown",
                    "mono",
                    "--aencoder",
                    "av_aac",
                    "--ab",
                    "48",
                    "-o",
                    f"{output_file}",
                ]

                process_1 = self._subprocess(
                    *args_1, encoding="utf-8", text=True
                )
                self.process_signal.emit(process_1)
                for t in process_1.stderr:
                    re_proc_hb = re.compile("work result = 0")
                    re_proc_hb_error = re.compile("work result = [1-9]")
                    proc_result = re_proc_hb.findall(t)
                    proc_result_error = re_proc_hb_error.findall(t)
                    if proc_result:
                        _ = Popen(
                            ["tskill", "HandBrakeCLI"],
                            stdout=DEVNULL,
                            stderr=DEVNULL,
                        )
                    elif proc_result_error:
                        self.error_signal.emit(
                            "Erro no processo de conversão."
                        )
                        return
            return output_file
        except Exception as e:
            self.error_signal.emit(f"Erro: {e}")
            return

    def _bar_mp4box(self, video_in: Text, std_out: Text) -> NoReturn:
        """Método para progress bar.

        :param video_in: video de entrada.
        :param std_out: standart output do processo de divisão.
        :return: None
        """

        regex_import_iso = re.compile(
            r"^Importing ISO File:\s*\|\S*\s*\|\s\([0-9]{2}"
        )
        regex_splitting = re.compile(r"^Splitting:\s*\|\S*\s*\|\s\([0-9]{2}")
        regex_iso_file = re.compile(
            r"^ISO File Writing:\s*\|\S*\s*\|\s\([0-9]{2}"
        )
        total_size = self._get_total_split_bar(video_in)
        count = 0
        for line in std_out:
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

    def mp4box(self, video_in: Text, video_out: Text) -> bool:
        """Método para divisão de arquivos de vídeo.

        :param video_in: vídeo de entrada.
        :param video_out: nome do vídeo de saíde
        :return: bool
        """
        if (
            int(path.getsize(video_in))
            <= self.settings["settings_split"]["split_size_bytes"]
        ):
            self.done_signal.emit("Video já está em tamanho apropriado!")
            return
        binary_mp4box = "MP4Box"
        video_file = video_in
        output_video_file = video_out
        try:
            if _windows:
                binary_mp4box = path.join(getcwd(), r"MP4Box\mp4box.exe")
                video_file = video_in.replace("/", "\\")
                output_video_file = video_out.replace("/", "\\")
            args = [
                f"{binary_mp4box}",
                "-add",
                f"{video_file}",
                "-split-size",
                f"{self.settings['settings_split']['split_size_kilobytes']}",
                f"{output_video_file}",
            ]
            process = self._subprocess(*args, universal_newlines=True)
            self.process_signal.emit(process)
            self._bar_mp4box(video_in, process.stderr)
            process.wait()
            if process.returncode:
                self.error_signal.emit(f"Erro: {process.returncode}")
                return
            if self.split_only:
                self.done_signal.emit("Divisão Concluída.")
                return True
            return True
        except Exception as e:
            self.error_signal.emit(f"Erro: {e}")
            return

    def _get_total_split_bar(self, input_file: Text) -> int:
        """Método para retorno do tamanho do progress bar da divisão.

        :param input_file: arquivo de mídia
        :return: int
        """
        file_size = int(path.getsize(input_file)) / 1024
        number_of_divisions = file_size / 30720
        return 294 + 100 * number_of_divisions

    def _get_sec(self, time_str: Text) -> int:
        """Método para retorno do tempo em seguntos.

        :param time_str: tempo no formato '00:00:00'
        :return: int
        """
        h, m, s = time_str.split(":")
        return int(h) * 3600 + int(m) * 60 + int(float(s))

    def _execute(self, input_file, output_path):
        """Método para execução da conversão ou divisão.
        param: input_file: arquivo de mídia
        param: output_path: caminho de saída
        :return: bool
        """

        regex_extensions = re.compile(
            r"\.(mp4|mp3|wav|vob|aac|mkv|m4v|flv|swf|avchd|mov|"
            r"qt|avi|wmv|mpeg|rmvb|ogg|ac3|flac|alac|[Ww]eb[Mm])"
        )
        regex_unknown_extension = re.compile(r"\.\S*")
        search_extensions = regex_extensions.findall(input_file)
        if search_extensions:
            re_split = regex_extensions.split(input_file)
            file = path.split(re_split[0])[1]
        else:
            re_unknown = regex_unknown_extension.split(input_file)
            file = path.split(re_unknown[0])[1]
        output_file = path.join(output_path, f"{file}_.mp4")

        result = self.ffmpeg(input_file, output_file)
        if not result:
            return
        if (
            int(path.getsize(result))
            > self.settings["settings_split"]["split_size_bytes"]
            and not self.not_split
            and not self.audio_only
        ):
            file = path.split(output_file)[1]
            result = self.mp4box(
                output_file, path.join(output_path, f"_{file[:-5]}.mp4")
            )
            if not result:
                return
            remove(output_file)
            return True
        return True

    def convert_or_split(self):
        """Método para conversão e divisão de mídias"""

        if self.split_only:
            file = path.split(self.input_file)[1]
            self.mp4box(
                self.input_file,
                path.join(self.output_path, f"_{file[:-4]}.mp4"),
            )
        else:
            if isinstance(self.input_file, list):
                input_files = [file for file in self.input_file]
                media_list = None
                count = 1
                for input_file in input_files:
                    self.line_input_file_signal.emit(
                        f"Convertendo {count} de {len(input_files)}"
                    )
                    media_list = self._execute(input_file, self.output_path)
                    if not media_list:
                        break
                    count += 1
                if media_list:
                    self.done_signal.emit(
                        "Conversões e/ou Divisões Concluídas."
                    )
            else:
                unit_conversion = self._execute(
                    self.input_file, self.output_path
                )
                if unit_conversion:
                    self.done_signal.emit("Conversão e/ou Divisão Concluída.")
