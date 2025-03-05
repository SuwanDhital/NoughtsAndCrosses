#You will have to import your other module in this module

"""
This module imports necessary functions from the 'noughtsandcrosses' module.

Imported functions:
- welcome: Displays the welcome message and game intro.
- menu: Shows and take the game menu options to the player.
- play_game: Manages the gameplay, handling player and computer moves.
- save_score: Saves player scores to a file.
- load_scores: Loads previous saved scores from a file.
- display_leaderboard: Displays the leaderboard with top player scores.
"""
from noughtsandcrosses_2509490__ import (welcome, menu, play_game,
                                        save_score, load_scores, display_leaderboard)


def main():

    """
    Main function to run the Tic-Tac-Toe game.
    It initializes the board, displays the welcome message, and allows the user to choose between:
    1 - Playing the game
    2 - Saving the current score to a file
    3 - Loading and displaying the leaderboard
    'q' - Quit the program
    """

    #Initializing the board with default values
    board = [ ['1','2','3'],
              ['4','5','6'],
              ['7','8','9']]
    #Display the welcome message and print the initial board
    welcome(board)

    #Initialize the total score
    total_score = 0

    while True:
        #Present the menu and get user choice
        choice = menu()
        if choice == '1':
            #Play the game and update the total score based on the outcome
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)

        if choice == '2':
            #Save the score to the leaderboard file
            save_score(total_score)

        if choice == '3':
            #Load the scores from the file and display the leaderboard
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            #Quit the program with a thank you message
            print("\n----------------------------------------------------------------------")
            print("    Thank you for playing the 'Unbeatable Noughts and Crosses' game....")
            print('                              Good bye!')
            print("----------------------------------------------------------------------\n")
            return

# Program execution begins here
if __name__ == '__main__':
    main()
