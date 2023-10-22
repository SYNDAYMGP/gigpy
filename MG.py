import logging
from telegram.ext import Updater, MessageHandler, Filters
from telegram import Document

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Ваш токен API бота
TOKEN = '6786106072:AAGz8bE4mNyJscUDrvARjYiXOCAyX5FukD4'


def handle_message(update, context):
    chat_id = update.effective_chat.id
    file_name = 'empty_pdf.pdf'

    with open(file_name, 'wb') as f:
        f.write(b'')

    # Отправка пустого файла PDF
    context.bot.send_document(chat_id=chat_id, document=open(file_name, 'rb'))

    # Опционально можно удалить файл после отправки
    # os.remove(file_name)


def start_bot():
    # Создание объекта Updater и передача ему токена API бота
    updater = Updater(TOKEN, use_context=True)

    # Получение диспетчера для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрация обработчика для сообщений
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Запуск бота
    updater.start_polling()

    # Можем отлавливать прерывания (нажатие Ctrl+C)
    updater.idle()


if __name__ == '__main__':
    start_bot()

_____________________________________________________
_____________________________________________________
_____________________________________________________

import logging
from pathlib import Path
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Устанавливаем уровень логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)


def start_command(update: Update, context) -> None:
    """Обрабатывает команду /start и отвечает пользователю."""
    update.message.reply_text('Привет! Отправь мне сообщение, чтобы получить пустую презентацию в формате PDF.')


def send_presentation(update: Update, context) -> None:
    """Отправляет пустую презентацию в формате PDF пользователю."""
    presentation_path = Path("empty_presentation.pdf")
    context.bot.send_document(chat_id=update.effective_chat.id, document=open(presentation_path, 'rb'))


def main() -> None:
    """Основная функция бота."""
    # Получаем токен от BotFather и инициализируем объект бота
    updater = Updater(token='YOUR_BOT_TOKEN', use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler("start", start_command))

    # Регистрируем обработчик всех остальных сообщений
    dp.add_handler(MessageHandler(Filters.text, send_presentation))

    # Запускаем бота
    updater.start_polling()

    # Ждем завершения работы с ботом
    updater.idle()


if __name__ == '__main__':
    main()


































