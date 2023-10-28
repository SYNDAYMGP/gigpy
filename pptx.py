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

