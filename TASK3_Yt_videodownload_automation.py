from pytube import YouTube

try:
    url = input("enter the youtube url : ")

    yt = YouTube(url)

    print("Title:", yt.title)
    print("Views:", yt.views)

    yd = yt.streams.get_highest_resolution()
    #downloading the video
    yd.download()

    print("download complete")
except Exception as e :
 print("an error occured :", str(e))













