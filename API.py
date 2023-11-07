(задаём ввопрос гпт чату)
import openai
# Здесь нужно указать ваш API-ключ от OpenAI
api_key = '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'
def generate_response(prompt):
    openai.api_key = api_key
    response = openai.Completion.create(
        engine="text-davinci-002",  # Выберите подходящий движок для задачи
        prompt=prompt,
        max_tokens=50,  # Максимальное количество токенов в ответе
    )
    return response.choices[0].text
# Пример вопроса о плане для доклада
question = "write a general plan for the report (world economy) your plan should contain at least 5 sections directly revealing the topic, your answer should consist only of the names of the sections.  In addition, number the names of the sections so 1,2,3, and so on"
response = generate_response(question)
# Сохранить ответ в файл 2.txt
with open("2.txt", "w", encoding="utf-8") as file:
    file.write(response)
print("Ответ сохранен в файле 2.txt")




@@@
@@@
@@@
@@@
@@@
сохраняем информацию из файла которая находится между 1 и 2 и записываем в переменную
with open('1.txt', 'r', encoding='utf-8') as file:
  text = file.read()
start = text.find('1') + 1
end = text.find('2')
extracted_text = text[start:end].strip()
ww = extracted_text
print(ww)

@@@
@@@
@@@
@@@
@@@

import g4f
# streamed completion
response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello"}],
    stream=True,
)
for message in response:
    print(message, flush=True, end='')











.
⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆ 
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿ 
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀ 
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀ 
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀
                  ⠉⠛⠻⠿⠿⠿⠿⠛⠉


import openai
import telebot
import time
import telebot
from docx import Document
import g4f
import time
bot = telebot.TeleBot('6786106072:AAGz8bE4mNyJscUDrvARjYiXOCAyX5FukD4')
openai.api_key = ""


@bot.message_handler(content_types=["text"]) 
def handle_text(message):
    bot.send_message(message.chat.id, 'Идёт генерация дождитесь ответа............')
    model_engine = "text-davinci-003"
    with open('1.txt', 'w') as file:
        file.write('')
    text = message.text
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll2 = ""
    prompt = "составь мне план (структуру) для моего доклада на тему (" + text + ") план должен состоять из глав в ответ ты должен записать только название глав без каких либо твоих пояснений и дополнений , не забудь пронумеровать их вот так 1, 2, 3, 4, 5 ,к тому же твой ответ не должен содержать ни каких Source то есть не должен указывать источники и ссылки"
    response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=3000,
    n=1,
    stop=None,
    temperature=0.5,
    )
    ll2 = response.choices[0].text
    print(ll2)
    time.sleep(60)
    #================СОЗДАНИЕ НИЖНЕГО ВОПРОСА===========================================( НЕ ЗАБЫВАЕМ МЕНЯТЬ по х-й главе ОТ ТОЙ КОТОРУЮ БЕРЁМ)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll3 = ""
    prompt = "(вот тема доклада (" + text + ") ,а вот план доклада состоящий из глав (" + ll2 + ") . Твоя задача написать первую главу данной темы. Твой ответ должен полностью раскрывать смысл главы , к тому же твой ответ не должен содержать ни каких Source то есть не должен указывать источники и ссылки"
    response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=3000,
    n=1,
    stop=None,
    temperature=0.5,
    )
    ll3 = response.choices[0].text
    print(ll3)
    time.sleep(60)
    #================СОЗДАНИЕ НИЖНЕГО ВОПРОСА===========================================( НЕ ЗАБЫВАЕМ МЕНЯТЬ по х-й главе ОТ ТОЙ КОТОРУЮ БЕРЁМ)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll4 = ""
    prompt = "(вот тема доклада (" + text + ") ,а вот план доклада состоящий из глав (" + ll2 + ") . Твоя задача написать вторую главу данной темы. Твой ответ должен полностью раскрывать смысл главы , к тому же твой ответ не должен содержать ни каких Source то есть не должен указывать источники и ссылки"
    response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=3000,
    n=1,
    stop=None,
    temperature=0.5,
    )
    ll4 = response.choices[0].text
    print(ll4)
    time.sleep(60)
    #================СОЗДАНИЕ НИЖНЕГО ВОПРОСА===========================================( НЕ ЗАБЫВАЕМ МЕНЯТЬ по х-й главе ОТ ТОЙ КОТОРУЮ БЕРЁМ)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll5 = ""
    prompt = "(вот тема доклада (" + text + ") ,а вот план доклада состоящий из глав (" + ll2 + ") . Твоя задача написать третью главу данной темы. Твой ответ должен полностью раскрывать смысл главы , к тому же твой ответ не должен содержать ни каких Source то есть не должен указывать источники и ссылки"
    response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=3000,
    n=1,
    stop=None,
    temperature=0.5,
    )
    ll5 = response.choices[0].text
    print(ll5)
    time.sleep(60)
    #================СОЗДАНИЕ НИЖНЕГО ВОПРОСА===========================================( НЕ ЗАБЫВАЕМ МЕНЯТЬ по х-й главе ОТ ТОЙ КОТОРУЮ БЕРЁМ)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll6 = ""
    prompt = "(вот тема доклада (" + text + ") ,а вот план доклада состоящий из глав (" + ll2 + ") . Твоя задача написать четвёртую главу данной темы. Твой ответ должен полностью раскрывать смысл главы , к тому же твой ответ не должен содержать ни каких Source то есть не должен указывать источники и ссылки"
    response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=3000,
    n=1,
    stop=None,
    temperature=0.5,
    )
    ll6 = response.choices[0].text
    print(ll6)
    time.sleep(60)
    #================СОЗДАНИЕ НИЖНЕГО ВОПРОСА===========================================( НЕ ЗАБЫВАЕМ МЕНЯТЬ по х-й главе ОТ ТОЙ КОТОРУЮ БЕРЁМ)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    ll7 = ""
    prompt = "(вот тема доклада (" + text + ") ,а вот план доклада состоящий из глав (" + ll2 + ") . Твоя задача написать пятую главу данной темы. Твой ответ должен полностью раскрывать смысл главы , к тому же твой ответ не должен содержать ни каких Source то есть не должен указывать источники и ссылки"
    response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=3000,
    n=1,
    stop=None,
    temperature=0.5,
    )
    ll7 = response.choices[0].text
    print(ll7)
    time.sleep(60)
    #================СОЗДАНИЕ НИЖНЕГО ВОПРОСА===========================================( НЕ ЗАБЫВАЕМ МЕНЯТЬ по х-й главе ОТ ТОЙ КОТОРУЮ БЕРЁМ)
    #================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
    
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

    



