#20/5/2026
#apenas uma mistura dos outros
import speech_recognition as sr
import pyttsx3
maquina = pyttsx3.init()
voices = maquina.getProperty('voices')
print("Voices disponiveis: \n")
for i, voice in enumerate(voices):
    print(f"{i}: {voice.name}")
indice_voz = int(input("Select:    "))
maquina.setProperty('voice', voices[indice_voz].id)
maquina.setProperty('rate', 170)
maquina.setProperty('volume', 1.0)
audio = sr.Recognizer()
def falar(texto):
    maquina.say(texto)
def ouvir():
    with sr.Microphone() as source:
        print("Fale algo: ")
        voz= audio.listen(source)
    try:
        global texto
        texto = audio.recognize_google(voz, language='pt-BR') 
        print("Você disse: " + texto)
        falar(texto)
    except:
        print("fala direito porra")
ouvir()
maquina.runAndWait()