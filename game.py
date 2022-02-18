import random


def select_player():
    rating_file = open("rating.txt", "r")

    ratings = rating_file.readlines()
    players = [rating.rstrip("\n").split(" ")[0] for rating in ratings]
    scores = [int(rating.rstrip("\n").split(" ")[1]) for rating in ratings]
    rating_dict = dict(zip(players, scores))
    player_name = input("Enter your name:")

    if player_name in players:
        print("Hello,", player_name)
    else:
        rating_dict[player_name] = 0

    rating_file.close()
    return player_name, rating_dict


def get_user_option(player, rating):
    possibilities = ("scissors", "paper", "rock", "!rating", "!exit")
    computer_option = ""
    while True:
        user_option = input()
        try:
            message = "Invalid input"
            assert user_option in possibilities, message
        except AssertionError as err:
            print(err)
        else:
            if user_option == '!exit':
                print("Bye!")
                exit()
            if user_option == "!rating":
                print(f"Your rating:", rating[player])
                return get_user_option(player, rating)
            if user_option != "!rating":
                computer_option = random.choice(possibilities[:-2])
                break

    return user_option, computer_option


def outcome(user_option, computer_option):
    condition_map = dict(scissors="rock", rock="paper", paper="scissors")
    if user_option == computer_option:
        return "draw"
    elif computer_option == condition_map[user_option]:
        return "lost"
    elif condition_map[computer_option] == user_option:
        return "win"


def battle(player, rating):
    user_choice, computer_choice = get_user_option(player, rating)
    battle_outcome = outcome(user_choice, computer_choice)
    if battle_outcome == "win":
        rating[player] += 100
        print(f"Well done. The computer chose {computer_choice} and failed")
    elif battle_outcome == "lost":
        print(f"Sorry, but the computer chose {computer_choice}")
    elif battle_outcome == "draw":
        rating[player] += 50
        print(f"There is a draw ({user_choice})")
    while True:
        return battle(player, rating)


def main():
    player, rating = select_player()
    battle(player, rating)


if __name__ == "__main__":
    main()
