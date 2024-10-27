from tkinter import *
from tkinter.font import Font
import settings
import utils
from cell import Cell

def initialize_board():
    if Cell.all:
        for cell in Cell.all:
            cell.cell_btn_object.destroy()
        Cell.all.clear()
        Cell.cell_count = settings.CELL_COUNT
        Cell.mine_count = settings.MINES_COUNT
    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
            c = Cell(x, y)
            c.create_btn_object(center_frame)
            c.cell_btn_object.grid(row=y, column=x)
            c.cell_btn_object.config(text='', state=NORMAL)
    
    Cell.create_cell_count_label(left_frame)
    Cell.cell_count_label_object.place(x=0, y=0)

    Cell.create_mine_count_label(left_frame)
    Cell.mine_count_label_object.place(x=0, y=40)

    Cell.randomize_mines()
    

root = Tk()

root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper game")
root.resizable(False, False)
root.configure(bg="cornsilk3")

top_frame = Frame(
    root,
    bg='cornsilk3',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='cornsilk3',
    text='Minesweeper Game',
    font=Font(size=35)
)

game_title.place(
    x=utils.width_prct(24), y=0
)

left_frame = Frame(
    root,
    bg="cornsilk3",
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg="cornsilk3",
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

initialize_board()

def check_game_over():
    retry = Cell.code
    if retry:
        initialize_board()
        Cell.code = False
    root.after(100, check_game_over)

root.after(100, check_game_over)
root.mainloop()