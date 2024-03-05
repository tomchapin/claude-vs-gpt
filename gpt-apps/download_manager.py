import tkinter as tk
from tkinter import messagebox, filedialog
import requests
from threading import Thread
from urllib.parse import urlparse
import os
import time
import tkinter.ttk as ttk

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def download_file(url, save_path, speed_label, progress_bar, size_label, downloaded_label):
    try:
        with requests.get(url, stream=True) as r:
            r.raise_for_status()
            total_size = int(r.headers.get('content-length', 0))
            size_label.config(text=f"Total Size: {total_size / 1024:.2f} KB")
            downloaded = 0
            start_time = time.time()
            with open(save_path, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
                        downloaded += len(chunk)
                        downloaded_label.config(text=f"Downloaded: {downloaded / 1024:.2f} KB")
                        progress_bar['value'] = (downloaded / total_size) * 100
                        speed = downloaded / (time.time() - start_time)
                        speed_label.config(text=f"Speed: {speed / 1024:.2f} KB/s")
                        root.update_idletasks()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def start_download(url_entry, speed_label, progress_bar, size_label, downloaded_label):
    url = url_entry.get()
    if not is_valid_url(url):
        messagebox.showerror("Error", "Please enter a valid URL")
        return
    save_path = filedialog.asksaveasfilename()
    if not save_path:
        messagebox.showerror("Error", "Please choose a location to save the file")
        return
    Thread(target=download_file, args=(url, save_path, speed_label, progress_bar, size_label, downloaded_label)).start()

root = tk.Tk()
root.title("Simple File Downloader")

frame = tk.Frame(root)
frame.pack(pady=20)

url_label = tk.Label(frame, text="Enter URL:")
url_label.grid(row=0, column=0, padx=5)

url_entry = tk.Entry(frame, width=50)
url_entry.grid(row=0, column=1, padx=5)

download_button = tk.Button(frame, text="Download", command=lambda: start_download(url_entry, speed_label, progress_bar, size_label, downloaded_label))
download_button.grid(row=0, column=2, padx=5)

progress_bar = tk.ttk.Progressbar(root, orient='horizontal', length=400, mode='determinate')
progress_bar.pack(pady=10)

speed_label = tk.Label(root, text="Speed: 0 KB/s")
speed_label.pack()

size_label = tk.Label(root, text="Total Size: 0 KB")
size_label.pack()

downloaded_label = tk.Label(root, text="Downloaded: 0 KB")
downloaded_label.pack()

root.mainloop()