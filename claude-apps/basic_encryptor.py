import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

class EncryptionApp:
    def __init__(self, master):
        self.master = master
        master.title("Encryption/Decryption App")

        self.input_text = tk.Text(master, height=10, width=50)
        self.input_text.pack(pady=10)

        self.encrypt_button = tk.Button(master, text="Encrypt", command=self.encrypt_text)
        self.encrypt_button.pack(side=tk.LEFT, padx=10)

        self.decrypt_button = tk.Button(master, text="Decrypt", command=self.decrypt_text)
        self.decrypt_button.pack(side=tk.LEFT)

        self.save_button = tk.Button(master, text="Save File", command=self.save_file)
        self.save_button.pack(side=tk.LEFT, padx=10)

        self.load_button = tk.Button(master, text="Load File", command=self.load_file)
        self.load_button.pack(side=tk.LEFT)

        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)

    def encrypt_text(self):
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            encrypted_text = self.fernet.encrypt(text.encode())
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert(tk.END, encrypted_text.decode())
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def decrypt_text(self):
        try:
            text = self.input_text.get("1.0", tk.END).strip()
            decrypted_text = self.fernet.decrypt(text.encode())
            self.input_text.delete("1.0", tk.END)
            self.input_text.insert(tk.END, decrypted_text.decode())
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def save_file(self):
        try:
            file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                     filetypes=[("Text Files", "*.txt"),
                                                                ("JSON Files", "*.json"),
                                                                ("CSV Files", "*.csv")])
            if file_path:
                with open(file_path, "w") as file:
                    file.write(self.input_text.get("1.0", tk.END).strip())
                messagebox.showinfo("Success", "File saved successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def load_file(self):
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt"),
                                                              ("JSON Files", "*.json"),
                                                              ("CSV Files", "*.csv")])
            if file_path:
                with open(file_path, "r") as file:
                    content = file.read()
                    self.input_text.delete("1.0", tk.END)
                    self.input_text.insert(tk.END, content)
        except Exception as e:
            messagebox.showerror("Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = EncryptionApp(root)
    root.mainloop()