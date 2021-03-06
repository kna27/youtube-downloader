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
        self.elemlist = []
    
    def browse(self):
        # Create brose menu to store file
        dir = filedialog.askdirectory()
        self.path_ent.delete(0,"end")
        self.path_ent.insert(0, str(dir))

    def downloadVid(self):
        #Downloads the selected resolution of the video the user chooses
        self.pickList[self.chosenRes].download(self.path_ent.get())

    def downloadAud(self):
            #Download audio as an mp4 file and converts it to mp3
            #pyTube does not give any mp3 options for audio, only mp4 and webm
            filename = self.pickList[self.chosenRes].download(self.path_ent.get())
            clip = AudioFileClip(filename)
            clip.write_audiofile(filename[:-4] + ".mp3", logger=None)
            clip.close()
            os.remove(filename)

    def chooseResVid(self):
        #Allows the user to choose which resolution video they want to download
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
            a = Radiobutton(self, text = i.resolution, variable = self.chosenRes, value = i, font=("Garamond", 15))
            a.grid(row = row, column = 0, sticky = W)
            self.reslist.append(a)
            row += 1   
        self.submitButton = Button(self, text = "Download", command = self.downloadVid, font=("Garamond", 13))
        self.submitButton.grid(row = row, column = 0, sticky=W)
        self.reslist.append(self.submitButton)

    def chooseResAudio(self):
        #Finds all possible audio files and chooses the highest bitrate
        for b in self.reslist:
            b.destroy()
        self.chosenRes = 0
        video_url = str(self.url.get())
        self.youtube = YouTube(video_url)
        audOptions = self.youtube.streams.filter(type='audio', subtype='mp4').all()
        self.pickList = []
        for x in audOptions:
            self.pickList.append(x)
        self.submitButton = Button(self, text = "Download", command = self.downloadAud, font=("Garamond", 13))
        self.submitButton.grid(row = 4, column = 0, sticky=W)
        self.reslist.append(self.submitButton)
        
    def vidDetails(self):
        #Finds the video's title and thumbnail
        try:
            for x in self.elemlist:
                x.destroy()

            video_url = str(self.url.get())
            self.youtube = YouTube(video_url)
            urllib.request.urlretrieve(self.youtube.thumbnail_url, "thumb.png")
            img = ImageTk.PhotoImage(Image.open("thumb.png").resize((160, 90)))
            title = Label(self, text = self.youtube.title,font=("Garamond", 14))
            title.grid(row = 1, column = 4, sticky=W)
            l= Label(self, image = img)
            l.grid(row=0,column=4)
            l.photo = img

            self.elemlist.append(title)
            self.elemlist.append(l)
        except:
            a = Label(self, text = "Please insert a valid URL!", font=("Garamond", 15, "bold"), fg="red")
            a.grid(row = 4, column = 0, sticky = W)
            self.reslist.append(a)

    def runVidFunc(self):
        #Runs vidDetails() and chooseResVid()
        try:
            self.vidDetails()
            self.chooseResVid()
        except:
            a = Label(self, text = "Please insert a valid URL!", font=("Garamond", 15, "bold"), fg="red")
            a.grid(row = 4, column = 0, sticky = W)
            self.reslist.append(a)

    def runAudFunc(self):
        #Runs vidDetails() and chooseResAudio()
        try:
            self.vidDetails()
            self.chooseResAudio()
        except:
            a = Label(self, text = "Please insert a valid URL!", font=("Garamond", 15, "bold"), fg="red")
            a.grid(row = 4, column = 0, sticky = W)
            self.reslist.append(a)
        
    def create_widgets(self):
        #Creates the starting widgets
        Label(self, text = "YouTube Downloader", justify="center", font=("Times", 24, "bold")).grid(row = 0, column = 0, columnspan = 2)
        Label(self, text = "Link: ", font=("Garamond", 15), width=20).grid(row = 1, column = 0, sticky=W)
        self.url = Entry(self, font=("Garamond", 13))
        self.url.grid(row = 1, column = 1, sticky = W)
        Label(self, text="Download Folder: ", font=("Garamond", 15), width=20).grid(row = 2, column = 0, sticky=W)   
        Label(self, text = "Directory Path: ").grid(row = 2, column = 1, sticky = W)
        self.path_ent = Entry(self, font=("Garamond", 13))
        self.path_ent.grid(row = 2, column = 1, sticky = W)
        Button(self, text="Browse", command = self.browse).grid(row = 2, column = 2)
        self.vidButton = Button(self, text = "Download video", font=("Garamond", 13), command = self.runVidFunc)
        self.vidButton.grid(row = 3, column = 0, sticky=W)
        self.audButton = Button(self, text = "Download audio", font=("Garamond", 13), command = self.runAudFunc)
        self.audButton.grid(row = 3, column = 1, sticky=W)
        
        self.grid_rowconfigure(1, minsize=20)
        self.grid_rowconfigure(2, minsize=20)
        self.grid_rowconfigure(3, minsize=60)

def on_closing():
    #Removes thumb.png when user tries to exit program
    if os.path.exists("thumb.png"):
        os.remove("thumb.png")
    root.destroy()

#Initialization
root = Tk()
root.title("YouTube Downloader")
root.protocol("WM_DELETE_WINDOW", on_closing)
app = Application(root)
root.mainloop()
