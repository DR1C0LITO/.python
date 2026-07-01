#20/5/2026      
import speech_recognition as sr
audio = sr.Recognizer()
with sr.Microphone() as source:
    print("Fale algo: ")
    voz= audio.listen(source)
    try:
        texto = audio.recognize_google(voz, language='pt-BR')
        print("Você disse: " + texto)
    except:
        print("fala direito porra")