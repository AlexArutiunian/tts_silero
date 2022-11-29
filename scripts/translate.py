import pdfminer.high_level
import translators as tts

# по 1 странице переводить в цикле затем по главам обьединить в файлы

f = open('howell5-11.txt', 'r')
if f.mode == 'r':
    print("access")
contents = f.read()
result = tts.google(contents, from_language='en', to_language='ru')
with open('erase.txt', 'w') as f_:
    f_.write(result.text)
print("access")    