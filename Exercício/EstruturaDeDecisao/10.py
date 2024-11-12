'''Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.'''
dicionario = {
    'm': 'Bom dia!',
    'v': 'Boa tarde!',
    'n': 'Boa noite!'
}
turno = input('Digite qual turno você estuda, digitar M-matutino ou V-Vespertino ou N- Noturno: ').lower()
for i in dicionario:
    if i == turno:
        print(dicionario[i])
    else:
        "Valor Inválido!"