#API key: 1f7cbc15e0c07c94eae330f3cfe7c532
import speech_recognition as sr
from googlesearch import search 
import pyttsx3
import requests
import datetime
import wikipedia
import webbrowser
import pywhatkit
from playsound import playsound
import os
import random
from urllib.parse import quote
import keyboard

audio = sr.Recognizer()
maquina = pyttsx3.init()    
voices = maquina.getProperty('voices')
for voice in voices:
    if "brazil" in voice.name.lower() or "portuguese" in voice.name.lower():
        maquina.setProperty('voice', voice.id)
with sr.Microphone() as source:
    audio.adjust_for_ambient_noise(source,duration=1)
def falar(texto):
    texto = str(texto)
    print(f"elizabetinha: {texto}")
    try:
        maquina.stop()
        maquina.say(texto)
        maquina.runAndWait()
        

    except Exception as e:
        print(f"Erro ao falar: {e}")
    
def comandos(comando):
    
  
                
    if "pesquisa" in comando or "pesquisar" in comando or "pesquise" in comando:
        procurar = comando.replace("pesquisa","").replace("pesquisar","").replace("pesquise","")
        webbrowser.open("https://www.google.com/search?q=" + quote(procurar))
    if "aura" in comando:
        falar(random.choice(["Ligando toda a sua aura", "To sobrecarregada de Aura, Ta dificil","AI MEU DEUs É MUITA AURA",]))
        phonk=random.choice(["sounds/passo.mp3","sounds/tiki.mp3","sounds/yara.mp3"])
        pywhatkit.playonyt(phonk)       
def ouvir1():
    comando = ""
    print("Ouvindo...")
    try:
        with sr.Microphone() as source:
           voz = audio.listen(source,phrase_time_limit=5)
           comando = audio.recognize_google(voz, language="pt-BR")
           comando = comando.lower()
           
           
           
        if "eliza" in comando:
            respostas =["eai mano","To pronto para te servir ","como posso ajudar","DRI DRII"]
            falar(random.choice(respostas))
            ouvir()
    except sr.UnknownValueError:
        pass
    except Exception as e:
        print(f"Erro: {e}")
        return ""

def ouvir():
    comando = ""
    print("Ouvindo...")
    try:
        with sr.Microphone() as source:
           voz = audio.listen(source,phrase_time_limit=5)
           comando = audio.recognize_google(voz, language="pt-BR")
           comando = comando.lower()
           print(f"comando recebido: {comando}")
           
           
        
        comandos(comando)
    except sr.UnknownValueError:
        pass
    except Exception as e:
        print(f"Erro: {e}")
        return ""

print("comando = end ") 

  
    
while True:
 ouvir1()

       
#executar_elizabetinha()        