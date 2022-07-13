from pytube import YouTube

continuar = True
print("Bem vindo ao Youtube Downloader!\n")

while continuar:
    url = input(str("Informe a url do vídeo: "))
    video = YouTube(url)

    print(f"Título: {video.title}")
    print(f"Visualizações: {video.views}")
    print(f"Publicação: {video.publish_date}")
    print(f"Canal: {video.author}\n")

    baixar = input("Deseja baixar esse vídeo? (sim ou não) ").lower()

    if baixar == "sim":
        print("Baixando..")
        video_down = video.streams.get_highest_resolution()
        video_down.download(output_path='C:/Users/Downloads')
        print("Download concluído!")
        continua_baixando = input("Deseja baixar mais algum video? (sim ou não) ").lower()
        if continua_baixando != "sim":
            continuar = False
    else:
        print("Obrigado por testar!")
        continuar = False

