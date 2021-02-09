#Mid Year Project
#Krish and Vansh

from pytube import YouTube
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
from moviepy.editor import *
import urllib.request
import os
class Application(Frame):


    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()
        self.reslist = []

    def browse(self):
        dir = filedialog.askdirectory()
        self.path_ent.delete(0,"end")
        self.path_ent.insert(0, str(dir))

    def downloadVid(self):
        self.pickList[self.chosenRes].download(self.path_ent.get())  # Path where to store the video
        self.submitButton['text'] = "Download a new video"

    def downloadAud(self):
        self.pickList[self.chosenRes].download(self.path_ent.get())

        # mp4FileName = self.youtube.title + ".mp4"
        # mp3FileName = self.youtube.title + ".mp3"

        # videoClip = VideoFileClip(mp4FileName)
        # audioClip = VideoClip.audio
        # audioClip.write_audiofile(mp3FileName)
        # audioClip.close()
        # videoClip.close()

    def chooseResVid(self):
        for b in self.reslist:
            b.destroy()

        self.chosenRes = 0
        video_url = str(self.url.get())
        self.youtube = YouTube(video_url)
        vidOptions = self.youtube.streams.filter(progressive=True, type='video', subtype='mp4').all()

        resOptions = []
        self.pickList = []
        for x in vidOptions:
            if x.resolution not in resOptions:
                resOptions.append(x.resolution)
                self.pickList.append(x)

        row = 4
        for i in self.pickList:       
            a = Radiobutton(self, text = i.resolution, variable = self.chosenRes, value = i)
            a.grid(row = row, column = 0, sticky = W)
            self.reslist.append(a)
            row += 1
            
        self.submitButton = Button(self, text = "Next", command = self.downloadVid)
        self.submitButton.grid(row = row, column = 0, sticky=W)
        self.reslist.append(self.submitButton)

    def chooseResAudio(self):
        for b in self.reslist:
            b.destroy()

        self.chosenRes = 0
        video_url = str(self.url.get())
        self.youtube = YouTube(video_url)
        audOptions = self.youtube.streams.filter(type='audio', subtype='mp4').all()

        self.pickList = []
        for x in audOptions:
            self.pickList.append(x)
        
        self.submitButton = Button(self, text = "Next", command = self.downloadAud)
        self.submitButton.grid(row = 4, column = 0, sticky=W)
        self.reslist.append(self.submitButton)
        
    def vidDetails(self):
        video_url = str(self.url.get())
        self.youtube = YouTube(video_url)
        urllib.request.urlretrieve(self.youtube.thumbnail_url, "thumb.png")
        img = ImageTk.PhotoImage(Image.open("thumb.png").resize((160, 90)))
        Label(self, text = self.youtube.title).grid(row = 1, column = 4, sticky=W)

        l= Label(self, image = img)
        l.grid(row=0,column=4)
        l.photo = img

    def runVidFunc(self):
        self.vidDetails()
        self.chooseResVid()

    def runAudFunc(self):
        self.vidDetails()
        self.chooseResAudio()
        
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
        self.vidButton = Button(self, text = "Download video", command = self.runVidFunc)
        self.vidButton.grid(row = 3, column = 0, sticky=W)
        self.audButton = Button(self, text = "Download audio", command = self.runAudFunc)
        self.audButton.grid(row = 3, column = 1, sticky=W)

def on_closing():
    if os.path.exists("thumb.png"):
        os.remove("thumb.png")
    root.destroy()

root = Tk()
root.title("YouTube Downloader")
root.protocol("WM_DELETE_WINDOW", on_closing)
app = Application(root)
root.mainloop()