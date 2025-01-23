import os
from tkinter import *
from utilities import *


class RPSPlayer():
    def __init__(self, name, plays):
        self.name = name
        self.plays = plays
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.series_wins = 0

    def calculate_score(self, player1_play, player2_play) -> int:
        score = 0
        self.p1 = player1_play
        self.p2 = player2_play
        for i in convert_to_play(self.p1):
            for j in convert_to_play(self.p2):
                if determine_winner(i, j) == 1:
                    score += 1
                    self.wins += 1
                    self.series_wins += 1
                if determine_winner(i, j) == 0:
                    score += 0.5
                    self.ties += 1
                    self.series_wins += 0.5
                if determine_winner(i, j) == -1:
                    score -= 1
                    self.losses += 1
                    self.series_wins -= 1
        return score

    def __str__(self):
        try:
            return f"{self.name}: plays: {convert_to_play(self.plays)} wins: {self.wins} losses: {self.losses} ties: {self.ties} series_wins: {self.series_wins}"
        except:
            return "ERROR"


joe_player = RPSPlayer("Joe", "r p s r r")
print(joe_player)
