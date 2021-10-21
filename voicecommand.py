#Metin için gerekli modülü içe aktardım.
from gtts import gTTS
import os
while(True):
    istenilen = input("Söylemek istediğiniz şeyi girin: ")
    language = 'tr'
    #dönüştürülen sesin olması gereken modül
    myobj = gTTS(text=istenilen, lang=language, slow=False)
    myobj.save("welcome.mp3")
    os.system("welcome.mp3")

    # say = gTTStext = istenilen.lang ("en")
    #say.save('isim.wav')
    #os.system('isim.wav')