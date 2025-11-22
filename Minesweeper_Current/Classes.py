class Board: 
    def __init__(self):
        self.board_surface = pygame.Surface(WIDTH, HEIGHT)
        self.dug = [] #empty list for dug bombs



    def place_clues():
        '''So far only have the logic for if it's not a bomb'''
        for x in GRID_ROWS: 
            for y in GRID_COLS: 
                if self.board[x][y].type != 'B':
                #B refers to the TYPE of Bombs written in ADVENTURE FUNCTIONS. 
                    total_bombs = self.bombs_near(x,y)
                    if total_bombs > 1:
                        self.board.image

#mine_location_dictionary(Total_bombs)

# Tile Types for 2D board
# "B" = Bomb
# "E" = Empty Square
# "C" = Clue Square
# "X" = Unknown Square
class Tile: 
    # so basically I am making a class for Tiles, x coordinate, y cordinate, and the type as parameter. I'm making revealed and flagged as false because they are not true yet
    def __init__(self, x, y, image, type, revealed=False, flagged=False):
        #now I am setting self.x and y to a box which is why it's 70/8 multiplied by the x value 
        self.x = x * (70 / 8)
        self.y = y * (70 / 8)
        self.image = image
        self.type = type
        self.revealed = revealed 
        self.flagged = flagged
    
    def square(self, board_surface):
        if not self.flagged and self.revealed:
            board_surface.blit(self.image, (self.x, self.y)) #in Pygame the code blit puts something ontop of another thing, x,y are used for the squares to put image above the square
        elif self.flagged and not self.revealed: 
            board_surface.blit(self.flagged, (self.x, self.y))
        elif not self.revealed:
            board_surface.blit(self.unknown, (self.x, self.y))


#def mine_location_dictionary(Total_bombs):
 #   Location_Bombs = {}
 #   for ix in GRID_ROWS:
 #       for iy in GRID_COLS:
 #           if Bombs.type == "B":
  #              Location_Bombs.append(ix, iy)
 #   print(Location_Bombs)
    #To see a 2D model of all bombs and their locations. 