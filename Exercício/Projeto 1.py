import time
import pyautogui
import webbrowser

def salvar(rua):    
    # Abre o site no navegador padrão
    webbrowser.open('https://www.google.com.br/maps/preview')
    
    # Espera 10 segundos para o navegador abrir
    time.sleep(10)
    
    # Pressiona teclas
    pyautogui.write(rua, interval=0.1)
    pyautogui.press('enter')
    time.sleep(20)
    for a in range(22):
        pyautogui.press('tab')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')
    pyautogui.press('enter')
    pyautogui.press('down')
    pyautogui.press('enter')

    # Espera 10 segundos para fechar o navegador
    time.sleep(10)
    pyautogui.hotkey('ctrl', 'w')

print('---- Salva rota ----')
print('Insira o endereço')
rua = input('-> ') # Entrada para inserir o endereço desejado
salvar(rua)