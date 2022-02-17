import random


def get_user_option():
    possibilities = ("scissors", "paper", "rock", "!exit")
    computer_option = ""
    while True:
        user_option = input()
        try:
            message = "Invalid input"
            assert user_option in possibilities, message
        except AssertionError as err:
            print(err)
        else:
            if user_option != "!exit":
                computer_option = random.choice(possibilities[:-1])
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


def main():
    user_choice, computer_choice = get_user_option()
    while user_choice != "!exit":
        battle_outcome = outcome(user_choice, computer_choice)
        if battle_outcome == "win":
            print(f"Well done. The computer chose {computer_choice} and failed")
        elif battle_outcome == "lost":
            print(f"Sorry, but the computer chose {computer_choice}")
        elif battle_outcome == "draw":
            print(f"There is a draw ({user_choice})")
        return main()
    else:
        print("Bye!")


if __name__ == "__main__":
    main()
