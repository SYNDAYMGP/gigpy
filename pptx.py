фул количество символов в подзоголовке = 1850





from pptx import Presentation
from pptx.util import Pt
root = Presentation()
first_slide_layout = root.slide_layouts[1]
slide = root.slides.add_slide(first_slide_layout)
# заголовок слайда
slide.shapes.title.text = 'Текст заголовка'

# подзаголовок слайда
text_frame = slide.placeholders[1].text_frame
text_frame.text = 'Текст подзаголовка'

# формирование формата текста
p = text_frame.paragraphs[0]
p.font.size = Pt(14) 
p.font.name = 'Times New Roman'

# сохранение презентации 
root.save('Example.pptx')




,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
from pptx import Presentation
from pptx.util import Pt
root = Presentation()

#создание первого слайда
first_slide_layout = root.slide_layouts[1]
slide = root.slides.add_slide(first_slide_layout)
# создание заголовка слайда
slide.shapes.title.text = 'Текст заголовка'
# создание подзаголовка слайда
text_frame = slide.placeholders[1].text_frame
text_frame.text = 'Текст подзаголовка'
# формирование формата текста
p = text_frame.paragraphs[0]
p.font.size = Pt(14) 
p.font.name = 'Times New Roman'


#создание второго слайда
first_slide_layout2 = root.slide_layouts[1]
slide = root.slides.add_slide(first_slide_layout2)
# создание заголовка слайда
slide.shapes.title.text = 'Текст заголовка'
# создание подзаголовка слайда
text_frame = slide.placeholders[1].text_frame
text_frame.text = 'Текст подзаголовка'
# формирование формата текста
p = text_frame.paragraphs[0]
p.font.size = Pt(14) 
p.font.name = 'Times New Roman'


# сохранение презентации 
root.save('Example.pptx')
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
,,,,,,,,,,,,,,,
import g4f
import telebot
from pptx import Presentation
from pptx.util import Pt


bot = telebot.TeleBot('6786106072:AAGz8bE4mNyJscUDrvARjYiXOCAyX5FukD4')
@bot.message_handler(content_types=["text"])
def handle_text(message):
  with open('1.txt', 'w') as file:
    file.write('')
  text = message.text
  response = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": 'составь мне план (структуру) для моего доклада на тему (' + text + ') план должен состоять из глав в ответ ты должен записать только название глав без каких либо твоих пояснений и дополнений , не забудь пронумеровать их вот так 1, 2, 3, 4, 5'}], 
    stream=True
  )
  for msg in response:
    with open('1.txt', 'a', encoding='utf-8') as file:
      file.write(msg)
  with open('1.txt', 'r', encoding='utf-8') as file:
    text = file.read()
  start = text.find('1') + 1
  end = text.find('2')
  extracted_text = text[start:end].strip()
  ww1 = extracted_text
  
  if ww1:
    response1 = g4f.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": ww1}], 
    stream=True
   )
    text = next(response1)
  for msg in response1:
     root = Presentation()
     #создание первого слайда
     first_slide_layout = root.slide_layouts[1]
     slide = root.slides.add_slide(first_slide_layout)
     # создание заголовка слайда
     slide.shapes.title.text = 'Текст заголовка'
     # создание подзаголовка слайда
     text_frame = slide.placeholders[1].text_frame
     text_frame.text = 'hello'
     # формирование формата текста
     p = text_frame.paragraphs[0]
     p.font.size = Pt(14) 
     p.font.name = 'Times New Roman'
     root.save('Example.pptx')
  bot.send_document(message.chat.id, open('Example.pptx', 'rb'))
bot.polling(none_stop=True, interval=0)

