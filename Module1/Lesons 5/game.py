import tkinter as tk
import random

# Налаштування гри
WIDTH = 400
HEIGHT = 400
TILE_SIZE = 40
ROWS = HEIGHT // TILE_SIZE
COLS = WIDTH // TILE_SIZE

# Ігрове поле
class Game:
    def __init__(self, root):
        self.canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='black')
        self.canvas.pack()
        self.board = [[' ' for _ in range(COLS)] for _ in range(ROWS)]
        self.bomberman_pos = [1, 1]
        self.bombs = []
        self.explosions = []
        self.enemies = [[COLS-2, ROWS-2]]  # Список ворогів
        self.create_walls()
        self.draw_board()
        root.bind('<Key>', self.key_pressed)

        self.update_game()

    def create_walls(self):
        for y in range(ROWS):
            for x in range(COLS):
                if x == 0 or y == 0 or x == COLS-1 or y == ROWS-1 or (x % 2 == 0 and y % 2 == 0):
                    self.board[y][x] = '#'
                elif random.random() < 0.2:
                    self.board[y][x] = '*'
        self.board[1][1] = ' '

    def draw_board(self):
        self.canvas.delete('all')
        for y in range(ROWS):
            for x in range(COLS):
                cell = self.board[y][x]
                color = 'black'
                if cell == '#': color = 'gray'
                elif cell == '*': color = 'brown'
                self.canvas.create_rectangle(x*TILE_SIZE, y*TILE_SIZE, (x+1)*TILE_SIZE, (y+1)*TILE_SIZE, fill=color)
        # Малюємо гравця
        x, y = self.bomberman_pos
        self.canvas.create_oval(x*TILE_SIZE, y*TILE_SIZE, (x+1)*TILE_SIZE, (y+1)*TILE_SIZE, fill='blue')
        # Малюємо ворогів
        for ex, ey in self.enemies:
            self.canvas.create_rectangle(ex*TILE_SIZE+10, ey*TILE_SIZE+10, (ex+1)*TILE_SIZE-10, (ey+1)*TILE_SIZE-10, fill='green')
        # Малюємо бомби
        for bx, by, timer in self.bombs:
            self.canvas.create_oval(bx*TILE_SIZE+10, by*TILE_SIZE+10, (bx+1)*TILE_SIZE-10, (by+1)*TILE_SIZE-10, fill='red')
        # Малюємо вибухи
        for ex, ey, timer in self.explosions:
            self.canvas.create_rectangle(ex*TILE_SIZE, ey*TILE_SIZE, (ex+1)*TILE_SIZE, (ey+1)*TILE_SIZE, fill='orange')

    def key_pressed(self, event):
        dx, dy = 0, 0
        if event.keysym == 'Up': dy = -1
        elif event.keysym == 'Down': dy = 1
        elif event.keysym == 'Left': dx = -1
        elif event.keysym == 'Right': dx = 1
        elif event.keysym == 'space':
            self.place_bomb()
            return

        new_x = self.bomberman_pos[0] + dx
        new_y = self.bomberman_pos[1] + dy
        if self.board[new_y][new_x] == ' ':
            self.bomberman_pos = [new_x, new_y]
        self.draw_board()

    def place_bomb(self):
        x, y = self.bomberman_pos
        if (x, y) not in [(bx, by) for bx, by, _ in self.bombs]:
            self.bombs.append([x, y, 3])

    def update_game(self):
        # Оновлення бомб
        new_bombs = []
        for bx, by, timer in self.bombs:
            if timer > 0:
                new_bombs.append([bx, by, timer - 1])
            else:
                self.trigger_explosion(bx, by)
        self.bombs = new_bombs

        # Оновлення вибухів
        new_explosions = []
        for ex, ey, timer in self.explosions:
            if timer > 0:
                new_explosions.append([ex, ey, timer - 1])
        self.explosions = new_explosions

        # Рух ворогів
        self.move_enemies()

        self.draw_board()
        self.canvas.after(500, self.update_game)

    def move_enemies(self):
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        new_positions = []
        for x, y in self.enemies:
            random.shuffle(directions)
            moved = False
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < COLS and 0 <= ny < ROWS and self.board[ny][nx] == ' ' and [nx, ny] != self.bomberman_pos:
                    new_positions.append([nx, ny])
                    moved = True
                    break
            if not moved:
                new_positions.append([x, y])
        self.enemies = new_positions

    def trigger_explosion(self, x, y):
        directions = [(0, 0), (1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < COLS and 0 <= ny < ROWS:
                if self.board[ny][nx] == '*':
                    self.board[ny][nx] = ' '
                self.explosions.append([nx, ny, 2])

root = tk.Tk()
root.title("BomberMan")
game = Game(root)
root.mainloop()
