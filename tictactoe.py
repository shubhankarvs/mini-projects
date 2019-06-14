board=["-","-","-", #declare the board
       "-","-","-",
       "-","-","-",]

game_still_going=True
winner=None
current_player="X"
def display_board():

    print(board[0]+"|"+board[1]+'|'+board[2]+
            "\n"+board[3]+"|"+board[4]+'|'+board[5]+
            "\n" + board[6] + "|" + board[7] + '|' + board[8])

def playgame():

    display_board()

    while game_still_going:
        take_user_input(current_player)   #take user input for the position

        check_if_game_still_running()   #check in win or tie

        flip_player()   #change the current player

    if winner=="X" or winner=="O":
        print(winner+" wins!")
    elif winner==None:
        print("Tie.")


def take_user_input(current_player):
    print(current_player+"'s turn.")
    position=input("Enter the position from 1 to 9")
    valid= False
    while not valid:
        while position not in["1","2","3","4","5","6","7","8","9"]:
            position=input("Enter the position from 1 to 9")

        position = int(position) - 1

        if board[position]=="-":
            valid = True

        elif board[position]!="-":
            print("You cannot perform this task.")

    board[position]=current_player
    print(display_board())

def check_if_game_still_running():
    check_win()
    check_tie()


def check_win():
    global winner
    #checkrow
    row_winner=check_row()
    #checkcol
    column_winner=check_column()
    #checkdiagonal
    diagonal_winner=check_diagonal()

    if row_winner:
        winner=row_winner
    elif column_winner:
        winner=column_winner
    elif diagonal_winner:
        winner=diagonal_winner
    else:
         winner=None

def check_row():
    global game_still_going
    row1 = board[0] == board[1] == board[2] !="-"
    row2 = board[3] == board[4] == board[5] !="-"
    row3 = board[6] == board[7] == board[8] !="-"

    if row1 or row2 or row3:
         game_still_going = False

    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    return None


def check_column():
    global game_still_going
    col1 = board[0] == board[3] == board[6] != "-"
    col2 = board[1] == board[4] == board[7] != "-"
    col3 = board[2] == board[5] == board[8] != "-"

    if col1 or col2 or col3:
        game_still_going = False

    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    return None


def check_diagonal():
    global game_still_going
    diag1 = board[0] == board[4] == board[8] != "-"
    diag2 = board[2] == board[4] == board[6] != "-"

    if diag1 or diag2:
        game_still_going = False

    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    return None


def check_tie():
    global game_still_going
    if "-" not in board:
        game_still_going=False
        return True
    else:
        return False



def flip_player():
    global current_player
    if current_player=="X":
        current_player="O"
    elif current_player=="O":
        current_player="X"


#def check_turns():








playgame()