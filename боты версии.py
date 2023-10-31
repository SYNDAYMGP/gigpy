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
  bot.send_message(message.chat.id, ll2)
    
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




















