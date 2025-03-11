from pytube import YouTube

try:
    url = input("enter the youtube url : ")

    yt = YouTube(url)

    print("Title:", yt.title)
    print("Views:", yt.views)








