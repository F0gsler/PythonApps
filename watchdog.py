import psutil
import sys
import os
import time


# Hvilket program skal holdes kørende
TARGET_APP = "badprograms.exe"


def app_dir():
    # Mappen hvor dette program selv ligger.
    # Virker både når det køres som .py og som .exe (frozen).
    if getattr(sys, 'frozen', False):
        return os.path.dirname(sys.executable)
    return os.path.dirname(os.path.abspath(__file__))


def is_app_running(app_name):
    for proc in psutil.process_iter(['name']):
        try:
            if app_name.lower() in proc.info['name'].lower():
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return False


def open_app(app_path):
    app_name = os.path.basename(app_path)
    if not is_app_running(app_name):
        if os.path.exists(app_path):
            os.startfile(app_path)
            return True
    return False


def watch_loop():
    # Leder efter badprograms.exe ved siden af watchdog selv
    app_path = os.path.join(app_dir(), TARGET_APP)
    while True:
        open_app(app_path)
        time.sleep(5)


if __name__ == "__main__":
    watch_loop()