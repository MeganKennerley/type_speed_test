from tkinter import *
import random

SECONDS = 60

root = Tk()
root.title("Type Speed Test")
root.geometry('600x600')
root.config(pady=70, padx=50)


def copy_text():
    texts = [
        "A 100 word paragraph typically refers to a paragraph that contains exactly 100 words. These paragraphs are "
        "often used in writing challenges or assignments where the writer must convey their thoughts or ideas within a "
        "strict word limit. Writing a 100-word paragraph requires concise and effective communication, as every word "
        "counts. It is a useful exercise in practicing brevity and ensuring that one's message is clear and impactful. "
        "Writers must carefully choose their words and structure their sentences to convey their intended meaning "
        "while adhering to the predetermined word count.",
        "It challenges writers to convey their message or ideas in a limited space, requiring them to carefully choose "
        "their words and create maximum impact with minimal text. A well-written 100-word paragraph can be both "
        "informative and engaging, capturing the reader's attention and delivering key points efficiently. Whether "
        "used in creative writing, journalism, or academic essays, a 100-word paragraph demonstrates the writer's "
        "ability to convey their thoughts effectively in a brief and compelling manner."
    ]
    text = random.choice(texts)
    text_box = Text(width=50, height=20)
    text_box.insert(INSERT, text)
    text_box.grid(column=1, row=1)


def go():
    global SECONDS
    countdown(SECONDS)


def countdown(count):
    count_label = Label(text=f"{count}")
    count_label.config(font="Helvetica 40")
    count_label.grid(column=1, row=4)
    if count > 9:
        count_label.config(fg="blue")
        root.after(1000, countdown, count-1)
    elif 0 < count < 10:
        count_label.config(fg="red", font="Helvetica 50")
        root.after(1000, countdown, count - 1)
    else:
        entry_text = entry.get()
        entry_list = entry_text.split()
        length_of_list = len(entry_list)
        Label(text=f"{length_of_list} words in 60 seconds!").grid(column=1, row=5)


text_button = Button(text="Generate Text", command=copy_text, highlightbackground="blue", fg="white",
                     highlightthickness=0, width=10, height=1, padx=10, pady=10)
text_button.grid(column=1, row=0, pady=10)

go_button = Button(text="Go!", command=go, highlightbackground="green", fg="white", highlightthickness=0,
                   width=10, height=1, padx=10, pady=10)
go_button.grid(column=1, row=2, pady=10)
entry = Entry()
entry.grid(column=1, row=3)
entry.config(width=55)

root.mainloop()
