'''
Faça um programa que faça 5 perguntas para uma pessoa sobre
um crime. As perguntas são:

"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime. Se a pessoa responder positivamente a 2 questões
ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como
"Inocente".
'''

def classificacao(lista_verificada):
    if lista_verificada == 2:
        classe = "Suspeita"
        return classe
    elif lista_verificada == 3 or lista_verificada == 4:
        classe = "Cúmplice"
        return classe
    elif lista_verificada == 5:
        classe = "Assassino"
        return classe
    else:
        classe = "Inocente"
        return classe
print("Reponda com sim ou não.\n")
pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")

lista = [pergunta1, pergunta2, pergunta3, pergunta4, pergunta5]
lista_verificada = 0

for i in lista:
    if i == "sim" or i == "Sim":
        lista_verificada += 1

verificacao = classificacao(lista_verificada)

print("\n=== CLASSIFICAÇÃO SOBRE A PARTICIPAÇÃO DA PESSOA NO CRIME ===\n")
print("Classificado como ", verificacao, '.')