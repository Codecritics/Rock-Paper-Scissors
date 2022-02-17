def get_user_option():
    while True:
        option = input()
        if option in ("scissors", "paper", "rock"):
            break
    return option


def find_option_wins_over(option):
    condition_map = dict(scissors="rock", rock="paper", paper="scissors")
    return condition_map[option]


def main():
    user_option = get_user_option()
    winning_user_option = find_option_wins_over(user_option)
    print("Sorry, but the computer chose", winning_user_option)


if __name__ == "__main__":
    main()
