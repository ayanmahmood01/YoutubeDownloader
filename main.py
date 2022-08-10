from pytube import YouTube
Path = "D:\Youtube Downloads USing Python"
link=str(input("Enter Your Link:"))
video=YouTube(link)
print("\n",video.title)
print("\n Length of video In Seconds ",video.length)
print("\n View Count :",video.views)
print("\nFor Audio Press 1")
print("\n For Video & With Audio Press 2")
A=int(input("\n Enter Your Choice:"))
if(A==2):
    resolutions=video.streams.filter(progressive=True)
    list=list(enumerate(resolutions))
    for i in list:
        print(i)
    dres=int(input("\nEnter Resolution:"))
    print("\n Downloading")
    resolutions[dres].download(Path)
    print("Downloaded")
else:
    resolutions=video.streams.filter(only_audio=True)
    list=list(enumerate(resolutions))
    for i in list:
        print(i)
    dres=int(input("\nEnter Resolution:"))
    print("\n Downloading.....")
    resolutions[dres].download(Path)
    print("Downloaded")