from PIL import Image, ImageDraw, ImageFont,ImageTk
from tkinter import Scale,HORIZONTAL
import tkinter as tk
from tkinter import filedialog
import customtkinter
  
FILE_NAME = None
pil_image = None
tk_image = None

def choose_image():
    global FILE_NAME,pil_image,tk_image
    FILE_NAME = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select Your Image File",
                                          filetypes = (("PNG Files","*.png*"),
                                                       ("JPEG Files","*.jpg*")
                                                        ))
    if FILE_NAME:
        original_image = Image.open(FILE_NAME)
        pil_image = original_image.resize((400, 400), Image.Resampling.LANCZOS)

        tk_image = ImageTk.PhotoImage(pil_image)
        canvas.create_image(100, 100, image=tk_image, anchor=tk.CENTER)



           
root = tk.Tk()


root.geometry("1440x1024")


watermark_label_title= tk.Label(root, text="Watermark")

watermark_label = tk.Label(root, text="Watermark", font=("Inter",24)).place(x=850,y=10)
#labels
x_label = tk.Label(root, text="x:", font=("Inter",24)).place(x=850,y=300 )
y_label = tk.Label(root, text="y:" , font=("Inter",24)).place(x=850,y=350 )
opacity = tk.Label(root, text="Opacity" , font=("Inter",24)).place(x=850,y=498)
font_size = tk.Label(root, text="Font Size", font=("Inter",24)).place(x=850,y=400 )
position = tk.Label(root, text="Position", font=("Inter",24)).place(x=850,y=260 )


#buttons
addImage_btn = customtkinter.CTkButton(root, text="Add Image", width=200 , height=40, corner_radius=40, command=choose_image).place( y= 600, x=280)
saveImage_btn = customtkinter.CTkButton(root, text="Save Image", corner_radius=40, width=200, height=40,  fg_color="#F20E0E").place(x=880, y=630)
modifyImage_btn= customtkinter.CTkButton(root, text="Modify Image", corner_radius=40, width=200, height=40).place(x=1130, y=630)
enter_btn = customtkinter.CTkButton(root, text="Enter", width=200 , height=40, corner_radius=40).place(x=970, y= 200)

#radio button
my_var = tk.StringVar()
watermark_text_input = tk.Radiobutton(root, text="Text", variable=my_var,font=("Inter",15)).place(x=850, y=100)
watermark_image_input= tk.Radiobutton(root, text="Image", variable=my_var,font=("Inter",15)).place(x=1200, y=100)

x_var=tk.StringVar()

# Entry
x_entry = tk.Entry(root, textvariable = x_var, font = ('calibre',10,'normal')).place(x=890,y=315)
y_entry = tk.Entry(root, textvariable = x_var, font = ('calibre',10,'normal')).place(x=890,y=365)


#sliders
font_size_value = tk.DoubleVar()
opacity_value = tk.DoubleVar()

# Create the slider
opacity_scale= Scale( root, variable = opacity_value, 
           from_ = 1, to = 100, 
           orient = HORIZONTAL).place(x=860, y=440)
fontsize_scale= Scale( root, variable = font_size_value, 
           from_ = 1, to = 100, 
           orient = HORIZONTAL).place(x=860, y=540)

#canvas
canvas = tk.Canvas(root, width=700, height=500, bg="Grey")
canvas.place(x=50,y=40)
# Optional: Resize the image
# canvas.create_image(200, 150, image=tk_image, anchor=tk.CENTER)
canvas.image = tk_image  # keep a reference!

root.mainloop()