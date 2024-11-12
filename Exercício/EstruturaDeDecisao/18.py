'''Faça um Programa que peça uma data no formato dd/mm/aaaa e 
determine se a mesma é uma data válida.'''
def verificacao(data):
    dd, mm, aaaa = data.split('/')
    dd, mm, aaaa = int(dd), int(mm), int(aaaa)
    if (0 < dd and dd <= 31) and (0 < mm and mm <= 12) and (1 < aaaa):
        return "Data válida."
    else:
        return "Data invalida."
data = input("Digite uma data no formato 'dd/mm/aaaa': ")
print(verificacao(data))