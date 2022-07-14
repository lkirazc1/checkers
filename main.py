import pygame


win = pygame.display.set_mode((850, 850))
pygame.display.set_caption("Checkers")
WIDTH, HEIGHT = win.get_width(), win.get_height()
RED = 1
BLACK = -1
RED_KING = 2
BLACK_KING = -2
NOTHING = 0
win.fill((255, 255, 255))

def draw_grid(win):
    win.fill((139, 69, 19))
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 1:
                pygame.draw.rect(win, (255, 0, 0), pygame.Rect(25 + i * 100, 25 + j * 100, 100, 100))
                continue
            pygame.draw.rect(win, (0, 0, 0), pygame.Rect(25 + i * 100, 25 + j * 100, 100, 100))

def draw_board(win, grid):
    # red will be 1 and black will be -1
    # kings will be one more than the normal
    # nothing will be 0
    draw_grid(win)
    pygame.display.update()



class Grid:
    def __init__(self) -> None:
        self.board = []
        self.width = 8
        for r in range(8):
            row = []
            for c in range(8):
                if (r + c) % 2 == 1 and r < 3:
                    row.append(BLACK)
                elif (r + c) % 2 == 1 and r >= 5:
                    row.append(RED)
                else:
                    row.append(NOTHING)
            self.board.append(row)
        self.turn = lambda x: x > 0
        self.player_positions = self.get_current_positions()

    def get_current_positions(self):
        positions = []
        for r in range(self.width):
            for c in range(self.width):
                if self.turn(self.board[r][c]):
                    positions.append((r, c))
        
        return positions

    def valid_takes(self, pos):
        pass
        


    def valid_moves(self, pos):
        """Valid moves that don't include taking"""
        if self.board[pos[0]][pos[1]] in [RED_KING, BLACK_KING]:
            moves = [(1, 1), (-1, -1), (-1, 1), (1, -1)]
        
        elif self.board[pos[0]][pos[1]] == RED:
            moves = [(-1 -1), (-1, 1)]
        elif self.board[pos[0]][pos[1]] == BLACK:
            moves = [(1, 1), (1, -1)]

        valid_positions = []


        for move in moves:
            if move[0] + pos[0] < 0 or move[0] + pos[0] >= self.width or move[1] + pos[1] < 0 or move[1] + pos[1] >= self.width:
                moves.remove(move)
                continue
            if self.board[pos[0] + move[0]][pos[1] + move[1]] != NOTHING:
                moves.remove(move)
            valid_positions.append((pos[0] + move[0], pos[1] + move[1]))

        return valid_positions
    
    

grid = Grid()


done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    draw_board(win, 0)
