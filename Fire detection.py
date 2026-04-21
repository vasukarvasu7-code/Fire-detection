import tkinter as tk
import random
import time

# For alarm sound (Windows)
try:
    import winsound
    SOUND = True
except:
    SOUND = False


class FireDetectionGUI:
    def __init__(self, root):
        self.root = root
        self.root.title(" Fire Detection System")
        self.root.geometry("500x400")

        self.threshold = 60

        # Title
        self.label_title = tk.Label(root, text="Fire Detection System", font=("Arial", 20, "bold"))
        self.label_title.pack(pady=20)

        # Temperature display
        self.temp_label = tk.Label(root, text="", font=("Arial", 18))
        self.temp_label.pack(pady=10)

        # Status display
        self.status_label = tk.Label(root, text="", font=("Arial", 18))
        self.status_label.pack(pady=20)

        # Start button
        self.start_btn = tk.Button(root, text="Start System", command=self.start_system, bg="green", fg="white")
        self.start_btn.pack(pady=10)

        # Stop button
        self.stop_btn = tk.Button(root, text="Stop System", command=self.stop_system, bg="red", fg="white")
        self.stop_btn.pack(pady=10)

        self.running = False

    def read_sensor(self):
        """Simulated temperature sensor"""
        return random.randint(20, 100)

    def check_fire(self, temp):
        return temp > self.threshold

    def alarm(self):
        if SOUND:
            winsound.Beep(1000, 500)
        else:
            print("Alarm!")

    def update_system(self):
        if not self.running:
            return

        temp = self.read_sensor()
        self.temp_label.config(text=f" Temperature: {temp} °C")

        if self.check_fire(temp):
            self.root.configure(bg="red")
            self.status_label.config(text=" FIRE DETECTED!", fg="white", bg="red")
            self.alarm()
        else:
            self.root.configure(bg="green")
            self.status_label.config(text="SAFE", fg="white", bg="green")

        # Repeat every 2 seconds
        self.root.after(2000, self.update_system)

    def start_system(self):
        self.running = True
        self.update_system()

    def stop_system(self):
        self.running = False
        self.root.configure(bg="white")
        self.status_label.config(text="System Stopped", bg="white", fg="black")
        self.temp_label.config(text="")


# Run app
if __name__ == "__main__":
    root = tk.Tk()
    app = FireDetectionGUI(root)
    root.mainloop()
