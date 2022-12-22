from func import *

def click():
    user_input = int(input("Введите число:  1 - скачать видео 2 - Скачать только Аудио: \n"))
    if user_input == 1:
        option_quality = int(input("Качество видео 1 - 1080p 2 - 720p: \n"))
        videourl = input("Введите url видео: \n")
        if option_quality == 1:
            downloadYouTube(videourl, './videos', "1080p")
        elif option_quality == 2:
            downloadYouTube(videourl, './videos', "720p")
        else:
            print("Ошибка")
    elif user_input == 2:
        videourl = input("Введите url видео: \n")
        downloadAudioFromYoutube(videourl)
    else:
        print("Ошибка")

