from pytubefix import YouTube
import requests
from sys import argv

url = argv[1]

yt = YouTube(url)
print(yt.views)

download=yt.streams.get_highest_resolution()
download.download(r"\Users\chirag\Desktop\ytdownloader\downloads")
