pyinstaller --noconfirm ^
     --onedir --windowed ^
     --icon "ui/img/main_icone.ico" ^
     --name "Conversor_Divisor" --log-level "DEBUG" ^
     --hidden-import "toml" ^
     --hidden-import "conversor_divisor" ^
     --add-data "conversor_divisor/FFmpeg;conversor_divisor/FFmpeg/" ^
     --add-data "conversor_divisor/MP4Box;conversor_divisor/MP4Box/" ^
     --add-data "conversor_divisor/HandBrakeCLI;conversor_divisor/HandBrakeCLI/" ^
     "conversor_divisor/app.py"



