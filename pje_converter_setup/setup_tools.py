from os import environ, path, getcwd, walk, listdir
from shutil import move
from time import sleep


def init_setup(progress_bar, button_finish):
    for i in range(10):
        sleep(0.1)       
        progress_bar.emit(i*100/10)
    progress_bar.emit(100)
    button_finish.emit("Finalizar")