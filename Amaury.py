import pyttsx3 #Biblioteca gratuita "Zira"
import datetime
import speech_recognition as sr
import webbrowser, os
import os

#cxfreeze Amaury.py --target-dir IAHS2

texto_fala = pyttsx3.init()

def falar(audio):
    rete = texto_fala.getProperty('rate')
    #texto_fala.setProperty("rate", 180)#Velocidade da fala
    texto_fala.setProperty("rate", 180)  # Velocidade da fala
    voices = texto_fala.getProperty('voices')
    texto_fala.setProperty('voice', voices[2].id)
    texto_fala.say(audio)
    texto_fala.runAndWait()

def tempo():
    Tempo = datetime.datetime.now().strftime("%I:%M")
    falar("A hora atual é:")
    falar(Tempo)

def data():
    ano  = str(datetime.datetime.now().year)
    mes = str(datetime.datetime.now().month)
    dia = str(datetime.datetime.now().day)
    falar("Data atual é:")
    falar(dia)
    falar("de" + mes)
    falar("de" + ano)

def google():
    falar("quero que você abra o google")
    url="https://google.com"
    webbrowser.open(url)

def crm():
    falar("quero que você abra o crm")
    url="http://b1.ativy.com:22579/"
    webbrowser.open(url)

def pastasTeste():
    falar("quero que você abra a pasta dos testes")
    caminho ="//avellweb/ProjetosOK/2-PROJETOS_DESENVOLVIMENTO/1.2-TESTES_AVELL"
    webbrowser.open(os.path.realpath(caminho))
    #\\avellweb\ProjetosOK\2-PROJETOS_DESENVOLVIMENTO\1.2-TESTES_AVELL

def sistemaControle():
    falar("quero que você abra o sistema de controle")
    url="http://192.168.247.94/avellweb"
    webbrowser.open(url)

#Abrir programa externo com python
def sistemaTeste():
    falar("quero que você abra o sistema de testes")
    caminho = os.startfile(r'C:/TESTES_AVELL/.executaveis/TESTE_MAQUINAS.exe')

def mostrarComandos():
    falar("lista de comandos")
    print('')
    print('lista de comandos')#Mostrar em outro local.
    print('código da placa do a70')
    print('quero que você abra o google')
    print('quero que você abra o crm')
    print('quero que você abra a pasta dos testes')
    print('quero que você abra o sistema de controle')
    print('quero que você abra o sistema de testes')
    print('abir apresentação dos testes')
    print('consultar internet')

    ##Chamar o script de mostrar comandos:
    #import lerTxt
    #def func2():
    #    print("Fazer a leitura de comandos")
    #    func2()
    #    func2().func1()

def pesquisaGoogle():
    falar("consultar internet")
    #Chama métodos em outra máquina
    import pesquisaGoogle
    def func2():
        print("Chamando script de pesquisas!")
        func2()
        func2().func1()

def bem_vindo():
    falar("Ativado")
    #tempo()
    #data()
    #google()

    hora = datetime.datetime.now().hour

    if hora >= 6 and hora < 12:
        falar("bom dia")
    elif hora >= 12 and hora < 18:
        falar("boa tarde")
    elif hora >= 18 and hora <= 24:
        falar("boa noite")
    else:
        falar("boa madrugada")
    falar("Alguma solicitação?")
#bem_vindo() - Exemplo anterior


#instalar o: #pip install pyaudio
def microne():
    # r = Tipo de dados que já vem na biblioteca speech
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.pause_threshold = 1
        audio = r.listen(source)
        
    try:
        print("Reconhecendo...")
        comando = r.recognize_google(audio,language='pt-br')
        print(comando)

    except Exception as e:
        print(e)
        #falar("Repita a informação")-Desabilitado para não ficar o tempo todo repetindo

        return "None"
    
    return comando

#microne() - Exemplo anterior

if __name__== "__main__":
    bem_vindo()

    while True:
        print("Escutando..")
        comando = microne().lower()

        if 'como você está' in comando:
            falar("Estou bem")

        if 'código da placa do a70' in comando:
            falar("A70 MOB 30 60 MP000390 / TAMBÉM - MP001925"
                  "TEMBÉM - A70 HYB 30 60 MP001016 / TAMBÉM A70HYB 30 50 BS MP001869")


        if 'hora' in comando:
            tempo()

        if 'data' in comando:
            data()

        if 'quero que você abra o google' in comando:
            google()

        if 'quero que você abra o crm' in comando:
            crm()

        if 'quero que você abra a pasta dos testes' in comando:
            pastasTeste()

        if 'quero que você abra o sistema de controle' in comando:
            sistemaControle()

        if 'quero que você abra o sistema de testes' in comando:
            sistemaTeste()

        if 'lista de comandos' in comando:
            mostrarComandos()

        elif 'consultar internet' in comando:
            pesquisaGoogle()