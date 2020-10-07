import re
from subprocess import Popen, PIPE, DEVNULL, CREATE_NEW_PROCESS_GROUP
from os import path, getcwd, remove


class Convert:

    regex_total_time = re.compile(
        r"\sDuration:\s[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{2}"
        )
    regex_elapsed_time = re.compile(
        r"time=\s?[0-9]{2}:[0-9]{2}:[0-9]{2}\.[0-9]{2}"
        )

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
        just_divide=None
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
                    output_video_file,
                    "-y"
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
                        time_duration = self.get_sec(tt[0].split()[1])
                    et = Convert.regex_elapsed_time.findall(line)
                    if et:
                        elapsed_time = self.get_sec(et[0].split("=")[1])
                    try:
                        self.progress_signal.emit(
                            int(elapsed_time/time_duration*100)
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
                    output_video_file,
                    "-y"
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
                        time_duration = self.get_sec(tt[0].split()[1])
                    et = Convert.regex_elapsed_time.findall(line)
                    if et:
                        elapsed_time = self.get_sec(et[0].split("=")[1])
                    try:
                        self.progress_signal.emit(
                            int(elapsed_time/time_duration*100)
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
                    "-add", input_file,
                    "-split-size",
                    "30000",
                    output_file,
                    ],
                    bufsize=1,
                    universal_newlines=True,
                    shell=True,
                    stdout=DEVNULL,
                    stderr=DEVNULL,
                    creationflags=CREATE_NEW_PROCESS_GROUP,
                    ) as process:
                self.process_signal.emit(process)
                process.wait()
                if process.returncode == 0:
                    return True
                else:
                    self.error_signal.emit(f"Erro: {process.returncode}")
                    return
        except Exception as e:
            self.error_signal.emit(f"Erro: {e}")
            return

    def get_sec(self,  time_str):

        h, m, s = time_str.split(':')
        return int(h) * 3600 + int(m) * 60 + int(float(s))

    def execute(self, input_file, output_path):

        file = path.split(input_file)[1][:-4]
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
        if int(path.getsize(output_file)) > 30000000 and not self.not_split:
            file = path.split(output_file)[1]
            result = self.mp4box(
                output_file.replace("/", "\\"),
                path.join(output_path, f"_{file[:-5]}.mp4").replace("/", "\\"),
                )
            remove(output_file)
            if not result:
                return
            else:
                True
        else:
            return True

    def convert_or_split(self):

        if self.just_divide:
            file = path.split(self.input_file)[1]
            mp4box = self.mp4box(
                self.input_file.replace("/", "\\"),
                path.join(
                    self.output_path, f"_{file[:-4]}.mp4").replace("/", "\\")
                    )
            if mp4box:
                self.done_signal.emit("Processo Concluído")
        else:
            if isinstance(self.input_file, list):
                videos_file = [video_file for video_file in self.input_file]
                exec_x = ""
                for video_file in videos_file:
                    exec_x = self.execute(video_file, self.output_path)
                if exec_x:
                    self.done_signal.emit("Processo Concluído")
            else:
                exec_ = self.execute(self.input_file, self.output_path)
                if exec_:
                    self.done_signal.emit("Processo Concluído")
