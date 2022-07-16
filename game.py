import numpy as np

tmp=np.zeros((9,), dtype=np.int64)

# tmp=[0,0,0,0,0,0,0,0,0]
# print(tmp) 
# tmp[0]=1
# tmp[4]=2
# for index,item in enumerate(tmp):
#     # print(f'{index} : {item}')
#     print(f"{index+1 if tmp[index] == 0 else ('O' if tmp[index]== 1 else 'X')}", end="")
#     if (index+1)%3 == 0:
#         print("\n---------")
#     else :
#         print(" | ", end="")

def display_board(board, playerMap):
    for index,item in enumerate(board):
        # print(f'{index} : {item}')
        print(f"{index+1 if board[index] == 0 else (playerMap[1] if board[index]== 1 else playerMap[2])}", end="")
        if (index+1)%3 == 0:
            print("\n---------")
        else :
            print(" | ", end="")

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
            
    return {1:player1, 2:player2}

def place_marker(board,marker,playerMap):
    print(f'player{marker} start to select: ')
    choice = ''
    while choice not in ['1','2','3','4','5','6','7','8','9']:
        choice = input('Which position do you want to choose?(1-9) ')
        if choice not in ['1','2','3','4','5','6','7','8','9']:
            clear_output()
            print("Sorry, there is no position which you chose. Please try again.")
        
        # TODO The selected position is occupied, please reselect

        if choice in ['1','2','3','4','5','6','7','8','9']:
            board[int(choice)-1] = marker
            display_board(board,playerMap)

# TODO check the right game over decision logic
def checkBoardIsOver(board):
    # 檢查board裡面沒有0 -> 每個位置都被玩家選曲 -> 終止
    if (0 in board) == False:
        return True
    else:
        return False
    # 判斷勝利條件


if __name__ == "__main__":
    # init game board
    # game_board = [0,0,0,0,0,0,0,0,0]
    game_board = np.zeros((9,), dtype=np.int64)

    # let player select marker 'O' or 'X'
    playerMap = player_input()
    print(f'Player1: {playerMap[1]}, player2: {playerMap[2]}')

    # display default board to the player to select
    print('Hi, game is starting, please select the available position on the board')
    display_board(game_board,playerMap)

    # player1 and player2 routing select the position on the board
    gameIsOver = False
    roundStep = 0

    while gameIsOver == False:    
        # currentPlayer:
        # player1: 0,2,4,6,8,10 ... 
        # player2: 1,3,5,7,9 ...
        place_marker(game_board, (roundStep%2 +1),playerMap)

        # if currentPlayer%2 == 0 :
        #     print('player1 start to select: ')
        #     place_marker(game_board, (currentPlayer%2 +1))
        # else:
        #     print('player2 start to select: ')
        #     place_marker(game_board, 2)

        roundStep = roundStep+1

        # check if the game is over: winner and draw
        print(f'####### {checkBoardIsOver(game_board)} ######')
        if checkBoardIsOver(game_board):
            gameIsOver = True

