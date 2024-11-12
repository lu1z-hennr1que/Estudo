# comando para instalar code: pip install pyttsx3;
# upgrade: python.exe -m pip install --upgrade pip;

import pyttsx3

# Inicialize o motor de sintese de fala
engine = pyttsx3.init()

# Texto que você deseja que seja lido em formato de audiobook
texto ="Luis e a coisa mais linda"

# Configuração da voz e da velocidade de leitura (opcional)
engine.setProperty("rate", 150)

# Gere o audiobook lendo o texto
engine.say(texto)

# Aguarde até que a leitura seja concluída
engine.runAndWait()

# Encerre o motor de sintese de fala
engine.stop()


