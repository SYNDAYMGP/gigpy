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


