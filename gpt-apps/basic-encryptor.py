import tkinter as tk
from tkinter import filedialog, messagebox
import os

# Caesar cipher encryption
def encrypt(text, shift=3):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

# Caesar cipher decryption
def decrypt(text, shift=3):
    return encrypt(text, -shift)

# Save file function
def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"), ("JSON files", "*.json"), ("CSV files", "*.csv")])
    if file_path:
        with open(file_path, 'w') as file:
            file.write(input_text.get("1.0", tk.END))

# Load file function
def load_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("JSON files", "*.json"), ("CSV files", "*.csv")])
    if file_path:
        with open(file_path, 'r') as file:
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, file.read())

# Encrypt function
def perform_encrypt():
    user_input = input_text.get("1.0", tk.END)
    encrypted_text = encrypt(user_input)
    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, encrypted_text)

# Decrypt function
def perform_decrypt():
    user_input = input_text.get("1.0", tk.END)
    decrypted_text = decrypt(user_input)
    input_text.delete("1.0", tk.END)
    input_text.insert(tk.END, decrypted_text)

# Create the main window
root = tk.Tk()
root.title("Encryptor/Decryptor")

# Create a text box
input_text = tk.Text(root, height=10, width=50)
input_text.pack()

# Create buttons
encrypt_button = tk.Button(root, text="Encrypt", command=perform_encrypt)
encrypt_button.pack(side=tk.LEFT, padx=(10, 0))

decrypt_button = tk.Button(root, text="Decrypt", command=perform_decrypt)
decrypt_button.pack(side=tk.LEFT)

save_button = tk.Button(root, text="Save File", command=save_file)
save_button.pack(side=tk.RIGHT, padx=(0, 10))

load_button = tk.Button(root, text="Load File", command=load_file)
load_button.pack(side=tk.RIGHT)

# Run the application
root.mainloop()