'''Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se
digitar outro valor deve aparecer valor inválido.'''
dicionario = {
    1: 'Domingo',
    2: 'Segunda',
    3: 'Terça',
    4: 'Quarta',
    5: 'Quinta',
    6: 'Sexta',
    7: 'Sábado'
}
dia = int(input('Digite um número correspondente ao dia da semana: '))
for i in dicionario:
    if dia == i:
        print(dicionario[i])
        break
else:
    print('Valor Inválido!')