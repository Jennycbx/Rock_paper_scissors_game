# from modules.player import Player

class Game():

    def __init__(self):
        self.win_lookup = {
            "scissors" : "paper",
            "paper" : "rock",
            "rock" : "scissors"
        }

 
# Stay with the code and figure out what each line means and how it leads onto the next line.
# The code (self. win_lookup) translates player1's entry into the thing that it beats. If it matches player 2's answer than we know that player1 won because they entered the thing that beat player2's entry. (The code only change's player1's answer within the code - player1 doesn't see this so as far as they're concerned, they still entered the same thing.)


    def play(self, player_1, player_2):
        winner = None
        if self.win_lookup[player_1.choice.lower()] == player_2.choice.lower():
            winner = player_1
        elif self.win_lookup[player_2.choice.lower()] == player_1.choice.lower():
            winner = player_2
        return winner


