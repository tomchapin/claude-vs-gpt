import tkinter as tk
from tkinter import messagebox

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def start_timer():
    try:
        seconds = int(seconds_entry.get())
        if seconds <= 0:
            raise ValueError
        countdown(seconds)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid positive integer for seconds.")

def stop_timer():
    window.after_cancel(timer)
    timer_label.config(text="00:00")

def countdown(seconds):
    global timer
    minutes, secs = divmod(seconds, 60)
    if is_prime(secs):
        timer_label.config(text="{:02d}:{:02d}".format(minutes, secs))
    else:
        timer_label.config(text="{:02d}:".format(minutes))
    if seconds > 0:
        timer = window.after(1000, countdown, seconds - 1)

# Create the main window
window = tk.Tk()
window.title("Prime Number Timer")
window.geometry("300x200")
window.configure(bg="#F0F0F0")

# Create the timer label
timer_label = tk.Label(window, text="00:00", font=("Arial", 24), bg="#F0F0F0")
timer_label.pack(pady=20)

# Create the seconds entry
seconds_entry = tk.Entry(window, font=("Arial", 14), justify=tk.CENTER)
seconds_entry.pack(pady=10)

# Create the start button
start_button = tk.Button(window, text="Start", font=("Arial", 14), command=start_timer, bg="#4CAF50", fg="white")
start_button.pack(side=tk.LEFT, padx=20)

# Create the stop button
stop_button = tk.Button(window, text="Stop", font=("Arial", 14), command=stop_timer, bg="#F44336", fg="white")
stop_button.pack(side=tk.RIGHT, padx=20)

# Start the main event loop
window.mainloop()