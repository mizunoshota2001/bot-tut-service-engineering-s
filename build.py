import os
import sys
import shutil
import subprocess
from pathlib import Path
from venv import EnvBuilder
os.chdir(Path(__file__).parent)

_PATH = {
    "venv": Path("./.venv"),
    "requirements": Path("./requirements.txt"),
    "lib-settings": Path("./lib/config/config/settings.json"),
    "settings": Path("./settings.json"),
}


def make_venv():
    if _PATH["venv"].exists():
        return
    _builder = EnvBuilder(with_pip=True)
    _builder.create(_PATH["venv"])


def install_requirements():
    if sys.platform == "win32":
        _pip = _PATH["venv"] / "Scripts" / "pip.exe"
    else:
        _pip = _PATH["venv"] / "bin" / "pip"
    subprocess.run([str(_pip), "install", "--upgrade",
                   "-r", str(_PATH["requirements"])])


def update_settings():
    shutil.copy(_PATH["settings"], _PATH["lib-settings"])


def main():
    print("Processing...\n")
    make_venv()
    update_settings()
    install_requirements()
    print("\ndone.")


if __name__ == "__main__":
    main()
