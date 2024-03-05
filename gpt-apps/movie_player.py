import tkinter as tk
from tkinter import filedialog
import vlc
import os

class MoviePlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("Simple Movie Player")

        # Initialize VLC player
        self.instance = vlc.Instance()
        self.player = self.instance.media_player_new()

        # Create a resizable panel for video output
        self.video_panel = tk.Frame(self.master)
        self.canvas = tk.Canvas(self.video_panel, bg='black')
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.video_panel.pack(fill=tk.BOTH, expand=True)

        # Create control panel
        self.control_panel = tk.Frame(self.master)
        self.play_button = tk.Button(self.control_panel, text="Play/Pause", command=self.toggle_play)
        self.play_button.pack(side=tk.LEFT)
        self.stop_button = tk.Button(self.control_panel, text="Stop", command=self.stop)
        self.stop_button.pack(side=tk.LEFT)
        self.forward_button = tk.Button(self.control_panel, text="Forward", command=lambda: self.skip(10))
        self.forward_button.pack(side=tk.LEFT)
        self.backward_button = tk.Button(self.control_panel, text="Backward", command=lambda: self.skip(-10))
        self.backward_button.pack(side=tk.LEFT)
        self.open_button = tk.Button(self.control_panel, text="Open", command=self.open_file)
        self.open_button.pack(side=tk.LEFT)
        self.control_panel.pack()

        # Bind events
        self.master.bind("<Configure>", self.on_resize)

    def toggle_play(self):
        if self.player.is_playing():
            self.player.pause()
        else:
            self.player.play()

    def stop(self):
        self.player.stop()

    def skip(self, seconds):
        if self.player.is_playing():
            time = self.player.get_time() + (seconds * 1000)
            self.player.set_time(time)

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if os.path.isfile(file_path):
            media = self.instance.media_new(file_path)
            self.player.set_media(media)
            if os.name == 'nt':  # for Windows
                self.player.set_hwnd(self.canvas.winfo_id())
            else:  # for Linux
                self.player.set_xwindow(self.canvas.winfo_id())
            self.toggle_play()

    def on_resize(self, event):
        # Update video output size
        self.player.video_set_scale(0)  # Autoscale the video

if __name__ == "__main__":
    root = tk.Tk()
    app = MoviePlayer(root)
    root.mainloop()