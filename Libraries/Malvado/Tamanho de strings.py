def tam(string):
    tamanho = len(string)
    return tamanho
print('Compara duas strings')
string1 = input("String 1: ")
string2 = input("String 2: ")
print(f'Tamanho de "{string1}": {tam(string1)} caracteres')
print(f'Tamanho de "{string2}": {tam(string2)} caracteres')
if tam(string1) == tam(string2):
    print("As duas strings são de tamanhos iguais.")
else:
    print("As duas strings são de tamanhos diferentes.")
if string1 == string2:
    print("As duas strings possuem conteúdo igual.")
else:
    print("As duas strings possuem conteúdo diferente.")