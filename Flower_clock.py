#导入依赖
import pygame
import pgzrun
import os
import sys
import turtle
import winreg
import math
import time
import subprocess
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
        return False  # 防止权限不足等情况导致崩溃
#测试用，新手引导开发完成后需删除
def is_first_run():
    return True
#初始化变量
project_path=os.getcwd()
pointer=0
I_F_R_N=is_first_run()
clock = pygame.time.Clock()
#设置窗口宽高、标题
WIDTH = 1400
HEIGHT = 700
TITLE = "Flower_clock"
#设置图标模式（真（True）代表不设置图标；假（False）代表设置图标）
icon_set = False
#循环更新
def update():
    #设置窗口图标
    global icon_set,pointer
    if not icon_set:
        try:
            icon = pygame.image.load('images/花钟.ico')
            pygame.display.set_icon(icon)
            icon_set = True
        except:
            pass
    #指针转动
    dt = clock.tick(60) / 1000.0  # 获取帧间隔时间(秒)
    pointer += 6 * dt  # 按实际时间增量旋转
#播放音频
if I_F_R_N:
    music.play(project_path+"/music/1.mp3")
#创建角色
bg=Actor(project_path+"/images/bg.png")
#绘制角色
def draw():
    global pointer
    screen.clear()
    radius = 100 / 2  # 半径
    end_x = 700 + radius * math.cos(math.radians(pointer))  # 末端x坐标
    end_y = 400 + radius * math.sin(math.radians(pointer))  # 末端y坐标

    if I_F_R_N:
        screen.draw.filled_circle((700, 400), 55, (255, 255, 255))
        screen.draw.filled_circle((700, 400), 50, (0, 0, 0))
        pygame.draw.line(screen.surface, (255, 255, 255), (end_x, end_y), (700,400), 5)
    else:
        bg.draw()
#最终调用
pgzrun.go()
if turtle.textinput("确认退出","请输入yes以确认退出：") == "yes":
    turtle.bye()
    sys.exit(0)
else:
    turtle.bye()
    pygame.mixer.init()
    if I_F_R_N:
        music.play(project_path+"/music/1.mp3")
    pgzrun.go()
    



