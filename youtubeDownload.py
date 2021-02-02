#Mid Year Project
#Krish and Vansh

from pytube import YouTube
from tkinter import filedialog
from tkinter import *

class Application(Frame):

    def browse(self):
        dir = filedialog.askdirectory()
        self.path_ent.delete(0,"end")
        self.path_ent.insert(0, str(dir)) 
        print(self.path_ent.get())

    def downloadVid(self):
        video_url = str(self.url.get())
        youtube = YouTube(video_url)
        video = youtube.streams.first()
        video.download(self.path_ent.get())  # Path where to store the video
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        
    def create_widgets(self):
        Label(self, text = "YouTube Downloader", justify="center", font=("Helvetica", 20, "bold")).grid(row = 0, column = 0, columnspan = 2)
        Label(self, text = "Link: ", justify="center", width=20).grid(row = 1, column = 0, sticky=W)
        self.url = Entry(self)
        self.url.grid(row = 1, column = 1, sticky = W)
        Label(self, text="Directory: ", justify="center", width=20).grid(row = 2, column = 0, sticky=W)
        
        Label(self, text = "Directory Path: ").grid(row = 2, column = 1, sticky = W)

        self.path_ent = Entry(self)
        self.path_ent.grid(row = 2, column = 1, sticky = W)
        
        Button(self, text="Browse", command = self.browse).grid(row = 2, column = 2)
        Button(self, text = "Submit", command = self.downloadVid).grid(row = 3, column = 0, sticky=W)

root = Tk()
root.title("YouTube Downloader")
app = Application(root)
root.mainloop()