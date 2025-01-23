from tkinter import *
from tkinter import filedialog
import os


class torn():
    def file_select(self):
        direct = filedialog.askopenfile(filetypes=("Multi Rock Paper Scissor (.mrps)", "*.mrps")))
            def print_all_playes(self):
            print(f"{self.data[0][0]}: plays: {self.data[0][1:6]} wins: {0} losses: {
                0} ties: {0} series_wins: {0}")
            self.entry_box.config(state="normal")
            self.entry_box.insert(END, f"{self.data[0][0]}: plays: {self.data[0][1:6]} wins: {0} losses: {
                0} ties: {0} series_wins: {0}\n")
            self.entry_box.config(state="disabled")

            def open_folder(self):
            self.rps_files= []
            self.hi= filedialog.askdirectory()
            self.h= os.listdir(self.hi)
            self.players.clear()
            for t in self.h:
            if t.endswith(".rps"):
                file_path = os.path.join(self.hi, t)
                with open(file_path, "r") as file:
                    read = file.readlines()
                    self.data = [line.strip().split(',') for line in read]
                    self.rps_files.append(self.data[0][0])
                    rpsplayers = [].append(self.data[0])
                    self.print_all_playes()
            self.entry_box.delete(1.0, END)
            self.entry_box.config(state="normal")
            for j in self.rps_files:
            self.entry_box.insert(END, f"{j}\n")
            self.entry_box.config(state="disabled")

            def __init__(self, window):
            self.window= window
            self.players= []
            f1= Frame(self.window)
            f1.pack()
            subframe1= Frame(f1)
            subframe1.grid(row=0, column=0)
            f2= Frame(self.window)
            f2.pack()
            subframe2= Frame(f1)
            subframe2.grid(row=0, column=1)
            Button(subframe1, text="Select File", font=("Comic Sans MS", 10), command=)
            Button(subframe1, text="Select Folder", font=(
                "Comic Sans MS", 10), command=self.open_folder).grid(row=1, column=0)
            Button(subframe2, text="Run Tournament", font=(
                "Comic Sans MS", 10)).grid(row=0, column=0)
            Label(subframe1, font=("Comic Sans MS", 10),
          text = "Speed").grid(row=2, column=0)
           Scale(subframe2, orient="horizontal").grid(row=1, column=0)
           self.entry_box = Text(f2, wrap="word", state="disabled")
           self.entry_box.grid(row=0, column=0)

           # def get_play(self):
            #    for item in self.h:
           #        file_path = os.path.join(self.hi, item)
                  #        if os.path.isfile(file_path):
                  #            with open(file_path, "r") as fil:
                  #                cont = fil.read()
                  #                print(cont)
                  #
                  # def help_me(self):
                  #    self.open_folder()
                  #    self.get_play()


                  # if __name__ == "__main__":
                  #    window = Tk()
                  #    h = torn(window=window)
                  #    h.help_me()
