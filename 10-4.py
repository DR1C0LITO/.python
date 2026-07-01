#20/5/2026
#respostas simples
import speech_recognition as sr
import pyttsx3
maquina = pyttsx3.init()
voices = maquina.getProperty('voices')
print("Voices disponiveis: \n")
for i, voice in enumerate(voices):
    print(f"{i}: {voice.name}")
indice_voz = 0
maquina.setProperty('voice', voices[indice_voz].id)
maquina.setProperty('rate', 170)
maquina.setProperty('volume', 1.0)
audio = sr.Recognizer()
def falar(texto):
    maquina.say(texto)
    maquina.runAndWait()
def ouvir():
    with sr.Microphone() as source:
        print("Fale algo: ")
        audio.adjust_for_ambient_noise(source,duration=3)
        voz= audio.listen(source)
    try:
        global comando
        comando = audio.recognize_google(voz, language='pt-BR') 
        print("Você disse: " + comando)
        comando = comando.lower()
        return comando
        
    except:
        print("fala direito porra")
        
while True:
    comando =ouvir()
    if "oi" in comando:
        falar("eai bro")
    if "seu nome" in comando:
        falar("Meu nome é elizabetinha")
    if "desliga" in comando:
        falar("tchau bro")
        break  
    