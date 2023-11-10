#+++++++++++++++++++++++++++++++++++
# главы в содержание с точками
input_file_path = '1.txt'
output_file_path = '1.txt'  # Можете изменить на нужный вам путь
with open(input_file_path, 'r', encoding='utf-8') as file:
    text = file.read()
# Разбиваем текст на строки и заполняем пропуски точками до конца каждой строки
filled_lines = [line.rstrip() + '.' * (80 - len(line.rstrip())) for line in text.split('\n')]
# Объединяем строки обратно в текст
filled_text = '\n'.join(filled_lines)
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(filled_text)
print(f'Заполненный текст сохранен в файле: {output_file_path}')
