from tkinter import *

def draw(board):
    root = Tk()
    root.title('Stalemates')
    c = Canvas(width=800, height=800)
    c.pack()
    root.geometry('800x800')

    for x in range(1, 9):
        if x % 2 == 0:
            board_square = c.create_rectangle(50 * x + 200 - 50, 200, 50 * x + 200, 250, fill='white')
            board_square = c.create_rectangle(50 * x + 200 - 50, 250, 50 * x + 200, 300, fill='brown')
            board_square = c.create_rectangle(50 * x + 200 - 50, 300, 50 * x + 200, 350, fill='white')
            board_square = c.create_rectangle(50 * x + 200 - 50, 350, 50 * x + 200, 400, fill='brown')
            board_square = c.create_rectangle(50 * x + 200 - 50, 400, 50 * x + 200, 450, fill='white')
            board_square = c.create_rectangle(50 * x + 200 - 50, 450, 50 * x + 200, 500, fill='brown')
            board_square = c.create_rectangle(50 * x + 200 - 50, 500, 50 * x + 200, 550, fill='white')
            board_square = c.create_rectangle(50 * x + 200 - 50, 550, 50 * x + 200, 600, fill='brown')
        else:
            board_square = c.create_rectangle(50 * x + 200 - 50, 200, 50 * x + 200, 250, fill='brown')
            board_square = c.create_rectangle(50 * x + 200 - 50, 250, 50 * x + 200, 300, fill='white')
            board_square = c.create_rectangle(50 * x + 200 - 50, 300, 50 * x + 200, 350, fill='brown')
            board_square = c.create_rectangle(50 * x + 200 - 50, 350, 50 * x + 200, 400, fill='white')
            board_square = c.create_rectangle(50 * x + 200 - 50, 400, 50 * x + 200, 450, fill='brown')
            board_square = c.create_rectangle(50 * x + 200 - 50, 450, 50 * x + 200, 500, fill='white')
            board_square = c.create_rectangle(50 * x + 200 - 50, 500, 50 * x + 200, 550, fill='brown')
            board_square = c.create_rectangle(50 * x + 200 - 50, 550, 50 * x + 200, 600, fill='white')

    for x in range(1, 9):
        for y in range(1, 9):
            if board[(x - 1) * 8 + y - 1] == 0:
                continue
            else:
                piece = c.create_text(50 * y + 200 - 25, 200 + 25 + x * 50 - 50, text=board[(x - 1) * 8 + y - 1],
                                      font=("Helvetica", 30))
    root.mainloop()
