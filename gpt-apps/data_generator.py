import tkinter as tk
from tkinter import messagebox
import json

class JSONGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Data Generator")

        # Create frames
        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(pady=20)

        self.output_frame = tk.Frame(self.root)
        self.output_frame.pack(pady=20)

        # Input fields
        self.name_label = tk.Label(self.input_frame, text="Name:")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.age_label = tk.Label(self.input_frame, text="Age:")
        self.age_label.grid(row=1, column=0, padx=5, pady=5)
        self.age_entry = tk.Entry(self.input_frame)
        self.age_entry.grid(row=1, column=1, padx=5, pady=5)

        self.id_label = tk.Label(self.input_frame, text="ID:")
        self.id_label.grid(row=2, column=0, padx=5, pady=5)
        self.id_entry = tk.Entry(self.input_frame)
        self.id_entry.grid(row=2, column=1, padx=5, pady=5)

        # Buttons
        self.generate_male_button = tk.Button(self.input_frame, text="Generate Male JSON", command=lambda: self.generate_json('male'))
        self.generate_male_button.grid(row=3, column=0, padx=5, pady=5)

        self.generate_female_button = tk.Button(self.input_frame, text="Generate Female JSON", command=lambda: self.generate_json('female'))
        self.generate_female_button.grid(row=3, column=1, padx=5, pady=5)

        # Output Text Box
        self.output_text = tk.Text(self.output_frame, height=10, width=50)
        self.output_text.pack()

    def generate_json(self, gender):
        name = self.name_entry.get()
        age = self.age_entry.get()
        user_id = self.id_entry.get()

        # Validate input
        if not name or not age.isdigit() or not user_id:
            messagebox.showerror("Input Error", "Please enter valid name, age, and ID.")
            return

        # Create JSON data
        data = {
            "name": name,
            "age": int(age),
            "id": user_id,
            "gender": gender
        }

        # Convert to JSON string
        json_data = json.dumps(data, indent=4)

        # Display JSON data
        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, json_data)

def main():
    root = tk.Tk()
    app = JSONGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()