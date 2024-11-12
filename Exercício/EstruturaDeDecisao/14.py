'''Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e
calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a mensagem “APROVADO” se o conceito for
A, B ou C ou “REPROVADO” se o conceito for D ou E.'''

def conceito_nota(media_nota):
    if media_nota > 9.0 and media_nota <= 10.0:
        conceito = 'A'
        return conceito
    elif media_nota > 7.5 and media_nota < 9.0:
        conceito = 'B'
        return conceito
    elif media_nota > 6.0 and media_nota < 7.5:
        conceito = 'C'
        return conceito
    elif media_nota > 4.0 and media_nota < 6.0:
        conceito = 'D'
        return conceito
    else:
        conceito = 'E'
        return conceito
print('''
Média de Aproveitamento  Conceito
    Entre 9.0 e 10.0         A
    Entre 7.5 e 9.0          B
    Entre 6.0 e 7.5          C
    Entre 4.0 e 6.0          D
    Entre 4.0 e zero         E
    ''')
while True: 

    print(35 * '=')
    nota = float(input('Digite sua primeira nota: '))
    nota2 = float(input('Digite sua segunda nota: '))
    media_nota = (nota+nota2) / 2
    conceito = conceito_nota(media_nota)
    
    if conceito == ['A', 'B', 'C']:
       aproveitamento = 'APROVADO'
    else:
       aproveitamento = 'REPROVADO'
    
    print('\nMédia: ', media_nota)
    print("Conceito :", conceito)
    print(aproveitamento)
    print(35 * '=')

    sair = input('\nDigite (s) para sair ou \n(Qualquer coisa) para recomeçar: ').lower()
    if sair == 's':
        break
    