import numpy as np

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
    endSelect = False
    while endSelect == False:
        choice = input('Which position do you want to choose?(1-9) ')
        # 當輸入的數字不屬於1~9, 提示使用者重新輸入
        if choice not in ['1','2','3','4','5','6','7','8','9']:
            print("Sorry, there is no position which you chose. Please try again.")
        # 當選擇的欄位不為0的時候, 代表選擇的欄位已經被填過
        elif board[int(choice)-1] != 0:
            print(f"Sorry, position {choice} has already been placed")
        else:
            board[int(choice)-1] = marker
            display_board(board,playerMap)
            endSelect = True

# check the right game over decision logic
# 0 => draw, 1 => playerMap[1] win, 2 => playerMap[2] win
def checkBoardIsOver(board):
    # 判斷勝利條件 
    # [0,1,2],[3,4,5],[6,7,8] 
    # [0,3,6],[1,4,7],[2,5,8]
    # [0,4,8],[2,4,6]
    for player in [1,2]:
        for check in [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]:
            if board[check[0]] == player and board[check[1]] == player and board[check[2]] == player:
                return player
        # if (board[0]==player and board[1]==player and board[2]==player) or (board[3]==player and board[4]==player and board[5]==player) or (board[6]==player and board[7]==player and board[8]==player) :
        #     return player
        # if (board[0]==player and board[3]==player and board[6]==player) or (board[1]==player and board[4]==player and board[7]==player) or (board[2]==player and board[5]==player and board[8]==player) :
        #     return player
        # if (board[0]==player and board[4]==player and board[8]==player) or (board[2]==player and board[4]==player and board[6]==player) :
        #     return player

    # 檢查board裡面沒有0 -> 每個位置都被玩家選曲 -> 終止
    if (0 in board) == False:
        return 0

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
        print(f'------- Round Step {roundStep+1} -------')

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

        if checkBoardIsOver(game_board) == 0 :
            gameIsOver = True
            print(f'DRAW!!!')
        elif checkBoardIsOver(game_board) == 1 or checkBoardIsOver(game_board) == 2:
            gameIsOver = True
            print(f'{playerMap[checkBoardIsOver(game_board)]} is winner!!!')

