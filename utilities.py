def determine_winner(player1, player2):
    """ Takes two strings (rock, paper, or scissors) and determines a winner. Returns 1 for player1, -1 for player2, and 0 for tie"""
    if player1 == "paper" and player2 == "rock":
        return 1
    if player1 == "scissors" and player2 == "paper":
        return 1
    if player1 == "rock" and player2 == "scissors":
        return 1
    if player1 == "rock" and player2 == "paper":
        return -1
    if player1 == "paper" and player2 == "scissors":
        return -1
    if player1 == "scissors" and player2 == "rock":
        return -1
    if player1 == "rock" and player2 == "rock":
        return 0
    if player1 == "paper" and player2 == "paper":
        return 0
    if player1 == "scissors" and player2 == "scissors":
        return 0


def convert_to_play(p: str):
    """convert_to_play(p: str) - converts r, p, or s to rock, paper, or scissors """
    l = []
    for i in p:
        if i == "r":
            i = "rock"
            l.append("rock")
        if i == "p":
            i = "paper"
            l.append("paper")
        if i == "s":
            i = "scissors"
            l.append("scissors")
    return l
