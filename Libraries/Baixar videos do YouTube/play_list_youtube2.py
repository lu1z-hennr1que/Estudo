# Para obter os vídeos de uma playlist, basta obtermos uma lista de urls
# de cada vídeo:
from pytube import YouTube, Playlist

PLAYLIST_URL = input("Cole o link aqui:")
playlist = Playlist(PLAYLIST_URL)

# Agora é só fazer como já vimos para baixar um vídeo a partir da url:
for url in playlist:
    video = YouTube(url)
    stream = video.streams.get_highest_resolution()
    stream.download(output_path='playlist')
    print('Download concluido!')

