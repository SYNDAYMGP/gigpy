///принемает текстовое сообщение пользователя, сохраняет его в txt файл, 
отправляет текстовое сообщение пользователю обратно.
import telebot
bot = telebot.TeleBot('6786106072:AAGz8bE4mNyJscUDrvARjYiXOCAyX5FukD4')
@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Я на связи. Напиши мне что-нибудь)')    
@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = message.text
    with open('1.txt', 'a') as f:
        f.write(text + '\n')
    bot.send_message(message.chat.id, 'Вы написали: ' + text)
bot.polling(none_stop=True, interval=0)
///
@@@@
@@@@
@@@@
@@@@
@@@@
///принемает текстовое сообщение пользователя, сохраняет его в txt файл при помощи раскадировки utf-8, 
отправляет текстовое сообщение пользователю обратно.
import telebot
bot = telebot.TeleBot('6786106072:AAGz8bE4mNyJscUDrvARjYiXOCAyX5FukD4')
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Я на связи. Напишите мне что-нибудь)')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = message.text
    with open('1.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')
    bot.send_message(message.chat.id, 'Вы написали: ' + text)
bot.polling(none_stop=True, interval=0)
///
@@@@
@@@@
@@@@
@@@@
@@@@
///принемает текстовое сообщение пользователя, сохраняет его в txt файл при помощи раскадировки utf-8, 
отправляет текстовое сообщение пользователю обратно + отправка пользователю файла 1.txt с раскадировкой.
import telebot
bot = telebot.TeleBot('6786106072:AAGz8bE4mNyJscUDrvARjYiXOCAyX5FukD4')
@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, 'Я на связи. Напишите мне что-нибудь)')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    text = message.text
    with open('1.txt', 'a', encoding='utf-8') as file:
        file.write(text + '\n')
    bot.send_message(message.chat.id, 'Вы написали: ' + text)
    # Открываем и отправляем файл пользователю
    with open('1.txt', 'rb') as file:
        bot.send_document(message.chat.id, file)
bot.polling(none_stop=True, interval=0)
///
@@@@
@@@@
@@@@
@@@@
@@@@
/// принемает текстовое сообщение пользователя, обрабатывает его через gp и ответ gp отсылает 
обратно пользователю в виде txt файла.
import g4f
import telebot
bot = telebot.TeleBot('6786106072:AAGz8bE4mNyJscUDrvARjYiXOCAyX5FukD4')
@bot.message_handler(content_types=["text"])
def handle_text(message):
  with open('1.txt', 'w') as file:
    file.write('')
  text = message.text
  response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": text}], 
    stream=True
  )
  for msg in response:
    with open('1.txt', 'a', encoding='utf-8') as file:
      file.write(msg)
  bot.send_document(message.chat.id, open('1.txt', 'rb'))
bot.polling(none_stop=True, interval=0)
///
@@@@
@@@@
@@@@
@@@@
@@@@
///
import g4f
import telebot
from pptx import Presentation
from pptx.util import Pt
bot = telebot.TeleBot('6786106072:AAGz8bE4mNyJscUDrvARjYiXOCAyX5FukD4')
@bot.message_handler(content_types=["text"]) 
def handle_text(message):
  text = message.text
  response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": text}],
    stream=True    
  )
  ll2 = ""
  for item in response:
    ll2 += item
    
  root = Presentation()
  #создание первого слайда
  first_slide_layout = root.slide_layouts[1]
  slide = root.slides.add_slide(first_slide_layout)
  # создание заголовка слайда
  slide.shapes.title.text = 'Текст заголовка'
  # создание подзаголовка слайда
  text_frame = slide.placeholders[1].text_frame
  text_frame.text = ll2
  # формирование формата текста
  p = text_frame.paragraphs[0]
  p.font.size = Pt(14) 
  p.font.name = 'Times New Roman'
  root.save('Example.pptx')
  bot.send_document(message.chat.id, open('Example.pptx', 'rb'))
    
bot.polling(none_stop=True, interval=0)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#

import g4f
import telebot
from pptx import Presentation
from pptx.util import Pt
bot = telebot.TeleBot('6786106072:AAGz8bE4mNyJscUDrvARjYiXOCAyX5FukD4')
@bot.message_handler(content_types=["text"]) 
#обработка сообщ => в главы
def handle_text(message):
  with open('1.txt', 'w') as file:
    file.write('')
  text = message.text
  response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": 'составь мне план (структуру) для моего доклада на тему (' + text + ') план должен состоять из глав в ответ ты должен записать только название глав без каких либо твоих пояснений и дополнений , не забудь пронумеровать их вот так 1, 2, 3, 4, 5'}],
    stream=True    
  )
  ll2 = ""
  for item in response:
    ll2 += item
  with open("1.txt", "w", encoding='utf-8') as file:
    file.write(ll2)
      
  #записываем каждую главу в переменную
  with open("1.txt", encoding='utf-8') as file:
    content = file.read()
    lines = content.split("\n")
    chapter_count = 0
    for line in lines:
      if line:
        if line[0].isdigit():
          chapter_count += 1
          chapter_variable_name = "ww" + str(chapter_count)
          exec(chapter_variable_name + ' = line')
    print("Количество глав:", chapter_count)
    for i in range(1, chapter_count + 1):
      chapter_variable_name = "ww" + str(i)
      # Убираем .decode()
      print(chapter_variable_name + ":", eval(chapter_variable_name))
        
bot.polling(none_stop=True, interval=0)






















# обработка ошибок в ваш код
import g4f
import telebot
from pptx import Presentation
from pptx.util import Pt
response = None
ll2 = ""
text = "человек паук"
while response is None:  # Запустить код заново, если ответ от GPT-3.5 Turbo не получен
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": 'составь мне план (структуру) для моего доклада на тему (' + text + ') план должен состоять из глав в ответ ты должен записать только название глав без каких либо твоих пояснений и дополнений , не забудь пронумеровать их вот так 1, 2, 3, 4, 5'}],
            stream=True    
        )

        for item in response:
            ll2 += item
        
    except Exception as e:
        print("Произошла ошибка:", e)
        response = None  # Сбросить значение response для повторной попытки получить ответ
print('1')
print('2')
print('3')
print('4')
print('5')
print(ll2)

@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#ЗАПРОСЫ ВМЕСТЕ С ОБРАБОТЧИКОМ ОШИБОК
import g4f
import telebot
from pptx import Presentation
from pptx.util import Pt
response = None
ll2 = ""
text = "человек паук"
while response is None:  # Запустить код заново, если ответ от GPT-3.5 Turbo не получен
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": 'составь мне план (структуру) для моего доклада на тему (' + text + ') план должен состоять из глав в ответ ты должен записать только название глав без каких либо твоих пояснений и дополнений , не забудь пронумеровать их вот так 1, 2, 3, 4, 5'}],
            stream=True    
        )
        for item in response:
            ll2 += item
    except Exception as e:
        print("Произошла ошибка:", e)
        response = None  # Сбросить значение response для повторной попытки получить ответ
#===========================================================
#===========================================================
#===========================================================
#===========================================================
#===========================================================
print(ll2)
with open("1.txt", "w", encoding='utf-8') as file:
    file.write(ll2)
#считаем кол глав и записываем в переменную
with open("1.txt", encoding='utf-8') as file:
  content = file.read()
  lines = content.split("\n")
  chapter_count = 0
  for line in lines:
    if line:
      if line[0].isdigit():
        chapter_count += 1
        chapter_variable_name = "ww" + str(chapter_count)
        exec(chapter_variable_name + ' = line')
  print("Количество глав:", chapter_count)
  for i in range(1, chapter_count + 1):
    chapter_variable_name = "ww" + str(i)
    # Убираем .decode()
    print(chapter_variable_name + ":", eval(chapter_variable_name))
print(ww1*6)  
#===========================================================
#===========================================================
#===========================================================
#===========================================================
#===========================================================  
response1 = None
ll21 = ""
text = "человек паук"
while response1 is None:  # Запустить код заново, если ответ от GPT-3.5 Turbo не получен
    try:
        response1 = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": 'распиши по подробнее тему (' + ww1 + ') '}],
            stream=True    
        )
        for item in response1:
            ll21 += item
    except Exception as e:
        print("Произошла ошибка:", e)
        response1 = None  # Сбросить значение response для повторной попытки получить ответ

print(ll21)
with open("2.txt", "w", encoding='utf-8') as file:
    file.write(ll21)
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#ЗАПРОСЫ ВМЕСТЕ С ОБРАБОТЧИКОМ ОШИБОК
import os
import g4f
import telebot
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor


for i in range(1):
  files = ['1.txt', '2.txt', '3.txt', '4.txt', '5.txt', '6.txt', '7.txt']
  for file in files:
    open(file, 'w').close()
  text = 'возникновение экономики'
  response = None
  ll2 = ""
  
  while response is None:  # Запустить код заново, если ответ от GPT-3.5 Turbo не получен
      try:
          response = g4f.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{"role": "user", "content": 'составь мне план (структуру) для моего доклада на тему (' + text + ') план должен состоять из глав в ответ ты должен записать только название глав без каких либо твоих пояснений и дополнений , не забудь пронумеровать их вот так 1, 2, 3, 4, 5'}],
              stream=True    
          )
          for item in response:
              ll2 += item
      except Exception as e:
          print("Произошла ошибка:", e)
          response = None  # Сбросить значение response для повторной попытки получить ответ
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================
  print(ll2)
  with open("1.txt", "w", encoding='utf-8') as file:
    file.write(ll2)
  #считаем кол глав и записываем в переменную
  with open("1.txt", encoding='utf-8') as file:
    content = file.read()
    lines = content.split("\n")
    chapter_count = 0
    for line in lines:
      if line:
        if line[0].isdigit():
          chapter_count += 1
          chapter_variable_name = "ww" + str(chapter_count)
          exec(chapter_variable_name + ' = line')
    print("Количество глав:", chapter_count)
    for i in range(1, chapter_count + 1):
      chapter_variable_name = "ww" + str(i)
      # Убираем .decode()
      print(chapter_variable_name + ":", eval(chapter_variable_name))
  print(ww1*6)  
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================  
  response1 = None
  vv1 = ""
  while response1 is None:  # Запустить код заново, если ответ от GPT-3.5 Turbo не получен
      try:
          response1 = g4f.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{"role": "user", "content": 'распиши по подробнее тему (' + ww1 + ') '}],
              stream=True    
          )
          for item in response1:
              vv1 += item
      except Exception as e:
          print("Произошла ошибка:", e)
          response1 = None  # Сбросить значение response для повторной попытки получить ответ

  print(vv1)
  with open("2.txt", "w", encoding='utf-8') as file:
      file.write(vv1)
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================  
  response2 = None
  vv2 = ""
  while response2 is None:  # Запустить код заново, если ответ от GPT-3.5 Turbo не получен
      try:
          response2 = g4f.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{"role": "user", "content": 'распиши по подробнее тему (' + ww2 + ') '}],
              stream=True    
          )
          for item in response2:
              vv2 += item
      except Exception as e:
          print("Произошла ошибка:", e)
          response2 = None  # Сбросить значение response для повторной попытки получить ответ
  
  print(vv2)
  with open("3.txt", "w", encoding='utf-8') as file:
      file.write(vv2)
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================  
  response3 = None
  vv3 = ""
  while response3 is None:  # Запустить код заново, если ответ от GPT-3.5 Turbo не получен
      try:
          response3 = g4f.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{"role": "user", "content": 'распиши по подробнее тему (' + ww3 + ') '}],
              stream=True    
          )
          for item in response3:
              vv3 += item
      except Exception as e:
          print("Произошла ошибка:", e)
          response3 = None  # Сбросить значение response для повторной попытки получить ответ

  print(vv3)
  with open("4.txt", "w", encoding='utf-8') as file:
      file.write(vv3)      
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================  
  response4 = None
  vv4 = ""
  while response4 is None:  # Запустить код заново, если ответ от GPT-3.5 Turbo не получен
      try:
          response4 = g4f.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{"role": "user", "content": 'распиши по подробнее тему (' + ww4 + ') '}],
              stream=True    
          )
          for item in response4:
              vv4 += item
      except Exception as e:
          print("Произошла ошибка:", e)
          response4 = None  # Сбросить значение response для повторной попытки получить ответ

  print(vv4)
  with open("5.txt", "w", encoding='utf-8') as file:
      file.write(vv4)      
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================  
  response5 = None
  vv5 = ""
  while response5 is None:  # Запустить код заново, если ответ от GPT-3.5 Turbo не получен
      try:
          response5 = g4f.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=[{"role": "user", "content": 'распиши по подробнее тему (' + ww5 + ') '}],
              stream=True    
          )
          for item in response5:
              vv5 += item
      except Exception as e:
          print("Произошла ошибка:", e)
          response5 = None  # Сбросить значение response для повторной попытки получить ответ

  print(vv5)
  with open("6.txt", "w", encoding='utf-8') as file:
      file.write(vv5)       
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================
  #===========================================================  
  # Открываем презентацию 111
  presentation = Presentation('ffq.pptx')
  # Получаем первый слайд
  slide = presentation.slides[1]
  # Получаем заголовок первого слайда и устанавливаем в него текст из переменной ww1
  title = slide.shapes.title
  title.text = ww1
  # Получаем подзаголовок первого слайда и устанавливаем в него текст из переменной ll2
  subtitle = slide.placeholders[1]
  subtitle.text = vv1
  subtitle.text_frame.paragraphs[0].font.color.rgb = RGBColor(255,255,255)
  # Сохраняем изменения в презентацию
  presentation.save('ffq3.pptx')
      

  # Открываем презентацию 222
  presentation = Presentation('ffq.pptx')
  # Получаем второй слайд
  slide = presentation.slides[2] 
  # Получаем заголовок второго слайда и устанавливаем текст из переменной ww2
  title = slide.shapes.title
  title.text = ww2
  # Получаем подзаголовок второго слайда и устанавливаем текст из переменной ll3
  subtitle = slide.placeholders[1]  
  subtitle.text = vv2
  subtitle.text_frame.paragraphs[0].font.color.rgb = RGBColor(255,255,255)
  # Сохраняем изменения в презентацию 
  presentation.save('ffq3.pptx')   
      
      
  # Открываем презентацию 333
  presentation = Presentation('ffq.pptx')
  # Получаем второй слайд
  slide = presentation.slides[3] 
  # Получаем заголовок второго слайда и устанавливаем текст из переменной ww2
  title = slide.shapes.title
  title.text = ww3
  # Получаем подзаголовок второго слайда и устанавливаем текст из переменной ll3
  subtitle = slide.placeholders[1]  
  subtitle.text = vv3
  subtitle.text_frame.paragraphs[0].font.color.rgb = RGBColor(255,255,255)
  # Сохраняем изменения в презентацию 
  presentation.save('ffq3.pptx')      
      
      
  # Открываем презентацию 444
  presentation = Presentation('ffq.pptx')
  # Получаем второй слайд
  slide = presentation.slides[4] 
  # Получаем заголовок второго слайда и устанавливаем текст из переменной ww2
  title = slide.shapes.title
  title.text = ww4
  # Получаем подзаголовок второго слайда и устанавливаем текст из переменной ll3
  subtitle = slide.placeholders[1]  
  subtitle.text = vv4
  subtitle.text_frame.paragraphs[0].font.color.rgb = RGBColor(255,255,255)
  # Сохраняем изменения в презентацию 
  presentation.save('ffq3.pptx')         
      
      
  # Открываем презентацию 555
  presentation = Presentation('ffq.pptx')
  # Получаем второй слайд
  slide = presentation.slides[5] 
  # Получаем заголовок второго слайда и устанавливаем текст из переменной ww2
  title = slide.shapes.title
  title.text = ww5
  # Получаем подзаголовок второго слайда и устанавливаем текст из переменной ll3
  subtitle = slide.placeholders[1]  
  subtitle.text = vv5
  subtitle.text_frame.paragraphs[0].font.color.rgb = RGBColor(255,255,255)
  # Сохраняем изменения в презентацию 
  presentation.save('ffq3.pptx') 































