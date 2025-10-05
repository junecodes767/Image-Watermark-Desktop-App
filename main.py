from PIL import Image, ImageDraw, ImageFont,ImageTk
from tkinter import Scale,HORIZONTAL,Toplevel,Canvas
import tkinter as tk
from tkinter import filedialog
import customtkinter
  
FILE_NAME = None
original_image = None
scaled_photo= None
tk_image = None
CANVAS_W, CANVAS_H = 700, 500 # canvas dimensions
WATERMARK_TEXT = None
FONT_SIZE = 40
FONT_COLOR = "black"
OVERLAY_IMAGE = None
OPACITY = 128

def scale_image(img, max_w, max_h):
    """Return a scaled copy of img that fits inside max_w × max_h."""
    img_w, img_h = img.size
    scale = min(max_w / img_w, max_h / img_h)  # scaling factor
    new_w = int(img_w * scale)
    new_h = int(img_h * scale)
    return img.resize((new_w, new_h), Image.Resampling.LANCZOS)


def choose_image():
    global FILE_NAME,pil_image,tk_image,scaled_photo,original_image
    FILE_NAME = filedialog.askopenfilename(
    initialdir="/",
    title="Select Your Image File",
    filetypes=(
        ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff"),
        ("All Files", "*.*")
    )
    )
    if FILE_NAME:
        original_image = Image.open(FILE_NAME)
        # pil_image = original_image.resize((400, 400), Image.Resampling.LANCZOS)
        #scale image
        scaled_photo =scale_image(original_image,CANVAS_W,CANVAS_H)
        
        tk_image = ImageTk.PhotoImage(scaled_photo)
        canvas.create_image(CANVAS_W/2, CANVAS_H/2, image=tk_image, anchor=tk.CENTER)

def text_on_image():
    """attaches the text unto the image as a watermark"""
    global original_image,WATERMARK_TEXT ,FONT_SIZE,FONT_COLOR
    img = original_image.copy()
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", FONT_SIZE)
    width, height = original_image.size
    bbox = draw.textbbox((0, 0), WATERMARK_TEXT, font=font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]

    position = ((width - text_w) / 2, (height - text_h) / 2)# Adjust coordinates as needed
    fill_color = FONT_COLOR # Red color
    

    draw.text(position, WATERMARK_TEXT, font=font, fill=fill_color)
    # rotate_text = draw.rotate(45, expand=True, fillcolor=(0,0,0,0))
    watermarked_image = img
    scaled_photo =scale_image(watermarked_image,CANVAS_W,CANVAS_H)
        
    tk_image = ImageTk.PhotoImage(scaled_photo)
    canvas.create_image(CANVAS_W/2, CANVAS_H/2, image=tk_image, anchor=tk.CENTER)
    canvas.image = tk_image

def get_fontsize(value):
    global FONT_SIZE
    FONT_SIZE = int(float(value)) * 5
    
    
def modify_image():
    """Update image when user changes different features"""
    global WATERMARK_TEXT
    if WATERMARK_TEXT != None:
        text_on_image()
    else:
        overlay_image()
    
def image_or_text():
    global radio_btn,OVERLAY_IMAGE,original_image, CANVAS_H, CANVAS_W,OPACITY
    if radio_btn.get() == "text":
        open_new_window()
    else:
        
        OVERLAY_IMAGE = filedialog.askopenfilename(
                        initialdir="/",
                        title="Select Your Image File",
                        filetypes=(
                            ("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif;*.tiff"),
                            ("All Files", "*.*")
                        )
                    )
        
        if OVERLAY_IMAGE:
           overlay_image()
  
def overlay_image ():
    global radio_btn,OVERLAY_IMAGE,original_image, CANVAS_H, CANVAS_W,OPACITY

    background = original_image.copy()
    #get the user image
        #open image using pillow
    overlay = Image.open(OVERLAY_IMAGE)
    overlay.putalpha(OPACITY)
    width, height = background.size
    ov_w, ov_h = overlay.size
    x = (width - ov_w) // 2
    y = (height - ov_h) // 2
    # Ensure the overlay image has an alpha channel if transparency is desired
    if overlay.mode != 'RGBA':
        overlay = overlay.convert('RGBA')
    position = (x,y)
    # Paste the overlay image onto the background
    # The 'mask' argument is used for handling transparency in the overlay image
    background.paste(overlay, position,overlay) # this is the alter image
    
    scaled_photo =scale_image(background,CANVAS_W,CANVAS_H) # scale the photo for the canvas
    
    tk_image = ImageTk.PhotoImage(scaled_photo) # turn the photo to a tkimage. This is reable by tkinter it gives a photo image object
    canvas.create_image(CANVAS_W/2, CANVAS_H/2, image=tk_image, anchor=tk.CENTER)  
    canvas.image = tk_image
       
def open_new_window():
    global WATERMARK_TEXT
    new_window = Toplevel(root) 
    new_window.title("Enter Text")
    new_window.geometry("400x150")  
    watermark_text = tk.StringVar()
    def submit_text():
        global WATERMARK_TEXT
        WATERMARK_TEXT = watermark_text.get()
        if WATERMARK_TEXT:  # only if user entered something
            text_on_image()
        else:
            print("still none")
     # Create a new window
    
    customtkinter.CTkLabel(new_window, text="Enter Text to Attach To Image:", font=("Inter",20)).place(x=10,y=50)
    
    customtkinter.CTkEntry(new_window, textvariable=watermark_text,width=200).place(x=10,y=90)
    # if watermark_text.get() not in ['',None]:
       
    enter_btn = customtkinter.CTkButton(new_window, text ="Enter", command =submit_text)
    enter_btn.place(x=250,y=90)
    # enter_btn.bind('<Button-1>',record_text)
        
        
        
        
     # close window on when the button is clicked

def change_font_color():
    global FONT_COLOR
    FONT_COLOR = color_btn.get() 
    print("Font color changed to:", FONT_COLOR) 
root = tk.Tk()



root.geometry("1440x1024")


watermark_label_title= tk.Label(root, text="Watermark")

watermark_label = tk.Label(root, text="Watermark", font=("Inter",24)).place(x=850,y=10)
#labels
# x_label = tk.Label(root, text="x:", font=("Inter",24)).place(x=850,y=300 )
# y_label = tk.Label(root, text="y:" , font=("Inter",24)).place(x=850,y=350 )
opacity = tk.Label(root, text="Opacity" , font=("Inter",24)).place(x=850,y=498)
font_size = tk.Label(root, text="Font Size", font=("Inter",24)).place(x=850,y=400 )
position = tk.Label(root, text="Color", font=("Inter",24)).place(x=850,y=260 )


#buttons
addImage_btn = customtkinter.CTkButton(root, text="Add Image", width=200 , height=40, corner_radius=40, command=choose_image).place( y= 600, x=280)
saveImage_btn = customtkinter.CTkButton(root, text="Save Image", corner_radius=40, width=200, height=40,  fg_color="#F20E0E").place(x=880, y=630)
modifyImage_btn= customtkinter.CTkButton(root, text="Modify Image", corner_radius=40, width=200, height=40,command=modify_image).place(x=1130, y=630)
enter_btn = customtkinter.CTkButton(root, text="Enter", width=200 , height=40, corner_radius=40,command=image_or_text).place(x=970, y= 200)

#radio button
radio_btn = tk.StringVar()
watermark_text_input = customtkinter.CTkRadioButton(root, text="Text", variable=radio_btn,font=("Inter",15),value ="text").place(x=850, y=100)
watermark_image_input= customtkinter.CTkRadioButton(root, text="Image", variable=radio_btn,font=("Inter",15),value ="image").place(x=1200, y=100)
color_btn = tk.StringVar()
# red_color = customtkinter.CTkRadioButton(root, text="Red", variable=color_btn,font=("Inter",15),value ="red").place(x=1050, y=320)
blue_color = customtkinter.CTkRadioButton(root, text="Blue", variable=color_btn,font=("Inter",15),value ="blue",command=change_font_color).place(x=870, y=320)
black_color = customtkinter.CTkRadioButton(root, text="Black", variable=color_btn,font=("Inter",15),value ="black", command=change_font_color).place(x=950, y=320)
white_color = customtkinter.CTkRadioButton(root, text="White", variable=color_btn,font=("Inter",15),value ="white", command=change_font_color).place(x=1030, y=320)
green_color = customtkinter.CTkRadioButton(root, text="Green", variable=color_btn,font=("Inter",15),value ="green", command= change_font_color).place(x=1120, y=320)

x_var=tk.StringVar()

#opacity radio buttons
def change_image_opacity():
    value =  opacity_value.get()
    print(value)
    global OPACITY
    if value =="25%":
        OPACITY=38
        print(OPACITY)
    if value =="50%":
        OPACITY =128
        print(OPACITY)
    if value =="75%":
        OPACITY=191
        print(OPACITY)
    if value == "100%":
        OPACITY=255
        print(OPACITY)
        
    
opacity_value = tk.StringVar()
opacity_values = ["25%","50%","75%","100%"]
x = 870
y = 560
for value in opacity_values:
    customtkinter.CTkRadioButton(root,text=value,variable=opacity_value, value =value, command=change_image_opacity).place(x=x,y=y)
    x +=80

# Entry
# x_entry = tk.Entry(root, textvariable = x_var, font = ('calibre',10,'normal')).place(x=890,y=315)
# y_entry = tk.Entry(root, textvariable = x_var, font = ('calibre',10,'normal')).place(x=890,y=365)


#sliders
font_size_value = tk.StringVar()

# Create the slider

fontsize_scale= Scale( root,from_ = 1, to = 100, 
           orient = HORIZONTAL,  command=get_fontsize)
fontsize_scale.place(x=860, y=440)

#canvas
canvas = customtkinter.CTkCanvas(root, width=CANVAS_W, height=CANVAS_H, bg="Grey")
canvas.place(x=50,y=40)
# Optional: Resize the image
# canvas.create_image(200, 150, image=tk_image, anchor=tk.CENTER)
canvas.image = tk_image  # keep a reference!

root.mainloop()