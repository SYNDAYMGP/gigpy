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


