import os
import shutil
import platform
import tkinter as tk
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk

def clean_temp_folder():
    if platform.system() == "Windows":
        temp_folder = os.environ.get("TEMP")
        if temp_folder:
            files = os.listdir(temp_folder)
            deleted_files = 0
            errors = []
            for file in files:
                try:
                    file_path = os.path.join(temp_folder, file)
                    if os.path.isfile(file_path):
                        os.remove(file_path)
                        deleted_files += 1
                    elif os.path.isdir(file_path):
                        shutil.rmtree(file_path)
                        deleted_files += 1
                except Exception as e:
                    errors.append((file, str(e)))
            
            if deleted_files > 0:
                messagebox.showinfo("Cleanup Complete", f"Deleted {deleted_files} files/folders from {temp_folder}")
            if errors:
                error_message = "\n".join([f"{file}: {error}" for file, error in errors])
                messagebox.showwarning("Errors", f"Failed to delete the following files/folders:\n{error_message}")
        else:
            messagebox.showwarning("Warning", "Unable to retrieve TEMP folder path.")
    else:
        messagebox.showinfo("Information", "This script is intended for Windows operating system.")

def clean_temp_gui():
    clean_temp_folder()

# Create the main window
root = tk.Tk()
root.maxsize(400, 300)
root.minsize(400, 300)
root.title("Temp Files Cleaner")

# Load the background image
image = Image.open("cleaner.jpg")  # Update the path to your background image
background_image = ImageTk.PhotoImage(image)

# Create a Canvas widget
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack(fill="both", expand=True)

# Set the background image
canvas.create_image(0, 0, image=background_image, anchor="nw")

# Add title label on the canvas
#title_label = tk.Label(root, text="Temp Files Cleaner", font=('Ubuntu Mono', 12), bg='white')
#canvas.create_window(200, 20, window=title_label)

# Add the Clean Temp Folder button on the canvas
clean_button = tk.Button(root, text="Clean Temp Folder", bg="light grey", command=clean_temp_gui, font=("Ubuntu Mono", 9))
canvas.create_window(200, 240, window=clean_button)

# Add the status bar on the canvas
status_bar = tk.Label(root, text="This app is created by MAX. Copyright @2024", bd=1, relief=tk.SUNKEN, anchor=tk.CENTER, justify=tk.CENTER, font=("Ubuntu Mono", 8), bg='white')
canvas.create_window(200, 280, window=status_bar)

# Set window size and center it
window_width = 400
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")
root.resizable(False, False)

# Run the application
root.mainloop()
