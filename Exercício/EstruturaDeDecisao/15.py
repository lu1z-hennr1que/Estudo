'''Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;'''
def e_triangulo(lado, lado2, lado3):
    if lado + lado2 > lado3 and lado3 + lado > lado2 and lado2 + lado3 > lado:
        return True
    else:
        return False
def qual_triangulo(lado, lado2, lado3):
    if lado == lado2 and lado == lado3 and lado2 == lado3:
        return 'Triângulo Equilátero'
    elif lado == lado2 or lado == lado3 or lado2 == lado3:
        return 'Triângulo Isósceles'
    else:
        return 'Triângulo Escaleno'

lado = float(input('Digite um lado: '))
lado2 = float(input('Digite mais um lado: '))
lado3 = float(input('Digite mais um lado: '))
if e_triangulo(lado, lado2, lado3) == True:
    print('É possivel fazer um ', qual_triangulo(lado, lado2, lado3))
else:
    print('Não é possível fazer um  Triângulo')