#Referencia: https://acervolima.com/ler-e-gravar-json-em-um-arquivo-em-python/
#Este Insere no arquivo Json
import json

dictionary ={
    "Componente" : "MOTHEBOARD3",
    "Codigo" : 202020203,
    "Quantidade em Estoque" : 103,
    "Local de Alocacao" : "Caixa1 rua13"
}
with open("C:\JsonPython\PartesPecas2.json", "w") as outfile:
    json.dump(dictionary, outfile)