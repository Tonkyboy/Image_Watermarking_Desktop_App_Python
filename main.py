from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import Image
from PIL import ImageTk
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np
from tkinter.colorchooser import askcolor
import os

watermarked_images = []

root = Tk()

# Default Watermark Settings
watermark_text = "Watermark"
font_family = "Hurricane_Regular"
font_color = "black"
font_size = 20
placement_direction = "Right-Bottom"

watermark_settings = {
    "Text": watermark_text,
    "Font_Family": font_family,
    "Font_Color": font_color,
    "Font_Size": font_size,
    "Placement_Direction": placement_direction
}


def show_canvas():
    filenames = watermarked_images
    preview_label.config(text="Preview", fg="black", font=("Courier", 25), bg="white", padx=15, pady=15, width="10")

    canvas = Canvas(width=300, height=300, bg="#f7f5dd", highlightthickness=0)

    width = 300
    height = 300
    print(filenames)

    # For opened images
    # img = Image.open(filenames[0])

    # For watermarked image
    img = filenames

    img = img.resize((width, height), Image.ANTIALIAS)
    key_image = ImageTk.PhotoImage(img)

    canvas_image = canvas.create_image(150, 150, state="normal", image=key_image)
    canvas.grid(column=1, row=4, columnspan=3)
    canvas.itemconfig(canvas_image, image=filenames)


def watermark(filenames, watermark_settings):
    # image opening
    image = Image.open(filenames[0])

    # text Watermark
    watermark_image = image.copy()

    draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.truetype(f"fonts/Hurricane-Regular.ttf", watermark_settings["Font_Size"])

    # add Watermark
    # (0,0,0)-black color text
    draw.text((0, 0), watermark_settings["Text"], watermark_settings["Font_Color"], font=font)
    plt.subplot(1, 2, 1)
    plt.title("black text")
    plt.imshow(watermark_image)

    # plt.show()

    global watermarked_images
    watermarked_images = watermark_image


def select_file():
    filetypes = (
        ("All files", "*.*"),
        ("PNG", "*.png"),
        ("JPEG", "*.jpg")
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    #    showinfo(
    #        title='Selected Files',
    #        message=filenames
    #    )
    watermarked_images = watermark(filenames=filenames, watermark_settings=watermark_settings)
    # show_canvas(filenames=filenames)
    # show_canvas(filenames=watermarked_images)

def save_images(watermarked_images):

    # image_path = "/Users/alexreute/Desktop"
    # os.mkdir(image_path)

    watermarked_images.save("geeks.png")

    # for images in watermarked_images:
    #     # images.save(f"{image_path}/{images}.png")
    #     images = images.save("images/geeks.png")


root.title("Watermark your Images")

root.minsize(width=500, height=500)
root.config(padx=50, pady=50)

root.resizable(False, False)

frm = ttk.Frame(root, width=80, height=80, padding=5)
frm.grid(column=2, row=8)

ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=2)

""" Settings Frame for watermark"""
settings_frm = ttk.Frame(root, width=150, height=150, padding=5)
settings_frm.grid(column=1, row=2)

ttk.Label(settings_frm, text="Watermark Settings").grid(column=1, row=1)

# Watermark Text
ttk.Label(settings_frm, text="Watermark Text:").grid(column=1, row=2)
user_input = StringVar()
entry = ttk.Entry(settings_frm, textvariable=user_input).grid(column=2, row=2)


# Font Family
ttk.Label(settings_frm, text="Font Family:").grid(column=1, row=3)
options = ['Hurricane-Regular', 'Inspiration-Regular', 'Pacifico-Regular', 'ShadowsIntoLight-Regular']
font_family = StringVar()
font_family.set(options[0])
OptionMenu(settings_frm, font_family, *options).grid(column=2, row=3)


# Font Color
ttk.Label(settings_frm, text="Font Color:").grid(column=1, row=4)

def change_color():
    colors = askcolor(title="Tkinter Color Chooser")
    watermark_settings["Font_Color"] = colors[0]

ttk.Button(
    settings_frm,
    text='Select a Color',
    command=change_color).grid(column=2, row=4)


# Fonts Size
ttk.Label(settings_frm, text="Font Size:").grid(column=1, row=5)
options = [20, 40, 60, 80]
font_size = StringVar()
font_size.set(options[0])
OptionMenu(settings_frm, font_size, *options).grid(column=2, row=5)

# Direction
ttk.Label(settings_frm, text="Direction:").grid(column=1, row=6)
options = ['Top Left', 'Top Right', 'Bottom Right', 'Bottom Left']
watermark_direction = StringVar()
watermark_direction.set(options[0])

OptionMenu(settings_frm, watermark_direction, *options).grid(column=2, row=6)

# Take Watermark Settings

def get_watermark_settings():
    watermark_settings["Font_Size"] = int(font_size.get())
    watermark_settings["Font_Family"] = font_family.get()
    watermark_settings["Text"] = user_input.get()
    watermark_settings["Placement_Direction"] = watermark_direction.get()

    watermark_text = watermark_settings["Text"]
    print(watermark_text)
    font_family_get = watermark_settings["Font_Family"]
    print(font_family_get)
    font_color_get = watermark_settings["Font_Color"]
    print(font_color_get)
    font_size_get = watermark_settings["Font_Size"]
    print(font_size_get)
    placement_direction = watermark_settings["Placement_Direction"]
    print(placement_direction)



save_button = ttk.Button(
    settings_frm,
    text="Save Watermark Settings",
    command=get_watermark_settings
)
save_button.grid(column=2, row=7)

""" Canvas Preview"""
preview_label = Label()
preview_label.config(text="", fg="black", font=("Courier", 25), bg="white", padx=15, pady=15, width="10")
preview_label.grid(column=1, row=3, columnspan=3)

canvas = Canvas(width=300, height=300, bg="grey", highlightthickness=0)

key_image = PhotoImage(file="images/Placeholder_Image.png")

# Placement of logo in Canvas
canvas_image = canvas.create_image(150, 150, image=key_image)

# Text in Canvas
preview_label.config(text="Preview", fg="black", font=("Courier", 25), bg="white", padx=15, pady=15, width="10")

# Placement in window
canvas.grid(column=1, row=4, columnspan=3)


# open button
open_button = ttk.Button(
    root,
    text="Open Images",
    command=select_file
)

open_button.grid(column=1, row=1)

# show preview button
preview_button = ttk.Button(
    root,
    text="Show Preview",
    command=show_canvas
)

preview_button.grid(column=3, row=1)

# save files to root
save_button = ttk.Button(
    root,
    text="Save to Root",
    command=lambda: save_images(watermarked_images=watermarked_images)
)

save_button.grid(column=2, row=7)

root.mainloop()
