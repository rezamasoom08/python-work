import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
root = tk.Tk()
root.title("Background Image Example")
root.geometry("400x300")

# Load the background image
image = Image.open("cleaner.jpg")
background_image = ImageTk.PhotoImage(image)

# Create a Canvas widget
canvas = tk.Canvas(root, width=200, height=100)
canvas.pack(fill="both", expand=True)

# Set the background image
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Optionally add other widgets on top of the canvas
label = tk.Label(root, text="Hello, World!", bg="white")
label_window = canvas.create_window(200, 150, window=label)

# Run the application
root.mainloop()
