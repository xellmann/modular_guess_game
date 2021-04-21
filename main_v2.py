import random
from functions import *

secret = random.randint(1, 30)
attempts = 0

with open("score_list.json", "r") as score_file:
    score_list = json.loads(score_file.read())

while True:
    game_decision = input("To play the guess game press 'A', to watch the best scores press 'B', "
                          "to quit the game press 'C'")
    if game_decision == "A":
        difficulty_level = input("To play difficulty level hard press 'A', to play difficulty level easy press 'B'")
        while True:

            play_guess_game()
            break
    elif game_decision == "B":
        get_high_score()
    else:
        break
