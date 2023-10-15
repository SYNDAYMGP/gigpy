# БИБЛИОТЕКИ
import pyautogui
import time
import random
import subprocess
import pyperclip
import os

# Стандартные настройки
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.8
duration = random.uniform(2, 3)

# 22
while True:
    while True:
        if pyautogui.locateOnScreen('22WR.PNG') is not None or pyautogui.locateOnScreen('33WR.PNG') is not None:
            if pyautogui.locateOnScreen('22WR.PNG') is not None:
                pyautogui.click('22WR.PNG')
            if pyautogui.locateOnScreen('33WR.PNG') is not None:
                pyautogui.click('33WR.PNG')
            for _ in range(1):
                # сохранение TH
                pyautogui.click(252, 252, duration=0.5)
                pyautogui.moveTo(800, 200, duration=0.3)
                pyautogui.doubleClick()
                time.sleep(10)
                pyautogui.click(1820, 980, duration=0.3)
                pyautogui.typewrite("=1=", interval=0.05)
                pyautogui.click(770, 510, duration=0.3)
                pyautogui.click(16, 262, duration=0.3)
                pyautogui.mouseDown()
                pyautogui.moveTo(212, 262, duration=0.3)
                pyautogui.mouseUp()
                pyautogui.hotkey('ctrl', 'c')
                pyautogui.click(863, 1059, duration=0.3)
                pyautogui.doubleClick(199, 197, duration=0.3)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(767, 1060, duration=0.3)
                pyautogui.click(1700, 165, duration=0.3)
                pyautogui.click(788, 101, duration=0.3)
                pyautogui.click(920, 96, duration=0.3)

                # WHISPER
                # Команда для выполнения в cmd и сохранения вывода в файл
                cmd_command = 'whisper "=1=.mp3" --model medium > feb1.txt'
                # Выполнить команду в cmd
                result = subprocess.run(cmd_command, shell=True)
                # Проверить, выполнена ли команда успешно
                if result.returncode == 0:
                    print("Команда успешно выполнена. Результат сохранен в feb1.txt.")
                else:
                    print("Команда завершилась с ошибкой.")

                # Открываем файл для чтения с явным указанием кодировки UTF-8
                with open('=1=.txt', 'r', encoding='utf-8') as source_file:
                    # Считываем содержимое из wwd1.txt
                    file_contents = source_file.read()

                # Копируем содержимое файла в буфер обмена
                pyperclip.copy(file_contents)

                print("Информация из =1=.txt скопирована в буфер обмена.")

                # открытие CLAUDE + делаем первый запрос
                pyautogui.click(715, 1065, duration=0.3)
                time.sleep(7)
                pyautogui.click(795, 86, duration=0.3)
                pyautogui.typewrite("https://claude.ai/", interval=0.01)
                time.sleep(5)
                pyautogui.press('enter')
                time.sleep(12)
                # создание 1 сапорт чат (0x0) компитентность
                pyautogui.click(540, 508, duration=0.3)
                pyautogui.typewrite(
                    "I'm giving you a conversation between the seller and the client, you should, based on this conversation, evaluate the professionalism of the seller on a ten-point scale and give a ",
                    interval=0.01)
                pyautogui.typewrite(
                    " couple of words describing his professionalism, the answer should not contain any comments and explanations and be something like this ((9/10) high level of service), give ",
                    interval=0.01)
                pyautogui.typewrite(" the answer very very briefly, also give the answer only in Russian ",
                                    interval=0.01)
                pyautogui.hotkey('ctrl', 'v')


                def locate_image():
                    try:
                        pyautogui.click('KRY1.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                time.sleep(22)
                # переход
                pyautogui.click(47, 177, duration=0.5)
                # создание 2 сапорт чат (&x&) вежливость
                pyautogui.click(540, 508, duration=0.3)
                pyautogui.typewrite(
                    " I am bringing you a conversation between a seller and a client, you should, based on this conversation, evaluate the seller's politeness on a ten-point scale and give a couple of words ",
                    interval=0.01)
                pyautogui.typewrite(
                    " describing his politeness, the answer should not contain any comments and explanations ",
                    interval=0.01)
                pyautogui.typewrite(
                    " and be something like this ((9/10) punctual answers), give an answer very, very briefly, also give an answer only in Russian",
                    interval=0.01)
                pyautogui.hotkey('ctrl', 'v')


                def locate_image():
                    try:
                        pyautogui.click('KRY1.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                time.sleep(22)
                # переход
                pyautogui.click(47, 177, duration=0.5)
                # создание 3 сапорт чат (8x8) удовлетворенность клиента
                pyautogui.click(540, 508, duration=0.3)
                pyautogui.typewrite(
                    "I am bringing you a conversation between a seller and a client, you should, based on this conversation, evaluate the satisfaction of the client on a ten-point scale and give a couple of ",
                    interval=0.01)
                pyautogui.typewrite(
                    " words describing his satisfaction the answer should not contain any comments and explanations and be something like this ",
                    interval=0.01)
                pyautogui.typewrite(
                    " ((9/10) the client is satisfied) give an answer very, very briefly, also give an answer only in Russian",
                    interval=0.01)
                pyautogui.hotkey('ctrl', 'v')


                def locate_image():
                    try:
                        pyautogui.click('KRY1.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                time.sleep(22)
                # копирую и вчтавляю из 3 сапорта
                pyautogui.moveTo(950, 305, duration=0.3)
                pyautogui.scroll(-2500)


                def locate_image():
                    try:
                        pyautogui.click('copy66.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.click(470, 859, duration=0.3)
                pyautogui.click(863, 1059, duration=0.3)
                pyautogui.doubleClick(1191, 197, duration=0.3)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(715, 1065, duration=0.3)
                pyautogui.click(899, 163, duration=0.3)
                pyautogui.click(920, 283, duration=0.3)
                time.sleep(2)
                pyautogui.click(1229, 639, duration=0.3)
                time.sleep(2)
                pyautogui.click(898, 709, duration=0.3)
                # копирую и вставляю из 2 сапорта
                pyautogui.moveTo(950, 305, duration=0.5)
                pyautogui.scroll(-2500)


                def locate_image():
                    try:
                        pyautogui.click('copy66.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.click(470, 859, duration=0.3)
                pyautogui.click(863, 1059)
                pyautogui.doubleClick(829, 197, duration=0.3)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(715, 1065, duration=0.3)
                pyautogui.click(899, 163, duration=0.3)
                pyautogui.click(920, 283, duration=0.3)
                time.sleep(2)
                pyautogui.click(1229, 639, duration=0.3)
                time.sleep(2)
                pyautogui.click(898, 709, duration=0.3)
                # копирую и вставляю из 1 сапорта
                pyautogui.moveTo(950, 305, duration=0.5)
                pyautogui.scroll(-2500)


                def locate_image():
                    try:
                        pyautogui.click('copy66.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.click(470, 859, duration=0.3)
                pyautogui.click(863, 1059)
                pyautogui.doubleClick(534, 197, duration=0.3)
                pyautogui.hotkey('ctrl', 'v')
                # обновление экселя
                pyautogui.click(185, 857, duration=0.3)
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.click(715, 1065, duration=0.3)
                pyautogui.click(899, 163, duration=0.3)
                pyautogui.click(920, 283, duration=0.3)
                time.sleep(2)
                pyautogui.click(1229, 639, duration=0.3)
                time.sleep(2)
                pyautogui.click(1881, 24, duration=0.3)
                pyautogui.click(767, 1060, duration=1)
                # удаление файлов
                # Задайте путь к директории, из которой нужно удалять файлы
                directory_path = r"D:\bot\pythonn"
                # Задайте список имен файлов, которые нужно удалить
                files_to_delete = ["=1=.json", "=1=.mp3", "=1=.srt", "=1=.tsv", "=1=.txt", "=1=.vtt"]
                try:
                    # Перебираем файлы и удаляем те, у которых имя в списке files_to_delete
                    for file_to_delete in files_to_delete:
                        file_path = os.path.join(directory_path, file_to_delete)
                        if os.path.exists(file_path):
                            os.remove(file_path)
                            print(f"Удален файл: {file_path}")
                        else:
                            print(f"Файл не найден: {file_path}")
                    print("Удаление завершено.")
                except Exception as e:
                    print(f"Произошла ошибка: {str(e)}")
            break
    continue

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
м + ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------


# ВЕРСИЯ 21.09.2023       ПОЛНОСТЬЮ рабочая ВРЕМЯ 8МИН
import pyautogui
import time
import random

# стандартные настройки
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.8
duration = random.uniform(2, 3)
time.sleep(5)

# 22
while True:
    while True:
        if pyautogui.locateOnScreen('22WR.PNG') is not None or pyautogui.locateOnScreen('33WR.PNG') is not None:
            if pyautogui.locateOnScreen('22WR.PNG') is not None:
                pyautogui.click('22WR.PNG')
            if pyautogui.locateOnScreen('33WR.PNG') is not None:
                pyautogui.click('33WR.PNG')
            for _ in range(1):
                # сохранение TH
                pyautogui.click(252, 252, duration=0.5)
                pyautogui.moveTo(800, 200, duration=0.3)
                pyautogui.doubleClick()
                time.sleep(10)
                pyautogui.click(1820, 980, duration=0.3)
                pyautogui.typewrite("=1=", interval=0.05)
                pyautogui.click(770, 510, duration=0.3)
                pyautogui.click(16, 262, duration=0.3)
                pyautogui.mouseDown()
                pyautogui.moveTo(212, 262, duration=0.3)
                pyautogui.mouseUp()
                pyautogui.hotkey('ctrl', 'c')
                pyautogui.click(863, 1059, duration=0.3)
                pyautogui.doubleClick(199, 197, duration=0.3)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(767, 1060, duration=0.3)
                pyautogui.click(1700, 165, duration=0.3)
                pyautogui.click(788, 101, duration=0.3)
                pyautogui.click(920, 96, duration=0.3)

                # открытие нейро WH
                pyautogui.click(715, 1065, duration=0.3)
                time.sleep(7)
                pyautogui.click(795, 86, duration=0.3)
                pyautogui.typewrite("https://colab.research.google.com/drive/18JMytvzNybyes7TwAv2r0R1FOZnXmaBv",
                                    interval=0.01)
                time.sleep(5)
                pyautogui.press('enter')
                time.sleep(16)
                pyautogui.click(35, 387, duration=0.3)
                pyautogui.moveTo(574, 347, duration=0.3)
                pyautogui.scroll(2000)
                pyautogui.click(815, 1045, duration=0.3)
                pyautogui.moveTo(1690, 376, duration=0.3)
                pyautogui.doubleClick()
                pyautogui.click(1508, 163, duration=0.3)
                pyautogui.mouseDown()
                pyautogui.moveTo(254, 593, duration=0.3)
                pyautogui.mouseUp()
                time.sleep(3)
                pyautogui.click(1309, 676, duration=0.3)
                pyautogui.click(815, 1045, duration=0.3)
                pyautogui.click(1406, 163, duration=0.3)
                pyautogui.rightClick()
                pyautogui.click(1265, 569, duration=0.3)
                pyautogui.click(1883, 19, duration=0.3)
                pyautogui.click(626, 242, duration=0.3)
                time.sleep(37)
                pyautogui.scroll(-900)
                time.sleep(2)


                def locate_image():
                    try:
                        pyautogui.click('Qq.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.move(-93, 0, duration=0.2)
                pyautogui.click()
                # time.sleep(295)
            break
    while True:
        if pyautogui.locateOnScreen('kkk.PNG') is not None:
            pyautogui.doubleClick('kkk.PNG', duration=1)
            for _ in range(1):
                # выделение txt
                pyautogui.moveTo(1428, 248, duration=0.5)
                pyautogui.mouseDown()
                pyautogui.scroll(-1400)
                pyautogui.moveTo(1474, 965, duration=1)
                pyautogui.mouseUp()
                pyautogui.hotkey('ctrl', 'c')

                # закрытие и подчищените WH  ###
                for _ in range(6):
                    pyautogui.moveTo(536, 406, duration=0.5)
                    pyautogui.click()
                    pyautogui.click(240, 531, duration=0.5)
                    pyautogui.click(1091, 654, duration=0.5)
                    time.sleep(2)
                pyautogui.click(1885, 18, duration=0.3)

                # открытие CLAUDE + делаем первый запрос
                pyautogui.click(715, 1065, duration=0.3)
                time.sleep(7)
                pyautogui.click(795, 86, duration=0.3)
                pyautogui.typewrite("https://claude.ai/", interval=0.01)
                time.sleep(5)
                pyautogui.press('enter')
                time.sleep(12)

                # создание 1 сапорт чат (0x0) компитентность
                pyautogui.click(540, 508, duration=0.3)
                pyautogui.typewrite(
                    "I will provide you with the correspondence between the manager and the client, your task is to evaluate it according to the criterion   ",
                    interval=0.01)
                pyautogui.typewrite(
                    "1) the competence of the manager. You also have to give an answer only in Russian, and your entire answer should be very, very brief, ",
                    interval=0.01)
                pyautogui.typewrite("no more than 10 words. At the end, give a rating on a ten-point scale",
                                    interval=0.01)
                pyautogui.hotkey('ctrl', 'v')


                def locate_image():
                    try:
                        pyautogui.click('KRY.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                time.sleep(22)
                # переход
                pyautogui.click(47, 177, duration=0.5)
                # создание 2 сапорт чат (&x&) вежливость
                pyautogui.click(540, 508, duration=0.3)
                pyautogui.typewrite(
                    "I will provide you with the correspondence between the manager and the client, your task is to evaluate it according to the criterion  ",
                    interval=0.01)
                pyautogui.typewrite(
                    "1) politeness of the manager. You also have to give an answer only in Russian, and your entire answer should be very, very brief,  ",
                    interval=0.01)
                pyautogui.typewrite("no more than 10 words. At the end, give a rating on a ten-point scale ",
                                    interval=0.01)
                pyautogui.hotkey('ctrl', 'v')


                def locate_image():
                    try:
                        pyautogui.click('KRY.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                time.sleep(22)
                # переход
                pyautogui.click(47, 177, duration=0.5)
                # создание 3 сапорт чат (8x8) удовлетворенность клиента
                pyautogui.click(540, 508, duration=0.3)
                pyautogui.typewrite(
                    "I will provide you with the correspondence between the manager and the client, your task is to evaluate it according to the criterion ",
                    interval=0.01)
                pyautogui.typewrite(
                    "1)customer satisfaction with the response received. You also have to give an answer only in Russian, and your entire answer should be very, very brief,  ",
                    interval=0.01)
                pyautogui.typewrite("no more than 10 words. At the end, give a rating on a ten-point scale ",
                                    interval=0.01)
                pyautogui.hotkey('ctrl', 'v')


                def locate_image():
                    try:
                        pyautogui.click('KRY.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                time.sleep(22)
                # копирую и вчтавляю из 3 сапорта
                pyautogui.moveTo(950, 305, duration=0.3)
                pyautogui.scroll(-2500)


                def locate_image():
                    try:
                        pyautogui.click('copy66.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.click(470, 859, duration=0.3)
                pyautogui.click(863, 1059, duration=0.3)
                pyautogui.doubleClick(1191, 197, duration=0.3)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(715, 1065, duration=0.3)
                pyautogui.click(899, 163, duration=0.3)
                pyautogui.click(920, 283, duration=0.3)
                time.sleep(2)
                pyautogui.click(1229, 639, duration=0.3)
                time.sleep(2)
                pyautogui.click(898, 709, duration=0.3)

                # копирую и вставляю из 2 сапорта
                pyautogui.moveTo(950, 305, duration=0.5)
                pyautogui.scroll(-2500)


                def locate_image():
                    try:
                        pyautogui.click('copy66.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.click(470, 859, duration=0.3)
                pyautogui.click(863, 1059)
                pyautogui.doubleClick(829, 197, duration=0.3)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(715, 1065, duration=0.3)
                pyautogui.click(899, 163, duration=0.3)
                pyautogui.click(920, 283, duration=0.3)
                time.sleep(2)
                pyautogui.click(1229, 639, duration=0.3)
                time.sleep(2)
                pyautogui.click(898, 709, duration=0.3)

                # копирую и вставляю из 1 сапорта
                pyautogui.moveTo(950, 305, duration=0.5)
                pyautogui.scroll(-2500)


                def locate_image():
                    try:
                        pyautogui.click('copy66.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.click(470, 859, duration=0.3)
                pyautogui.click(863, 1059)
                pyautogui.doubleClick(534, 197, duration=0.3)
                pyautogui.hotkey('ctrl', 'v')
                # обновление экселя
                pyautogui.click(185, 857, duration=0.3)
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.click(715, 1065, duration=0.3)
                pyautogui.click(899, 163, duration=0.3)
                pyautogui.click(920, 283, duration=0.3)
                time.sleep(2)
                pyautogui.click(1229, 639, duration=0.3)
                time.sleep(2)
                pyautogui.click(1881, 24, duration=0.3)
                pyautogui.click(767, 1060, duration=1)
            break
    continue

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
v






# 18.09.23
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------

import pyautogui
import time
import random

# стандартные настройки
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.8
duration = random.uniform(2, 3)
time.sleep(5)

# 22
while True:
    while True:
        if pyautogui.locateOnScreen('22WR.PNG') is not None or pyautogui.locateOnScreen('33WR.PNG') is not None:
            if pyautogui.locateOnScreen('22WR.PNG') is not None:
                pyautogui.click('22WR.PNG')
            if pyautogui.locateOnScreen('33WR.PNG') is not None:
                pyautogui.click('33WR.PNG')
            for _ in range(1):
                # сохранение TH
                pyautogui.click(252, 252, duration=0.8)
                pyautogui.moveTo(800, 200, duration=1)
                pyautogui.doubleClick()
                time.sleep(10)
                pyautogui.click(1820, 980, duration=0.8)
                pyautogui.typewrite("=1=", interval=0.05)
                pyautogui.click(770, 510, duration=0.8)
                pyautogui.click(16, 262, duration=0.4)
                pyautogui.mouseDown()
                pyautogui.moveTo(212, 262, duration=0.4)
                pyautogui.mouseUp()
                pyautogui.hotkey('ctrl', 'c')
                pyautogui.click(863, 1059, duration=0.8)
                pyautogui.doubleClick(199, 197, duration=0.8)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(767, 1060, duration=1)
                pyautogui.click(1700, 165, duration=0.8)
                pyautogui.click(788, 101, duration=0.5)
                pyautogui.click(920, 96, duration=0.5)

                # открытие нейро WH
                pyautogui.click(715, 1065, duration=0.8)
                time.sleep(7)
                pyautogui.click(795, 86, duration=0.8)
                pyautogui.typewrite("https://colab.research.google.com/drive/18JMytvzNybyes7TwAv2r0R1FOZnXmaBv",
                                    interval=0.05)
                time.sleep(5)
                pyautogui.press('enter')
                time.sleep(16)
                pyautogui.click(35, 387, duration=0.8)
                pyautogui.moveTo(574, 347, duration=0.5)
                pyautogui.scroll(2000)
                pyautogui.click(815, 1045, duration=0.8)
                pyautogui.moveTo(1690, 376, duration=0.5)
                pyautogui.doubleClick()
                pyautogui.click(1508, 163, duration=0.8)
                pyautogui.mouseDown()
                pyautogui.moveTo(254, 593, duration=0.5)
                pyautogui.mouseUp()
                time.sleep(3)
                pyautogui.click(1309, 676, duration=0.8)
                pyautogui.click(815, 1045, duration=0.8)
                pyautogui.click(1406, 163, duration=0.5)
                pyautogui.rightClick()
                pyautogui.click(1265, 569, duration=0.8)
                pyautogui.click(1883, 19, duration=0.8)
                pyautogui.click(626, 242, duration=0.8)
                time.sleep(37)
                pyautogui.scroll(-900)
                time.sleep(2)


                def locate_image():
                    try:
                        pyautogui.click('Qq.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.move(-93, 0, duration=0.2)
                pyautogui.click()
                # time.sleep(295)
            break
    while True:
        if pyautogui.locateOnScreen('kkk.PNG') is not None:
            pyautogui.doubleClick('kkk.PNG', duration=1)
            for _ in range(1):
                # выделение txt
                pyautogui.moveTo(1428, 248, duration=0.5)
                pyautogui.mouseDown()
                pyautogui.scroll(-1400)
                pyautogui.moveTo(1474, 965, duration=1)
                pyautogui.mouseUp()
                pyautogui.hotkey('ctrl', 'c')

                # закрытие и подчищените WH  ###
                for _ in range(6):
                    pyautogui.moveTo(536, 406, duration=1)
                    pyautogui.click()
                    pyautogui.click(240, 531, duration=1)
                    pyautogui.click(1091, 654, duration=1)
                    time.sleep(2)
                pyautogui.click(1885, 18, duration=0.6)

                # открытие CLAUDE + делаем первый запрос
                pyautogui.click(715, 1065, duration=0.8)
                time.sleep(7)
                pyautogui.click(795, 86, duration=0.8)
                pyautogui.typewrite("https://claude.ai/", interval=0.05)
                time.sleep(5)
                pyautogui.press('enter')
                time.sleep(12)

                # создание 1 сапорт чат (0x0) компитентность
                pyautogui.click(540, 508, duration=0.8)
                pyautogui.typewrite(
                    "I will provide you with the correspondence between the manager and the client, your task is to evaluate it according to the criterion   ",
                    interval=0.03)
                pyautogui.typewrite(
                    "1) the competence of the manager. You also have to give an answer only in Russian, and your entire answer should be very, very brief, ",
                    interval=0.03)
                pyautogui.typewrite("no more than 10 words. At the end, give a rating on a ten-point scale",
                                    interval=0.03)
                pyautogui.hotkey('ctrl', 'v')


                def locate_image():
                    try:
                        pyautogui.click('KRY.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                time.sleep(22)
                # переход
                pyautogui.click(47, 177, duration=1)
                # создание 2 сапорт чат (&x&) вежливость
                pyautogui.click(540, 508, duration=0.8)
                pyautogui.typewrite(
                    "I will provide you with the correspondence between the manager and the client, your task is to evaluate it according to the criterion  ",
                    interval=0.03)
                pyautogui.typewrite(
                    "1) politeness of the manager. You also have to give an answer only in Russian, and your entire answer should be very, very brief,  ",
                    interval=0.03)
                pyautogui.typewrite("no more than 10 words. At the end, give a rating on a ten-point scale ",
                                    interval=0.03)
                pyautogui.hotkey('ctrl', 'v')


                def locate_image():
                    try:
                        pyautogui.click('KRY.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                time.sleep(22)
                # переход
                pyautogui.click(47, 177, duration=1)
                # создание 3 сапорт чат (8x8) удовлетворенность клиента
                pyautogui.click(540, 508, duration=0.8)
                pyautogui.typewrite(
                    "I will provide you with the correspondence between the manager and the client, your task is to evaluate it according to the criterion ",
                    interval=0.03)
                pyautogui.typewrite(
                    "1)customer satisfaction with the response received. You also have to give an answer only in Russian, and your entire answer should be very, very brief,  ",
                    interval=0.03)
                pyautogui.typewrite("no more than 10 words. At the end, give a rating on a ten-point scale ",
                                    interval=0.03)
                pyautogui.hotkey('ctrl', 'v')


                def locate_image():
                    try:
                        pyautogui.click('KRY.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                time.sleep(22)
                # копирую и вчтавляю из 3 сапорта
                pyautogui.moveTo(950, 305, duration=0.5)
                pyautogui.scroll(-2500)


                def locate_image():
                    try:
                        pyautogui.click('copy66.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.click(470, 859, duration=0.5)
                pyautogui.click(863, 1059, duration=0.8)
                pyautogui.doubleClick(1191, 197, duration=0.8)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(715, 1065, duration=0.8)
                pyautogui.click(899, 163, duration=0.8)
                pyautogui.click(920, 283, duration=0.8)
                time.sleep(2)
                pyautogui.click(1229, 639, duration=0.8)
                time.sleep(2)
                pyautogui.click(898, 709, duration=0.8)

                # копирую и вставляю из 2 сапорта
                pyautogui.moveTo(950, 305, duration=0.5)
                pyautogui.scroll(-2500)


                def locate_image():
                    try:
                        pyautogui.click('copy66.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.click(470, 859, duration=0.5)
                pyautogui.click(863, 1059)
                pyautogui.doubleClick(829, 197, duration=0.8)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(715, 1065, duration=0.8)
                pyautogui.click(899, 163, duration=0.8)
                pyautogui.click(920, 283, duration=0.8)
                time.sleep(2)
                pyautogui.click(1229, 639, duration=0.8)
                time.sleep(2)
                pyautogui.click(898, 709, duration=0.8)

                # копирую и вставляю из 1 сапорта
                pyautogui.moveTo(950, 305, duration=0.5)
                pyautogui.scroll(-2500)


                def locate_image():
                    try:
                        pyautogui.click('copy66.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.click(470, 859, duration=0.5)
                pyautogui.click(863, 1059)
                pyautogui.doubleClick(534, 197, duration=0.8)
                pyautogui.hotkey('ctrl', 'v')
                # обновление экселя
                pyautogui.click(185, 857, duration=0.4)
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.click(715, 1065, duration=0.8)
                pyautogui.click(899, 163, duration=0.8)
                pyautogui.click(920, 283, duration=0.8)
                time.sleep(2)
                pyautogui.click(1229, 639, duration=0.8)
                time.sleep(2)
                pyautogui.click(1881, 24, duration=0.8)
                pyautogui.click(767, 1060, duration=1)
            break
    continue

# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------




-----------------------------
----------------------------------
----------------------------------
--------------------------------------------
import pyautogui
import time
import random

# стандартные настройки
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.8
duration = random.uniform(2, 3)
time.sleep(5)

# 22
while True:
    while True:
        if pyautogui.locateOnScreen('22WR.PNG') is not None:
            pyautogui.click('22WR.PNG')
            for _ in range(1):
                # сохранение TH
                pyautogui.click(252, 252, duration=0.8)
                pyautogui.moveTo(800, 200, duration=1)
                pyautogui.doubleClick()
                time.sleep(10)
                pyautogui.click(1820, 980, duration=0.8)
                pyautogui.typewrite("=1=", interval=0.05)
                pyautogui.click(770, 510, duration=0.8)
                pyautogui.click(1700, 165, duration=0.8)

                # открытие нейро WH
                pyautogui.click(715, 1065, duration=0.8)
                time.sleep(7)
                pyautogui.click(795, 86, duration=0.8)
                pyautogui.typewrite("https://colab.research.google.com/drive/18JMytvzNybyes7TwAv2r0R1FOZnXmaBv",
                                    interval=0.05)
                time.sleep(5)
                pyautogui.press('enter')
                time.sleep(16)
                pyautogui.click(35, 387, duration=0.8)
                pyautogui.moveTo(574, 347, duration=0.5)
                pyautogui.scroll(2000)
                pyautogui.click(815, 1045, duration=0.8)
                pyautogui.moveTo(1690, 376, duration=0.5)
                pyautogui.doubleClick()
                pyautogui.click(1508, 163, duration=0.8)
                pyautogui.mouseDown()
                pyautogui.moveTo(254, 593, duration=0.5)
                pyautogui.mouseUp()
                time.sleep(3)
                pyautogui.click(1309, 676, duration=0.8)
                pyautogui.click(815, 1045, duration=0.8)
                pyautogui.click(1406, 163, duration=0.5)
                pyautogui.rightClick()
                pyautogui.click(1265, 569, duration=0.8)
                pyautogui.click(1883, 19, duration=0.8)
                pyautogui.click(626, 242, duration=0.8)
                time.sleep(37)
                pyautogui.scroll(-1200)
                time.sleep(2)


                def locate_image():
                    try:
                        pyautogui.click('Qjj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.move(-93, 0, duration=0.2)
                pyautogui.click()
                # time.sleep(295)
            break
    while True:
        if pyautogui.locateOnScreen('kk.PNG') is not None:
            pyautogui.doubleClick('kk.PNG', duration=1)
            for _ in range(1):
                # выделение txt
                pyautogui.moveTo(1428, 248, duration=0.5)
                pyautogui.mouseDown()
                pyautogui.scroll(-15400)
                pyautogui.moveTo(1474, 965, duration=1)
                pyautogui.mouseUp()
                pyautogui.hotkey('ctrl', 'c')

                # закрытие и подчищените WH  ###
                for _ in range(6):
                    pyautogui.moveTo(536, 406, duration=1)
                    pyautogui.click()
                    pyautogui.click(240, 531, duration=1)
                    pyautogui.click(1091, 654, duration=1)
                    time.sleep(2)
                pyautogui.click(1885, 18, duration=0.6)

                # открытие GPT + делаем первый запрос
                pyautogui.click(715, 1065, duration=0.8)
                time.sleep(7)
                pyautogui.click(795, 86, duration=0.8)
                pyautogui.typewrite("https://chat.openai.com", interval=0.05)
                time.sleep(5)
                pyautogui.press('enter')
                time.sleep(12)

                # создание 1 сапорт чат (0x0) компитентность
                pyautogui.click(170, 168, duration=0.8)
                pyautogui.click(618, 912, duration=1)
                pyautogui.typewrite(
                    "I will provide you with the correspondence between the manager and the client, your task is to evaluate it  ",
                    interval=0.03)
                pyautogui.typewrite(
                    " according to the criterion 1) the competence of the manager. You must also give an answer only in Russian, ",
                    interval=0.03)
                pyautogui.typewrite(
                    " and your entire answer must consist of no more than 30 words. At the end, give an assessment on a decitibal scale",
                    interval=0.03)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(1641, 909, duration=1)
                time.sleep(20)
                pyautogui.click(352, 299, duration=0.8)
                pyautogui.tripleClick(186, 296, duration=1)
                pyautogui.typewrite("0x0", interval=0.1)

                # создание 2 сапорт чат (&x&) вежливость
                pyautogui.click(170, 168, duration=0.8)
                pyautogui.click(618, 912, duration=1)
                pyautogui.typewrite(
                    " I will provide you with the correspondence between the manager and the client, your task is to evaluate it ",
                    interval=0.03)
                pyautogui.typewrite(
                    " according to the criterion 1) politeness of the manager. You must also give an answer only in Russian, and your ",
                    interval=0.03)
                pyautogui.typewrite(
                    " entire answer must consist of no more than 30 words. At the end, give an assessment on a decitibal scale",
                    interval=0.03)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(1641, 909, duration=1)
                time.sleep(20)
                pyautogui.click(352, 299, duration=0.8)
                pyautogui.tripleClick(186, 296, duration=1)
                pyautogui.typewrite("&x&", interval=0.1)

                # создание 3 сапорт чат (8x8) удовлетворенность клиента
                pyautogui.click(170, 168, duration=0.8)
                pyautogui.click(618, 912, duration=1)
                pyautogui.typewrite(
                    " I will provide you with the correspondence between the manager and the client, your task is to evaluate it ",
                    interval=0.03)
                pyautogui.typewrite(
                    " according to the criterion 1)customer satisfaction with the response received. You must also give an answer only in Russian, and your entire ",
                    interval=0.03)
                pyautogui.typewrite(
                    " answer must consist of no more than 30 words. At the end, give an assessment on a decitibal scale",
                    interval=0.03)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.click(1641, 909, duration=1)
                time.sleep(20)
                pyautogui.click(352, 299, duration=0.8)
                pyautogui.tripleClick(186, 296, duration=1)
                pyautogui.typewrite("8x8", interval=0.1)

                # копирую критерии и вставляю их в эксель, скролю эксель , подчищаю gpt
                # копирую и вставляю из 3 сапорта
                pyautogui.moveTo(1159, 411, duration=0.7)
                time.sleep(10)
                pyautogui.scroll(1570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.scroll(-570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается
                locate_image()
                pyautogui.scroll(-570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается
                locate_image()
                pyautogui.scroll(-570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается
                locate_image()
                pyautogui.scroll(-570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается
                locate_image()
                pyautogui.click(863, 1059, duration=0.8)
                pyautogui.doubleClick(1191, 197, duration=0.8)
                pyautogui.hotkey('ctrl', 'v')

                # копирую и вставляю из 2 сапорта
                pyautogui.click(715, 1065, duration=0.8)
                pyautogui.click(248, 371, duration=0.8)
                pyautogui.moveTo(1159, 411, duration=0.7)
                pyautogui.scroll(1570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.scroll(-570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается
                locate_image()
                pyautogui.scroll(-570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается
                locate_image()
                pyautogui.scroll(-570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается
                locate_image()
                pyautogui.scroll(-570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается
                locate_image()
                pyautogui.click(863, 1059, duration=0.8)
                pyautogui.doubleClick(829, 197, duration=0.8)
                pyautogui.hotkey('ctrl', 'v')
                # копирую и вставляю из 1 сапорта
                pyautogui.click(715, 1065, duration=0.8)
                pyautogui.click(243, 446, duration=0.8)
                pyautogui.moveTo(1159, 411, duration=0.7)
                pyautogui.scroll(1570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается ы
                locate_image()
                pyautogui.scroll(-570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается
                locate_image()
                pyautogui.scroll(-570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается
                locate_image()
                pyautogui.scroll(-570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается
                locate_image()
                pyautogui.scroll(-570)


                def locate_image():
                    try:
                        pyautogui.click('ghj.PNG')
                    except Exception as e:
                        print(f"An error occurred: {e}")


                # Вызывается
                locate_image()
                pyautogui.click(863, 1059, duration=0.8)
                pyautogui.doubleClick(534, 197, duration=0.8)
                pyautogui.hotkey('ctrl', 'v')

                # обновление экселя
                pyautogui.click(185, 857, duration=0.4)
                pyautogui.press('down')
                pyautogui.press('down')
                pyautogui.click(715, 1065, duration=0.8)
                # подчищение GPT
                for _ in range(3):
                    pyautogui.click(391, 301, duration=duration)
                    time.sleep(1)
                    pyautogui.click()
                    time.sleep(4)
                    pyautogui.click(1196, 677, duration=duration)
                    time.sleep(7)
                pyautogui.click(1885, 18, duration=0.8)
                pyautogui.click(760, 1060, duration=1)
            break
    continue
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
###################################################################################################
#################################################################################################
###############################################################################################
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------





#   10.09.2023            12/35 sek
import pyautogui
import time
import random

# стандартные настройки
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.8
duration = random.uniform(2, 3)
time.sleep(5)

# старт зaход в почту сохраняет первое сообщение
# автаматический старт цикл
while True:
    if pyautogui.locateOnScreen('WR.PNG') is not None:
        pyautogui.click('WR.PNG')
        for _ in range(1):
            # сохранение TH
            pyautogui.click(252, 252, duration=0.8)
            pyautogui.moveTo(800, 200, duration=1)
            pyautogui.doubleClick()
            time.sleep(10)
            pyautogui.click(1820, 980, duration=0.8)
            pyautogui.typewrite("=1=", interval=0.05)
            pyautogui.click(770, 510, duration=0.8)
            pyautogui.click(1700, 165, duration=0.8)

            # открытие нейро WH
            pyautogui.click(715, 1065, duration=0.8)
            time.sleep(7)
            pyautogui.click(795, 86, duration=0.8)
            pyautogui.typewrite("https://colab.research.google.com/drive/18JMytvzNybyes7TwAv2r0R1FOZnXmaBv",
                                interval=0.05)
            time.sleep(5)
            pyautogui.press('enter')
            time.sleep(16)
            pyautogui.click(35, 387, duration=0.8)
            pyautogui.moveTo(574, 347, duration=0.5)
            pyautogui.scroll(2000)
            pyautogui.click(815, 1045, duration=0.8)
            pyautogui.moveTo(1690, 376, duration=0.5)
            pyautogui.doubleClick()
            pyautogui.click(1508, 163, duration=0.8)
            pyautogui.mouseDown()
            pyautogui.moveTo(254, 593, duration=0.5)
            pyautogui.mouseUp()
            time.sleep(3)
            pyautogui.click(1309, 676, duration=0.8)
            pyautogui.click(815, 1045, duration=0.8)
            pyautogui.click(1406, 163, duration=0.5)
            pyautogui.rightClick()
            pyautogui.click(1265, 569, duration=0.8)
            pyautogui.click(1883, 19, duration=0.8)
            pyautogui.click(626, 242, duration=0.8)
            time.sleep(37)
            pyautogui.scroll(-1200)
            time.sleep(2)


            def locate_image():
                try:
                    pyautogui.click('Qjj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается ы
            locate_image()
            pyautogui.move(-93, 0, duration=0.2)
            pyautogui.click()
            time.sleep(295)
            pyautogui.doubleClick(209, 561, duration=1)

            # выделение txt
            pyautogui.moveTo(1428, 248, duration=0.5)
            pyautogui.mouseDown()
            pyautogui.scroll(-1400)
            pyautogui.moveTo(1474, 965, duration=1)
            pyautogui.mouseUp()
            pyautogui.hotkey('ctrl', 'c')

            # закрытие и подчищените WH  ###
            for _ in range(6):
                pyautogui.moveTo(536, 406, duration=1)
                pyautogui.click()
                pyautogui.click(240, 531, duration=1)
                pyautogui.click(1091, 654, duration=1)
                time.sleep(2)
            pyautogui.click(1885, 18, duration=0.6)

            # открытие GPT + делаем первый запрос
            pyautogui.click(715, 1065, duration=0.8)
            time.sleep(7)
            pyautogui.click(795, 86, duration=0.8)
            pyautogui.typewrite("https://chat.openai.com", interval=0.05)
            time.sleep(5)
            pyautogui.press('enter')
            time.sleep(12)

            # создание 1 сапорт чат (0x0) компитентность
            pyautogui.click(170, 168, duration=0.8)
            pyautogui.click(618, 912, duration=1)
            pyautogui.typewrite(
                "I will provide you with the correspondence between the manager and the client, your task is to evaluate it  ",
                interval=0.03)
            pyautogui.typewrite(
                " according to the criterion 1) the competence of the manager. You must also give an answer only in Russian, ",
                interval=0.03)
            pyautogui.typewrite(
                " and your entire answer must consist of no more than 30 words. At the end, give an assessment on a decitibal scale",
                interval=0.03)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.click(1641, 909, duration=1)
            time.sleep(13)
            pyautogui.click(352, 299, duration=0.8)
            pyautogui.tripleClick(186, 296, duration=1)
            pyautogui.typewrite("0x0", interval=0.1)

            # создание 2 сапорт чат (&x&) вежливость
            pyautogui.click(170, 168, duration=0.8)
            pyautogui.click(618, 912, duration=1)
            pyautogui.typewrite(
                " I will provide you with the correspondence between the manager and the client, your task is to evaluate it ",
                interval=0.03)
            pyautogui.typewrite(
                " according to the criterion 1) politeness of the manager. You must also give an answer only in Russian, and your ",
                interval=0.03)
            pyautogui.typewrite(
                " entire answer must consist of no more than 30 words. At the end, give an assessment on a decitibal scale",
                interval=0.03)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.click(1641, 909, duration=1)
            time.sleep(13)
            pyautogui.click(352, 299, duration=0.8)
            pyautogui.tripleClick(186, 296, duration=1)
            pyautogui.typewrite("&x&", interval=0.1)

            # создание 3 сапорт чат (8x8) удовлетворенность клиента
            pyautogui.click(170, 168, duration=0.8)
            pyautogui.click(618, 912, duration=1)
            pyautogui.typewrite(
                " I will provide you with the correspondence between the manager and the client, your task is to evaluate it ",
                interval=0.03)
            pyautogui.typewrite(
                " according to the criterion 1)customer satisfaction with the response received. You must also give an answer only in Russian, and your entire ",
                interval=0.03)
            pyautogui.typewrite(
                " answer must consist of no more than 30 words. At the end, give an assessment on a decitibal scale",
                interval=0.03)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.click(1641, 909, duration=1)
            time.sleep(13)
            pyautogui.click(352, 299, duration=0.8)
            pyautogui.tripleClick(186, 296, duration=1)
            pyautogui.typewrite("8x8", interval=0.1)

            # копирую критерии и вставляю их в эксель, скролю эксель , подчищаю gpt
            # копирую и вставляю из 3 сапорта
            pyautogui.moveTo(1159, 411, duration=0.7)
            time.sleep(10)
            pyautogui.scroll(1570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается ы
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.click(863, 1059, duration=0.8)
            pyautogui.doubleClick(1191, 197, duration=0.8)
            pyautogui.hotkey('ctrl', 'v')

            # копирую и вставляю из 2 сапорта
            pyautogui.click(715, 1065, duration=0.8)
            pyautogui.click(248, 371, duration=0.8)
            pyautogui.moveTo(1159, 411, duration=0.7)
            pyautogui.scroll(1570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается ы
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.click(863, 1059, duration=0.8)
            pyautogui.doubleClick(829, 197, duration=0.8)
            pyautogui.hotkey('ctrl', 'v')

            # копирую и вставляю из 1 сапорта
            pyautogui.click(715, 1065, duration=0.8)
            pyautogui.click(243, 446, duration=0.8)
            pyautogui.moveTo(1159, 411, duration=0.7)
            pyautogui.scroll(1570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается ы
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.click(863, 1059, duration=0.8)
            pyautogui.doubleClick(534, 197, duration=0.8)
            pyautogui.hotkey('ctrl', 'v')

            # обновление экселя
            pyautogui.click(185, 857, duration=0.4)
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.click(715, 1065, duration=0.8)
            # подчищение GPT
            for _ in range(3):
                pyautogui.click(391, 301, duration=duration)
                time.sleep(1)
                pyautogui.click()
                time.sleep(4)
                pyautogui.click(1196, 660, duration=duration)
                time.sleep(7)
            pyautogui.click(1885, 18, duration=0.8)
            pyautogui.click(760, 1060, duration=1)
    else:
        continue
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------------------------------------------------------------------------------------------------------









# 09.09.2023


import pyautogui
import time
import random

# стандартные настройки
pyautogui.FAILSAFE = True
pyautogui.PAUSE = 0.8
duration = random.uniform(2, 3)
time.sleep(5)

# старт зaход в почту сохраняет первое сообщение
# автаматический старт цикл
while True:
    if pyautogui.locateOnScreen('WR.PNG') is not None:
        pyautogui.click('WR.PNG')
        for _ in range(1):
            # сохранение TH
            pyautogui.moveTo(252, 252, duration=1)
            pyautogui.click()
            pyautogui.moveTo(800, 200, duration=1)
            pyautogui.doubleClick()
            time.sleep(10)
            pyautogui.moveTo(1820, 980, duration=1)
            pyautogui.click()
            pyautogui.typewrite("=1=", interval=0.05)
            pyautogui.moveTo(770, 510, duration=1)
            pyautogui.click()
            pyautogui.moveTo(1700, 165, duration=1)
            pyautogui.click()

            # открытие нейро WH
            pyautogui.moveTo(715, 1065, duration=0.5)
            pyautogui.click()
            time.sleep(7)
            pyautogui.moveTo(795, 86, duration=0.5)
            pyautogui.click()
            pyautogui.typewrite("https://colab.research.google.com/drive/18JMytvzNybyes7TwAv2r0R1FOZnXmaBv",
                                interval=0.05)
            time.sleep(5)
            pyautogui.press('enter')
            time.sleep(16)
            pyautogui.moveTo(35, 387, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(574, 347, duration=0.5)
            pyautogui.scroll(2000)
            pyautogui.moveTo(815, 1045, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(1690, 376, duration=0.5)
            pyautogui.doubleClick()
            pyautogui.moveTo(1508, 163, duration=0.5)
            pyautogui.click()
            pyautogui.mouseDown()
            pyautogui.moveTo(254, 593, duration=0.5)
            pyautogui.mouseUp()
            time.sleep(3)
            pyautogui.moveTo(1309, 676, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(815, 1045, duration=0.5)
            pyautogui.click()
            pyautogui.click(1406, 163, duration=0.5)
            pyautogui.rightClick()
            pyautogui.moveTo(1265, 569, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(1883, 19, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(626, 242, duration=0.5)
            pyautogui.click()
            time.sleep(37)
            pyautogui.scroll(-1200)
            time.sleep(2)


            def locate_image():
                try:
                    pyautogui.click('Qjj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается ы
            locate_image()
            pyautogui.move(-93, 0, duration=0.2)
            pyautogui.click()
            time.sleep(295)
            pyautogui.moveTo(209, 561, duration=1)
            pyautogui.doubleClick()

            # выделение txt
            pyautogui.moveTo(1428, 248, duration=0.5)
            pyautogui.mouseDown()
            pyautogui.scroll(-1400)
            pyautogui.moveTo(1474, 965, duration=1)
            pyautogui.mouseUp()
            pyautogui.hotkey('ctrl', 'c')

            # закрытие и подчищените WH  ###
            for _ in range(6):
                pyautogui.moveTo(536, 406, duration=0.4)
                pyautogui.click()
                pyautogui.moveTo(240, 531, duration=0.4)
                pyautogui.click()
                pyautogui.moveTo(1091, 654, duration=0.4)
                pyautogui.click()
                time.sleep(2)
            pyautogui.moveTo(1885, 18, duration=0.5)
            pyautogui.click()

            # открытие GPT + делаем первый запрос
            pyautogui.moveTo(715, 1065, duration=0.5)
            pyautogui.click()
            time.sleep(7)
            pyautogui.moveTo(795, 86, duration=0.5)
            pyautogui.click()
            pyautogui.typewrite("https://chat.openai.com", interval=0.05)
            time.sleep(5)
            pyautogui.press('enter')
            time.sleep(12)

            # создание 1 сапорт чат (0x0) компитентность
            pyautogui.moveTo(170, 168, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(618, 912, duration=1)
            pyautogui.click()
            pyautogui.typewrite(
                "I will provide you with the correspondence between the manager and the client, your task is to evaluate it  ",
                interval=0.1)
            pyautogui.typewrite(
                " according to the criterion 1) the competence of the manager. You must also give an answer only in Russian, ",
                interval=0.1)
            pyautogui.typewrite(
                " and your entire answer must consist of no more than 30 words. At the end, give an assessment on a decitibal scale",
                interval=0.1)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.moveTo(1641, 909, duration=1)
            pyautogui.click()
            time.sleep(23)
            pyautogui.moveTo(352, 299, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(186, 296, duration=0.5)
            pyautogui.tripleClick()
            pyautogui.typewrite("0x0", interval=0.1)

            # создание 2 сапорт чат (&x&) вежливость
            pyautogui.moveTo(170, 168, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(618, 912, duration=1)
            pyautogui.click()
            pyautogui.typewrite(
                " I will provide you with the correspondence between the manager and the client, your task is to evaluate it ",
                interval=0.1)
            pyautogui.typewrite(
                " according to the criterion 1) politeness of the manager. You must also give an answer only in Russian, and your ",
                interval=0.1)
            pyautogui.typewrite(
                " entire answer must consist of no more than 30 words. At the end, give an assessment on a decitibal scale",
                interval=0.1)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.moveTo(1641, 909, duration=1)
            pyautogui.click()
            time.sleep(23)
            pyautogui.moveTo(352, 299, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(186, 296, duration=0.5)
            pyautogui.tripleClick()
            pyautogui.typewrite("&x&", interval=0.1)

            # создание 3 сапорт чат (8x8) удовлетворенность клиента
            pyautogui.moveTo(170, 168, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(618, 912, duration=1)
            pyautogui.click()
            pyautogui.typewrite(
                " I will provide you with the correspondence between the manager and the client, your task is to evaluate it ",
                interval=0.1)
            pyautogui.typewrite(
                " according to the criterion 1)customer satisfaction with the response received. You must also give an answer only in Russian, and your entire ",
                interval=0.1)
            pyautogui.typewrite(
                " answer must consist of no more than 30 words. At the end, give an assessment on a decitibal scale",
                interval=0.1)
            pyautogui.hotkey('ctrl', 'v')
            pyautogui.moveTo(1641, 909, duration=1)
            pyautogui.click()
            time.sleep(23)
            pyautogui.moveTo(352, 299, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(186, 296, duration=0.5)
            pyautogui.tripleClick()
            pyautogui.typewrite("8x8", interval=0.1)

            # копирую критерии и вставляю их в эксель, скролю эксель , подчищаю gpt
            # копирую и вставляю из 3 сапорта
            pyautogui.moveTo(1159, 411, duration=0.7)
            time.sleep(10)
            pyautogui.scroll(1570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается ы
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.moveTo(863, 1059, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(1191, 197, duration=0.5)
            pyautogui.doubleClick()
            pyautogui.hotkey('ctrl', 'v')

            # копирую и вставляю из 2 сапорта
            pyautogui.moveTo(715, 1065, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(248, 371, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(1159, 411, duration=0.7)
            pyautogui.scroll(1570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается ы
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.moveTo(863, 1059, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(829, 197, duration=0.5)
            pyautogui.doubleClick()
            pyautogui.hotkey('ctrl', 'v')

            # копирую и вставляю из 1 сапорта
            pyautogui.moveTo(715, 1065, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(243, 446, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(1159, 411, duration=0.7)
            pyautogui.scroll(1570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается ы
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.scroll(-570)


            def locate_image():
                try:
                    pyautogui.click('ghj.PNG')
                except Exception as e:
                    print(f"An error occurred: {e}")


            # Вызывается
            locate_image()
            pyautogui.moveTo(863, 1059, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(534, 197, duration=0.5)
            pyautogui.doubleClick()
            pyautogui.hotkey('ctrl', 'v')

            # обновление экселя
            pyautogui.moveTo(185, 857, duration=0.2)
            pyautogui.click()
            pyautogui.press('down')
            pyautogui.press('down')
            pyautogui.moveTo(715, 1065, duration=0.5)
            pyautogui.click()
            # подчищение GPT
            for _ in range(3):
                pyautogui.moveTo(391, 301, duration=duration)
                pyautogui.click()
                time.sleep(1)
                pyautogui.click()
                time.sleep(4)
                pyautogui.moveTo(1196, 660, duration=duration)
                pyautogui.click()
                time.sleep(9)
            pyautogui.moveTo(1885, 18, duration=0.5)
            pyautogui.click()
            pyautogui.moveTo(760, 1060, duration=1)
            pyautogui.click()
    else:
        continue





