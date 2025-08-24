import pystray
import threading
import sys
import os
import subprocess
from PIL import Image

def create_tray_icon():
    menu = (
        pystray.MenuItem('显示窗口', show_window),
        pystray.MenuItem('退出', exit_app)
    )
    icon = pystray.Icon("tray_icon", Image.open("images/Flower_clock.ico"), "Flower Clock", menu)
    icon.run()

def show_window(icon, item):
    subprocess.Popen("Flower_Clock.exe", shell=True)

def exit_app(icon, item):
    icon.stop()

tray_thread = threading.Thread(target=create_tray_icon)
tray_thread.start()











