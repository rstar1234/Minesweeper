import sys
from tkinter import Button, Label
import random
from tkinter.font import Font
import settings
import ctypes

class Cell:
    all = []
    code = 0
    cell_count = settings.CELL_COUNT
    mine_count = settings.MINES_COUNT
    cell_count_label_object = None
    mine_count_label_object = None
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width = 8,
            height = 3,
            # font = Font(size = 10)
        )
        btn.bind('<Button-1>', self.left_click_actions) #left click
        btn.bind('<Button-3>', self.right_click_actions) #right click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        lbl = Label(
            location,
            bg = "cornsilk3",
            text = f"Cells left:{Cell.cell_count}",
            font = Font(size = 20)
        )
        Cell.cell_count_label_object = lbl
    
    @staticmethod
    def create_mine_count_label(location):
        lbl = Label(
            location,
            bg = "cornsilk3",
            text = f"Mines left:{Cell.mine_count}",
            font = Font(size = 20)
        )
        Cell.mine_count_label_object = lbl

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            #self.cell_btn_object.configure(state = "disabled")
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            # If Mines count is equal to the cells left count, the player won
            if Cell.cell_count == settings.MINES_COUNT:
                 ctypes.windll.user32.MessageBoxW(0, 'You won!', 'Congratulations', 0)

        # Cancel left and right click events if the cell is already opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y +1 ),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1
        return counter

    def show_cell(self):    
        if not self.is_opened:

            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f"Cells left:{Cell.cell_count}")
            self.cell_btn_object.configure(bg = "SystemButtonFace")
        # If this was a mine candidate, change the bg color back to default
        self.is_opened = True

        if self.surrounded_cells_mines_length == 0:
            for cell in self.surrounded_cells:
                if not cell.is_opened:
                    cell.show_cell()

    def show_mine(self):
        # Logic to interrupt the game and display a message that that player lost
       self.cell_btn_object.configure(
            bg = "red"
        ) 
       Cell.code = ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine!', 'Game Over', 5)
       sys.exit()
        

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg = "pink")
            self.is_mine_candidate = True
            Cell.mine_count -= 1
            Cell.mine_count_label_object.configure(text = f"Mines left:{Cell.mine_count}")
        else:
            Cell.mine_count += 1
            self.cell_btn_object.configure(bg = "SystemButtonFace")
            Cell.mine_count_label_object.configure(text = f"Mines left:{Cell.mine_count}")
            self.is_mine_candidate = False
            

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
