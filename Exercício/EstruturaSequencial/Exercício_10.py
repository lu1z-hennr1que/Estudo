#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
temp_cels = float(input('Digite a temperatura em Celsius:'))
temp_fahr = temp_cels*1.8+32
print(f'Temperatura altual em graus Fahrenheit é aproximadamente {temp_fahr:.2f}')
