import json


def get_high_score():
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
    prihisco = print("Top scores: " + str(score_list))
    return prihisco


def play_guess_game(difficulty):
    import datetime
    import json
    import random
    secret = random.randint(1, 30)
    attempts = 0
    with open("score_list.json", "r") as score_file:
        score_list = json.loads(score_file.read())
    while True:
        guess = int(input("Guess the secret number (between 1 and 30): "))
        attempts += 1

        if guess == secret:
            score_list.append({"attempts": attempts, "date": str(datetime.datetime.now())})
            with open("score_list.json", "w") as score_file:
                score_file.write(json.dumps(score_list))

            print("You've guessed it - congratulations! It's number " + str(secret))
            print("Attempts needed: " + str(attempts))
            break
        elif guess > secret and difficulty == "B":
            print("Your guess is not correct... try something smaller")
        elif guess < secret and difficulty == "B":
            print("Your guess is not correct... try something bigger")


def game_decision():
    decision = input("To play the guess game press 'A', to watch the best scores press 'B', "
            "to quit the game press 'C'")
    return decision
