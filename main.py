import os
import tkinter as tk
from tkinter import filedialog
import urllib.request

# List of predefined zip files to download
zip_files = ['file1.zip', 'file2.zip', 'file3.zip']

# Default destination folder path
default_path = r'C:\Games\World_of_Tanks'

# Create the main window
window = tk.Tk()
window.title("Zip File Downloader")
window.geometry("640x480")

# Create a checkbox for each zip file
checkboxes = []
for file in zip_files:
    var = tk.IntVar()
    checkbox = tk.Checkbutton(window, text=file, variable=var)
    checkbox.pack()
    checkboxes.append(var)

# Create a button to select the destination folder path
def select_path():
    path = filedialog.askdirectory(initialdir=default_path)
    path_label.config(text=path)

path_button = tk.Button(text="Select Destination Folder", command=select_path)
path_button.pack()

# Create a label to display the selected folder path
path_label = tk.Label(window, text=default_path)
path_label.pack()

# Create a download button
def download():
    path = path_label.cget("text")
    for i, file in enumerate(zip_files):
        if checkboxes[i].get() == 1:
            url = "https://www.blackwot.org/downloads/" + file
            urllib.request.urlretrieve(url, os.path.join(path, file))

download_button = tk.Button(text="Download", command=download)
download_button.pack()

window.mainloop()
