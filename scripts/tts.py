
from gtts import gTTS

txt = '«Привет, мама, - неуверенно говорю я. "Ты в порядке? Мы обычно говорим о Воскресенье. Я смотрю сквозь занавески над своей кроватью.'
tts = gTTS(text=txt,lang='ru', tld='com.au', slow=True)
tts.save("SAVE.mp3")