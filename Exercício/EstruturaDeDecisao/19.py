'''Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16.'''
lista = [326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7, 16]
print("Teste com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16")
for i in lista: 
    inteiro = i
    if inteiro > 0:
        if inteiro <= 9 and inteiro >= 1:
            print(f'{inteiro} = {inteiro} unidades.')
        elif inteiro <= 99 and inteiro >= 10:
            unidade, dezena = inteiro%10, inteiro//10
            if unidade == 0:
                print(f'{inteiro} = {dezena} dezenas.')
            else:
                print(f'{inteiro} = {dezena} dezenas e {unidade} unidades. ')
        elif inteiro <= 999 and inteiro >= 100:
            unidade, dezena, centena = inteiro%10, (inteiro//10)%10, inteiro//100
            if unidade == 0 and dezena > 0:
                print(f'{inteiro} = {centena} centenas e {dezena} dezenas.')
            elif dezena == 0 and unidade > 0:
                print(f'{inteiro} = {centena} centenas e {unidade} unidades.') 
            elif dezena == 0 and unidade == 0:
                print(f'{inteiro} = {centena} centenas.')
            else:
                print(f'{inteiro} = {centena} centenas, {dezena%10} dezenas e {unidade} unidades. ')
        else:
            print('Digite um valor menor.')
    else:
        print('Digite um valor positivo.')