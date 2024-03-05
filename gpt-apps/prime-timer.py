import tkinter as tk
from threading import Thread
import time

# Check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

# Countdown function
def countdown(count):
    while count > 0:
        time.sleep(1)
        count -= 1
        if is_prime(count):
            time_var.set(count)

# Start the countdown
def start_timer():
    #stop_event.clear()
    try:
        count = int(entry.get())
        time_var.set(count)
        t = Thread(target=countdown, args=(count,))
        t.start()
    except ValueError:
        time_var.set("Enter a valid number")

# Stop the countdown
def stop_timer():
    stop_event.set()

# Create the main application window
root = tk.Tk()
root.title("Prime Number Countdown Timer")

# Entry variable
time_var = tk.StringVar()

# Stop event for the thread
stop_event = tk.Event()

# Entry widget
entry = tk.Entry(root, font=('Arial', 18))
entry.grid(row=0, column=0, columnspan=2, sticky='nsew')

# Timer display
timer_display = tk.Label(root, textvariable=time_var, font=('Arial', 18))
timer_display.grid(row=1, column=0, columnspan=2, sticky='nsew')

# Start button
start_button = tk.Button(root, text="Start", command=start_timer, font=('Arial', 18))
start_button.grid(row=2, column=0, sticky='nsew')

# Stop button
stop_button = tk.Button(root, text="Stop", command=stop_timer, font=('Arial', 18))
stop_button.grid(row=2, column=1, sticky='nsew')

# Make the grid cells expandable
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Run the application
root.mainloop()