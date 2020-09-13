# Pawn
A simple, lightweight, python chess graphics engine.

## Installation

Use the pip to install

    pip install Pawn

## Graphics

Use draw_board to create graphics.
    
    draw_board(board_array, next_back=false)
    
The `board_array` parameter is the array of the board possition. It should
look a little bit like this:

    board = ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖",
            "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙",
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             "♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟",
             "♜", "♞", "♝", 0, "♚", "♝", "♞", "♜"]
             
Zeros mean that the square is empty. 

The `next_back` parameter defaults to false. If you have multiple positions
you want to simulate, then you should set this to true. Make sure that you then
change your board array to look like this:

    board = [["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖",
            "♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙",
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             0, 0, 0, 0, 0, 0, 0, 0,
             "♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟",
             "♜", "♞", "♝", 0, "♚", "♝", "♞", "♜"],
             ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖",
            "♙", "♙", 0, "♙", "♙", "♙", "♙", "♙",
             0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, "♙", 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0,
            "♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟",
            "♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"]]
            
The parameter will output 2 buttons below the board, next and back. They will
change the position to go forward or backward to the previous or next position
in the game.
