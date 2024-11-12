'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''
numero, numero2, numero3 = float(input('Digite um número: ')), float(input('Digite um outro número: ')), float(input('Digite um outro número: '))

lista = sorted([numero, numero2, numero3])
print(f'O maior é {lista[2]} e o menor é {lista[0]}')