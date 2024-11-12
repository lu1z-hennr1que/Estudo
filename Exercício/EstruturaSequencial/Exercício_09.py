#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = (5 * ((F-32) / 9).
temp_fahr = float(input('Digite a temperatura em fahrenheit:'))
temp_cels = 5*((temp_fahr-32)/9)
print(f'Temperatura altual em graus Celsius é aproximadamente {temp_cels:.2f}')
