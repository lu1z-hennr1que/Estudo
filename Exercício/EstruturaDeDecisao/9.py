'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''
numero = float(input('Digite um número: '))
numero2 = float(input('Digite um outro número: '))
numero3 = float(input('Digite um outro número: '))
lista_de_numeros = reversed(sorted([numero, numero2, numero3]))
for i in lista_de_numeros:
    print(i)