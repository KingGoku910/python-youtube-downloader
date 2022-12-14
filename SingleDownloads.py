from pytube import YouTube

video_list = open("multi_file_downoad.txt", "r")

for i in video_list:
    yt = YouTube(i)
    
    try:
        dw = yt.streams.get_by_itag(22)

        dw.download("C://Users//Administrator//Desktop//Python Projects//Video Downloader//Downloads")

        print("Downloaded", i)
    except:
        print("Download failed for ", i)
