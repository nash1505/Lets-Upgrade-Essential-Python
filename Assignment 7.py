from pytube import YouTube
from tkinter import *
import os
root = Tk()
root.geometry('600x500')
root.title("my first page")

Label_1=Label(root,text="Download Youtube Video Paste Link Here", font=("bold",20),background="orangered")
Label_1.place(x=80,y=20)

mylink=StringVar()

pastelink=Entry(root, width=60, textvariable=mylink)
pastelink.place(x=140, y=80)

def downloadVideo():
    x=str(mylink.get())
    ytvideo=YouTube(x).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
    if not os.path.exists('D:/jupyter notebook'):
        os.makedirs('D:/jupyter notebook')
    ytvideo.download('D:/jupyter notebook') 


Button(root,text="Download Video", width=20, bg='green',fg="white", command=downloadVideo).place(x=220, y=110)
root.mainloop()
 
