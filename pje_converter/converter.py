from subprocess import Popen, DEVNULL
from os import path


def converter_and_split(video_file):
    split_video_path = path.split(video_file)
    output_video_file = f"{split_video_path[0]}/convertido_{split_video_path[1]}"
    ffmpeg = Popen(
        [
            "bin\\ffmpeg.exe",
            "-i",
            video_file,
            output_video_file
        ], 
        stderr=DEVNULL,
        stdout=DEVNULL,
        )
    ffmpeg.wait()

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
            stderr=DEVNULL,
            stdout=DEVNULL,
                )
        mp4box.wait()
