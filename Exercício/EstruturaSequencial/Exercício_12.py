#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
altura = int(input('Digite sua altura em CM:'))
print(f'Seu peso ideal é {72.7*(altura/100)-58:.3f}Kg')