import g4f
import telebot
from pptx import Presentation
from pptx.util import Pt
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

    #первый запрос 111
    response1 = g4f.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": 'распиши по подробнее данную тему(' + ww1 + ')в ответе ты должен раскрыть данную тему целиком, дай ответ объёмно '}],
      stream=True    
    )
    ll2q2 = ""
    for item in response1:
      ll2q2 += item
    with open("2.txt", "w", encoding='utf-8') as file:
      file.write(ll2q2)
    #первый запрос 222
    response2 = g4f.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": 'распиши по подробнее данную тему(' + ww2 + ')в ответе ты должен раскрыть данную тему целиком, дай ответ объёмно '}],
      stream=True    
    )
    ll2q3 = ""
    for item in response2:
      ll2q3 += item
    with open("3.txt", "w", encoding='utf-8') as file:
      file.write(ll2q3)
    #первый запрос 333
    response3 = g4f.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": 'распиши по подробнее данную тему(' + ww3 + ')в ответе ты должен раскрыть данную тему целиком, дай ответ объёмно '}],
      stream=True    
    )
    ll2q4 = ""
    for item in response3:
      ll2q4 += item
    with open("4.txt", "w", encoding='utf-8') as file:
      file.write(ll2q4)
    #первый запрос 444
    response4 = g4f.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": 'распиши по подробнее данную тему(' + ww4 + ')в ответе ты должен раскрыть данную тему целиком, дай ответ объёмно '}],
      stream=True    
    )
    ll2q5 = ""
    for item in response4:
      ll2q5 += item
    with open("5.txt", "w", encoding='utf-8') as file:
      file.write(ll2q5)
    #первый запрос 555
    response5 = g4f.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": 'распиши по подробнее данную тему(' + ww5 + ')в ответе ты должен раскрыть данную тему целиком, дай ответ объёмно '}],
      stream=True    
    )
    ll2q6 = ""
    for item in response5:
      ll2q6 += item
    with open("6.txt", "w", encoding='utf-8') as file:
      file.write(ll2q6)
    #первый запрос 666
    response6 = g4f.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=[{"role": "user", "content": 'распиши по подробнее данную тему(' + ww6 + ')в ответе ты должен раскрыть данную тему целиком, дай ответ объёмно '}],
      stream=True    
    )
    ll2q7 = ""
    for item in response6:
      ll2q7 += item
    with open("7.txt", "w", encoding='utf-8') as file:
      file.write(ll2q7)
