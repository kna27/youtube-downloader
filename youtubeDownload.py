#Mid Year Project
#Krish and Vansh

from pytube import YouTube
from tkinter import filedialog
from tkinter import *
from PIL import Image, ImageTk
import urllib.request
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
        print(self.path_ent.get())

    def downloadVid(self):
        self.pickList[self.chosenRes].download(self.path_ent.get())  # Path where to store the video
        self.submitButton['text'] = "Download a new video"

    def chooseResVid(self):
        for b in self.reslist:
            b.destroy()

        self.chosenRes = 0
        video_url = str(self.url.get())
        youtube = YouTube(video_url)
        vidOptions = youtube.streams.filter(progressive=True, type='video', subtype='mp4').all()

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
        youtube = YouTube(video_url)
        audOptions = youtube.streams.filter(type='audio').all()

        resOptions = []
        self.pickList = []
        for x in audOptions:
            if x.abr not in resOptions:
                resOptions.append(x.abr)
                self.pickList.append(x)

        row = 4
        for i in self.pickList:       
            a = Radiobutton(self, text = i.abr, variable = self.chosenRes, value = i)
            a.grid(row = row, column = 0, sticky = W)
            self.reslist.append(a)
            row += 1
        
        self.submitButton = Button(self, text = "Next", command = lambda:[self.downloadVid, self.vidDetails])
        self.submitButton.grid(row = row, column = 0, sticky=W)
        self.reslist.append(self.submitButton)
        
    def vidDetails(self):
        video_url = str(self.url.get())
        youtube = YouTube(video_url)
        urllib.request.urlretrieve(youtube.thumbnail_url, "thumb.png")
        img = ImageTk.PhotoImage(Image.open("thumb.png").resize((160, 90)))
        Label(self, text = youtube.title).grid(row = 1, column = 4, sticky=W)

        l= Label(self, image = img)
        l.grid(row=0,column=4)
        l.photo = img

    def runVidFunc(self):
        self.vidDetails()
        self.chooseResVid()

        
        
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
        self.audButton = Button(self, text = "Download audio", command = self.chooseResAudio)
        self.audButton.grid(row = 3, column = 1, sticky=W)

root = Tk()
root.title("YouTube Downloader")
app = Application(root)
root.mainloop()