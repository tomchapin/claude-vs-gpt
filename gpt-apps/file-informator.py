import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import mimetypes

# Function to open a file and return its content
def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        try:
            file_info = os.stat(file_path)
            file_type, _ = mimetypes.guess_type(file_path)
            basic_info = {
                'File Name': os.path.basename(file_path),
                'File Type': file_type or 'Unknown',
                'File Size': f'{file_info.st_size} bytes'
            }
            advanced_info = {
                'Created': file_info.st_ctime,
                'Last Modified': file_info.st_mtime,
                'Last Accessed': file_info.st_atime
            }
            display_info(basic_info, advanced_info)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

# Function to display file information
def display_info(basic_info, advanced_info):
    basic_info_text.delete('1.0', tk.END)
    advanced_info_text.delete('1.0', tk.END)
    
    for key, value in basic_info.items():
        basic_info_text.insert(tk.END, f"{key}: {value}\n")
    
    for key, value in advanced_info.items():
        advanced_info_text.insert(tk.END, f"{key}: {value}\n")

# Main application window
root = tk.Tk()
root.title("File Information Viewer")

# Frame for basic and advanced info
info_frame = ttk.Frame(root)
info_frame.pack(padx=10, pady=10, fill='x', expand=True)

# Basic info section
basic_info_label = ttk.Label(info_frame, text="Basic Information")
basic_info_label.pack()
basic_info_text = tk.Text(info_frame, height=10, width=50)
basic_info_text.pack()

# Advanced info section
advanced_info_label = ttk.Label(info_frame, text="Advanced Information")
advanced_info_label.pack()
advanced_info_text = tk.Text(info_frame, height=10, width=50)
advanced_info_text.pack()

# Upload button
upload_button = ttk.Button(root, text="Upload File", command=open_file)
upload_button.pack(pady=10)

# Run the application
root.mainloop()