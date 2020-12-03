import re
from subprocess import Popen, PIPE, CREATE_NEW_PROCESS_GROUP
from os import path, getcwd, remove


class Convert:

    regex_total_time = re.compile(
        r"\sDuration:\s[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{2}"
    )
    regex_elapsed_time = re.compile(
        r"time=\s?[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{2}"
    )

    regex_import_iso = re.compile(
        r"^Importing ISO File:\s*\|\S*\s*\|\s\([0-9]{2}"
    )
    regex_splitting = re.compile(r"^Splitting:\s*\|\S*\s*\|\s\([0-9]{2}")
    regex_iso_file = re.compile(r"^ISO File Writing:\s*\|\S*\s*\|\s\([0-9]{2}")
    regex_video_extensions = re.compile(
        r"\.(mp4|mkv|flv|swf|avchd|mov|qt|avi|wmv|mpeg|rmvb|[Ww]eb[Mm])"
    )
    regex_unknown_extension = re.compile(r"\.\S*")

    def __init__(
        self,
        input_file,
        output_path,
        process_signal=None,
        progress_signal=None,
        error_signal=None,
        done_signal=None,
        low=None,
        not_split=None,
        just_divide=None,
    ):
        self.input_file = input_file
        self.output_path = output_path
        self.process_signal = process_signal
        self.progress_signal = progress_signal
        self.error_signal = error_signal
        self.done_signal = done_signal
        self.low = low
        self.not_split = not_split
        self.just_divide = just_divide

    def ffmpeg_low(self, video_file, output_video_file):
        try:
            binary_ffmpeg = path.join(getcwd(), "bin\\ffmpeg.exe")
            with Popen(
                [
                    binary_ffmpeg,
                    "-i",
                    video_file,
                    "-s",
                    "320x240",
                    "-vcodec",
                    "mpeg4",
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
                    output_video_file,
                    "-y",
                ],
                bufsize=1,
                universal_newlines=True,
                shell=True,
                stdout=PIPE,
                stderr=PIPE,
                creationflags=CREATE_NEW_PROCESS_GROUP,
            ) as process:
                self.process_signal.emit(process)
                time_duration = 0
                elapsed_time = 0
                for line in process.stderr:
                    tt = Convert.regex_total_time.findall(line)
                    if tt:
                        time_duration = self._get_sec(tt[0].split()[1])
                    et = Convert.regex_elapsed_time.findall(line)
                    if et:
                        elapsed_time = self._get_sec(et[0].split("=")[1])
                    try:
                        self.progress_signal.emit(
                            int(elapsed_time / time_duration * 100)
                        )
                    except ZeroDivisionError:
                        pass
                process.wait()
                if process.returncode == 0:
                    return True
                else:
                    self.error_signal.emit(f"Erro: {process.returncode}")
                    return
        except Exception as e:
            self.error_signal.emit(f"Erro: {e}")

    def ffmpeg(self, video_file, output_video_file):
        try:
            binary_ffmpeg = path.join(getcwd(), "bin\\ffmpeg.exe")
            with Popen(
                [
                    binary_ffmpeg,
                    "-i",
                    video_file,
                    "-max_muxing_queue_size",
                    "9999",
                    output_video_file,
                    "-y",
                ],
                bufsize=1,
                universal_newlines=True,
                shell=True,
                stdout=PIPE,
                stderr=PIPE,
                creationflags=CREATE_NEW_PROCESS_GROUP,
            ) as process:
                self.process_signal.emit(process)
                time_duration = 0
                elapsed_time = 0
                for line in process.stderr:
                    tt = Convert.regex_total_time.findall(line)
                    if tt:
                        time_duration = self._get_sec(tt[0].split()[1])
                    et = Convert.regex_elapsed_time.findall(line)
                    if et:
                        elapsed_time = self._get_sec(et[0].split("=")[1])
                    try:
                        self.progress_signal.emit(
                            int(elapsed_time / time_duration * 100)
                        )
                    except ZeroDivisionError:
                        pass
                process.wait()
                if process.returncode == 0:
                    return True
                else:
                    self.error_signal.emit(f"Erro: {process.returncode}")
                    return
        except Exception as e:
            self.error_signal.emit(f"Erro: {e}")

    def mp4box(self, input_file, output_file):

        try:
            binary_mp4box = path.join(getcwd(), "bin\\gpac_mp4box\\mp4box.exe")
            with Popen(
                [
                    binary_mp4box,
                    "-add",
                    input_file,
                    "-split-size",
                    "30720",  # Quilobytes
                    output_file,
                ],
                bufsize=1,
                universal_newlines=True,
                shell=True,
                stdout=PIPE,
                stderr=PIPE,
                creationflags=CREATE_NEW_PROCESS_GROUP,
            ) as process:
                self.process_signal.emit(process)
                count = 0
                for line in process.stderr:
                    import_iso = Convert.regex_import_iso.findall(line)
                    split_file = Convert.regex_splitting.findall(line)
                    iso_file = Convert.regex_iso_file.findall(line)
                    if import_iso:
                        self.progress_signal.emit(
                            int(
                                count
                                / self._get_total_split_bar(self.input_file)
                                * 100
                            )
                        )
                        count += 1
                    elif split_file:
                        self.progress_signal.emit(
                            int(
                                count
                                / self._get_total_split_bar(self.input_file)
                                * 100
                            )
                        )
                        count += 1
                    elif iso_file:
                        if (
                            int(
                                count
                                / self._get_total_split_bar(self.input_file)
                                * 100
                            )
                            <= 100
                        ):
                            self.progress_signal.emit(
                                int(
                                    count
                                    / self._get_total_split_bar(
                                        self.input_file
                                    )
                                    * 100
                                )
                            )
                            count += 1
                process.wait()
                if process.returncode == 0:
                    if self.just_divide:
                        self.done_signal.emit("Divisão Concluída.")
                        return True
                    return True
                else:
                    self.error_signal.emit(f"Erro: {process.returncode}")
                    return
        except Exception as e:
            self.error_signal.emit(f"Erro: {e}")
            return

    def _get_total_split_bar(self, input_file):

        file_size = int(path.getsize(self.input_file)) / 1024
        number_of_divisions = file_size / 30720
        return 294 + 100 * number_of_divisions

    def _get_sec(self, time_str):

        h, m, s = time_str.split(":")
        return int(h) * 3600 + int(m) * 60 + int(float(s))

    def execute(self, input_file, output_path):

        search_ext = Convert.regex_video_extensions.findall(input_file)
        if search_ext:
            re_split = Convert.regex_video_extensions.split(input_file)
            file = path.split(re_split[0])[1]
        else:
            re_unknown = Convert.regex_unknown_extension.split(input_file)
            file = path.split(re_unknown[0])[1]
        output_file = path.join(output_path, f"{file}_.mp4")
        if self.low:
            result = self.ffmpeg_low(
                input_file.replace("/", "\\"),
                output_file.replace("/", "\\"),
            )
            if not result:
                return
        else:
            result = self.ffmpeg(
                input_file.replace("/", "\\"),
                output_file.replace("/", "\\"),
            )
            if not result:
                return
        if int(path.getsize(output_file)) > 31457280 and not self.not_split:
            file = path.split(output_file)[1]
            result = self.mp4box(
                output_file.replace("/", "\\"),
                path.join(output_path, f"_{file[:-5]}.mp4").replace("/", "\\"),
            )
            remove(output_file)
            if not result:
                return
            else:
                return True
        else:
            return True

    def convert_or_split(self):

        if self.just_divide:
            if int(path.getsize(self.input_file)) <= 31457280:  # Bytes
                self.done_signal.emit("Video já está em tamanho apropriado!")
                return
            file = path.split(self.input_file)[1]
            self.mp4box(
                self.input_file.replace("/", "\\"),
                path.join(self.output_path, f"_{file[:-4]}.mp4").replace(
                    "/", "\\"
                ),
            )
        else:
            if isinstance(self.input_file, list):
                videos_file = [video_file for video_file in self.input_file]
                cd_n = False
                for video_file in videos_file:
                    cd_n = self.execute(video_file, self.output_path)
                if cd_n:
                    self.done_signal.emit(
                        "Conversões e/ou Divisões Concluídas."
                    )
            else:
                cd_1 = self.execute(self.input_file, self.output_path)
                if cd_1:
                    self.done_signal.emit("Conversão e/ou Divisão Concluída.")
