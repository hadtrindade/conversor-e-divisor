from os.path import exists, join
from os import makedirs
from pathlib import Path
from typing import Dict, Text, NoReturn
import toml


class Settings:
    """Classe para gravação de configurações."""

    def __init__(self):

        self.application_user_path = join(Path.home(), ".conversor&divisor")
        self.default_settings = {
            "title": "Convert Split Settings",
            "settings_split": {
                "split_size_bytes_v": 31457280,
                "split_size_kilobytes_v": 30720,
                "split_size_mb_v": 30,
                "split_size_bytes_a": 10485760,
                "split_size_kilobytes_a": 10240,
                "split_size_mb_a": 10,
            },
            "settings_convert": {
                "resolution_value": "320x240",
                "resolution_index_value": 0,
            },
        }

    def read_settings(self) -> Dict:
        """Método para leitura das configurações.

        :return: dict
        """
        try:
            data_settings = toml.load(
                join(self.application_user_path, "settings.toml")
            )
            return data_settings
        except FileNotFoundError:
            self.writer_settings("settings")
            return self.default_settings

    def writer_settings(self, setting: Text, **kwargs) -> NoReturn:
        """Método para gravação de configurações.

        :param setting: tipo de configuração a ser gravada
        :return: None
        """
        if not exists(join(self.application_user_path, "settings.toml")):
            makedirs(self.application_user_path)
            with open(
                join(self.application_user_path, "settings.toml"), "w"
            ) as f:
                toml.dump(self.default_settings, f)

        else:
            data_settings = toml.load(
                join(self.application_user_path, "settings.toml")
            )
            for k, v in kwargs.items():
                data_settings[setting][k] = v
            with open(
                join(self.application_user_path, "settings.toml"), "w"
            ) as f:
                toml.dump(data_settings, f)
