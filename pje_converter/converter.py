from subprocess import Popen, DEVNULL
from os import path, getcwd
from time import sleep


def ffmpeg_low(video_file, output_video_file):
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
    process.wait()
    

def ffmpeg(video_file, output_video_file):
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
    process.wait()
    


def mp4box(output_video_file, output_file):
    process = Popen(
        [
            "bin\\gpac_mp4box\\mp4box.exe",
            "-add", output_video_file,
            "-split-size",
            "30000",
            output_file,
            ],
            stderr=DEVNULL,
            stdout=DEVNULL,
            shell=True,
            )
    process.wait()
    


def converter_and_split(
    input_file,
    ouput_path,
    low,
    progress_bar,
    button,
    done,
    error,
    ):

    try:
        video_files = input_file.toPlainText().split("\n")
        if len(video_files) > 1:
            video_files.pop()
        else:
            progress_bar.emit(50)
        button.emit("Aguarde!")
        count = 0
        for video_file in video_files:
            if len(video_files) > 1:
                progress_bar.emit(count*100/len(video_files))

            split_video_file = path.split(video_file)
            file = split_video_file[1][:-4]
            output_video_file = f"{ouput_path}/convertido_{file}.mp4"
            if low:
                ffmpeg_low(video_file, output_video_file)
                
            ffmpeg(video_file, output_video_file)

            if int(path.getsize(output_video_file)) > 30000000:
                output_file = f"{ouput_path}/part_{file}.mp4"
                mp4box(output_video_file, output_file)
            count+=1

        progress_bar.emit(100)
        button.emit("Iniciar")
        done.emit("ok")
    except Exception as e:
        error.emit(f"ERRO EMITIDO{e}, {getcwd()}")