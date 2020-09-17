from subprocess import Popen, DEVNULL
from os import path
from PyQt5 import QtWidgets


def done_popup(pb):
    msg_box = QtWidgets.QMessageBox()
    msg_box.setWindowTitle("PJe Converter")
    msg_box.setText(
        "Processo Concluído.\nVideos Convertivos e/ou Dividos"
        "\nestão no mesmo local do video original"
        )
    msg_box.setIcon(QtWidgets.QMessageBox.Information)
    msg_box.exec_()
    pb(0)


def converter_and_split(input_file, pb, button):
    video_file = input_file.text()
    button("Aguarde!")
    pb(20)
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
        stderr=DEVNULL,
        stdout=DEVNULL,
        )
    ffmpeg.wait()
    pb(70)
    if int(path.getsize(output_video_file)) > 20000000:
        ouput_file = f"{split_video_path[0]}/part_{split_video_path[1]}"
        mp4box = Popen(
            [
                "bin\\gpac_mp4box\\mp4box.exe",
                "-add", output_video_file,
                "-split-size",
                "5000",
                ouput_file
            ],
            stderr=DEVNULL,
            stdout=DEVNULL,
                )
        pb(90)
        mp4box.wait()
        pb(100)
    else:
        pb(100)
    input_file.clear()
    button("Iniciar")
    done_popup(pb)
