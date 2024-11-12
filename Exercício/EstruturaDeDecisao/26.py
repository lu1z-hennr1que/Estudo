'''
Um posto está vendendo combustíveis com a seguinte tabela de
descontos:
Álcool:
 até 20 litros, desconto de 3% por litro
 acima de 20 litros, desconto de 5% por litro
Gasolina:
 até 20 litros, desconto de 4% por litro
 acima de 20 litros, desconto de 6% por litro

Escreva um algoritmo que leia o número de litros vendidos, o
tipo de combustível (codificado da seguinte forma: A-álcool,
G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço
do litro do álcool é R$ 1,90.
'''


try:
    lit_ = float(input("Digite a quantidade de litros que vai levar: "))
    try:
        tipo_C = input("Digite A-álcool ou G-gasolina: ")
        if tipo_C == "A" or tipo_C == "a":
            pagar = lit_*1.9
            tipo = "Álcool"
        elif tipo_C == "G" or tipo_C == "g":
            pagar = lit_*2.5
            tipo = "Gasolina"
        else:
            print("Error no programa!")

        print(f"Tipo de combustível: {tipo}")
        print(f"Valor a ser pago: {pagar}")
    except:
        print("Digite algo corretamente na próxima, error no programa.")

except:
    print("Por favor digite corretamente, error no programa.")

