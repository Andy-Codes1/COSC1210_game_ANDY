from Settings import * 
#the * is a wildcard import, so I can directly mention all files without having to put Settings._ in front of it.
import random
import pygame 


# Tile Types for 2D board
# "B" = Bomb
# "E" = Empty Square
# "C" = Clue Square
# "X" = Unknown Square
class Tile: 
    # so basically I am making a class for Tiles, x coordinate, y cordinate, and the type as parameter. I'm making revealed and flagged as false because they are not true yet
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        #now I am setting self.x and y to a box which is why it's 70/8 multiplied by the x value 
        self.x = x * TILE_SIZE
        self.y = y * TILE_SIZE
        self.image = image
        self.type = type
        self.revealed = revealed 
        self.flagged = flagged
    
    def square(self, board_surface):
        if not self.flagged and self.revealed:
            board_surface.blit(self.image, (self.x, self.y)) #in Pygame the code blit puts something ontop of another thing, x,y are used for the squares to put image above the square
        elif self.flagged and not self.revealed: 
            board_surface.blit(tile_flagged, (self.x, self.y))
        elif not self.revealed:
            board_surface.blit(tile_unknown, (self.x, self.y))

def __repr__(self): #dunder method, for why the list response with a developer output list in main game loop
    return self.type

class Board:
    def __init__(self): #board doesn't need any instance variables
        self.board_surface = pygame.Surface((WIDTH, HEIGHT))
        self.board_list = [[Tile(col, row, tile_empty, "X") for row in range(GRID_ROWS)] for col in range(GRID_COLS)] #creates board list
        self.place_mines()
        self.place_clues()
        self.dug = [] 
    def place_mines(self):
        for i in range(MINES):
            while True:
                x = random.randint(0, GRID_ROWS-1)
                y = random.randint(0, GRID_COLS-1) #select a random tile and put a bomb there
                if self.board_list[x][y].type == "X":
                    self.board_list[x][y].image = tile_mine 
                    self.board_list[x][y].type = "B"
                    break
    
    def place_clues(self):
        for x in range(GRID_ROWS):
            for y in range(GRID_COLS):
                if self.board_list[x][y].type != "B":
                    MINES = self.check_neighbours(x,y)
                    if MINES > 0:
                        self.board_list[x][y].image = tile_numbers[MINES-1]
                        self.board_list[x][y].type = "C"

    @staticmethod #static methods are associated with a class, but don't do anything in it, its just for organization, this function here sees if x and y is inside the map
    def inside(x,y):
        return 0 <= x < GRID_ROWS and 0 <= y < GRID_COLS
    

    # To check for neighbouring bombs, the code will take in an x and y for a square, bombs nearby will be initalized to 0, then 
    # then we will check toward the left of the bomb and right of the bomb thus the starting at -1, and ending before 2, and top and down 
    # if the bomb is inside the 8x8 map and the square is a bomb then the square will add one bomb to its clue. after, we return that final number
    def check_neighbours(self, x, y):
        MINES = 0 
        for x_offset in range(-1,2):
            for y_offset in range(-1,2):
                neighbour_x = x + x_offset
                neighbour_y = y + y_offset
                if self.inside(neighbour_x, neighbour_y) and self.board_list[neighbour_x][neighbour_y].type == "B":
                    MINES +=1 
        return MINES

    def draw(self, screen):
        for row in self.board_list:
            for tile in row:
                tile.square(self.board_surface)
        screen.blit(self.board_surface, (0,0))
    def dig(self, x, y):
        self.dug.append((x, y))
        if self.board_list[x][y].type == "B":
            self.board_list[x][y].revealed = True
            self.board_list[x][y].image = tile_exploded
            return False
        elif self.board_list[x][y].type == "C":
            self.board_list[x][y].revealed = True
            return True

        self.board_list[x][y].revealed = True

        for row in range(max(0, x-1), min(GRID_ROWS-1, x+1) + 1):
            for col in range(max(0, y-1), min(GRID_COLS-1, y+1) + 1):
                if (row, col) not in self.dug:
                    self.dig(row, col)
        return True

    def display_board(self):
        for row in self.board_list:
            print(row)
