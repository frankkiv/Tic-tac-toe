
# tmp=[0,0,0,0,0,0,0,0,0]
# tmp[0]='O'
# tmp[4]='X'
# for index,item in enumerate(tmp):
#     # print(f'{index} : {item}')
#     print(f"{index+1 if tmp[index] == 0 else tmp[index]} | ", end="")
#     if (index+1)%3 == 0:
#         print("\n---------")



def display_board(board):
    print(board[6] + "|" + board[7] + "|" + board[8])
    print('-----')
    print(board[3] + "|" + board[4] + "|" + board[5])
    print('-----')
    print(board[0] + "|" + board[1] + "|" + board[2])

def player_input():
    marker = ''
    while marker != 'O' and marker != 'X':
        marker = input('player1, which mark do you want? O or X: ')
        if marker != 'O' and marker != 'X':
            print("please input the valid mark")

    player1 = marker
    if player1 == 'O':
        player2 = 'X'
    else:
        player2 = 'O'
            
    return (player1,player2)

def place_marker(board,marker):
    choice = ''
    
    while choice not in ['1','2','3','4','5','6','7','8','9']:
        choice = input('Which position do you want to choose?(1-9) ')
        if choice not in ['1','2','3','4','5','6','7','8','9']:
            clear_output()
            print("Sorry, there is no position which you chose. Please try again.")
        
        # TODO The selected position is occupied, please reselect

        if choice in ['1','2','3','4','5','6','7','8','9']:
            board[int(choice)-1] = marker
            display_board(board)

# TODO check the right game over decision logic
def checkBoardIsOver(board):
    # 檢查board已經填滿了, 沒得玩結束
    # 1~9 都不存在於board -> 終止
    nonExist = 0
    for num in ['1','2','3','4','5','6','7','8','9']:
        # board = ['O', '2', 'X', ....]
        if (num in board) == False:
            nonExist=nonExist+1
    if nonExist == 9:
        return True
    
    # 判斷勝利條件


if __name__ == "__main__":
    # init game board
    game_board = ['1','2','3','4','5','6','7','8','9']

    # let player select marker 'O' or 'X'
    player1, player2 = player_input()
    print(f'Player1: {player1}, player2: {player2}')

    # display default board to the player to select
    print('Hi, game is starting, please select the available position on the board')
    display_board(game_board)

    # player1 and player2 routing select the position on the board
    gameIsOver = False
    currentPlayer = 0

    while gameIsOver == False:    
        # currentPlayer:
        # player1: 0,2,4,6,8,10 ... 
        # player2: 1,3,5,7,9 ...

        if currentPlayer%2 == 0 :
            print('player1 start to select: ')
            place_marker(game_board, player1)
        else:
            print('player2 start to select: ')
            place_marker(game_board, player2)

        currentPlayer = currentPlayer+1

        # check if the game is over: winner and draw
        print(f'####### {checkBoardIsOver(game_board)} ######')
        if checkBoardIsOver(game_board):
            gameIsOver = True

