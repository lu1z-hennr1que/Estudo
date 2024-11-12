#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7
genero = input("Digite (M) para Homem e (F) para Mulher:")
if genero == 'M' or genero == 'm':
    print('Homen, okay.')
    h = int(input("Digite sua altura em CM:"))
    print(f"Seu peso ideal é {72.7 * (h / 100) - 58:.3f}")
elif genero == 'F' or genero == 'f':
    print('Mulher, okay.')
    h = int(input("Digite sua altura em CM:"))
    print(f"Seu peso ideal é {62.1 * (h / 100) - 44.7:.3f}")
else:
    print('Error, tente novamente!')