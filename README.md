# Pawn
A simple, lightweight, python chess graphics engine.

## Installation

Use the pip to install

    pip install Pawn

## Import

To import pawn to use graphics, use this:

    from Pawn import *
   
This will import everything in the library.

## Graphics

Use `draw_board()` to create graphics.
    
    draw_board(board_array, next_back=false)
    
The `board_array` parameter is the array of the board position. It should
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