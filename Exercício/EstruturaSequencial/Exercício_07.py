#Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
def cal_ (base, altura):
   print(f"A área do quadrado é {base*altura}")
   print(f"O dobro dessa área é {(base*altura)*2}")
base, altura =  float(input("Digite a base do quadrado:\n")), float(input("Digite a altura do quadrado:\n"))
cal_(base, altura)
