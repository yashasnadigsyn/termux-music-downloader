from pytube import YouTube
import requests

topic = input("Enter song name:")
r=requests.get(f"https://pywhatkit.herokuapp.com/playonyt?topic={topic}").text

#ask for the link from user
link = r
yt = YouTube(link)

#Showing details
print("Title: ",yt.title)
print("""
         1. 240
         2. 139
         3. press 'q' for quit
""")
itag = input("> ")
if itag == 'q':
    exit()
ys = yt.streams.get_by_itag(itag)
filename = input("filename:")
print("Downloading...")
ys.download(filename=filename)
print("Download completed!!")
