from tkinter import *
from PIL import Image, ImageTk

# ----------------------
# QUIZ BANK
# ----------------------

questions = [
    {"q": "What type of biryani is ths", "options": ["Kolkata", "Chicken", "Mutton", "Sindhi"], "answer": "Chicken"},
    {"q": "what is the most well known dish in japan", "options": ["Ramen", "Mochi", "Sushi", "Tempura"],
     "answer": "Sushi"},
    {"q": "what is the national fruit in India, often used in various dishes",
     "options": ["Pineapple", "Apple", "Mangosteen", "Mango"], "answer": "Mango"},
    {"q": "In what country did tiramisu originate", "options": ["Japan", "Italy", "South Korea", "Mexico"],
     "answer": "Italy"},
    {"q": "what is the most well known dish in japan", "options": ["Ramen", "Mochi", "Sushi", "Tempura"],
     "answer": "Sushi"},
    {"q": "True or false: Ceviche is the national dish in Peru", "options": ["True", "False"], "answer": "True"},
    {"q": "The korean food, kimchi, is a what?", "options": ["Pickle", "Sausage", "Candy", "Rice"], "answer": "Pickle"},
    {"q": "True or false: Saganaki, is a Japanese dish.", "options": ["True", "False"], "answer": "False"},
    {"q": "Where did the name ‘Mocha’ originate from?", "options": ["Italy", "Yemen", "UAE", "France"],
     "answer": "Yemen"},
    {"q": "The Georgian dish, Khinkali, is what", "options": ["The national dish", "Pudding", "side dish", "Dumplings"],
     "answer": "Dumplings"},
]

score = 0
q_index = 0
frames = {}


# ----------------------
# PAGE SETTING FEATURE
# ----------------------

class PageSetting(Frame):

    def set_background(self, image_path):
        try:
            self.original_image = Image.open(image_path)
            self.bg_label = Label(self)
            self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
            self.bind("<Configure>", self.resize_bg)
        except Exception:
            # Fallback background color if image isn't in folder yet
            self.config(bg="#e4643a")

    def resize_bg(self, event):
        if hasattr(self, 'original_image') and event.width > 10 and event.height > 10:
            resized = self.original_image.resize((event.width, event.height))
            self.bg = ImageTk.PhotoImage(resized)
            self.bg_label.config(image=self.bg)
            self.bg_label.image = self.bg


class HomePage(PageSetting):

    def __init__(self, parent):
        super().__init__(parent)
        self.set_background("homescreen-background.png")

        self.button = Button(self, text="Click to Begin!!", command=lambda: show_frame(QuizPage))
        self.button.place(relx=0.5, rely=0.8, anchor="center")
        self.button.config(height="2", width="25", font=("helvetica", 20, "bold"),
                           bg="#e4643a", fg="#ffffff",
                           activebackground="#f67950", activeforeground="#ffffff")


class QuizPage(PageSetting):

    def __init__(self, parent):
        super().__init__(parent)
        self.set_background("quiz-background.png")
        self.answered = False

        self.question_label = Label(self, text="", font=("helvetica", 20, "bold"), fg="#ffffff", bg="#e4643a",
                                    wraplength=600)
        self.question_label.place(relx=0.5, rely=0.15, anchor="center")

        self.selected = StringVar()
        self.options = []

        for i in range(4):
            btn = Radiobutton(self, text="", variable=self.selected, value="", font=("helvetica", 16, "bold"),
                              fg="#ffffff", bg="#e4643a", selectcolor="#e4643a",
                              activebackground="#f67950", activeforeground="#ffffff")
            btn.place(relx=0.3, rely=0.3 + (i * 0.08), relwidth=0.4)
            self.options.append(btn)

        self.feedback_text = Label(self, text="", font=("helvetica", 18, "bold"), fg="#ffffff", bg="#e4643a")
        self.feedback_text.place(relx=0.5, rely=0.68, anchor="center")

        self.next_button = Button(self, text="Submit!", font=("helvetica", 18, "bold"), command=self.next_question)
        self.next_button.place(relx=0.5, rely=0.8, anchor="center")

        self.load_question()

    def load_question(self):
        global q_index

        q_data = questions[q_index]

        self.question_label.config(text=q_data["q"])
        self.selected.set("")
        self.feedback_text.config(text="")
        self.next_button.config(text="Submit!")
        self.answered = False

        for i, option in enumerate(q_data["options"]):
            self.options[i].config(text=option, value=option, state="normal")
            self.options[i].place(relx=0.3, rely=0.3 + (i * 0.08), relwidth=0.4)

        # Hide unused option buttons for questions with fewer choices (e.g. True/False)
        for i in range(len(q_data["options"]), 4):
            self.options[i].place_forget()

    def next_question(self):
        global score, q_index

        if self.answered:
            q_index += 1
            if q_index < len(questions):
                self.load_question()
            else:
                show_frame(ResultPage)
            return

        if self.selected.get() == "":
            self.feedback_text.config(text="Must select an answer!", fg="#ffffff")
            return

        q_data = questions[q_index]

        if self.selected.get() == q_data["answer"]:
            score += 1
            self.feedback_text.config(text="Correct!", fg="#51fc5c")
        else:
            self.feedback_text.config(text=f"Wrong! Answer was: {q_data['answer']}", fg="#fc5151")

        self.answered = True
        self.next_button.config(text="Next Question")


class ResultPage(PageSetting):

    def __init__(self, parent):
        super().__init__(parent)
        self.set_background("Result-page.png")

        self.result_label = Label(self, text="", font=("helvetica", 22, "bold"), fg="#ffffff", bg="#e4643a")
        self.result_label.place(relx=0.5, rely=0.3, anchor="center")

        Button(self, text="Try again", font=("helvetica", 18, "bold"), fg="#ffffff", bg="#e4643a",
               command=self.restart).place(relx=0.4, rely=0.5)
        Button(self, text="Quit", font=("helvetica", 18, "bold"), fg="#ffffff", bg="#e4643a",
               command=root.destroy).place(relx=0.55, rely=0.5)

    def tkraise(self, *args, **kwargs):
        self.result_label.config(text=f"Well done! You got: {score}/{len(questions)}")
        super().tkraise(*args, **kwargs)

    def restart(self):
        global score, q_index
        score = 0
        q_index = 0
        frames[QuizPage].load_question()
        show_frame(HomePage)


def show_frame(page):
    frames[page].tkraise()


# --------------------
# TO GET THINGS STARTED
# --------------------
if __name__ == "__main__":

    root = Tk()
    root.title("Food from parts of the world")

    try:
        root.state("zoomed")
    except Exception:
        root.attributes("-fullscreen", True)

    container = Frame(root)
    container.pack(side="top", fill="both", expand=True)

    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)

    for Page in (HomePage, QuizPage, ResultPage):
        frame = Page(container)
        frames[Page] = frame
        frame.grid(row=0, column=0, sticky="nsew")

    show_frame(HomePage)
    root.mainloop()


        




