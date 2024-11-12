'''Faça um Programa que leia três números e mostre o maior deles.'''
# Função para verificar o maior
def maior(num1, num2, num3):
    a = sorted([num1, num2, num3]) # Coloca todos em uma lista em ordem crescente
    return a[2] # Retorna o maior deles

# inserção de dados
num1 = float(input('Digite um número: '))
num2 = float(input('Digite um outro número: '))
num3 = float(input('Digite um outro número: '))

valor = maior(num1, num2, num3)
print('O maior é ', valor)