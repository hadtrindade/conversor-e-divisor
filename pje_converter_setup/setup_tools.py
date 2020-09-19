from shutil import copy, copytree, rmtree
from os import listdir, path, chdir, getcwd, makedirs
from contextlib import contextmanager
from time import sleep


def init_setup(dst, progress_bar, button_finish):

    source = "C:\\Users\\hadd\\Desktop\\compartilhamento\\app"
    if path.exists(dst):
        rmtree(dst)
    makedirs(dst, mode=777)
    old_path = getcwd()
    chdir(source)
    files = [paths for paths in listdir(".")]
    for i in range(len(files)):
        if path.isfile(files[i]):
            copy(files[i], dst)
            progress_bar.emit(i*100/len(files))
        elif path.isdir(files[i]):
            copytree(files[i], path.join(dst, files[i]))
            progress_bar.emit(i*100/len(files))
    sleep(1)
    chdir(old_path)
    progress_bar.emit(100)
    button_finish.emit("Finalizar")
    
