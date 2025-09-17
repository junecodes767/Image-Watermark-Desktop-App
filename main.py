from PIL import Image, ImageDraw, ImageFont
from tkinter import *
import tkinter as tk
import os

from tkinterdnd2 import DND_FILES, TkinterDnD

def text_to_wtrmark(image,text):
    # this turns the image into 
    img = Image.open(image)
    draw = ImageDraw.Draw(img)

    watermark_text = text
    font = ImageFont.truetype("arial.ttf", 40) # Adjust font size as needed

    width, height = img.size
    text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) / 2
    y = (height - text_height) / 2

    draw.text((x, y), watermark_text, fill=(0, 0, 0, 128), font=font) # Black with 50% opacity

def image_to_wtrmark():
    img = Image.open("your_image.jpg")
    watermark = Image.open("watermark_logo.png")
    watermark = watermark.resize((100, 100)) # Example resize
    position = (50, 50) # Example: 50 pixels from top and left
    img.paste(watermark, position, watermark)
    img.save("image_with_logo_watermark.jpg")
    
    
root = TkinterDnD.Tk()
root.geometry("400x600")
title = Label(root,text="Insert your image here").pack()

img = tk.Entry(root)
img.insert(1,"Please Enter your Image here:")
img.pack()
img_bttn = tk.Button(width=5,text="Enter").pack()

watermark_txt_label = tk.Label(text="Enter the text to turn into watermark below").pack()
watermark_txt = tk.Entry(root).pack(pady=10)
watermark_txt_bttn = tk.Button(width=5,text="Enter").pack()

# Define what happens on drop
def drop(event):
    img.insert(tk.END, event.data)  # Add dropped file
    
img.drop_target_register(DND_FILES)
img.dnd_bind('<<Drop>>',drop)



root.mainloop()