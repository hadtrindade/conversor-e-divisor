from os import path
import toml


data_settings = toml.load(f"{path.dirname(__file__)}/cd_settings.toml")
SPLIT_SIZE_BYTES = data_settings["settings_split"]["split_size_bytes"]
SPLIT_SIZE_KILOBYTES = data_settings["settings_split"]["split_size_kilobytes"]
SPLIT_SIZE_MB = data_settings["settings_split"]["split_size_mb"]


def writer_config(**args):

    data_settings = toml.load(f"{path.dirname(__file__)}/cd_settings.toml")

    for k, v in args.items():
        data_settings["settings_split"][k] = v
    with open(path.join(path.dirname(__file__), "cd_settings.toml"), "w") as f:
        toml.dump(data_settings, f)
    global SPLIT_SIZE_BYTES
    global SPLIT_SIZE_KILOBYTES
    global SPLIT_SIZE_MB

    SPLIT_SIZE_BYTES = data_settings["settings_split"]["split_size_bytes"]
    SPLIT_SIZE_KILOBYTES = data_settings["settings_split"][
        "split_size_kilobytes"
    ]
    SPLIT_SIZE_MB = data_settings["settings_split"]["split_size_mb"]
