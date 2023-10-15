#БИБЛИОТЕКИ
import pyautogui
import time
import random
import subprocess
import pyperclip
import os
#Стандартные настройки
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
                pyautogui.click(540, 470, duration=0.3)
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
                pyautogui.click(540, 470, duration=0.3)
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
                pyautogui.click(540, 470, duration=0.3)
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

