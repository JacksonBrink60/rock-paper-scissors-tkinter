from tkinter import *
import random
import torn as to
wins = 0
losses = 0
ties = 0
window = Tk()
window.geometry("400x400")
window.grid_columnconfigure(0, weight=1)
window.title("Rock, Paper, Scissors")
menubar = Menu(window)
window.config(menu=menubar)


def tornment():
    new_win = Toplevel()
    win = to.torn(new_win)


filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Options", menu=filemenu)
filemenu.add_command(label="Tournament Mode", command=tornment)


def reset():
    rps.set(NONE)
    player_choice.config(image=tbd)
    computer_choice.config(image=tbd)
    win.config(text="Wins: 0")
    loss.config(text="Losses: 0")
    tie.config(text="Ties: 0")


def pla():
    global wins
    global losses
    global ties
    comp = random.randint(0, 2)
    if comp == 0:
        choice1 = rock
    elif comp == 1:
        choice1 = paper
    elif comp == 2:
        choice1 = scissors
    computer_choice.config(image=choice1)
    if rps.get() == "Rock" and comp == 2:
        wins += 1
        win.config(text=f"Wins: {wins}")
    elif rps.get() == "Rock" and comp == 1:
        losses += 1
        loss.config(text=f"Losses: {losses}")
    elif rps.get() == "Rock" and comp == 0:
        ties += 1
        tie.config(text=f"Ties: {ties}")
    elif rps.get() == "Paper" and comp == 0:
        wins += 1
        win.config(text=f"Wins: {wins}")
    elif rps.get() == "Paper" and comp == 2:
        losses += 1
        loss.config(text=f"Losses: {losses}")
    elif rps.get() == "Paper" and comp == 1:
        ties += 1
        tie.config(text=f"Ties: {ties}")
    elif rps.get() == "Scissors" and comp == 1:
        wins += 1
        win.config(text=f"Wins: {wins}")
    elif rps.get() == "Scissors" and comp == 0:
        losses += 1
        loss.config(text=f"Losses: {losses}")
    elif rps.get() == "Scissors" and comp == 2:
        ties += 1
        tie.config(text=f"Ties: {ties}")


def ha():
    if rps.get() == "Rock":
        choice = rock
    elif rps.get() == "Paper":
        choice = paper
    elif rps.get() == "Scissors":
        choice = scissors
    player_choice.config(image=choice)


f1 = Frame(window)
f1.grid(column=0, row=0)
f2 = Frame(window)
f2.grid(column=0, row=1)
f3 = Frame(window)
f3.grid(column=0, row=2)
f4 = Frame(window)
f4.grid(column=0, row=3)
f5 = Frame(window)
f5.grid(column=0, row=4)
rps = StringVar(value=NONE)

Radiobutton(f1, text="Rock", variable=rps,
            value="Rock", command=ha).grid(row=0, column=0)
Radiobutton(f1, text="Paper", variable=rps,
            value="Paper", command=ha).grid(row=0, column=1)
Radiobutton(f1, text="Scissors", variable=rps,
            value="Scissors", command=ha).grid(row=0, column=2)

rock = PhotoImage(file="./rock100.png")
paper = PhotoImage(file="./paper100.png")
scissors = PhotoImage(file="./scissors100.png")
tbd = PhotoImage(file="./tbd100.png")


player_choice = Label(f2, image=tbd, bg="white")
player_choice.grid(row=0, column=0)
Label(f2, text="VS", font=("Comic Sans MS", 20)).grid(row=0, column=1)
computer_choice = Label(f2, image=tbd, bg="white")
computer_choice.grid(row=0, column=2)

Label(f3, text="Make Your Move!", font=(
    "Comic Sans MS", 15, "bold")).grid(row=0, column=0)

win = Label(f4, font=("Comic Sans MS", 15), text="Wins: 0")
win.grid(row=0, column=0)
loss = Label(f4, font=("Comic Sans MS", 15), text="Losses: 0")
loss.grid(row=0, column=1)
tie = Label(f4, font=("Comic Sans MS", 15), text="Ties: 0")
tie.grid(row=0, column=2)

play = Button(f5, font=("Comic Sans MS", 10), text="Play", command=pla)
play.grid(row=0, column=0, padx=10)
Button(f5, font=("Comic Sans MS", 10), text="Reset Scores",
       command=reset).grid(row=0, column=1)

window.mainloop()
