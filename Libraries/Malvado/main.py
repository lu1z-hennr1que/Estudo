#!/usr/bin/envpython3
import tkinter as tk

# Cria a janela principal
root = tk.Tk()

# Define o título da janela
root.title("Minha Aplicação")

# Define o tamanho da janela (Largura x Altura)
root.geometry("800x500")

# Cria um rótulo (label)
label = tk.Label(root, text="Olá, Tkinter!")
label.pack()

# Inicia o loop principal da aplicação
root.mainloop()

'''
class App:
    def __init__(self):
        numeros = input().split()
        self.numeros = list(map(int, numeros))
        self.numeros.sort()
    def iniciar(self):
        for n in self.numeros:
            print(n)
        pula = input()
        return pula
    def remover(self):
        try:
            del self.numeros[-1]
        except:
            return "sair"

if __name__ == "__main__":
    app = App()
    while True:
        if app.iniciar() == '':
            if app.remover() == "sair":
                print("Finalizando programa...")

                break
'''