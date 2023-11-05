*********************ЗАПРОС С ИСПОЛЬЗОВАНИЕМ КОНТЕКСТА ЧЕРЕЗ ПЕРЕМЕННЫЕ гпт*****************
import openai
import os
import g4f
import telebot
from pptx import Presentation
from pptx.util import Pt
from pptx.dml.color import RGBColor
import time
openai.api_key = "АЛЁ ВВЕДИ АПИ"
model_engine = "text-davinci-003"
text = 'Халк'

#================СОЗДАНИЕ ВЫСШЕГО ВОПРОСА===========================================
ll2 = ""
prompt1 = "составь мне план (структуру) для моего доклада на тему (" + text + ") план должен состоять из глав в ответ ты должен записать только название глав без каких либо твоих пояснений и дополнений , не забудь пронумеровать их вот так 1, 2, 3, 4, 5"
response = openai.Completion.create(
 engine=model_engine,
 prompt=prompt1,
 max_tokens=400,
 n=1,
 stop=None,
 temperature=0.5,
)
ll2 = response.choices[0].text
print(ll2)
with open("2.txt", "w", encoding='utf-8') as file:
 file.write(ll2)

#================СОЗДАНИЕ НИЖНЕГО ВОПРОСА===========================================( НЕ ЗАБЫВАЕМ МЕНЯТЬ по х-й главе ОТ ТОЙ КОТОРУЮ БЕРЁМ)
prompt4 = "Вот тема моего доклада «" + text + "» , у этой темы есть план (" + ll2 +") Расскажи мне про тему доклада «" + text + "» по 2-й главе предоставленной мной очень очень кратко ответ должен содержать не более 37 слов."
response4 = openai.Completion.create(
 engine=model_engine,
 prompt=prompt4,
 max_tokens=500,
 n=1,
 stop=None,
 temperature=0.5,
)
vv3 = response4.choices[0].text
print(vv3)
with open("4.txt", "w", encoding='utf-8') as file:
    file.write(vv3)
#================
#================
#================
#================
#================
import g4f
response = None
ll2 = ""
text = "человек паук"
while response is None:
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "составь мне план (структуру) для моего доклада на тему (" + text + ") план должен состоять из глав в ответ ты должен записать только название глав без каких либо твоих пояснений и дополнений , не забудь пронумеровать их вот так 1, 2, 3, 4, 5" }],
            stream=True    
        )
        ll2 = "".join(response)
    except Exception as e:
        print("Произошла ошибка:", e)
        response = None  # Сбросить значение response для повторной попытки получить ответ
print(ll2)
#================СОЗДАНИЕ НИЖНЕГО ВОПРОСА===========================================
response = None
ll2 = ""
text = "человека паука"
while response is None:  # Запустить код заново, если ответ от GPT-3.5 Turbo не получен
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": "(вот тема доклада (человек паук) ,а вот план доклада состоящий из глав (1. Введение 2. История создания персонажа 3.Суперспособности Человека-паука 4. Враги и союзники Человека-паука 5. Влияние Человека-паука на поп-культуру) . Твоя задача написать первую главву данной темы. Твой ответ должен полностью раскрывать смысл главы " }],
            stream=True    
        )
        for item in response:
            ll2 += item
    except Exception as e:
        print("Произошла ошибка:", e)
        response = None  # Сбросить значение response для повторной попытки получить ответ
print(ll2)
