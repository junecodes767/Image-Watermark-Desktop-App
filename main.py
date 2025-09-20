from PIL import Image, ImageDraw, ImageFont,ImageTk
from tkinter import *
import tkinter as tk
from tkinter import filedialog
    
root = tk.Tk()
root.geometry("1440x1024")


watermark_label_title= tk.Label(root, text="Watermark")

watermark_label = tk.Label(root, text="Watermark")
#labels
# x_label = tk.Label(root, text="x")
# y_label = tk.Label(root, text="y")
opacity = tk.Label(root, text="Opacity")
font_size = tk.Label(root, text="Font Size")

#buttons
addImage_btn = tk.Button(root, text="Click Me")
saveImage_btn = tk.Button(root, text="Click Me")
modifyImage_btn= tk.Button(root, text="Click Me")
enter_btn = tk.Button(root, text="Click Me")

#radio button
my_var = tk.StringVar()
watermark_text_input = tk.Radiobutton(root, text="Text", variable=my_var)
watermark_image_input= tk.Radiobutton(root, text="Image", variable=my_var)

#sliders
slider_value = tk.DoubleVar()

# Create the slider
v1 = DoubleVar()
opacity_scale= Scale( root, variable = v1, 
           from_ = 1, to = 100, 
           orient = HORIZONTAL) 
fontsize_scale= Scale( root, variable = v1, 
           from_ = 1, to = 100, 
           orient = HORIZONTAL) 

#canvas
canvas = tk.Canvas(root, width=400, height=300, bg="Grey")
# original_image = Image.open(FILE_NAME)
# Optional: Resize the image
# pil_image = original_image.resize((200, 150), Image.Resampling.LANCZOS)
# tk_image = ImageTk.PhotoImage(original_image)
# canvas.create_image(200, 150, image=tk_image, anchor=tk.CENTER)

root.mainloop()