
import sys
from tkinter import *
from tkinter.font import Font
import settings
import utils
import cell


root = Tk()
#Window customization
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper game")
root.resizable(False, False)
root.configure(bg = "cornsilk3")

top_frame = Frame(
    root,
    bg = 'cornsilk3',
    width = settings.WIDTH,
    height = utils.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg = 'cornsilk3',
    text = 'Minesweeper Game',
    font = Font(size = 35)
)

game_title.place(
    x = utils.width_prct(24), y = 0
)

left_frame = Frame(
    root,
    bg = "cornsilk3",
    width = utils.width_prct(25),
    height = utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg = "cornsilk3",
    width = utils.width_prct(75),
    height = utils.height_prct(75)
)
center_frame.place(
    x=utils.width_prct(25),
    y=utils.height_prct(25)
)

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = cell.Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            row=y, column=x
        )
#print(Cell.all)

cell.Cell.create_cell_count_label(left_frame)
cell.Cell.cell_count_label_object.place(x=0, y=0)

cell.Cell.create_mine_count_label(left_frame)
cell.Cell.mine_count_label_object.place(x = 0, y = 40)

cell.Cell.randomize_mines()

#Running the window
root.mainloop()

if(cell.Cell.code == 4): #ID RETRY
    #root.quit()
    root.mainloop()