import os

def create_board(line, column):
    board = []
    
    for i in range(line):
        
        line_create = []
        for j in range(column):
            line_create.append(' ')
        board.append(line_create)

    return board

def show_board(board):
    for line in board:
        print(line)

def clear_terminal():
    os.system('cls')

def create_index_board(line, column):

    board_dict = {}
        
    index = 0
        
    for i in range(line):
        for j in range(column):
            index+=1
            board_dict[index] = (i,j)
                
    return board_dict

def defining_player():
    player1 = 'Wrong'

    while player1 not in ['X','O']:
        player1 = input('What character you want to use (X or O): ')
        if player1 not in ['X','O']:
            print('Invalid character, choose X or O')
                        
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    players = [player1, player2]
    return players

def select_position(board_dict):
    selected_position = int(input("Select the position that you wanna fill (1-9): "))
    position = board_dict[selected_position]
    return position

def validate_position(board, player_selected_position):
    (selected_line, selected_column) = player_selected_position
    if board[selected_line][selected_column] == (' '):
        return True
    else:
        return False
    
def applying_X_O(board, current_player, player_selected_position):
      
    (selected_line, selected_column) = player_selected_position
    board[selected_line][selected_column] = current_player
    return True

def validate_line(board, line, column, current_player):

    player_counter = 0

    for i in range(line):
        for j in range(column):
            if board[i][j] == current_player:
                player_counter += 1
        if player_counter == 3:
            return True
        else:
            player_counter = 0
    return False

def validate_column(board, line, column, current_player):

    player_counter = 0

    for j in range(column):
        for i in range(line):
            if board[i][j] == current_player:
                player_counter+=1
        if player_counter == 3:
            return True
        else:
            player_counter = 0
    return False

def validate_main_diagonal(board, current_player):

    if (board[0][0] == current_player) and (board[1][1] == current_player) and (board[2][2] == current_player):
        return True
    else:
        return False

def validate_secondary_diagonal(board, current_player):
    
    if (board[0][2] == current_player) and (board[1][1] == current_player) and (board[2][0] == current_player):
        return True
    else:
        return False

def validate_win(board, line, column, current_player):

    if validate_line(board, line, column, current_player) :
        return True
    elif validate_column(board, line, column, current_player):
        return True
    elif validate_main_diagonal(board, current_player):
        return True
    elif validate_secondary_diagonal(board, current_player):
        return True
    else: 
        return False
    
def main():
    board = create_board(3,3)
    board_dict = create_index_board(3,3)
    players = defining_player()

    turn = 0
    victory = False
    

    while (not victory) and (turn !=9):
        clear_terminal()
        show_board(board)
        current_player = players[turn%2]

        chosen_position = False

        while chosen_position != True:
            player_selected_position = select_position(board_dict)
            chosen_position = validate_position(board, player_selected_position)

            if chosen_position == False:
                print('Position alredy filled, choose another')

        applying_X_O(board, current_player, player_selected_position)

        victory = validate_win(board, 3, 3, current_player)
        show_board(board)

        if victory == True:
            print(f"Player {current_player} won")
            break
        elif victory == False and turn == 8:
            print("Match ends in a draw")
            break
        else:
            turn +=1

main()