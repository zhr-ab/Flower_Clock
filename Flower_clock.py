#导入依赖1
import sys
import tkinter as tk
from tkinter import messagebox
import time
import ctypes
import os
with open('run.txt', 'w') as file:
    file.write("0")
def initialize():
    global is_first_run
    #导入依赖2
    import pygame
    from PIL import Image, ImageTk
    
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
        splash_image = pygame.image.load("images/start.bmp")
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
    #导入依赖3
    import math
    import subprocess
    import mysql.connector
    import winreg
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
    # 数据库增、删、改、查
    # 数据库配置
    DB_CONFIG = {
        "host": "apiflowerclock.dpdns.org",
        "port": 3306,
        "user": "hanhan",
        "password": "Zzzhhhrrr0624@flowerclockSQL",
        "database": "flowerclockSQL_1"
    }

    def create_record(sql: str, params: tuple = None) -> int:
        """写入数据（增）"""
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount  # 返回受影响行数
        except mysql.connector.Error as err:
            messagebox.showerror(f"数据库写入失败，错误信息（如果需要的话）：{err}")
            return 0
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

    def read_record(sql: str, params: tuple = None) -> list:
        """读取数据（查）"""
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute(sql, params)
            return cursor.fetchall()  # 返回结果列表
        except mysql.connector.Error as err:
            messagebox.showerror(f"数据库读取失败，错误信息（如果需要的话）：{err}")
            return []
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

    def update_record(sql: str, params: tuple = None) -> int:
        """更新数据（改）"""
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount  # 返回受影响行数
        except mysql.connector.Error as err:
            messagebox.showerror(f"数据库更新失败，错误信息（如果需要的话）：{err}")
            return 0
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()

    def delete_record(sql: str, params: tuple = None) -> int:
        """删除数据（删）"""
        try:
            conn = mysql.connector.connect(**DB_CONFIG)
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
            return cursor.rowcount  # 返回受影响行数
        except mysql.connector.Error as err:
            messagebox.showerror(f"数据库删除失败，错误信息（如果需要的话）：{err}")
            return 0
        finally:
            if 'conn' in locals() and conn.is_connected():
                cursor.close()
                conn.close()
    #参数设定
    version = ("2025.0.0.1")
    pygame.quit()
if __name__ == "__main__":
    #初始化各模块
    # 创建主窗口但不显示
    root = tk.Tk()
    root.withdraw()
    #获取管理员权限
    if ctypes.windll.shell32.IsUserAnAdmin():
        is_first_run = None
        initialize()
        import pgzrun
        WIDTH = 1400
        HEIGHT = 800
        TITLE = "Flower Clock"
        ICON = "images/Flower_clock.ico"  # 确保路径正确

        def draw():
            screen.clear()
            if is_first_run:
                screen.fill((255,255,255))
        def update():
            pass
        pgzrun.go()
        # 销毁tkinter主窗口
        root.destroy()
    else:  
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
        time.sleep(10)
        # 弹出提示窗口
        while True:
            with open('run.txt', 'r') as file:
                if file.read() == "0":
                    result = messagebox.askretrycancel("权限错误", "获取管理员权限失败，是否重试？")
                    if not result:
                        is_first_run = None
                        initialize()
                        import pgzrun
                        WIDTH = 1400
                        HEIGHT = 800
                        TITLE = "Flower Clock"
                        ICON = "images/Flower_clock.ico"  # 确保路径正确

                        def draw():
                            screen.clear()
                            if is_first_run:
                                screen.fill((255,255,255))
                        def update():
                            pass
                        pgzrun.go()
                        # 销毁tkinter主窗口
                        root.destroy()
                    else:
                        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
                else:
                    sys.exit(0)
