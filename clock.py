import tkinter as tk
import time

def tick():
    time_string = time.strftime('%H:%M:%S')
    clock.config(text=time_string)
    clock.after(1000, tick)

root = tk.Tk()
root.title("Digital Clock")

clock = tk.Label(root, font=('Impact', 100, 'bold italic'), bg='black', fg='skyblue')
clock.pack(fill='both', expand=1)

tick()
root.mainloop()
