#Referencia: https://acervolima.com/ler-e-gravar-json-em-um-arquivo-em-python/
#Este Lê o arquivo Json
import json

with open('C:\JsonPython\PartesPecas2.json', 'r') as openfile:
    json_object = json.load(openfile)

print(json_object)
print(type(json_object))