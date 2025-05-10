#导入依赖
import pygame
import pgzrun
import os
import sys
import turtle
import winreg
#执行次数
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
        return False  # 防止权限不足等情况导致崩溃
#初始化变量
project_path=os.getcwd()
#设置窗口宽高
WIDTH = 1400
HEIGHT = 700
TITLE = "Flower_clock"
#播放音乐
music.play(project_path+"/music/1.mp3")
#创建角色
bg=Actor(project_path+"/images/bg.png")
#设置图标模式（真（True）代表不设置图标；假（False）代表设置图标）
icon_set = False
#循环更新
def update():
    global icon_set
    if not icon_set:
        try:
            icon = pygame.image.load('images/花钟.ico')
            pygame.display.set_icon(icon)
            icon_set = True
        except:
            pass
#绘制角色
def draw():
    screen.clear()
    bg.draw()
#最终调用
pgzrun.go()


