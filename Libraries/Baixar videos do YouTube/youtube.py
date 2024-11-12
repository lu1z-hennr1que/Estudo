from pytube import YouTube

def baixar(urls):

    for url in urls:    
        yt = YouTube(url)
        # Vamos listar todas as opções de stream disponíveis em uma url:
        #for stream in yt.streams:
        #    print(stream)
        # Podemos escolher a stream de melhor qualidade e fazer o seu download:
        video = yt.streams.get_highest_resolution()
        video.download(output_path='.')  
    return print("Download concluido!")
while True:
    urls = input('Cole aqui o link ou lista de links separado por ",": ').split(',')
    baixar(urls)


