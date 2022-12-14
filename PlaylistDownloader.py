from pytube import Playlist

playlist = Playlist('https://www.youtube.com/watch?v=55NvZjUZIO8&list=PLEiEAq2VkUULzCiDV5VyF7zR6zoDIT_eH')
print('Number of videos in playlist: %s' % len(playlist.video_urls))

# Loop through all videos in the playlist and download them
for video in playlist.videos:
    video.streams.get_by_itag(22).download("C://Users//Administrator//Desktop//Python Projects//Video Downloader//Downloads")
    print("Downloaded", video)