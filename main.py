import time
from tkinter import *
import all_type_of_mode


def input_new_words_mode():
    def submit_new_word():
        word_posv = part_of_speech_value.get()
        word_Translate = translate.get()
        word_eng = Vocabulary.get()
        t = time.time()
        tt = time.localtime(t)
        
        if word_Translate == "" or word_eng == "":
            the_word_has_been_added.config(text = "One of entry is empty! Please try again")
        else:
            with open("vocabularies.dat", "a", encoding= "utf-8") as File:
                File.write(f"Vocabulary_ADDED = {word_eng}, Translate = {word_Translate}, POSV = {word_posv}, Date = {tt.tm_year}/{tt.tm_mon}/{tt.tm_mday} \n")
            the_word_has_been_added.config(text = (f"Vocabulary = {word_eng}, Translate = {word_Translate}, POSV = {word_posv}, Date = {tt.tm_year}/{tt.tm_mon}/{tt.tm_mday} \n"))
            the_word_has_been_added.pack()

    input_new_words_win = Toplevel(mainwin)

    input_new_words_win.geometry(f"{700}x{370}+{left - (WINDOWS_WIDTH // 2) -400}+{top - (WINDOWS_HEIGHT// 2)}")
    input_new_words_win.title("Input New Vocabularies")
    input_new_words_win.config(background = "#333333")

    input_new_words_win_title = Label(input_new_words_win, text = "Input New Vocabularies\n Word:", font = "arial 20", bg = "#333333",fg = "white")
    input_new_words_win_title.pack()
    Vocabulary = Entry(input_new_words_win, font = "arial 20")
    Vocabulary.pack()

    translate_label = Label(input_new_words_win, text = "Translate:", font = "arial 20", bg = "#333333",fg = "white")
    translate_label.pack()
    
    translate = Entry(input_new_words_win, font = "arial 20")
    translate.pack()

    part_of_speech = Label(input_new_words_win, text = "Part of speech:", font = "arial 20", bg = "#333333",fg = "white")
    part_of_speech.pack()

    part_of_speech_value = StringVar()
    part_of_speech_value.set("Noun")

    part_of_speech_menu = OptionMenu(input_new_words_win, part_of_speech_value, "Noun", "Pronoun", "Verb", "Adjective", "Adverb", "Preposition", "Conjunction", "Interjection")
    part_of_speech_menu.pack()

    submit = Button(input_new_words_win, text = "Submit", font = "arial 15", command =submit_new_word)
    submit.pack()

    the_word_has_been_added = Label(input_new_words_win, text = "" ,font = "arial 15", bg = "#333333",fg = "white")
    
        

def qquit():
    quit()

english_part_of_speech_list = ["Noun", "Pronoun", "Verb", "Adjective", "Adverb", "Preposition", "Conjunction", "Interjection"]

with open("vocabularies.dat", encoding= "utf-8") as words:
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

Study_by_curve = Button(text = "Study By The Curve", font = "arial 25")
Study_by_curve.pack()

read_all_vocabularies_from_past = Button(text = "Read All Vocabularies From Past", font = "arial 25")
read_all_vocabularies_from_past.pack()

quiz = Button(text = "Quiz", font = "arial 25",command=qquit)
quiz.pack()
    
mainwin.mainloop()