import tkinter as tk

root = tk.Tk()
root.title('Custom Styling Example')

label = tk.Label(root, text="Fancy Label", bg="purple", fg="white", font=("Helvetica", 16, "bold"))
label.pack(pady=10, padx=10)

button = tk.Button(root, text="Stylish Button", bg="green", fg="white", font=("Times New Roman", 12))
button.pack(pady=5, padx=5)

root.mainloop()