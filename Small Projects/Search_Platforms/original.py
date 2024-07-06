import tkinter as tk
from tkinter import *
import webbrowser

#Define the main window
root = tk.Tk()
root.title("YOUR AI ASSISTANT")

root.maxsize(500, 250)
root.minsize(500, 250)

#Adding a background color
root.configure(bg="grey")

#Define the function to automate Youtube search
def search_youtube():
    query = entry.get()
    url = f"https://www.youtube.com/results?search_query={query}"
    webbrowser.open(url)

#Define the function to automate Google search
def search_google():
    query = entry.get()
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)

#Define the function to automate Instagram search
def search_kbpage():
    query = entry.get()
    url = f"https://teva.service-now.com/$knowledge.do?sysparm_kb=2530c50f4f329a0086503c728110c72e&sysparm_type_filter=all&query={query}&sysparm_order=relevancy"
    webbrowser.open(url)

#Define the function to automate Service-Now search
def search_snow():
    query = entry.get()
    url = f"https://teva.service-now.com/now/nav/ui/search/0f8b85d0c7922010099a308dc7c2606a/params/search-term/{query}/global-search-data-config-id/c861cea2c7022010099a308dc7c26041/back-button-label/Unified%20Navigation%20App/search-context/now%2Fnav%2Fui"
    webbrowser.open(url)

#Create input field, label, and buttons
Label(root, text="Enter your search word:", font=("Ubuntu Mono", 9)).pack(pady=10)
entry = Entry(root, width=60)
entry.pack(pady=10)

Button(root, text = "Google", command=search_google, width=30, font=("Ubuntu Mono", 9), bg="grey").pack(pady=5)
Button(root, text = "Youtube", command=search_youtube, width=30, font=("Ubuntu Mono", 9), bg="grey").pack(pady=5)
Button(root, text = "Service-Now", command=search_snow, width=30, font=("Ubuntu Mono", 9), bg="grey").pack(pady=5)
Button(root, text = "Knowledge Page", command=search_kbpage, width=30, font=("Ubuntu Mono", 9), bg="grey").pack(pady=5)

#Desin status bar
status_bar = tk.Label(root, text="This App is Designed and Created by MAX. Copyright @2024", bd=1, relief=tk.SUNKEN, anchor=tk.CENTER, justify=tk.CENTER, font=("Ubuntu Mono", 8))
status_bar.pack(side=tk.BOTTOM, fill=tk.X)

#Run the GUI event loop
root.mainloop()
