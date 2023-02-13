import tkinter as tk
import pytube

class YoutubeDownloader(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.label_url = tk.Label(self, text="YouTube URL:")
        self.entry_url = tk.Entry(self)
        self.label_format = tk.Label(self, text="Format:")
        self.format = tk.StringVar(self)
        self.format.set("mp4")
        self.option_mp4 = tk.Radiobutton(self, text="MP4", variable=self.format, value="mp4")
        self.option_webm = tk.Radiobutton(self, text="WEBM", variable=self.format, value="webm")
        self.option_3gp = tk.Radiobutton(self, text="3GP", variable=self.format, value="3gp")
        self.label_quality = tk.Label(self, text="Quality:")
        self.quality = tk.StringVar(self)
        self.quality.set("360p")
        self.option_360p = tk.Radiobutton(self, text="360p", variable=self.quality, value="360p")
        self.option_720p = tk.Radiobutton(self, text="720p", variable=self.quality, value="720p")
        self.option_1080p = tk.Radiobutton(self, text="1080p", variable=self.quality, value="1080p")
        self.button_download = tk.Button(self, text="Download", command=self.download)
        self.label_url.pack()
        self.entry_url.pack()
        self.label_format.pack()
        self.option_mp4.pack()
        self.option_webm.pack()
        self.option_3gp.pack()
        self.label_quality.pack()
        self.option_360p.pack()
        self.option_720p.pack()
        self.option_1080p.pack()
        self.button_download.pack()

    def download(self):
        url = self.entry_url.get()
        format = self.format.get()
        quality = self.quality.get()
        try:
            video = pytube.YouTube(url)
            stream = video.streams.filter(file_extension=format, res=quality).first()
            stream.download()
            self.label_status = tk.Label(self, text="Download complete!")
            self.label_status.pack()
        except:
            self.label_status = tk.Label(self, text="Error downloading video.")
            self.label_status.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = YoutubeDownloader(master=root)
    app.mainloop()
