import sys
import tkinter as tk
from tkinter import messagebox
import time
import ctypes
with open('run.txt', 'w') as file:
    file.write("0")
def main():
    #导入依赖
    import pygame
    import pgzrun
    import os
    import winreg
    import math
    import subprocess
    with open('run.txt', 'w') as file:
        file.write("1")
    #执行次数(注册表读取实现)
    def is_first_run():
        key_path = r"Software\zhr\Flower_clock"
        value_name = "FirstRun"
        try:
            # 尝试打开现有键
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
            winreg.CloseKey(key)
            return False
        except FileNotFoundError:
            # 创建新键并写入标记值
            key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
            winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, "1")
            winreg.CloseKey(key)
            return True
        except Exception:
            return True
    #参数设定
    version = ("2025.0.0.1")
if __name__ == "__main__":
    #初始化各模块
    # 创建主窗口但不显示
    root = tk.Tk()
    root.withdraw()
    #获取管理员权限
    if ctypes.windll.shell32.IsUserAnAdmin():
        # 销毁主窗口
        root.destroy()
        main()
    else:  
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
        time.sleep(2)
        # 弹出提示窗口
        while True:
            with open('run.txt', 'r') as file:
                if file.read() == "0":
                    result = messagebox.askretrycancel("权限错误", "获取管理员权限失败，是否重试？")
                    if not result:
                        sys.exit(0)
                    else:
                        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
                else:
                    sys.exit(0)


 



