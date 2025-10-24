from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk

root = tk.Tk()
root.title("IMG slider")

images_path=[
    r"C:\Users\razia\Downloads\pexels-diji-aderogba-351053474-31653067.jpg",
    r"C:\Users\razia\Downloads\pexels-oskar-gross-1074333632-34125822.jpg",
    r"C:\Users\razia\Downloads\pexels-dirk-pothen-2149332904-32801962.jpg"
]

image_size = (1080,1080)
images = [Image.open(path). resize(image_size) for path in images_path]
photo_images= [ImageTk.PhotoImage(image) for image in images]

label = tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow = cycle(photo_images)

def start_slideshow():
    for _ in range(len(images_path)):
        update_image()

play_button = tk.Button(root, text='play slider', command=start_slideshow)
play_button.pack()

root.mainloop()