import time
from tkinter import *
import all_type_of_mode

def input_new_words_mode(*e):
    input_new_words_win = Tk()

    input_new_words_win.geometry(f"{450}x{300}+{left - (WINDOWS_WIDTH // 2) -300}+{top - (WINDOWS_HEIGHT// 2)}")
    input_new_words_win.title("Input New Vocabularies")
    input_new_words_win.config(background = "#333333")

    input_new_words_win_title = Label(input_new_words_win, text = "Input New Vocabularies\n word:", font = "arial 20", bg = "#333333",fg = "white")
    input_new_words_win_title.pack()
    Vocabulary = Entry(input_new_words_win, font = "arial 20")
    Vocabulary.pack()

    translate_label = Label(input_new_words_win, text = "translate:", font = "arial 20", bg = "#333333",fg = "white")
    translate_label.pack()
    
    translate = Entry(input_new_words_win, font = "arial 20")
    translate.pack()

    part_of_speech = Label(input_new_words_win, text = "part_of_speech:", font = "arial 20", bg = "#333333",fg = "white")
    part_of_speech.pack()

    part_of_speech_value = StringVar()
    part_of_speech_value.set(english_part_of_speech_list[0])
    part_of_speech_value.trace('w', input_new_words_mode) # need to fix

    part_of_speech_menu = OptionMenu(input_new_words_win, part_of_speech_value, *english_part_of_speech_list)
    part_of_speech_menu.config(width=10, fg='white')
    part_of_speech_menu.pack()

english_part_of_speech_list = ["Noun", "Pronoun", "Verb", "Adjective", "Adverb", "Preposition", "Conjunction", "Interjection"]

with open("vocabularies.dat") as words:
    content = words.read()

mainwin = Tk()
left = (mainwin.winfo_screenwidth()//2)
top = (mainwin.winfo_screenheight()//2)
WINDOWS_WIDTH = 650
WINDOWS_HEIGHT = 600

mainwin.geometry(f"{WINDOWS_WIDTH}x{400}+{left - (WINDOWS_WIDTH // 2)}+{top - (WINDOWS_HEIGHT// 2)}")
mainwin.title("English Review")
mainwin.resizable(False,False)
mainwin.config(background = "#333333")

input_new_words = Button(text = "Input New Vocabularies", font = "arial 25",command= input_new_words_mode)
input_new_words.pack()

Study_by_curve = Button(text = "Study By Curve", font = "arial 25")
Study_by_curve.pack()

read_all_vocabularies_from_past = Button(text = "Read All Vocabularies From Past", font = "arial 25")
read_all_vocabularies_from_past.pack()

quiz = Button(text = "Quiz", font = "arial 25")
quiz.pack()


mainwin.mainloop()