from func import *


def ui():
    import sys
    from PyQt5 import QtWidgets
    from user_interface import Ui_download_youtube

    app = QtWidgets.QApplication(sys.argv)

    download_youtube = QtWidgets.QMainWindow()
    ui = Ui_download_youtube()
    ui.setupUi(download_youtube)
    download_youtube.show()

    def down_video():
        videourl = ui.url_adress.text()
        ui.url_adress.setText("")
        print(videourl)
        downloadYouTube(videourl)

    def down_audio():
        videourl = ui.url_adress.text()
        ui.url_adress.setText("")
        print(videourl)
        downloadAudioFromYoutube(videourl)



    ui.download_video.clicked.connect(down_video)
    ui.download_audio.clicked.connect(down_audio)

    sys.exit(app.exec_())


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

ui()