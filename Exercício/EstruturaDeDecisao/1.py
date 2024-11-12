import pyttsx3
engine = pyttsx3.init()
engine.say('Faça um Programa que peça dois números e imprima o maior deles.')
engine.runAndWait()
engine.stop()

'''Faça um Programa que peça dois números e imprima o maior deles.'''

num_1 = float(input('Digite um número: '))
num_2 = float(input('Digite um segundo número: '))

if num_1 > num_2:
    print(f'O número {num_1} é maior')
else:
    print(f'O número {num_2} é o maior')