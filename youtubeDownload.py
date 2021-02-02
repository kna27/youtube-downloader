#Mid Year Project
#Krish and Vansh

from pytube import YouTube
from tkinter import *


class Application(Frame):

    def downloadVid(self):
        video_url = str(self.url.get())
        youtube = YouTube(video_url)
        video = youtube.streams.first()
        video.download("D:/")  # Path where to store the video

    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        Label(self, text = "YouTube Downloader", justify="center", font=("Helvetica", 20, "bold")).grid(row = 0, column = 0, columnspan = 2)
        Label(self, text = "Link: ", justify="center", width=20).grid(row = 1, column = 0, sticky=W)
        self.url = Entry(self)
        self.url.grid(row = 1, column = 1, sticky = W)
        Button(self, text = "Submit", command = self.downloadVid).grid(row = 2, column = 0, sticky=W)

root = Tk()
root.title("YouTube Downloader")
app = Application(root)
root.mainloop()