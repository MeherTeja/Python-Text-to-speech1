from gtts import gTTS
import os

a="Text to speech convertor using python"
language= 'en'
output=gTTS(text=a,lang=language,slow=False)

output.save("output.mp3");

os.system("start output.mp3")