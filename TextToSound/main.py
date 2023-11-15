import os
import time
from gtts import gTTS

with open('text.txt', 'r', encoding='utf-8') as f:
    metin = f.read()
tts = gTTS(text=metin, lang='tr')
tts.save('sesli_metin.mp3')
os.system('mpg321 -g 50 -s 20 sesli_metin.mp3')
