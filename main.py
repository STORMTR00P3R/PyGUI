import tkinter as tk
from tkinter import messagebox
import socket


def get_ip_address():
    try:
        hostname = socket.gethostname()  # what your device is called on the network
        ip_address = socket.gethostbyname(hostname)  # IP Address associated with your device
        messagebox.showinfo("IP Address:", f"Your IP Address is {ip_address}")
    except Exception as e:
        messagebox.showerror("Error:", f"Error ocurred: {e}")


window = tk.Tk()
window.title("Hello, World!")

def handle_button_press():
    # window.destroy()
    get_ip_address()

button = tk.Button(text="My simple app.", command=handle_button_press)
button.pack()

window.mainloop()