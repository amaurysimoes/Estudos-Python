#Criação de Aquivo Json com Informações

import json

QuantidadeItens = int(input("Qual a quantidade de Itens à Cadastrar?: "))
ComponenteEstoque = [0] * QuantidadeItens
CodigoComponente = [0] * QuantidadeItens

for i in range(QuantidadeItens):
    ComponenteEstoque[i] = input("Digite o Nome do Componente à Cadastrar : ")
    CodigoComponente[i] = float(input("Digite o Código da Peça: "))

for j in range(QuantidadeItens):
    CodigosEstoque = {
        "ItensNotebook": [{
            "Componente": ComponenteEstoque[j],
            "Codigo": CodigoComponente[j]
        }]
    }


with open("PartesPecas1.json", "w") as arquivo:
    json.dump(CodigosEstoque, arquivo, indent=4)