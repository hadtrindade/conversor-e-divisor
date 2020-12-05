from configparser import ConfigParser
from os import path


config = ConfigParser(allow_no_value=True,
                      inline_comment_prefixes="#",
                      strict=False,
                      )

config.read(f"{path.dirname(__file__)}/cd_settings.ini")
default_config = dict(config['DEFAULT'])


def writer_config(**args):

    for k, v in args.items():
        config['DEFAULT'][k] = v
    with open(f"{path.dirname(__file__)}/cd_settings.ini", "w") as configfile:
        config.write(configfile)


SPLIT_SIZE_BYTES = config['DEFAULT']['split_size_bytes']
SPLIT_SIZE_KILOBYTES = config['DEFAULT']['split_size_kilobytes']
SPLIT_SIZE_MB = config['DEFAULT']['split_size_mb']
