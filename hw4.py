def get_num_xp():
    while True:
        num_xp = input("Enter amount of XP needed to reach desired level: ")
        if num_xp.strip("-").isdigit():
            num_xp = int(num_xp)
            if num_xp < 0:
                print("Please enter a positive number.")
            else:
                break
        else:
            print("Please enter a number.")
    return num_xp


def get_num_earned():
    while True:
        num_earned = input("Enter the amount of XP you earn each game: ")
        if num_earned.strip("-").isdigit():
            num_earned = int(num_earned)
            if num_earned < 0:
                print("Please enter a positive number.")
            else:
                break
        else:
            print("Please enter a number.")
    return num_earned

def main():
    print("----------------------")
    num_xp = get_num_xp()
    num_earned = get_num_earned()
    print("----------------------")
    num_games = num_xp / num_earned
    import math
    num_games = math.ceil(num_games)
    print("You need to play", num_games, "more games to reach your desired level.")
    print("----------------------")

main()