import tkinter as tk

window = tk.Tk()
window.title("Hello, World!")

def handle_button_press():
    window.destroy()

button = tk.Button(text="My simple app.", command=handle_button_press)
button.pack()

window.mainloop()