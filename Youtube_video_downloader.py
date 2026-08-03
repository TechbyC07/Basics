import yt_dlp
#from pytube import YouTube

#url input
url = input("Pate Youtube video link: ")

ydl_opts = {
    "outtmpl": "%(title)s.%(ext)s"
}
#yt = YouTube(url)

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download done!")
#print("The video is")
#print("Title:", yt.title)

#stream = yt.streams.get_highest_resolution()

#stream.download()
