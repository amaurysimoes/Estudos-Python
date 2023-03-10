#link de como fazer pesquisa google python
#https://www.youtube.com/watch?v=heeSp3qPJ8k
#Instalar os pacotes: pip install google / no linux: sudo pip install google
import webbrowser

from googlesearch import search

for resultado in search('"amaury huerb simões" google', stop=10):
    print (resultado)
    #Consulta do google
    url = resultado
    webbrowser.open(url)

for resultado in search('"amaury huerb simões" youtube', stop=10):
    print (resultado)
    #Consulta do youtube
    url = resultado
    webbrowser.open(url)

for resultado in search('"amaury huerb simões" hotmail', stop=10):
    print (resultado)
    #Consulta do hotmail
    url = resultado
    webbrowser.open(url)

for resultado in search('"amaury huerb simões" facebook', stop=10):
    print (resultado)
    #Consulta do facebook
    url = resultado
    webbrowser.open(url)

for resultado in search('"amaury huerb simões" linkedin', stop=10):
    print (resultado)
    #Consulta do Linkedin
    url = resultado
    webbrowser.open(url)

for resultado in search('"amaury huerb simões" github', stop=10):
    print (resultado)
    #Consulta do gitHub
    url = resultado
    webbrowser.open(url)