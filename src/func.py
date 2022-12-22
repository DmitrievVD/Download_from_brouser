import requests
from pytube import YouTube
import os


def youtube(url):
    if "youtu.be" in url:  # Проверка ссылки содержит ли youtu.be
        download(url.split('e/')[1])
    elif "youtube.com" in url:  # Проверка ссылки содержит ли youtube.com
        download(url.split('=')[1])
    else:
        print("Не корректная ссылка \n Формат: https://youtu.be/zNyYDHCg06c или https://www.youtube.com/zNyYDHCg06c")

def downloadYouTube(videourl, path, video_quality):
    try:
        print("Идет загрузка")
        yt = YouTube(videourl)
        yt = yt.streams.filter(res=video_quality).order_by('resolution').first()
        if not os.path.exists(path):
            os.makedirs(path)
        yt.download(path)
        print("Готово")
    except:
        print("Не удалось загрузить файл")


def downloadAudioFromYoutube(videourl):
    try:
        yt = YouTube(videourl)
        video = yt.streams.filter(only_audio=True).first()

        out_file = video.download(output_path="./audio")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("Готово")
    except:
        print("Ошибка")


