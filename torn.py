from tkinter import *
from tkinter import filedialog
import os


class torn():
    def add_images(self):
        tbd = PhotoImage(file="./tbd100.png")
        self.images = {"rock": PhotoImage(file="./rock100.png"), "paper": PhotoImage(
            file="./paper100.png"), "scissors": PhotoImage(file="./scissors100.png")}
        self.rps_frame = Frame(self.f2)
        self.rps_frame.grid(row=0, column=0)
        self.p1 = Label(self.rps_frame, image=tbd)
        self.p1.grid(row=0, column=0)
        Label(self.rps_frame, text="VS", font=(
            "Comic Sans MS", 20)).grid(row=0, column=1)
        self.p2 = Label(self.rps_frame, image=tbd)
        self.p2.grid(row=0, column=2)

    def add_info(self):
        pass

    def file_select(self):
        direct = filedialog.askopenfilename(title="Select File", filetypes=[
            ("multi rock_paper_scissor", "*.mrps")])
        with open(direct, "r") as file:
            self.data = [line.strip().split(",") for line in file.readlines()]

        for p in self.data:

            player_name = p[0]
            player_moves = p[1:6]
            output = f"{player_name}: plays: {
                player_moves} wins: 0 losses: 0 ties: 0 series_wins: 0"
            # Print each player's details in the format you want
            print(output)
            self.entry_box.config(state="normal")
            self.entry_box.insert(END, output + "\n")
            self.entry_box.config(state="disabled")

    def print_all_playes(self):
        print(f"{self.data[0][0]}: plays: {self.data[0][1:6]} wins: {0} losses: {
            0} ties: {0} series_wins: {0}")
        self.entry_box.config(state="normal")
        self.entry_box.insert(END, f"{self.data[0][0]}: plays: {self.data[0][1:6]} wins: {0} losses: {
            0} ties: {0} series_wins: {0}\n")
        self.entry_box.config(state="disabled")

    def open_folder(self):
        self.rps_files = []
        self.hi = filedialog.askdirectory()
        self.h = os.listdir(self.hi)
        self.players.clear()
        for t in self.h:
            if t.endswith(".rps"):
                file_path = os.path.join(self.hi, t)
                with open(file_path, "r") as file:
                    read = file.readlines()
                    self.data = [line.strip().split(',') for line in read]
                    print(self.data[0][0])
                    self.rps_files.append(self.data[0][0])
                    rpsplayers = [].append(self.data[0])
                    self.print_all_playes()
        self.entry_box.delete(1.0, END)
        self.entry_box.config(state="normal")
        for j in self.rps_files:
            self.entry_box.insert(END, f"{j}\n")
        self.entry_box.config(state="disabled")

    def __init__(self, window):
        self.window = window
        self.players = []
        self.f1 = Frame(self.window)
        self.f1.pack()
        self.subframe1 = Frame(self.f1)
        self.subframe1.grid(row=0, column=0)
        self.f2 = Frame(self.window)
        self.f2.pack()
        self.subframe2 = Frame(self.f1)
        self.subframe2.grid(row=0, column=1)
        Button(self.subframe1, text="Select File", font=(
            "Comic Sans MS", 10), command=self.file_select).grid(row=0, column=0)
        Button(self.subframe1, text="Select Folder", font=(
            "Comic Sans MS", 10), command=self.open_folder).grid(row=1, column=0)
        Button(self.subframe2, text="Run Tournament", font=(
            "Comic Sans MS", 10)).grid(row=0, column=0)
        Label(self.subframe1, font=("Comic Sans MS", 10),
              text="Speed").grid(row=2, column=0)
        Scale(self.subframe2, orient="horizontal").grid(row=1, column=0)
        self.entry_box = Text(self.f2, wrap="word", state="disabled")
        self.entry_box.grid(row=1, column=0)
        self.add_images()
