from flask import render_template, request, redirect
from app import app
from app.modules.player_list import players
from app.modules.game import Game
from app.modules.player import *

@app.route('/')
def welcome():
    return render_template('welcome.html', title='Welcome')

# @app.route("/rps/<choice_1>/<choice_2>")
# def rps(choice_1, choice_2):
#     player_1 = Player("Emma", choice_1)
#     player_2 = Player("Alice", choice_2)
#     game = Game()
#     winner = game.play(player_1, player_2)
#     if winner:
#         return f"The winner is {winner.name} with {winner.choice}!"
#     else:
#         return "It was a draw!"


@app.route("/play")
def index():
    return render_template("index.html", title="Play the Game")

@app.route("/play", methods=["POST"])
def rps():
    player_1_name = request.form["player_1_name"]
    player_2_name = request.form["player_2_name"]
    player_1_choice = request.form["choice_1"]
    player_2_choice = request.form["choice_2"]
    player_1 = Player(player_1_name, player_1_choice)
    player_2 = Player(player_2_name, player_2_choice)
    game = Game()
    winner = game.play(player_1, player_2)
    if winner:
        return render_template("index.html", title="Play the Game", result=f"The winner is {winner.name} with {winner.choice}!")
    else:
        return render_template("index.html", title="Play the Game", result="It was a draw!")
    return redirect("/play")
    




