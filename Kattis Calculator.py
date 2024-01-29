import tkinter
from tkinter import *
win = Tk()
win.geometry("462x272")
win.title("Kattis Calculator")
def calculate():
    # Getting the inputs and variables we want to use.
    them = float(their_entry.get())
    you = float(your_entry.get())
    difference = them - you
    
    # The problem point estimations.
    one_four_calc = str(round(difference / 1.4))
    one_four_text.config(text = "You need to solve " + one_four_calc + " more 1.4 rated problems to achieve your competitions score.")
    one_five_calc = str(round(difference / 1.5))
    one_five_text.config(text = "You need to solve " + one_five_calc + " more 1.5 rated problems to achieve your competitions score.")
    one_six_calc = str(round(difference / 1.6))
    one_six_text.config(text = "You need to solve " + one_six_calc + " more 1.6 rated problems to achieve your competitions score.")

    # Your solved and their Solved
    your_calc = str(round(you / 1.6))
    your_solved.config(text = "You have likely solved " + your_calc + " 1.6 rated Kattis problems so far.")
    their_calc = str(round(them/1.6))
    their_solved.config(text = "They have likely solved " + their_calc + " 1.6 rated Kattis problems so far.")

    # Percent complete
    percent = str(round((you / them) * 100))
    complete_percent.config(text = "You are " + percent + "% Complete.")

# Text and Inputs
their_text = Label(win, text = "Please type your competitions score.")
their_text.pack()
their_entry = Entry(win)
their_entry.pack()
your_text = Label(win, text = "Please type your current score.")
your_text.pack()
your_entry = Entry(win)
your_entry.pack()
# Calculate Box
Button(win, text = "Calculate",command = calculate).pack()

# Empty Text Boxes for after calculation
one_four_text = Label(win, text = "")
one_four_text.pack()
one_five_text = Label(win, text = "")
one_five_text.pack()
one_six_text = Label(win, text = "")
one_six_text.pack()
blank = Label(win, text = "")
blank.pack()
your_solved = Label(win, text = "")
your_solved.pack()
their_solved = Label(win, text = "")
their_solved.pack()
blank.pack()
complete_percent = Label(win, text = "")
complete_percent.pack()

win.mainloop()