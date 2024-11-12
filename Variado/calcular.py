def somar (a, b):
    c = a+b
    return c
def dividir (a, b):
    c = a/b
    return c
def subritair (a, b):
    c = a-b
    return c
def multiplicar (a, b):
    c = a*b
    return c
a = float(input("Digite um número: "))
b = float(input("Digite um segundo número: "))
d = input("Digite S-soma, D-dividir, X-subritair e M-multiplicar: ")
if d == "s" or d == "S":
    print(somar(a, b))
elif d == "d" or d == "D":
    print(dividir(a, b))
elif d == "x" or d == "X":
    print(subritair(a, b))
elif d == "m" or d == "M":
    print(multiplicar(a, b))
else:
    print("Erro no programa")