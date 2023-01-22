from board import Board
from player import Player
import random

while input("Do you want to play ? (T/F) :  ") == "T":
    
    board = Board()
    player1 = Player(input("o or x :  "))
    player2 = Player("o" if player1.value == "x" else "x")

    move = 0
    run = True
    board.draw()
    while run:
        
        if move % 2 == 0:
            x = int(input("pos x :  "))
            y = int(input("pos y :  "))
            if board.grid[x][y] == " ":
                board.update((x,y), player1)
                move += 1
            else:
                continue
        else:
            while True:
                x = random.randint(0,2)
                y = random.randint(0,2)
                if board.grid[x][y] == " ":
                    board.update((x,y), player2)
                    move += 1
                    break
        
        board.draw()

        if move == 9:
            print("null nobody win")
            break
        winner = board.winner()
        if winner != None:
            if winner == player1.value: print("You win")
            else: print("You lose")
            break