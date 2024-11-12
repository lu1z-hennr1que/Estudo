from pytube import YouTube
import os
def baixar_lista(links):
    baixados = []
    for url in links:
        yt = YouTube(url)
        # filtrando o video 
        video = yt.streams.filter(only_audio=True).first()
        # baixando o arquivo
        arquivo = video.download(output_path='Desktop')
        # salvando o arquivo
        base, ext = os.path.splitext(arquivo)
        arquivo_final = base + '.mp3'
        os.rename(arquivo, arquivo_final)
        # mensagem de sucesso
        baixados.append(yt.title)
    return baixados
print(" PROGAMA PARA BAIXAR ÁUDIO DE VIDEO DO YOUTUBE ".center(60, '='))
print('''
(s) se deseja sair.
(url) cole a url do video(do youtube) que deseja baixar.
(n) para criar uma nova pasta para a musica.
(l) para baixar lista de musica
''')
  
while True:
    
    print(60 * '=')
    # Entrada do user
    url = input("$: ")
    if url == 's':
        break
    elif url == 'n':
        destino = input('insira o nome da pasta.\n$: ')
        url = input('Agora insira a (url) do video.\n$: ')
        try:
            yt = YouTube(url)
            # filtrando o video 
            video = yt.streams.filter(only_audio=True).first()
            # baixando o arquivo
            arquivo = video.download(output_path=destino)
            # salvando o arquivo
            base, ext = os.path.splitext(arquivo)
            arquivo_final = base + '.mp3'
            os.rename(arquivo, arquivo_final)
            # mensagem de sucesso
            print(yt.title + ' baixado com sucesso.')
            print(60 * '=')
        except:
            print('Por favor, insira algo valido.\n')
            print(60 * '=')
    elif url == 'l':
        links = input('Cole a lista de musicas separados por virgula:\n').split(',')
        baixar_lista(links)
    else:
        try:
            yt = YouTube(url)
            # filtrando o video 
            video = yt.streams.filter(only_audio=True).first()
            # baixando o arquivo
            arquivo = video.download(output_path='Desktop')
            # salvando o arquivo
            base, ext = os.path.splitext(arquivo)
            arquivo_final = base + '.mp3'
            os.rename(arquivo, arquivo_final)
            # mensagem de sucesso
            print(yt.title + ' baixado com sucesso.')
            print(60 * '=')
        except:
            print('Por favor, insira algo valido.\n')
            print(60 * '=')
            