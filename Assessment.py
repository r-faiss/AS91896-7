import tkinter
import tkinter as tk
from tkinter import *

question_answers = [

{"question": "What type of briyani is ths",
   "options": ["Kolkata", "Chicken", "Mutton", "Sindhi"],
   "answer": "2"},

{"question": "what is the most well known dish in japan",
   "options": ["Ramen", "Mochi", "Sushi", "Tempura"],
   "answer": "3"},

{"question": "what is the national fruit in india, often used in various dishes",
   "options": ["Pineapple", "Apple", "Mangosteen", "Mango"],
   "answer": "4"},

{"question": "In what country did tiramisu originate",
   "options": ["Japan", "Italy", "South Korea", "Mexico"],
   "answer": "2"},

{"question": "what is the most well known dish in japan",
   "options": ["Ramen", "Mochi", "Sushi", "Tempura"],
   "answer": "3"},

{"question": "True or false: Ceviche is the national dish in peru",
   "options": ["True", "False"],
   "answer": "1"},

{"question": "The korean food, kimchi, is a what?",
   "options": ["Pickle", "Sausage", "Candy", "Rice"],
   "answer": "1"},

{"question": "True or false: Saganaki, is a Japanese dish.",
   "options": ["True", "False"],
   "answer": "2"},

{"question": "Where did the name ‘Mocha’ originate from?",
   "options": ["Italy", "Yemen", "UAE", "France"],
   "answer": "2"},

{"question": "The Georgian dish, Khinkali, is what",
   "options": ["The national dish", "Pudding", "side dish", "Dumplings"],
   "answer": "4"},
]

current_question = question_answers[0]

def start_quiz():
    start_button.forget()
    #--------------------
    #  Starting screen
    #--------------------

class question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

def answer_quiz():


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
start_button = tkinter.Button(root, text = "Click to Begin!!")
start_button.place(x=950, y=736)
start_button.config( height = "2", width = "25", font=("helvetica", 40, "bold"),
             bg = "#e4643a", fg = "#ffffff",
             activebackground = "#f67950", activeforeground = "#ffffff")


# Help button work
button = tkinter.Button(root, text = "Need Help ᝰ..ᐣ .ᐣ .ᐣ",)
button.place(x=62, y=930)
button.config(height = "2", width = "23", font=("helvetica", 10, "bold"),
              bg="#e4643a", fg="#ffffff",
              activebackground="#f67950", activeforeground="#ffffff")
root.mainloop()
