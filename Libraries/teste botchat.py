import random
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import wikipediaapi
import requests
import pyttsx3

# Inicializar o motor de sintese de fala
engine = pyttsx3.init()

# Baixar os recursos necessários do NLTK
#nltk.download('punkt')
#nltk.download('stopwords')

# Criar um objeto Wikipedia com um agente de usuário específico
wiki = wikipediaapi.Wikipedia(
    language='pt',
    extract_format=wikipediaapi.ExtractFormat.WIKI,
    user_agent="BotChat/1.0 (https://github.com/seu-usuario/bot-chat)"
)

# Dicionário de respostas
respostas = {
    "e ai": ["Olá!", "Oi!", "E aí?"],
    "eai": ["Olá!", "Oi!", "E aí?"],
    "oi": ["Olá!", "Oi!", "E aí?"],
    "como vai": ["Estou bem, obrigado por perguntar.", "Tudo tranquilo!", "Ótimo, e você?"],
    "tudo bem": ["Estou bem, obrigado por perguntar.", "Tudo tranquilo!", "Ótimo, e você?"],
    "olá": ["Olá!", "Oi!", "E aí?"],
    "como você está": ["Estou bem, obrigado por perguntar.", "Tudo tranquilo!", "Ótimo, e você?"],
    "qual é o seu nome": ["Meu nome é Chatbot.", "Você pode me chamar de Chatbot.", "Sou o Chatbot."],
    "tchau": ["Até mais!", "Até logo!", "Até a próxima!"],
    "o que você pode fazer": ["Posso responder suas perguntas, contar piadas, e muito mais!"],
    "conte-me uma piada": ["Por que o programador foi preso? Porque ele tinha muitos bugs!",
                           "O que o HTML diz para o CSS? Meu estilo é melhor que o seu!"],
    "qual é a capital do brasil": ["A capital do Brasil é Brasília."],
    "quem é o presidente do brasil": ["O presidente do Brasil é Jair Bolsonaro."],
    "quanto é 2 mais 2": ["2 mais 2 é igual a 4."],
    "o que é programação": [
        "Programação é o processo de criar instruções que um computador pode seguir para realizar uma tarefa."],
    "como está o clima em": ["Vou verificar o clima em {}."]
}


# Função para remover caracteres especiais e tokenizar a entrada do usuário
def preprocessamento(mensagem):
    mensagem = mensagem.lower()  # Converter para minúsculas
    mensagem = ''.join(e for e in mensagem if e.isalnum() or e.isspace())  # Remover caracteres especiais, mantendo espaços
    return mensagem

# Função para encontrar a resposta mais apropriada
def encontrar_resposta(tokens):
    possiveis_respostas = []
    for palavra_chave, respostas_chave in respostas.items():
        if palavra_chave.lower() in tokens:
            possiveis_respostas.extend(respostas_chave)

    #    if "clima" in tokens and "em" in tokens:
    #        index_clima = tokens.index("clima")
    #        index_em = tokens.index("em")
    #        if index_clima < index_em:
    #            cidade = ' '.join(tokens[index_em + 1:])
    #            possiveis_respostas.append(obter_clima(cidade))

    if possiveis_respostas:
        return random.choice(possiveis_respostas)
    else:
        return buscar_wikipedia(entrada)


# Função para buscar informações na Wikipedia
def buscar_wikipedia(entrada):
    page = wiki.page(entrada)
    if page.exists():
        return page.summary[:200] + '...'  # Retorna os primeiros 200 caracteres do resumo da página
    else:
        return "Desculpe, não encontrei informações sobre isso na Wikipedia."


# Função para obter o clima de uma cidade usando a API OpenWeatherMap
#def obter_clima(cidade):
#    API_KEY = 'eb0964a879b290ac77b2bb1c63d15ad0'
#    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'
#    PARAMS = {'q': cidade, 'appid': API_KEY, 'lang': 'pt', 'units': 'metric'}
#    response = requests.get(BASE_URL, params=PARAMS)
#    data = response.json()
#    if data['cod'] == 200:
#        clima_descricao = data['weather'][0]['description']
#        temperatura = data['main']['temp']
#        return f"O clima em {cidade.title()} está {clima_descricao} com temperatura de {temperatura}°C."
#    else:
#        return "Não foi possível obter informações sobre o clima da cidade."

# Função falar
def fale(resposta):
    engine.say(resposta)
    engine.runAndWait()
    engine.stop()

# Loop de conversação
print("Olá! Eu sou um chatbot. Você pode conversar comigo ou digitar 'Tchau' para sair.")
engine.say("Olá! Eu sou um chatbot. Você pode conversar comigo ou digitar 'Tchau' para sair.")
engine.runAndWait()
engine.stop()
while True:
    entrada = input("Você: ")  # Convertendo entrada do usuário para minúsculas
    if entrada == 'tchau':
        print("Chat finalizado.")
        break
    tokens_entrada = preprocessamento(entrada)
    resposta = encontrar_resposta(tokens_entrada)
    print("Chatbot:", resposta)
    fale(resposta)
