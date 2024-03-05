import tkinter as tk
import json

class JSONGenerator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("JSON Generator")
        self.geometry("600x400")

        self.male_frame = tk.LabelFrame(self, text="Male")
        self.male_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.female_frame = tk.LabelFrame(self, text="Female")
        self.female_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

        self.create_input_fields(self.male_frame)
        self.create_input_fields(self.female_frame)

        self.output_text = tk.Text(self, height=10, width=60)
        self.output_text.pack(padx=20, pady=10)

    def create_input_fields(self, frame):
        tk.Label(frame, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(frame)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(frame, text="Age:").grid(row=1, column=0, padx=5, pady=5)
        age_entry = tk.Entry(frame)
        age_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(frame, text="ID:").grid(row=2, column=0, padx=5, pady=5)
        id_entry = tk.Entry(frame)
        id_entry.grid(row=2, column=1, padx=5, pady=5)

        generate_button = tk.Button(frame, text="Generate", command=lambda: self.generate_json(name_entry.get(), age_entry.get(), id_entry.get()))
        generate_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

    def generate_json(self, name, age, id):
        try:
            data = {
                "name": name,
                "age": int(age),
                "id": id
            }
            json_data = json.dumps(data, indent=4)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, json_data)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid input. Please enter valid values.")
        except Exception as e:
            tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    app = JSONGenerator()
    app.mainloop()