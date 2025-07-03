import sys
import tkinter as tk
from tkinter import messagebox
import time
import ctypes
import os
import winreg  # 将winreg导入移到顶部
with open('run.txt', 'w') as file:
    file.write("0")
def main():
    #导入依赖
    import math
    import subprocess
    import pygame
    from PIL import Image, ImageTk  # 确保已安装Pillow库
    
    with open('run.txt', 'w') as file:
        file.write("1")
    # 初始化 Pygame
    pygame.init()
    
    # 设置窗口大小
    window_width = 800
    window_height = 600
    
    # 创建窗口并居中显示
    screen = pygame.display.set_mode((window_width, window_height),pygame.NOFRAME)
    
    # 加载图片
    try:
        # 替换为你的图片路径
        splash_image = pygame.image.load(r"images\start.bmp")
        # 调整图片大小以适应窗口
        splash_image = pygame.transform.scale(splash_image, (window_width, window_height))
    except pygame.error as e:
        print(f"无法加载图片: {e}")
        pygame.quit()
        sys.exit()
    
    # 显示图片
    screen.blit(splash_image, (0, 0))
    pygame.display.flip()

    #初始化程序
    #执行次数(注册表读取实现)
    key_path = r"Software\zhr\Flower_clock"
    value_name = "FirstRun"
    try:
        # 尝试打开现有键
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, key_path, 0, winreg.KEY_READ)
        winreg.CloseKey(key)
        is_first_run = False
    except FileNotFoundError:
        # 创建新键并写入标记值
        key = winreg.CreateKey(winreg.HKEY_CURRENT_USER, key_path)
        winreg.SetValueEx(key, value_name, 0, winreg.REG_SZ, "1")
        winreg.CloseKey(key)
        is_first_run = True
    except Exception:
        is_first_run = True
    #参数设定
    version = ("2025.0.0.1")
    pygame.quit()
    
    import pgzrun

if __name__ == "__main__":
    #初始化各模块
    # 创建主窗口但不显示
    root = tk.Tk()
    root.withdraw()
    #获取管理员权限
    if ctypes.windll.shell32.IsUserAnAdmin():
        main()
    else:  
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
        time.sleep(10)
        # 弹出提示窗口
        while True:
            with open('run.txt', 'r') as file:
                if file.read() == "0":
                    result = messagebox.askretrycancel("权限错误", "获取管理员权限失败，是否重试？")
                    if not result:
                        main()
                    else:
                        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
                else:
                    sys.exit(0)
