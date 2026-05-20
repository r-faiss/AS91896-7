import numbers
import tkinter
import tkinter as tk
from tkinter import *


root = Tk()
root.geometry("7200x7200")


#inserting image...
bg = PhotoImage(file = "Images/homescreen-background.png")
def on_resize(event):
   print(F"New size: [{event.width}, {event.height}]")


#canvas create
canvas1 = Canvas(root, width = 600 , height = 600)
canvas1.pack(fill = "both", expand = True)


#image display
canvas1.create_image(0,0 , image = bg, anchor = "nw")


#activate button
def button_clicked():
   print("button")


#button work
button = tkinter.Button(root, text = "Click to Begin")
button.place(x=954, y=736)
button.config( height = "2", width = "25", font=("helvetica", 40, "bold"),
              bg = "#e4643a", fg = "#ffffff",
              activebackground = "#f67950", activeforeground = "#ffffff" )

# Help button work
button = tkinter.Button(root, text = "Need Help?")
button.place(x=62, y=930)
button.config( height = "2", width = "20",
               bg = "#e4643a", fg = "#ffffff",
               activebackground = "#f67950", activeforeground = "#ffffff")



root.mainloop()

