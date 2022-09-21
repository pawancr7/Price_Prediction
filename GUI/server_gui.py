import os


def server_gi():
    import tkinter as tk
    from tkinter import ttk

    def start():
        os.system('python3 scripts/server.py')

        def stop():
            root.destroy()
            server_gi()

        def update_status1(step):
            progress.step(step)
            root.after(1000, lambda: update_status1(10))

        status = tk.Label(root, text="Server Running", bg='#000', fg='#fff')
        status.grid(row=0, column=3, padx=100, pady=20)

        progress = ttk.Progressbar(root, length=250)
        progress.grid(row=1, column=3, padx=100)
        progress.after(1, lambda: update_status1(2))

        B = tk.Button(text="Stop", command=stop)
        B.config(height=2, width=12)
        B.grid(row=2, column=3, padx=200, pady=20)

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
    root.title("MongoDB Server")
    # text
    B = tk.Button(text="Start", command=start)
    B.config(height=2, width=12)
    B.grid(row=4, column=6, padx=200, pady=80)

    root.mainloop()


server_gi()
