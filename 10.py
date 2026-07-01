import speech_recognition as sr
import pyttsx3
engine = pyttsx3.init()
voz =engine.getProperty('voices')
print("disponiveis: \n")
for i, voice in enumerate(voz):
    print(f"{i}: {voice.name}") 
indice_voz = int(input("Select:    "))

engine.setProperty('voice', voz[indice_voz].id)
engine.setProperty('rate', 170)
engine.setProperty('volume', 1.0)
        
def speak(text):
    
    engine.say(text)
    
texto= sr.Recognizer()
with sr.Microphone() as source:
    print("Diga algo:")
    audio = texto.listen(source)
speak(texto.recognize_google(audio))
engine.runAndWait()