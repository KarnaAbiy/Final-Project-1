import tkinter as tk
from tkinter import tkk
from editBar import EditBar
from imageViewer import ImageViewer

class Fp(tk.Tk):
  
  def__init__(self):
    tk.Tk.__init__(self)
    
    self.filename = ""
    self.original_image = None
