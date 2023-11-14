    ll7 = ""
    response = None
    while response is None or (response and 'Hm' in ll7):  # Запустить код заново, если ответ от GPT-3.5 Turbo не получен
        try:
            response = g4f.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": " Иван, вот тема доклада: " + text + ". А вот план доклада, состоящий из следующих глав: " + ll2 + ". Напиши, пожалуйста, полный текст пятой главы, раскрывающий ее смысл и не содержащий ссылок и источников." }],
                stream=True    
            )
            for item in response:
                ll7 += item
        except Exception as e:
            print("Произошла ошибка:", e)
            response = None  # Сбросить значение response для повторной попытки получить ответ
    print(ll7)
    time.sleep(80)

    # Список переменных для записи в файл
    variables_to_write = [ll2, ll3, ll4, ll5, ll6, ll7]
    # Открываем файл для записи с кодировкой UTF-8
    with open('1.txt', 'w', encoding='utf-8') as file:
        for i, variable in enumerate(variables_to_write):
            # Записываем содержимое переменной
            file.write(variable)

            # Добавляем пустую строку после каждой переменной, кроме последней
            if i < len(variables_to_write) - 1:
                file.write('\n\n\n')
    print("Содержимое переменных записано в файл 1.txt с использованием кодировки UTF-8")
    bot.send_document(message.chat.id, open('1.txt', 'rb'))
    bot.send_message(message.chat.id, 'Следующая генерация будет доступна через 5 мин')
bot.polling(none_stop=True, interval=0)



























import re
import openai
import telebot
import time
import telebot
from docx import Document
import time
bot = telebot.TeleBot('6786106072:AAGz8bE4mNyJscUDrvARjYiXOCAyX5FukD4')
openai.api_key = ""


@bot.message_handler(content_types=["text"]) 
def handle_text(message):
    bot.send_message(message.chat.id, 'Идёт генерация дождитесь ответа............')
    model_engine11 = "text-davinci-003"
    model_engine = "gpt-3.5-turbo"
    with open('1.txt', 'w') as file:
        file.write('')
    with open('2.txt', 'w') as file:
        file.write('')
    text = message.text
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    time.sleep(60)
    ll2 = ""
    prompt = "составь мне план (структуру) для моего доклада на тему (" + text + ") план должен состоять из шести глав ,а главы должны состоять из двух под глав, в ответ ты должен записать только название глав и название подглав к ним без каких либо твоих пояснений и дополнений , не забудь пронумеровать главы вот так (1, 2, 3, 4, 5, 6) , а под главы пронумеруй так (1.1 1.2, 2.1 2.2 , 3.1 3.2, 4.1 4.2, 5.1 5.2 , 6.1 6.2)"
    response = openai.Completion.create(
    engine=model_engine11,
    prompt=prompt,
    max_tokens=2750,
    n=1,
    stop=None,
    temperature=0.5,
    )
    ll2 = response.choices[0].text
    print(ll2)
    time.sleep(60)
    with open("1.txt", "w", encoding='utf-8') as file:
      file.write(ll2)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    # Открываем файл для чтения с указанием кодировки UTF-8
    with open('1.txt', 'r', encoding='utf-8') as file:
      lines = file.readlines()
    ww_vars = []
    for line in lines:
      if re.search(r'\d', line) and len(line.strip()) > 0:
        ww_vars.append(line)
    print(ww_vars[0])
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #1================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll3 = ""
    prompt = "Распиши по подробнее эту часть доклада(" + ww_vars[1] + "), относящуюся к данной главе (" + ww_vars[0] + "), данного доклада (" + text + ")"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll3 = response['choices'][0]['message']['content']
    print(ll3)
    time.sleep(60)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #2================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll4 = ""
    prompt = "Распиши по подробнее эту часть доклада(" + ww_vars[2] + "), относящуюся к данной главе (" + ww_vars[0] + "), данного доклада (" + text + ")"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll4 = response['choices'][0]['message']['content']
    print(ll4)
    time.sleep(60)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #3================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll5 = ""
    prompt = "Распиши по подробнее эту часть доклада(" + ww_vars[4] + "), относящуюся к данной главе (" + ww_vars[3] + "), данного доклада (" + text + ")"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll5 = response['choices'][0]['message']['content']
    print(ll5)
    time.sleep(60)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #4================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll6 = ""
    prompt = "Распиши по подробнее эту часть доклада(" + ww_vars[5] + "), относящуюся к данной главе (" + ww_vars[3] + "), данного доклада (" + text + ")"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll6 = response['choices'][0]['message']['content']
    print(ll6)
    time.sleep(60)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #5================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll7 = ""
    prompt = "Распиши по подробнее эту часть доклада(" + ww_vars[7] + "), относящуюся к данной главе (" + ww_vars[6] + "), данного доклада (" + text + ")"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll7 = response['choices'][0]['message']['content']
    print(ll7)
    time.sleep(60)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #6================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll8 = ""
    prompt = "Распиши по подробнее эту часть доклада(" + ww_vars[8] + "), относящуюся к данной главе (" + ww_vars[6] + "), данного доклада (" + text + ")"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll8 = response['choices'][0]['message']['content']
    print(ll8)
    time.sleep(60)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #7================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll9 = ""
    prompt = "Распиши по подробнее эту часть доклада(" + ww_vars[10] + "), относящуюся к данной главе (" + ww_vars[9] + "), данного доклада (" + text + ")"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll9 = response['choices'][0]['message']['content']
    print(ll9)
    time.sleep(60)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #8================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll10 = ""
    prompt = "Распиши по подробнее эту часть доклада(" + ww_vars[11] + "), относящуюся к данной главе (" + ww_vars[9] + "), данного доклада (" + text + ")"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll10 = response['choices'][0]['message']['content']
    print(ll10)
    time.sleep(60)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #9================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll11 = ""
    prompt = "Распиши по подробнее эту часть доклада(" + ww_vars[13] + "), относящуюся к данной главе (" + ww_vars[12] + "), данного доклада (" + text + ")"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll11 = response['choices'][0]['message']['content']
    print(ll11)
    time.sleep(60)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #10================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll12 = ""
    prompt = "Распиши по подробнее эту часть доклада(" + ww_vars[14] + "), относящуюся к данной главе (" + ww_vars[12] + "), данного доклада (" + text + ")"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll12 = response['choices'][0]['message']['content']
    print(ll12)
    time.sleep(60)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #11================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll13 = ""
    prompt = "Распиши по подробнее эту часть доклада(" + ww_vars[16] + "), относящуюся к данной главе (" + ww_vars[15] + "), данного доклада (" + text + ")"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll13 = response['choices'][0]['message']['content']
    print(ll13)
    time.sleep(60)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    #12================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll14 = ""
    prompt = "Распиши по подробнее эту часть доклада(" + ww_vars[17] + "), относящуюся к данной главе (" + ww_vars[15] + "), данного доклада (" + text + ")"
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    if response['choices']:
        ll14 = response['choices'][0]['message']['content']
    print(ll14)
    time.sleep(60)
    # Список переменных для записи в файл
    variables_to_write = [ll2, ll3, ll4, ll5, ll6, ll7, ll8, ll9, ll10, ll11, ll12, ll13, ll14]
    # Открываем файл для записи с кодировкой UTF-8
    with open('2.txt', 'w', encoding='utf-8') as file:
        for i, variable in enumerate(variables_to_write):
            # Записываем содержимое переменной
            file.write(variable)

            # Добавляем пустую строку после каждой переменной, кроме последней
            if i < len(variables_to_write) - 1:
                file.write('\n\n\n')
    print("Содержимое переменных записано в файл 2.txt с использованием кодировки UTF-8")
    bot.send_document(message.chat.id, open('2.txt', 'rb'))
    bot.send_message(message.chat.id, 'Следующая генерация будет доступна через 5 мин')
bot.polling(none_stop=True, interval=0)


    

    








