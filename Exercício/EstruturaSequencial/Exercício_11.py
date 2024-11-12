#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.
num_1, num_2, num_3 = int(input("Digite um número inteiro:")), int(input("Digite outro número inteiro:")), float(input("Digite um número real:"))
print(f"a. {(num_1*2)*(num_2/2)}")
print(f"b. {num_1*3+num_3}")
print(f"c. {num_3**3}")