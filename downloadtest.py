from pytube import YouTube
from pytube import Playlist

link = YouTube("https://youtube.com/watch?v=yEgHrxvLsz0&si=EnSIkaIECMiOmarE")

link.streams.get_highest_resolution().download()
print("downloaded")