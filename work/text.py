from gtts import gTTS
import os

a="Hello World"
language= 'en'
output=gTTS(text=a,lang=language,slow=False)

output.save("output.mp3")

os.system("start output.mp3")