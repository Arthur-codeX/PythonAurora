from board import *
from rook_module import *
from knight_module import *
from util import *

board = [
    ["B-A1,  ", "W-B1,WN", "B-C1,  ", "W-D1,  ", "B-E1,  ", "W-F1,  ", "B-G1,  ", "W-H1,  "],
    ["W-A2,  ", "B-B2,  ", "W-C2,  ", "B-D2,  ", "W-E2,  ", "B-F2,  ", "W-G2,  ", "B-H2,  "],
    ["B-A3,  ", "W-B3,  ", "B-C3,  ", "W-D3,  ", "B-E3,  ", "W-F3,  ", "B-G3,  ", "W-H3,  "],
    ["W-A4,  ", "B-B4,  ", "W-C4,  ", "B-D4,  ", "W-E4,  ", "B-F4,  ", "W-G4,  ", "B-H4,  "],
    ["B-A5,  ", "W-B5,  ", "B-C5,  ", "W-D5,  ", "B-E5,  ", "W-F5,  ", "B-G5,  ", "W-H5,  "],
    ["W-A6,  ", "B-B6,  ", "W-C6,  ", "B-D6,  ", "W-E6,  ", "B-F6,  ", "W-G6,  ", "B-H6,  "],
    ["B-A7,  ", "W-B7,  ", "B-C7,  ", "W-D7,  ", "B-E7,  ", "W-F7,  ", "B-G7,  ", "W-H7,  "],
    ["W-A8,BR", "B-B8,  ", "W-C8,  ", "B-D8,  ", "W-E8,  ", "B-F8,  ", "W-G8,  ", "B-H8,  "]
]

# type of board

knight = {"x": 1, "y": 0}
rook = {"x": 0, "y": 7}

def main():
    global rook  # Declare rook as global to update it inside the function
    global knight
    while True:
        printBoard(board)
        rook_moves = rookPosibleMoves(rook,knight)
        to_human_coordinates = toHumanCordinates(rook_moves)
        print("Possible moves with the rook are")
        print(to_human_coordinates)
        user_input = input("Make a move: ")
        user_input = user_input.upper().strip()

        if user_input not in to_human_coordinates:
            print("Invalid move")
            main()
            return
        print("Making that move")
        human_conv_coordinates = toPcCordinates(user_input)
        makeMove(board, rook, human_conv_coordinates)
        rook = human_conv_coordinates  # Update the rook position
        print("",rook)
        printBoard(board)
        knight_moves=knightPosibleMoves(knight)
        human_conv_coordinates_knight=toHumanCordinates(knight_moves)
        print("Possible moves with the knight ")
        print(human_conv_coordinates_knight)
        # Stupid one.
        # The first available move.
        knight_move=pc_make_move(knight_moves)
        makeMove(board,knight,knight_move)
        print("I made a smart move your turn.")
        knight=knight_move
    # printBoard(board)
    # print("Game over")
    # print("Rook position",rook)
    # print("Knight position", knight)



main()
