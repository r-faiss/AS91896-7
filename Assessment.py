from tkinter import *
from tkinter import messagebox
from tkinter import PhotoImage

root = Tk()

score = 0
qnum = 0

root.geometry("7200x7200")

background_image_1 = "homescreen-background.png"
background_image_2 = "Quiz-1-bg.png"


quiz_answers = [
{"question": "What type of briyani is ths",
  "options": ["Kolkata", "Chicken", "Mutton", "Sindhi"],
  "answer": "2"},


{"question": "what is the most well known dish in japan",
  "options": ["Ramen", "Mochi", "Sushi", "Tempura"],
  "answer": "3"},


{"question": "what is the national fruit in India, often used in various dishes",
  "options": ["Pineapple", "Apple", "Mangosteen", "Mango"],
  "answer": "4"},


{"question": "In what country did tiramisu originate",
  "options": ["Japan", "Italy", "South Korea", "Mexico"],
  "answer": "2"},


{"question": "what is the most well known dish in japan",
  "options": ["Ramen", "Mochi", "Sushi", "Tempura"],
  "answer": "3"},


{"question": "True or false: Ceviche is the national dish in Peru",
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


class QuizHomePage:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(self.parent, bg=background_image_1)
        self.frame.pack(fill="both", expand=True)

        button = Button(root, text="Click to Begin!!")
        button.place(x=954, y=736)
        button.config(height="2", width="25", font=("helvetica", 40, "bold"),
                      bg="#e4643a", fg="#ffffff",
                      activebackground="#f67950", activeforeground="#ffffff")

        button = Button(root, text="Need Help ᝰ..ᐣ .ᐣ .ᐣ")
        button.place(x=62, y=930)
        button.config(height="2", width="23", font=("helvetica", 10, "bold"),
                      bg="#e4643a", fg="#ffffff",
                      activebackground="#f67950", activeforeground="#ffffff")

        def start_quiz(self):
           


class QuizPages:
    def __init__(self, parent):
        self.parent = parent
        self.frame = Frame(self.parent)
        self.frame.pack(fill="both", expand=True)

        container = Frame(self.frame)
        container.pack(expand=True, fill="x")


