'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da
operação deve ser acompanhado de uma frase que diga se o número é:
- par ou ímpar;
- positivo ou negativo;
- inteiro ou decimal.
'''
def calcular(operacao, var_1, var_2):
    if operacao == "a" or operacao == "A":
        soma = var_1+var_2
        return soma
    elif operacao == "b" or operacao == "B":
        subtrair = var_1-var_2
        return subtrair
    elif operacao == "c" or operacao == "C":
        divisao = var_1/var_2
        return divisao
    elif operacao == "d" or operacao == "D":
        multiplica = var_1*var_2
        return multiplica
    else:
        return print("Erro no programa")
def ver_1(cal):
    if cal % 2 == 0:
        print("Número par")
    else:
        print("Número impar")
def ver_2(cal):
    if cal > 0:
        print("Número positivo")
    else:
        print("Número negativo")
def ver_3(cal):
    n = int(cal)
    m = n*10
    v = cal*10
    if m == v:
        print("Número inteiro")
    else:
        print("Número decimal")

var_1 = float(input("Digite o primeiro número: "))
var_2 = float(input("Digite o segundo número: "))
operacao = input("\na) somar;\n"
                 "b) subitrair;\n"
                 "c) Dividir;\n"
                 "d) Multiplicar.\n"
                 "Digite qual opeção deseja realizar: ")
cal = calcular(operacao, var_1, var_2)
print(' ')
print(cal)w
ver_1(cal)
ver_2(cal)
ver_3(cal)