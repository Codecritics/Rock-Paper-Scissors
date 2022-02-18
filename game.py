import random


def rotate_list(options_list, index):
    result = (options_list[len(options_list) - index:len(options_list)]
              + options_list[0:len(options_list) - index])
    return result


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
    options = input()
    if options != "":
        game_options = options.split(',')
    else:
        game_options = ["rock", "paper", "scissors"]
    return player_name, rating_dict, game_options


def get_user_option(player, rating, game_options):
    computer_option = ""
    while True:
        user_option = input()
        try:
            message = "Invalid input"
            assert user_option in game_options or user_option == "!rating" or user_option == "!exit", message
        except AssertionError as err:
            print(err)
        else:
            if user_option == '!exit':
                print("Bye!")
                exit()
            if user_option == "!rating":
                print(f"Your rating:", rating[player])
                return get_user_option(player, rating, game_options)
            if user_option != "!rating":
                computer_option = random.choice(game_options)
                break

    return user_option, computer_option


def outcome(user_option, computer_option, game_options):
    copy_game_options = game_options.copy()
    index_chosen = copy_game_options.index(user_option)

    copy_game_options = rotate_list(copy_game_options, len(game_options) - index_chosen)
    copy_game_options.remove(user_option)

    middle_index = len(copy_game_options) // 2
    if user_option == computer_option:
        return "draw"
    elif computer_option in copy_game_options[:middle_index]:
        return "lost"
    elif computer_option in copy_game_options[middle_index:]:
        return "win"


def battle(player, rating, game_options):
    user_choice, computer_choice = get_user_option(player, rating, game_options)
    battle_outcome = outcome(user_choice, computer_choice, game_options)
    if battle_outcome == "win":
        rating[player] += 100
        print(f"Well done. The computer chose {computer_choice} and failed")
    elif battle_outcome == "lost":
        print(f"Sorry, but the computer chose {computer_choice}")
    elif battle_outcome == "draw":
        rating[player] += 50
        print(f"There is a draw ({user_choice})")
    while True:
        return battle(player, rating, game_options)


def main():
    player, rating, game_options = select_player()
    print("Okay, let's start")
    battle(player, rating, game_options)


if __name__ == "__main__":
    main()
