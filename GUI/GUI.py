import os
import tkinter as tk
from tkinter import ttk
import time
start_time = time.time()


def gui():
    def update_status1(step):
        progress.step(step)
        root.after(1000, lambda: update_status1(10))

    def update_status():
        current_status = status["text"]
        if current_status == ("Working on Databases..."):
            current_status = "Working on Cleaning data"
            os.system('python3 scripts/DataClean.py')

        elif current_status == ("Working on Cleaning data..."):
            current_status = "Working on Model Training"
            os.system('python3 scripts/train_model.py')

        else:
            current_status += "."
        status["text"] = current_status
        root.after(1000, update_status)
        t = (round(time.time()) - round(start_time))
        if t == 20:
            root.destroy()

    def cancel():
        root.destroy()
    root = tk.Tk()
    # position
    w = 500
    h = 200
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    # icon
    root.iconbitmap('GUI\icon.ico')
    root.configure(background='black')
    root.title("Working on Data")
    # text
    status = tk.Label(root, text="Working on Databases", bg='#000', fg='#fff')
    status.grid(row=0, column=3, padx=100, pady=30)
    root.after(10, update_status)
    # Progressbar
    progress = ttk.Progressbar(root, length=250)
    progress.grid(row=1, column=3, padx=100)
    progress.after(1, lambda: update_status1(2))
    B = tk.Button(text="Cancel", command=cancel)
    B.grid(row=4, column=3, padx=100, pady=20)

    root.mainloop()
