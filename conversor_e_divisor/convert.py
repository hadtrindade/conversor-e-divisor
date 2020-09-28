from subprocess import Popen, DEVNULL
from threading import Thread, Event
from itertools import cycle
from os import path, getcwd, remove
from time import sleep



def spin(spinner_signal, done):

    for i in cycle(list(range(1, 101, 20))):
        spinner_signal.emit(i)
        sleep(.3)
        if done.wait(.1):
            spinner_signal.emit(0)
            break


def ffmpeg_low(video_file, output_video_file, pid_process, error_signal):
    try:
        process = Popen(
                [
                    "bin\\ffmpeg.exe",
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
                    stderr=DEVNULL,
                    stdout=DEVNULL,
                    shell=True,
                    )
        pid_process.emit(process)
        process.wait()
    except Exception as e:
        error_signal.emit(f"Erro: {e}")
        return
    return True

def ffmpeg(video_file, output_video_file, pid_process, error_signal):
    try:
        process = Popen(
                [
                    "bin\\ffmpeg.exe",
                    "-i",
                    video_file,
                    output_video_file,
                    "-y"
                    ],
                    stderr=DEVNULL,
                    stdout=DEVNULL,
                    shell=True,
                    )
        pid_process.emit(process)
        process.wait()
    except Exception as e:
        error_signal.emit(f"Erro: {e}")
        return
    return True


def mp4box(input_file, output_file, pid_process, error_signal):

    try:
        process = Popen(
            [
                "bin\\gpac_mp4box\\mp4box.exe",
                "-add", input_file,
                "-split-size",
                "30000",
                output_file,
                ],
                stderr=DEVNULL,
                stdout=DEVNULL,
                shell=True,
                )
        pid_process.emit(process)
        process.wait()

    except Exception as e:
        error_signal.emit(f"Erro: {e}")
        return
    else:
        return True
    

def converter_split(input_file, output_path, low, not_split, pid_process, error_signal):

    try:
        videos_file = input_file
        if isinstance(input_file, str):
            videos_file = input_file.split()
        for video_file in videos_file:

            split_video_file = path.split(video_file)
            file = split_video_file[1][:-4]
            output_video_file = f"{output_path}_{file}.mp4"
            if low:
                result = ffmpeg_low(
                    video_file,
                    output_video_file,
                    pid_process,
                    error_signal
                    )
                if not result:
                    break
            else:
                result = ffmpeg(
                    video_file,
                    output_video_file,
                    pid_process,
                    error_signal
                    )
                if not result:
                    break
            if int(path.getsize(output_video_file)) > 30000000 and not not_split:
                file = path.split(output_video_file)
                result = mp4box(
                    output_video_file,
                    f"{output_path}/_{file[1]}",
                    pid_process,
                    error_signal
                    )
                remove(output_video_file)
                if not result:
                    break
    except Exception as e:
        error_signal.emit(f"Erro: {e}")
        return
    return True


def convert_or_split(input_file,
                     output_path,
                     split,
                     not_split=False,
                     spinner_signal=None,
                     done_signal=None,
                     pid_process_signal=None,
                     error_signal=None,
                     low=False,
                     ):
    
    if not split:
        done = Event()
        spinner = Thread(target=spin, args=(spinner_signal, done))
        spinner.start()
        result = converter_split(
            input_file,
            output_path,
            not_split,
            low,
            pid_process_signal,
            error_signal
            )
        done.set()
        spinner.join()
        if result:
            done_signal.emit("Processo Concluído")
    else:
        file = path.split(input_file)
        result = mp4box(
            input_file,
            f"{output_path}/_{file[1]}",
            pid_process_signal,
            error_signal
            )
        if result:
            done_signal.emit("Processo Concluído")


