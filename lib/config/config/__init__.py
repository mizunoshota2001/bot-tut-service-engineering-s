__all__ = ["CONFIG"]
import json
from pathlib import Path
from collections.abc import Mapping

_PATH = {
    "config": Path(__file__).parent/'config.json',
    "settings": Path(__file__).parent/'settings.json',
}


def __update(config: dict, settings: dict) -> dict:
    for k, v in settings.items():
        config[k] = \
            __update(config.get(k, {}), v) \
            if isinstance(v, Mapping) \
            else v
    return config


CONFIG: dict = json.load(_PATH["config"].open("r", encoding="utf-8"))
__settings: dict = json.load(_PATH["settings"].open("r", encoding="utf-8"))
CONFIG = __update(CONFIG, __settings)
