from tkinter import *
class PhotoEd:
  def __init__(self):
    self.root = Tk()
    self.init()
    
  def init(self):
    self.root.title("Photo Editor")
    self.root.iconbitmap()
    
    self.root.bind("<Escape>", self._close)
  
  def run(self):
    self.draw_menu()
    self.draw_widgets()
    
    self.root.mainloop()
    
    def draw_menu(self):
      pass
    
    def draw_widgets(self):
      pass
   
    def close(self):
      self.root.quit()
      
if __name__  == "__main__":
  PhotoEd().run
      
      
