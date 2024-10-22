from itertools import cycle
from PIL import Image, ImageTk
import time
import tkinter as tk 


root=tk.Tk()
root.title("Image Slide Viewer")

#list of image path
image_paths=[r"C:\Users\Shashi Shekhar\Pictures\Shashi\photo1.jpg",
             r"C:\Users\Shashi Shekhar\Pictures\Shashi\photo2.jpg",
             r"C:\Users\Shashi Shekhar\Pictures\Shashi\photo3.jpg",
             r"C:\Users\Shashi Shekhar\Pictures\Shashi\photo4.png",
             r"C:\Users\Shashi Shekhar\Pictures\Shashi\photo5.png",
             r"C:\Users\Shashi Shekhar\Pictures\Shashi\photo6.jpg",
             ]

#resize the image to 1080x1080
image_size=(1080,1080)
images=[Image.open(path).resize(image_size) for path in image_paths]
photo_images=[ImageTk.PhotoImage(image)for image in images]


label=tk.Label(root)
label.pack()

def update_image():
    for photo_image in photo_images:
        label.config(image=photo_image)
        label.update()
        time.sleep(3)

slideshow=cycle(photo_images)

def start_slideshow():
    for _ in range(len(image_paths)):
        update_image()

play_button = tk.Button(root, text="Play", command=start_slideshow)
play_button.pack()

root.mainloop()
