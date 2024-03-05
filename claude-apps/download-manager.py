import os
import requests
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from urllib.parse import urlparse

class FileDownloader(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("File Downloader")
        self.geometry("400x200")

        self.url_label = ttk.Label(self, text="URL:")
        self.url_label.pack()

        self.url_entry = ttk.Entry(self, width=50)
        self.url_entry.pack()

        self.speed_var = tk.StringVar(value="MB")
        self.speed_dropdown = ttk.OptionMenu(self, self.speed_var, "MB", "KB", "GB")
        self.speed_dropdown.pack()

        self.download_button = ttk.Button(self, text="Download", command=self.download_file)
        self.download_button.pack()

        self.progress_bar = ttk.Progressbar(self, length=200, mode="determinate")
        self.progress_bar.pack()

        self.file_size_label = ttk.Label(self, text="")
        self.file_size_label.pack()

        self.downloaded_label = ttk.Label(self, text="")
        self.downloaded_label.pack()

    def download_file(self):
        url = self.url_entry.get()
        if not self.is_valid_url(url):
            messagebox.showerror("Error", "Invalid URL")
            return

        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()

            total_size = int(response.headers.get("Content-Length", 0))
            self.progress_bar["maximum"] = total_size

            file_name = os.path.basename(urlparse(url).path)
            save_path = filedialog.asksaveasfilename(defaultextension=os.path.splitext(file_name)[1],
                                                     initialfile=file_name)
            if not save_path:
                return

            downloaded_size = 0
            with open(save_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
                        downloaded_size += len(chunk)
                        self.progress_bar["value"] = downloaded_size
                        self.update_labels(downloaded_size, total_size)
                        self.update()

            messagebox.showinfo("Success", "File downloaded successfully")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", str(e))
        except Exception as e:
            messagebox.showerror("Error", "An error occurred during download")

    def is_valid_url(self, url):
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except ValueError:
            return False

    def update_labels(self, downloaded_size, total_size):
        speed_unit = self.speed_var.get()
        if speed_unit == "KB":
            downloaded_size /= 1024
            total_size /= 1024
        elif speed_unit == "MB":
            downloaded_size /= 1024 ** 2
            total_size /= 1024 ** 2
        elif speed_unit == "GB":
            downloaded_size /= 1024 ** 3
            total_size /= 1024 ** 3

        self.file_size_label.config(text=f"Total Size: {total_size:.2f} {speed_unit}")
        self.downloaded_label.config(text=f"Downloaded: {downloaded_size:.2f} {speed_unit}")

if __name__ == "__main__":
    app = FileDownloader()
    app.mainloop()