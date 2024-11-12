'''Faça um programa para a leitura de duas notas parciais de um aluno.
O programa deve calcular a média alcançada por aluno e apresentar:
a-A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
b- A mensagem "Reprovado", se a média for menor do que sete;
c- A mensagem "Aprovado com Distinção", se a média for igual a dez.'''

# Função para calcular média do aluno
def calcularMedia(nota1, nota2):
    media = (nota1+nota2)/2
    if media == 10:
        return 'Aprovado com Distinção.'
    elif media >= 7:
        return 'Aprovado.'
    else:
        return 'Reprovado.'

# Entrada de dados
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

classificacao = calcularMedia(nota1, nota2)
print('Esse aluno foi ', classificacao)