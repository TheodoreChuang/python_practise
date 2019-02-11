# Introduction to Python 3 Programming Tutorial - Sentdex
# Basic Tic-Tac-Toe Game
# https://www.youtube.com/watch?v=eXBD2bB9-RA&index=1&list=PLQVvvaa0QuDeAams7fkdcwOGBpGdHpXln

import itertools


def win(current_game):

    def all_same(direction):
        if direction.count(direction[0]) == len(direction) and direction[0] != 0:
            return True
        else:
            return False

    # Horizontal Wins
    for row in game:
        if all_same(row):
            print(f"Player {row[0]} won horizontally!")
            return True

    # Vertical Wins
    for col in range(len(game)):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} won vertically!")
            return True

    # Diagonal Win Descending
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags):
        print(f"Player {diags[0]} won diagonally!")
        return True

    # Diagonal Win Ascending
    diags = []
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags):
        print(f"Player {diags[0]} won diagonally!")
        return True

    return False


# Set Up Board
def game_board(game_map, player=0, row=0, column=0, just_display=False):
    try:
        if game_map[row][column] != 0:
            print("This position has already been played. Choose another")
            return game_map, False
        # print column label
        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
         # print row label and board row
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map, True
    except IndexError as error:
        print("Error: please input 0, 1, or 2", error)
        return game_map, False
    except Exception as error:
        print("Catch all other errors")
        return game_map, False


play = True
players = [1, 2]
while play:
    game = [[0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]]

    game_won = False
    game, played = game_board(game, just_display=True)
    player_choice = itertools.cycle([1, 2])
    while not game_won:
        current_player = next(player_choice)
        print(f"Current Player: {current_player}")
        played = False

        while not played:
            row_choice = int(
                input("What row do you want to play? (0, 1, 2): "))
            column_choice = int(
                input("What column do you want to play? (0, 1, 2): "))
            game, played = game_board(
                game, current_player, row_choice, column_choice)

        if win(game):
            game_won = True
            again = input("Game over. Play again? (y/n) ")
            if again.lower() == "y":
                print("restarting...")
            elif again.lower() == "n":
                print("See you next time.")
                play = False
            else:
                print("Not valid answer, see you next time.")
                play = False
