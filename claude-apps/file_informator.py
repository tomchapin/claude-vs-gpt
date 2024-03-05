import os
import tkinter as tk
from tkinter import filedialog, ttk
from PIL import Image
from mutagen import File

class FileAnalyzer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Analyzer")
        self.geometry("800x600")

        self.create_widgets()

    def create_widgets(self):
        self.upload_button = ttk.Button(self, text="Upload File", command=self.upload_file)
        self.upload_button.pack(pady=10)

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(fill=tk.BOTH, expand=True)

        self.basic_info_frame = ttk.Frame(self.notebook)
        self.advanced_info_frame = ttk.Frame(self.notebook)

        self.notebook.add(self.basic_info_frame, text="Basic Information")
        self.notebook.add(self.advanced_info_frame, text="Advanced Information")

        self.basic_info_text = tk.Text(self.basic_info_frame, wrap=tk.WORD)
        self.basic_info_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.advanced_info_text = tk.Text(self.advanced_info_frame, wrap=tk.WORD)
        self.advanced_info_text.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def upload_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            try:
                file_name = os.path.basename(file_path)
                file_size = os.path.getsize(file_path)
                file_type = os.path.splitext(file_path)[1]

                basic_info = f"File Name: {file_name}\nFile Size: {file_size} bytes\nFile Type: {file_type}"
                self.basic_info_text.delete(1.0, tk.END)
                self.basic_info_text.insert(tk.END, basic_info)

                advanced_info = ""

                if file_type in [".txt", ".py", ".java", ".c", ".cpp"]:
                    with open(file_path, "r") as file:
                        content = file.read()
                        advanced_info = f"File Content:\n{content}"
                elif file_type in [".jpg", ".jpeg", ".png", ".gif"]:
                    image = Image.open(file_path)
                    width, height = image.size
                    format = image.format
                    mode = image.mode
                    advanced_info = f"Image Width: {width}\nImage Height: {height}\nImage Format: {format}\nImage Mode: {mode}"
                elif file_type in [".mp3", ".wav", ".flac"]:
                    audio = File(file_path)
                    duration = audio.info.length
                    bitrate = audio.info.bitrate
                    sample_rate = audio.info.sample_rate
                    advanced_info = f"Duration: {duration:.2f} seconds\nBitrate: {bitrate} bps\nSample Rate: {sample_rate} Hz"
                elif file_type in [".mp4", ".avi", ".mkv"]:
                    video = File(file_path)
                    duration = video.info.length
                    bitrate = video.info.bitrate
                    resolution = f"{video.info.width}x{video.info.height}"
                    advanced_info = f"Duration: {duration:.2f} seconds\nBitrate: {bitrate} bps\nResolution: {resolution}"

                self.advanced_info_text.delete(1.0, tk.END)
                self.advanced_info_text.insert(tk.END, advanced_info)
            except Exception as e:
                tk.messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    app = FileAnalyzer()
    app.mainloop()