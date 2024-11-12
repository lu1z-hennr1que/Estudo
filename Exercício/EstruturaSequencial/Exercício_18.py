
'''Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o
 tempo aproximado de download do arquivo usando este link (em minutos).'''
import pyttsx3
engine = pyttsx3.init()

engine.say('Digite o tamanho de um arquivo para download (em MB):')
engine.runAndWait()
arquivo = int(input('Digite o tamanho de um arquivo para download (em MB): '))

engine.say('Digite a velocidade de um link de internet (em Mbps):')
engine.runAndWait()
velocidade = int(input('Digite a velocidade de um link de internet (em Mbps): '))

engine.stop()

tempo = (arquivo/velocidade)/60
print(f'Tempo aproximado de download do arquivo usando este link é de {tempo:.2f} minutos')
