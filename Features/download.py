import requests
import tkinter as tk
from tkinter import filedialog

def download_file(url):
    filename = url.split("/")[-1]
    with open(filename, "wb") as f:
        response = requests.get(url, stream=True)
        total_length = response.headers.get("content-length")

        if total_length is None:  # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                print("\r[%s%s]" % ("=" * done, " " * (50 - done)), end="")
            print()

    return filename

def gui_download():
    url = input_url.get()
    filename = download_file(url)
    download_label.config(text=f"File {filename} downloaded")

root = tk.Tk()


input_url = tk.Entry(root, width=50)
input_url.pack()

download_button = tk.Button(root, text="Download", command=gui_download)
download_button.pack()

download_label = tk.Label(root, text="")
download_label.pack()

root.mainloop()
