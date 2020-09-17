from subprocess import Popen, DEVNULL
from os import path


def converter_and_split(input_file, progress_bar, button, done):

    video_file = input_file.text()
    button.emit("Aguarde!")
    progress_bar.emit(40)
    split_video_path = path.split(video_file)
    file = split_video_path[1][:-4]
    output_video_file = f"{split_video_path[0]}/convertido_{file}.mp4"
    ffmpeg = Popen(
        [
            "bin\\ffmpeg.exe",
            "-i",
            video_file,
            output_video_file,
            "-y"
        ], 

        )
    ffmpeg.wait()
    progress_bar.emit(70)
    if int(path.getsize(output_video_file)) > 30000000:
        ouput_file = f"{split_video_path[0]}/part_{split_video_path[1]}"
        mp4box = Popen(
            [
                "bin\\gpac_mp4box\\mp4box.exe",
                "-add", output_video_file,
                "-split-size",
                "30000",
                ouput_file
            ],

                )
        progress_bar.emit(90)
        mp4box.wait()
        progress_bar.emit(100)
    else:
        progress_bar.emit(100)
    input_file.clear()
    progress_bar.emit(0)
    button.emit("Iniciar")
    done.emit("ok")
