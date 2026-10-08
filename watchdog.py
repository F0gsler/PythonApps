import psutil
import sys
import os
import time


# Hvilket program skal holdes kørende
TARGET_APP = "badprograms.exe"


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.dirname(__file__), relative_path)


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
        os.startfile(app_path)
        return True
    return False


def watch_loop():
    app_path = resource_path(TARGET_APP)
    while True:
        open_app(app_path)
        time.sleep(5)


if __name__ == "__main__":
    watch_loop()