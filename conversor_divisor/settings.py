from os.path import exists, join
from os import makedirs
from pathlib import Path
import toml


class Settings:
    def __init__(self):

        self.application_user_path = join(Path.home(), ".conversor&divisor")
        self.default_settings = {
            "title": "Convert Split Settings",
            "settings_split": {
                "split_size_bytes": 31457280,
                "split_size_kilobytes": 30720,
                "split_size_mb": 30,
            },
            "settings_convert": {
                "resolution_value": "320x240",
                "resolution_index_value": 0,
            },
        }

    def read_settings(self):

        try:
            data_settings = toml.load(
                join(self.application_user_path, "settings.toml")
            )
            return data_settings
        except FileNotFoundError:
            self.writer_settings("settings")
            return self.default_settings

    def writer_settings(self, setting, **args):
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
            for k, v in args.items():
                data_settings[setting][k] = v
            with open(
                join(self.application_user_path, "settings.toml"), "w"
            ) as f:
                toml.dump(data_settings, f)
