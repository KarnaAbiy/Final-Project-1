from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfilename, asksaveasfilename
from PIL import Image, ImageTk, ImageFilter, ImageEnhance, ImageOps
import os

root = Tk()
root.title("Photo editor")
root.geometry("640x640")
root.iconbitmap("D:/projects/images/Ala-Too_Icon.png")

def selected():
    global img_path, img
    img_path = filedialog.askopenfilename(initialdir=os.getcwd())
    img.thumbnail((350,350))

    img1 = ImageTk.PhotoImage(img)
    canvas2.create_image(300, 210, image=img1)
    canvas2.image=img1
def blur(event):
    global img_path, img1, imgg
    for m in range (0, v1.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350,350))
            imgg = img.filter(ImageFilter.BoxBlur(m))
            img1 = ImageTk.PhotoImage(imgg)
            canvas2.create_image(300, 210, image=img1)
            canvas2.image=img1
def brightness(event):
    global img_path, img2, img3
    for m in range(0, v2.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Brightness(img)
            img2 = imgg.enhance(m)
            img3 = ImageTk.PhotoImage(img2)
            canvas2.create_image(300, 210, image=img3)
            canvas2.image=img3
def contrast(event):
    global img_path, img4, img5
    for m in range(0, v3.get()+1):
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Contrast(img)
            img4 = imgg.enhance(m)
            img5 = ImageTk.PhotoImage(img4)
            canvas2.create_image(300, 210, image=img5)
            canvas2.image=img5
def rotate_image(event):
    global img_path, img6, img7
            img = Image.open(img_path)
            img.thumbnail((350, 350))
            imgg = ImageEnhance.Brightness(img)
            img6 = imgg.enhance(m)
            img7 = ImageTk.PhotoImage(img6)
            canvas2.create_image(300, 210, image=img7)
            canvas2.image=img7
