
import os
from pathlib import Path

PARENT_DIR = Path(__file__).parent
filename = 'referat.txt'
filename_dst = 'referat2.txt'

file_path = os.path.join(PARENT_DIR, filename)
with open(file_path) as f:
    text = f.read()

text_len = len(text)
print(f'Длина текста: {text_len} символов')

words_cnt = len(text.split())
print(f'Количество слов: {words_cnt}')

text = text.replace('.', '!')
file_path = os.path.join(PARENT_DIR, filename_dst)
with open(file_path, 'w') as f:
    f.write(text)
