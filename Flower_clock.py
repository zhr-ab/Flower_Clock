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
    # 在导入 mysql.connector 前添加以下代码忽略特定警告
    import warnings
    warnings.filterwarnings("ignore", message=r'"is" with a literal. Did you mean "=="?',category=SyntaxWarning,module=r'mysql\.connector\.(abstracts|optionfiles)')
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
    items = language_tags = [
        'zh-cn', 'zh-tw', 'zh-hk', 'zh-sg', 'en-us', 'en-gb', 'en-au', 'en-ca', 'en-in', 'es-es',
        'es-mx', 'es-ar', 'fr-fr', 'fr-ca', 'fr-be', 'ar-sa', 'ar-eg', 'ar-ma', 'hi-in', 'pt-pt',
        'pt-br', 'ru-ru', 'ja-jp', 'de-de', 'de-at', 'ko-kr', 'it-it', 'nl-nl', 'nl-be', 'tr-tr',
        'vi-vn', 'th-th', 'pl-pl', 'sv-se', 'da-dk', 'no-no', 'fi-fi', 'id-id', 'ms-my', 'fil-ph',
        'el-gr', 'cs-cz', 'hu-hu', 'ro-ro', 'bg-bg', 'uk-ua', 'he-il', 'fa-ir', 'ur-pk', 'bn-bd',
        'ta-in', 'te-in', 'mr-in', 'gu-in', 'kn-in', 'ml-in', 'or-in', 'pa-in', 'si-lk', 'km-kh',
        'lo-la', 'my-mm', 'ne-np', 'uz-uz', 'kk-kz', 'az-az', 'ka-ge', 'hy-am', 'et-ee', 'lv-lv',
        'lt-lt', 'sk-sk', 'sl-si', 'hr-hr', 'sr-rs', 'mk-mk', 'sq-al', 'sw-ke', 'am-et', 'yo-ng',
        'ha-ng', 'ig-ng', 'zu-za', 'xh-za', 'af-za', 'st-ls', 'rw-rw', 'mg-mg', 'eu-es', 'ca-es',
        'gl-es', 'cy-gb', 'ga-ie', 'gd-gb', 'mt-mt', 'is-is', 'lb-lu', 'bo-cn', 'ug-cn', 'mn-mn'
    ]
    language_native_with_region = [
        "中文(中国)", "中文(台灣)", "中文(香港)", "中文(新加坡)", "English(United States)",
        "English(United Kingdom)", "English(Australia)", "English(Canada)", "English(India)", "español(España)",
        "español(México)", "español(Argentina)", "français(France)", "français(Canada)", "français(Belgique)",
        "العربية(السعودية)", "العربية(مصر)", "العربية(المغرب)", "हिन्दी(भारत)", "português(Portugal)",
        "português(Brasil)", "русский(Россия)", "日本語(日本)", "Deutsch(Deutschland)", "Deutsch(Österreich)",
        "한국어(대한민국)", "italiano(Italia)", "Nederlands(Nederland)", "Nederlands(België)", "Türkçe(Türkiye)",
        "Tiếng Việt(Việt Nam)", "ไทย(ประเทศไทย)", "polski(Polska)", "svenska(Sverige)", "dansk(Danmark)",
        "norsk(Norge)", "suomi(Suomi)", "Bahasa Indonesia(Indonesia)", "Bahasa Melayu(Malaysia)", "Filipino(Pilipinas)",
        "ελληνικά(Ελλάδα)", "čeština(Česko)", "magyar(Magyarország)", "română(România)", "български(България)",
        "українська(Україна)", "עברית(ישראל)", "فارسی(ایران)", "اردو(پاکستان)", "বাংলা(বাংলাদেশ)",
        "தமிழ்(இந்தியா)", "తెలుగు(భారతదేశం)", "मराठी(भारत)", "ગુજરાતી(ભારત)", "ಕನ್ನಡ(ಭಾರತ)",
        "മലയാളം(ഇന്ത്യ)", "ଓଡ଼ିଆ(ଭାରତ)", "ਪੰਜਾਬੀ(ਭਾਰਤ)", "සිංහල(ශ්‍රී ලංකාව)", "ភាសាខ្មែរ(កម្ពុជា)",
        "ພາສາລາວ(ລາວ)", "မြန်မာဘာသာ(မြန်မာ)", "नेपाली(नेपाल)", "Oʻzbekcha(Oʻzbekiston)", "қазақ тілі(Қазақстан)",
        "azərbaycan dili(Azərbaycan)", "ქართული(საქართველო)", "հայերեն(Հայաստան)", "eesti(Eesti)", "latviešu(Latvija)",
        "lietuvių(Lietuva)", "slovenčina(Slovensko)", "slovenščina(Slovenija)", "hrvatski(Hrvatska)", "српски(Србија)",
        "македонски(Северна Македонија)", "shqip(Shqipëria)", "Kiswahili(Kenya)", "አማርኛ(ኢትዮጵያ)", "Yorùbá(Nàìjíríà)",
        "Hausa(Nijeriya)", "Igbo(Naịjịrịa)", "isiZulu(iNingizimu Afrika)", "isiXhosa(iMzantsi Afrika)", "Afrikaans(Suid-Afrika)",
        "Sesotho(Lesotho)", "Kinyarwanda(U Rwanda)", "Malagasy(Madagasikara)", "euskara(Espainia)", "català(Espanya)",
        "galego(España)", "Cymraeg(Prydain)", "Gaeilge(Éire)", "Gàidhlig(Alba)", "Malti(Malta)",
        "íslenska(Ísland)", "Lëtzebuergesch(Lëtzebuerg)", "བོད་ཡིག(རྒྱ་ནག)", "ئۇيغۇر تىلى(جۇڭخۇا)", "монгол хэл(Монгол)"
    ]

    selected_index = -1
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
            if True:
                screen.fill((255,255,255))
                pic = Actor("fcsettl.png",(350,450))
                pic.draw()
                screen.draw.text()
        def update():
            pass
        pgzrun.go()
        # 销毁tkinter主窗口
        root.destroy()
    else:  
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, sys.argv[0], None, 1)
        sys.exit(0)
