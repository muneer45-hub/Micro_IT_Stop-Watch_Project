import tkinter as tk
from datetime import datetime
import time
import threading

class StopwatchClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Stopwatch & Clock")

        # Clock label
        self.clock_label = tk.Label(root, text="", font=("Helvetica", 24), fg="blue")
        self.clock_label.pack(pady=10)

        # Stopwatch label
        self.stopwatch_label = tk.Label(root, text="00:00:00", font=("Helvetica", 36), fg="green")
        self.stopwatch_label.pack(pady=10)

        # Buttons
        self.start_button = tk.Button(root, text="Start", width=10, command=self.start_stopwatch)
        self.start_button.pack(side="left", padx=10, pady=10)

        self.stop_button = tk.Button(root, text="Stop", width=10, command=self.stop_stopwatch)
        self.stop_button.pack(side="left", padx=10)

        self.reset_button = tk.Button(root, text="Reset", width=10, command=self.reset_stopwatch)
        self.reset_button.pack(side="left", padx=10)

        # Stopwatch logic
        self.running = False
        self.start_time = 0
        self.elapsed_time = 0

        # Update both clock and stopwatch
        self.update_clock()
        self.update_stopwatch()

    def update_clock(self):
        now = datetime.now().strftime("%H:%M:%S")
        self.clock_label.config(text="Current Time: " + now)
        self.root.after(1000, self.update_clock)

    def update_stopwatch(self):
        if self.running:
            self.elapsed_time = time.time() - self.start_time
        mins, secs = divmod(int(self.elapsed_time), 60)
        hours, mins = divmod(mins, 60)
        self.stopwatch_label.config(text=f"{hours:02}:{mins:02}:{secs:02}")
        self.root.after(100, self.update_stopwatch)

    def start_stopwatch(self):
        if not self.running:
            self.running = True
            self.start_time = time.time() - self.elapsed_time

    def stop_stopwatch(self):
        if self.running:
            self.running = False

    def reset_stopwatch(self):
        self.running = False
        self.elapsed_time = 0
        self.stopwatch_label.config(text="00:00:00")

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = StopwatchClockApp(root)
    root.mainloop()
