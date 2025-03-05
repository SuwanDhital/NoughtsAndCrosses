"""
These module handles the generation of random numbers, JSON file
for a Tic-Tac-Toe game.

Dependencies:
- random: Its used to generate random moves.
- json: Its used to read and write leaderboard data to and from a file in JSON format.

"""
import random
import json
random.seed()


def draw_board(board):
    """
    Draws the Tic-Tac-Toe game board.
    
    Args:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.
    """
    # develop code to draw the board
    print("\n                           |-----------------|")
    print(f"                           |  {board[0][0]}  |  {board[0][1]}  |  {board[0][2]}  |")
    print("                           |-----------------|")
    print(f"                           |  {board[1][0]}  |  {board[1][1]}  |  {board[1][2]}  |")
    print("                           |-----------------|")
    print(f"                           |  {board[2][0]}  |  {board[2][1]}  |  {board[2][2]}  |")
    print("                           |-----------------|")

def welcome(board):
    """
    Prints the welcome message and the initial game board.
    
    Args:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.
    """
    # prints the welcome message
    print("\n\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
    print("======================================================================")
    print("                        Welcome to TIC-TAC-TOE game")
    print("                         Developed by Suwan Dhital")
    print("======================================================================\n")
    print("                             Layout Structure")

    # display the board by calling draw_board(board)
    draw_board(board)

def initialise_board(board):
    """
    Initializes the Tic-Tac-Toe board by setting all cells empty.
    
    Args:
        board (list): A 3x3 list having the Tic-Tac-Toe board data.
    
    Returns:
        list: A 3x3 list with all cells set to ' '.
    """
    # develop code to set all elements of the board to one space ' '
    for i in range(len(board)):
        for j in range(len(board[i])):
            board[i][j] = ' '
    return board

def get_player_move(board):
    """
    Asks the player to choose a square (1-9) and returns choosen row and column.
    
    Args:
        board (list): A 3x3 list representing the Tic-Tac-Toe board.
    
    Returns:
        tuple: The row and column where the player wants to choose their box.
    """
    # develop code to ask the user for the cell to put the X in,
    # and return row and col
    while True:
        try:
            print("\n                                              1 2 3")
            print("                                              4 5 6")
            print("                                              7 8 9")
            square = int(input('Choose Your Square reference to this position=======>'))
            match square:
                case 1:
                    row, col = 0, 0
                case 2:
                    row, col = 0, 1
                case 3:
                    row, col = 0, 2
                case 4:
                    row, col = 1, 0
                case 5:
                    row, col = 1, 1
                case 6:
                    row, col = 1, 2
                case 7:
                    row, col = 2, 0
                case 8:
                    row, col = 2, 1
                case 9:
                    row, col = 2, 2
                case _:
                    print("\n===================================================================")
                    print("[Invalid Input] ==> Please re-enter your choice..")
                    print("===================================================================\n")
                    continue

            if board[row][col] == ' ':
                return row, col

            print("\n======================================================================")
            print("[Already Occupied] ==> Please re-enter your choice..")
            print("======================================================================\n")


        except ValueError:
            print("\n======================================================================")
            print("[Invalid Row and Column] ==> Row and Column should be numerical value..")
            print("======================================================================\n")
            continue

def choose_computer_move(board):
    """
    Chooses a random square for the computer to place its '◯' mark 
    and returns the random row and column.
    
    Args:
        board (list): A 3x3 list having the Tic-Tac-Toe board data.
    
    Returns:
        tuple: The row and column where the computer wants to choose its selection.
    """
    # develop code to let the computer chose a cell to put a nought in
    # and return row and col
    while True:
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if 0 <= row <3 and 0<=col<3:
            if board[row][col] == ' ':
                return row, col


def check_for_win(board, mark):
    """
    Checks if player or computer has winned by matching three of their marks in
    a row, column, or diagonal.
    
    Args:
        board (list): A 3x3 list having Tic-Tac-Toe board data.
        mark (str): mark stores '✕' or '◯' to check for win.
    
    Returns:
        bool: True if the player or computer has won, False otherwise.
    """
    # develop code to check if either the player or the computer has won
    # return True if someone won, False otherwise
    for i in range(0,3):
        if (board[i][0] == board[i][1] == board[i][2] !=' '
            or board[0][i] == board[1][i] == board[2][i] !=' '
            or  board[0][0] == board[1][1] == board[2][2] !=' '
            or board[0][2] == board[1][1] == board[2][0] !=' '):

            if mark in ('✕','◯'):
                return True
    return False

def check_for_draw(board):
    """
    Checks if the game is a draw by checking if all cells are occupied.
    
    Args:
        board (list): A 3x3 list having the Tic-Tac-Toe board data.
    
    Returns:
        bool: True if game is a draw, False otherwise.
    """
    # develop cope to check if all cells are occupied
    # return True if it is, False otherwise
    count=0
    for i in range(0,3):
        for j in range(0,3):
            if board[i][j] != ' ':
                count +=1
                if count==9:
                    return True
    return False

def play_game(board):
    """
    The main game loop where the player and computer make moves
    and checks for a win or draw after every move.
    
    Args:
        board (list): A 3x3 list having the Tic-Tac-Toe board data.
    
    Returns:
        int: 1 if player wins, -1 if computer wins, 0 if it's draw.
    """
    # develop code to play the game
    # star with a call to the initialise_board(board) function to set
    # the board cells to all single spaces ' '
    board_data = initialise_board(board)

    # then draw the board
    draw_board(board_data)

    # then in a loop, get the player move, update and draw the board
    while True:
        user_row,user_col = get_player_move(board_data)
        board_data[user_row][user_col] ='✕'
        draw_board(board_data)

        # check if the player has won by calling check_for_win(board, mark),
        # if so, return 1 for the score
        if check_for_win(board_data,'✕') is True:
            print("\n----------------------------------------------------------------------")
            print("                 Congratulations! You winned the game...")
            print("----------------------------------------------------------------------\n")
            return 1

        # if not check for a draw by calling check_for_draw(board)
        # if drawn, return 0 for the score
        if check_for_draw(board_data) is True:
            print("\n----------------------------------------------------------------------")
            print("                 Great! You have challanged the Computer...")
            print("----------------------------------------------------------------------\n")
            return 0

        # if not, then call choose_computer_move(board)
        # to choose a move for the computer
        computer_row, computer_col = choose_computer_move(board_data)

        # update and draw the board
        board_data[computer_row][computer_col] = '◯'
        draw_board(board_data)

        # check if the computer has won by calling check_for_win(board, mark),
        # if so, return -1 for the score
        if check_for_win(board_data, '◯') is True:
            print("\n----------------------------------------------------------------------")
            print("         Sorry to say! You have loose the game, Please try again...")
            print("----------------------------------------------------------------------\n")
            return -1

        # if not check for a draw by calling check_for_draw(board)
        # if drawn, return 0 for the score
        if check_for_draw(board_data) is True:
            return 0

        #repeat the loop

def menu():
    """
    Displays the main menu and ask the user to make a choice.
    
    Returns:
        str: The user's choice ('1', '2', '3', or 'q').
    """
    # get user input of either '1', '2', '3' or 'q'
    # 1 - Play the game
    # 2 - Save score in file 'leaderboard.txt'
    # 3 - Load and display the scores from the 'leaderboard.txt'
    # q - End the program
    while True:
        print("\n\n======================================================================")
        print("Please enter the number as per the given task:\n")
        print(" 1 - Play the game")
        print(" 2 - Save score in file 'leaderboard.txt'")
        print(" 3 - Load and display the scores from the 'leaderboard.txt'")
        print(" q - End the program")
        print("======================================================================\n")
        choice = str.strip(str.lower(input("\nEnter your choice ==> ")))
        if choice in ['1', '2', '3', 'q']:
            return choice
        print("\n----------------------------------------------------------------------")
        print("                    Invalid choice. Please try again.")
        print("----------------------------------------------------------------------\n")

def load_scores():
    """
    Loads leaderboard scores from file 'leaderboard.txt'.
    
    Returns:
        dict: A dictionary with keys and values.
    """
    # develop code to load the leaderboard scores
    # from the file 'leaderboard.txt'
    # return the scores in a Python dictionary
    # with the player names as key and the scores as values
    try:
        with open('leaderboard.txt', 'r',encoding="utf-8") as file:
            file_data = file.read()
            leaders = json.loads(file_data)

        # return the dictionary in leaders
        return leaders
    except FileNotFoundError:
        print("\n----------------------------------------------------------------------")
        print("                      File can't be found")
        print("----------------------------------------------------------------------\n")
    return leaders

def save_score(score):
    """
    Ask player to enter name and saves score to the 'leaderboard.txt' file.
    
    Args:
        score (int): The score to save.
    """
    # develop code to ask the player for their name
    while True:
        name = input("Enter your name:")
        if name not in ('', ' '):
            score = int(score)
            leaders = load_scores()
            leaders[name] = score
            # and then save the current score to the file 'leaderboard.txt'
            with open('leaderboard.txt', 'w',encoding="utf-8") as file:
                json.dump(leaders, file)
                break


def display_leaderboard(leaders):
    """
    Displays the leaderboard sorted by score.
    
    Args:
        leaders (dict): A dictionary with keys and values.
    """
    # develop code to display the leaderboard scores
    # passed in the Python dictionary parameter leader
    if not leaders:
        print("\n----------------------------------------------------------------------")
        print("                    Scores Aren't Available ")
        print("----------------------------------------------------------------------\n")
        return

    sorted_leaders = []
    for name, score in leaders.items():
        inserted = False
        for i in range(len(sorted_leaders)):
            if score > sorted_leaders[i][1]:
                sorted_leaders.insert(i, (name, score))
                inserted = True
                break
        if not inserted:
            sorted_leaders.append((name, score))
    print("\n         =========================================================")
    print("         |                        LEADERBOARD                    |")
    print("         |=======================================================|")
    print("         |       Rank    |          Name            |   Score    |")
    print("         |-------------------------------------------------------|")
    rank = 1
    for leader in sorted_leaders:
        name, score = leader
        print(f"         |         {rank:<5} |      {name:<15}     | {score:>5}      |")
        rank += 1
    print("         =========================================================")
