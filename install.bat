pyinstaller --noconfirm ^
     --onedir --windowed ^
     --icon "ui/main_icone.ico" ^
     --name "Conversor_Divisor" --log-level "DEBUG" ^
     --hidden-import "toml" ^
     --add-data "conversor_divisor/__init__.py;." ^
     --add-data "conversor_divisor/cd_settings.toml;." ^
     --add-data "conversor_divisor/config.py;." ^
     --add-data "conversor_divisor/convert.py;." ^
     --add-data "conversor_divisor/resources_cd_rc.py;." ^
     --add-data "conversor_divisor/ui_cd.py;." ^
     --add-data "conversor_divisor/ui_functions.py;." ^
     --add-data "conversor_divisor/worker.py;."  ^
     --add-data "FFmpeg;FFmpeg/" ^
     --add-data "MP4Box;MP4Box/" ^
     "conversor_divisor/app.py"



