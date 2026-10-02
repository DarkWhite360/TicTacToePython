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
    print(board_dict)
    selected_position = int(input("Select the position that you wanna fill: "))
    position = board_dict[selected_position]
    return position

def applying_X_O(board, current_player, player_selected_position):
      
    (selected_line, selected_column) = player_selected_position
    board[selected_line][selected_column] = current_player
    return board

def main():
    board = create_board(3,3)
    board_dict = create_index_board(3,3)
    players = defining_player()

    turn = 0

    while turn !=9:
        show_board(board)
        current_player = players[turn%2]
        player_selected_position = select_position(board_dict)
        applying_X_O(board, current_player, player_selected_position)
        show_board(board)
        turn += 1

main()