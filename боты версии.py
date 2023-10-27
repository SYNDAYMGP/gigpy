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






















