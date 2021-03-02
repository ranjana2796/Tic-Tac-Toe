board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

temp = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]


def new_board(t):
    return t.copy()


current_player = 'X'
gameisgoing = True
winner = None

print("{} WELCOME TO TIC-TAC-TOE GAME {}".format("*" * 3, "*" * 3))
print("\t\t Positions")
print("\t\t 0", "|", "1", "|", "2",
      "\n\t\t 3", "|", "4", "|", "5",
      "\n\t\t 6", "|", "7", "|", "8")

print()


def display_board():
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])


def handle_turn():
    position = int(input("Choose a random position form [0 to 8]: "))
    board[position] = current_player


def swap_players():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


def check_winner():
    global winner
    row_winner = check_row()
    col_winner = check_column()
    dia_winner = check_diagonal()
    check_tie()

    if row_winner:
        winner = row_winner

    elif col_winner:
        winner = col_winner

    else:
        winner = dia_winner



def check_row():
    global gameisgoing
    row1 = board[0] == board[1] == board[2] != "-"
    row2 = board[3] == board[4] == board[5] != "-"
    row3 = board[6] == board[7] == board[8] != "-"

    if row1 or row2 or row3:
        gameisgoing = False

    if row1:
        return board[0]

    elif row2:
        return board[3]

    elif row3:
        return board[6]


def check_column():
    global gameisgoing
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        gameisgoing = False

    if col1:
        return board[0]

    elif col2:
        return board[1]

    elif col3:
        return board[2]


def check_diagonal():
    global gameisgoing
    dia1 = board[0] == board[4] == board[8] != "-"
    dia2 = board[6] == board[4] == board[2] != "-"

    if dia1 or dia2:
        gameisgoing = False

    if dia1:
        return board[4]

    elif dia2:
        return board[6]


def check_tie():
    global gameisgoing
    if "-" not in board:
        gameisgoing = False
        print("Match is drawn/tied")


def play_game():
    while gameisgoing:
        handle_turn()
        display_board()
        swap_players()
        check_winner()

    print("congrats...player {} is the winner".format(winner))



while True:
    choose = input("Press [S or s] to start game and  [q or Q] to quit game: ")

    if choose.lower() == 's':
        play_game()
        board.clear()
        board = new_board(temp)
        gameisgoing = True
        current_player = 'X'

    elif choose.lower() == 'q':
        print("Game Over...Thank You..!!")
        break
