from subprocess import Popen, DEVNULL
from os import path
from time import sleep

def converter_and_split(
    input_file,
    ouput_path,
    progress_bar,
    button,
    done
    ):

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
        ffmpeg = Popen(
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
        ffmpeg.wait()

        if int(path.getsize(output_video_file)) > 30000000:
            output_file = f"{ouput_path}/part_{file}.mp4"
            mp4box = Popen(
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
            mp4box.wait()
        count+=1

    progress_bar.emit(100)
    button.emit("Iniciar")
    done.emit("ok")