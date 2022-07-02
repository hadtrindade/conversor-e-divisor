import sys
from pathlib import Path
from typing import Any, Dict, Text

import toml

PLATFORM = sys.platform


class Settings:
    """Classe para gravação de configurações."""

    def __init__(self):

        self.path = Path.home().joinpath('.conversor&divisor')
        self.default = {
            'title': 'Convert & Split Settings',
            'split': {
                'v_split_size_b': 31457280,
                'v_split_size_kb': 30720,
                'v_split_size_mb': 30,
                'a_split_size_b': 10485760,
                'a_split_size_kb': 10240,
                'a_split_size_mb': 10,
            },
            'convert': {
                'resolution': '320x240',
                'resolution_index': 0,
            },
        }

    def read(self) -> Dict:
        """Método para leitura das configurações.

        :return: dict
        """
        try:
            file_settings = self.path.joinpath('settings.toml').absolute()
            data = toml.load(file_settings)
            if data.keys() == self.default.keys():
                if data['split'].keys() == self.default['split'].keys():
                    if (
                        data['convert'].keys()
                        == self.default['convert'].keys()
                    ):
                        return data
                    else:
                        file_settings.unlink()
                        return self.write()
                else:
                    file_settings.unlink()
                    return self.write()
            else:
                file_settings.unlink()
                return self.write()
        except FileNotFoundError:
            return self.write()

    def write(self, setting: Text = None, **kwargs: Any) -> None:
        """Método para gravação de configurações.

        :param setting: tipo de configuração a ser gravada
        :return: None
        """
        file_settings = self.path.joinpath('settings.toml').absolute()
        if not self.path.exists():
            self.path.mkdir()
        if self.path.exists() and not file_settings.exists():
            with open(file_settings, 'w') as file:
                toml.dump(self.default, file)
                return self.default
        else:
            data = toml.load(file_settings)
            for k, v in kwargs.items():
                data[setting][k] = v
            with open(
                self.path.joinpath('settings.toml').absolute(), 'w'
            ) as f:
                toml.dump(data, f)
            return self.read()
