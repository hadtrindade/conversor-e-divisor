pyinstaller --noconfirm ^
     --onedir --windowed ^
     --icon "ui/img/main_icone.ico" ^
     --name "Conversor_Divisor" --log-level "DEBUG" ^
     --hidden-import "toml" ^
     --hidden-import "ui_conversor_divisor" ^
     --add-data "conversor_divisor/__init__.py;." ^
     --add-data "conversor_divisor/settings.py;." ^
     --add-data "conversor_divisor/convert.py;." ^
     --add-data "conversor_divisor/ui_functions.py;." ^
     --add-data "conversor_divisor/worker.py;."  ^
     --add-data "FFmpeg;FFmpeg/" ^
     --add-data "MP4Box;MP4Box/" ^
     "conversor_divisor/app.py"



