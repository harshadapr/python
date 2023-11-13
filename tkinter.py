import tkinter as tk

def on_button_click():
    label.config(text="Hello, " + entry.get())

# Create a simple GUI window
window = tk.Tk()
window.title("Simple Tkinter GUI")

# Add widgets to the window
label = tk.Label(window, text="Enter your name:")
label.pack()

entry = tk.Entry(window)
entry.pack()

button = tk.Button(window, text="Say Hello", command=on_button_click)
button.pack()

# Start the GUI event loop
window.mainloop()
