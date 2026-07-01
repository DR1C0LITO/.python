#27/5/2026
#API key: 1f7cbc15e0c07c94eae330f3cfe7c532
import speech_recognition as sr
import pyttsx3
import requests
from urllib.parse import quote
audio = sr.Recognizer()
maquina = pyttsx3.init()
voices = maquina.getProperty('voices')      
for voice in voices:
    if "brazil" in voice.name.lower() or "portuguese" in voice.name.lower():
        maquina.setProperty('voice', voice.id)
        break
def falar(texto):
    print("Elizabetinha: " + texto)
    maquina.say(texto)
    maquina.runAndWait()
def ouvir():
    try:
        with sr.microphone() as source:
            print("\n fale nome da cidade:")
            audio.adjust_for_ambient_noise(source,duration=1)#ajuste para ruídos
            voz = audio.listen(source,phrase_time_limit=5) #limite de tempo para ouvir
            comando = audio.recognize_google(voz, language='pt-BR').lower()
            print("Você disse: " + comando)                    
            return comando
    except:
        falar("Não consegui ouvir, tente novamente.")
        return "" 
def clima(cidade):
    api_key = "1f7cbc15e0c07c94eae330f3cfe7c532"
    cidade_codificada = quote(cidade)
    link = f"http://api.openweathermap.org/data/2.5/weather?q={cidade_codificada}&appid={api_key}&lang=pt_br&units=metric"
    try:
        requisicao = requests.get(link)
        dados = requisicao.json()
        if dados['cod']==200:
            descricao = dados['weather'][0]['description']
            temperatura = dados['main']['temp']
            return f'em {cidade},faz {temperatura:.1f}°C e o clima é {descricao}'
        else:
            return "Cidade não encontrada."
        
    except: 
        return "Erro ao acessar internet." 
falar("iniciando elizabetinha, diga o nome da cidade para saber o clima")
while True:
    cidade = ouvir()
    if cidade !="":
        resultado = clima(cidade)
        falar(resultado)
    falar("Deseja consultar outra cidade? Diga sim ou não.")
    resposta = ouvir()
    if "não" in resposta or "nao" in resposta:
        falar("tchau bro")
        break