# players pseudocode
# Rank  Player  Wins    Losses  Ties
# ====  ======  ====    ======  ====
#   1   Dave    50      10      0
#   2   Bob     47      11      2
#   3   Alexa   39      17      4
players = {
    "Dave": {
        "Wins": 50,
        "Losses": 10,
        "Ties": 0
        },
    "Bob": {
        "Wins": 50,
        "Losses": 10,
        "Ties": 0
        },
    "Alexa": {
        "Wins": 39,
        "Losses": 17,
        "Ties": 4
    } 
}

def player_prompt():
    message = "\nALL PLAYERS:\n"
    message += "============\n"
    names = list(players.keys())
    names.sort()
    for player in names:
        message += player + "\n"
    message +="\nEnter a player name: "
    return message;

def main():
    print("Game Stats App")
    choice = "y"
    while choice != "n":
        player_name = input(player_prompt())
        display_player_summary(player_name)
        choice = input("Continue? (y/n): ")
    print("Bye")

def display_player_summary(player_name):
    if player_name in players:
        stats = players.get(player_name)
        print(f"Wins:    {stats['Wins']}")
        print(f"Losses:  {stats['Losses']}")
        print(f"Ties:    {stats['Ties']}")
        print()
    else:
        print(f"There's no player named '{player_name}'.")
if __name__ == "__main__":
    main()

