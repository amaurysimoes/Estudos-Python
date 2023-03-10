#Referencia: https://acervolima.com/ler-e-gravar-json-em-um-arquivo-em-python/
#Este Cria o arquivo Json
import json

dictionary ={
    "Componente" : "MOTHEBOARD",
    "Codigo" : 20202020,
    "Quantidade em Estoque" : 10,
    "Local de Alocação" : "Caixa1 rua1"
}
json_object = json.dumps(dictionary, indent = 4)
with open("C:\JsonPython\PartesPecas2.json", "w") as outfile:
    outfile.write(json_object)