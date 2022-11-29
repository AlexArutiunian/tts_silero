import pdfminer.high_level
from googletrans import Translator

with open('howell.1980-5-11.pdf', 'rb') as file:
    file1 = open(r'howell5-11.txt', 'a+')
    pdfminer.high_level.extract_text_to_fp(file, file1)
    file1.close()
print("now book is in txt")