import sys
import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PINK = (255, 0, 255)
PURPLE = (128, 0, 128)
ORANGE = (255, 99, 71)
GRAY = (119, 136, 153)
LIGHTBLUE = (60, 170, 255)
BEIGE = (178, 168, 152)
BORDER_THICKNESS = 1.0
HEIGHT_TOTAL = 680
WIDTH = 600
HEIGHT = 600
SCREEN_SIZE = (WIDTH, HEIGHT_TOTAL)
SIZE = 30
touch_area1 = pygame.Rect(210, 280, 200, 60)
touch_area2 = pygame.Rect(240, 360, 138, 60)
touch_area3 = pygame.Rect(250, 440, 115, 60)
touch_area4 = pygame.Rect(150, 280, 300, 60)
touch_area5 = pygame.Rect(150, 360, 300, 60)
touch_area6 = pygame.Rect(150, 280, 140, 60)
touch_area7 = pygame.Rect(310, 280, 140, 60)
touch_area8 = pygame.Rect(150, 360, 140, 60)
touch_area9 = pygame.Rect(310, 360, 140, 60)
touch_area10 = pygame.Rect(150, 440, 140, 60)
touch_area11 = pygame.Rect(310, 440, 140, 60)
touch_area12 = pygame.Rect(180, 605, 75, 20)
touch_area13 = pygame.Rect(285, 605, 75, 20)
touch_area14 = pygame.Rect(390, 605, 75, 20)
touch_area15 = pygame.Rect(495, 605, 75, 20)
touch_area16 = pygame.Rect(180, 630, 110, 20)
touch_area17 = pygame.Rect(320, 630, 110, 20)
touch_area18 = pygame.Rect(460, 630, 110, 20)
touch_area19 = pygame.Rect(180, 655, 110, 20)
touch_area20 = pygame.Rect(320, 655, 110, 20)
touch_area21 = pygame.Rect(460, 655, 110, 20)
touch_area22 = pygame.Rect(500, 0, 100, 100)

bg = pygame.image.load('Background (1).png')
bgr = pygame.image.load('Background_register.png')
tom_easy_mode = pygame.image.load('tom_easy_mode.webp')
tom_normal_mode = pygame.image.load('tom_normal_mode.webp')
tom_hard_mode = pygame.image.load('tom_hard_mode.webp')
jerry_easy_mode = pygame.image.load('jerry_easy_mode.webp')
jerry_normal_mode = pygame.image.load('jerry_normal_mode.webp')
jerry_hard_mode = pygame.image.load('jerry_hard_mode.webp')
cheese = pygame.image.load('cheese.png')
cheese_easy_mode = pygame.image.load('cheese_easy_mode.png')
cheese_normal_mode = pygame.image.load('cheese_normal_mode.png')
cheese_hard_mode = pygame.image.load('cheese_hard_mode.png')
speaker_off = pygame.image.load('speaker_off.png')
speaker_on = pygame.image.load('speaker_on.png')

pygame.mixer.init()
menu_music = pygame.mixer.Sound("menu_music.mp3")
game_music = pygame.mixer.Sound("game_music.mp3")
button_sound = pygame.mixer.Sound("mouse_click.mp3")

def read_accounts(file_name):
    accounts = {}
    try:
        with open(file_name, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            for line in lines:
                if line.strip():
                    file.write(line)
        with open(file_name, 'r') as file:
            for line in file:
                username, password = line.strip().split(',')
                accounts[username] = password
    except FileNotFoundError:
        return accounts
    return accounts

def read_names(file_name):
    names = []
    try:
        with open(file_name, 'r+') as file:
            lines = file.readlines()
            file.seek(0)
            file.truncate()
            for line in lines:
                if line.strip():
                    file.write(line)
        with open(file_name, 'r') as file:
            for line in file:
                name = line.strip()
                names.append(name)
    except FileNotFoundError:
        return names
    return names

def valid_name(file_name, name):
    names = read_names(file_name)
    if name in names:
        return False
    else:
        return True

def register(file_name, username):
    accounts = read_accounts(file_name)
    if username in accounts:
        return False
    else:
        return True

def login(file_name, username, password):
    accounts = read_accounts(file_name)
    if username in accounts and accounts[username] == password:
        return True
    else:
        return False

def text(background, message, color, size, coordinate_x, coordinate_y):
    font = pygame.font.SysFont(None, size)
    text = font.render(message, True, color)
    background.blit(text, [coordinate_x, coordinate_y])

def draw_rounded_rect(surface, color, rect, corner_radius):
    pygame.draw.rect(surface, color, (rect[0] + corner_radius, rect[1], rect[2] - 2 * corner_radius, rect[3]))
    pygame.draw.rect(surface, color, (rect[0], rect[1] + corner_radius, rect[2], rect[3] - 2 * corner_radius))
    pygame.draw.circle(surface, color, (rect[0] + corner_radius, rect[1] + corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (rect[0] + rect[2] - corner_radius, rect[1] + corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (rect[0] + corner_radius, rect[1] + rect[3] - corner_radius), corner_radius)
    pygame.draw.circle(surface, color, (rect[0] + rect[2] - corner_radius, rect[1] + rect[3] - corner_radius), corner_radius)

class NodeBorder():
    def __init__(self, pos_x, pos_y, width, height):
        self.color = BLACK
        self.thickness = BORDER_THICKNESS
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = width
        self.height = height

    def render(self, background):
        pygame.draw.rect(background, self.color, [self.pos_x, self.pos_y, self.width, self.height])

class Node():
    def __init__(self, pos_x, pos_y):
        self.color = BEIGE
        self.energy_point = False
        self.visited = False
        self.explored = False
        self.explored1 = False
        self.matrix_pos_x = 0
        self.matrix_pos_y = 0
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.width = SIZE
        self.height = SIZE
        self.top_border = NodeBorder(self.pos_x, self.pos_y, SIZE, BORDER_THICKNESS)
        self.bottom_border = NodeBorder(self.pos_x, self.pos_y + SIZE - BORDER_THICKNESS, SIZE, BORDER_THICKNESS)
        self.right_border = NodeBorder(self.pos_x + SIZE - BORDER_THICKNESS, self.pos_y, BORDER_THICKNESS, SIZE)
        self.left_border = NodeBorder(self.pos_x, self.pos_y, BORDER_THICKNESS, SIZE)
        self.neighbors = []
        self.neighbors_connected = []
        self.parent = None
        self.parent1 = None
        self.parent2 = None
        self.parent3 = None

    def render(self, background):
        pygame.draw.rect(background, self.color, [self.pos_x, self.pos_y, self.width, self.height])
        self.top_border.render(background)
        self.bottom_border.render(background)
        self.right_border.render(background)
        self.left_border.render(background)

class Maze():
    def __init__(self, background):
        self.maze = []
        self.total_nodes = 0
        self.minimum_steps = 0
        self.maze_created = False
        self.initial_coordinate_x = 0
        self.initial_coordinate_y = 0
        self.final_coordinate_x = 1
        self.final_coordinate_y = 1
        x = 0
        y = 0
        for i in range(0, WIDTH, SIZE):
            self.maze.append([])
            for j in range(0, HEIGHT, SIZE):
                self.maze[x].append(Node(i, j))
                self.total_nodes += 1
                y += 1
            x += 1
        self.define_neighbors()

    def add_edge(self, node, neighbor):
        neighbor.neighbors_connected.append(node)
        node.neighbors_connected.append(neighbor)

    def remove_neighbors_visited(self, node):
        node.neighbors = [x for x in node.neighbors if not x.visited]

    def define_neighbors(self):
        for i in range(0, int(HEIGHT / SIZE)):
            for j in range(0, int(WIDTH / SIZE)):
                self.maze[i][j].matrix_pos_x = i
                self.maze[i][j].matrix_pos_y = j
                if i > 0 and j > 0 and i < int(HEIGHT / SIZE) - 1 and j < int(HEIGHT / SIZE) - 1:
                    self.maze[i][j].neighbors.append(self.maze[i + 1][j])
                    self.maze[i][j].neighbors.append(self.maze[i - 1][j])
                    self.maze[i][j].neighbors.append(self.maze[i][j + 1])
                    self.maze[i][j].neighbors.append(self.maze[i][j - 1])
                elif i == 0 and j == 0:
                    self.maze[i][j].neighbors.append(self.maze[i][j + 1])
                    self.maze[i][j].neighbors.append(self.maze[i + 1][j])
                elif i == int(HEIGHT / SIZE) - 1 and j == 0:
                    self.maze[i][j].neighbors.append(self.maze[i - 1][j])
                    self.maze[i][j].neighbors.append(self.maze[i][j + 1])
                elif i == 0 and j == int(WIDTH / SIZE) - 1:
                    self.maze[i][j].neighbors.append(self.maze[i][j - 1])
                    self.maze[i][j].neighbors.append(self.maze[i + 1][j])
                elif i == int(HEIGHT / SIZE) - 1 and j == int(WIDTH / SIZE) - 1:
                    self.maze[i][j].neighbors.append(self.maze[i][j - 1])
                    self.maze[i][j].neighbors.append(self.maze[i - 1][j])
                elif j == 0:
                    self.maze[i][j].neighbors.append(self.maze[i - 1][j])
                    self.maze[i][j].neighbors.append(self.maze[i][j + 1])
                    self.maze[i][j].neighbors.append(self.maze[i + 1][j])
                elif i == 0:
                    self.maze[i][j].neighbors.append(self.maze[i + 1][j])
                    self.maze[i][j].neighbors.append(self.maze[i][j + 1])
                    self.maze[i][j].neighbors.append(self.maze[i][j - 1])
                elif i == int(HEIGHT / SIZE) - 1:
                    self.maze[i][j].neighbors.append(self.maze[i - 1][j])
                    self.maze[i][j].neighbors.append(self.maze[i][j + 1])
                    self.maze[i][j].neighbors.append(self.maze[i][j - 1])
                elif j == int(WIDTH / SIZE) - 1:
                    self.maze[i][j].neighbors.append(self.maze[i + 1][j])
                    self.maze[i][j].neighbors.append(self.maze[i - 1][j])
                    self.maze[i][j].neighbors.append(self.maze[i][j - 1])

    def break_border(self, node, neighbor, color):
        if (neighbor.matrix_pos_x == node.matrix_pos_x + 1) and (neighbor.matrix_pos_y == node.matrix_pos_y):
            node.right_border.color = color
            neighbor.left_border.color = color
        elif (neighbor.matrix_pos_x == node.matrix_pos_x - 1) and (neighbor.matrix_pos_y == node.matrix_pos_y):
            node.left_border.color = color
            neighbor.right_border.color = color
        elif (neighbor.matrix_pos_x == node.matrix_pos_x) and (neighbor.matrix_pos_y == node.matrix_pos_y + 1):
            node.bottom_border.color = color
            neighbor.top_border.color = color
        elif (neighbor.matrix_pos_x == node.matrix_pos_x) and (neighbor.matrix_pos_y == node.matrix_pos_y - 1):
            node.top_border.color = color
            neighbor.bottom_border.color = color

    def create_maze(self, background):
        current_cell = random.choice(random.choice(self.maze))
        current_cell.visited = True
        current_cell.color = GREEN
        stack = [current_cell]
        visited_cells = 1
        while visited_cells != self.total_nodes or len(stack) != 0:
            self.remove_neighbors_visited(current_cell)
            if len(current_cell.neighbors) > 0:
                random_neighbor = random.choice(current_cell.neighbors)
                self.break_border(current_cell, random_neighbor, GREEN)
                self.add_edge(current_cell, random_neighbor)
                current_cell = random_neighbor
                stack.append(current_cell)
                current_cell.visited = True
                current_cell.color = GREEN
                visited_cells += 1
            else:
                current_cell.color = BEIGE
                for border in [current_cell.top_border, current_cell.bottom_border, current_cell.right_border, current_cell.left_border]:
                    if border.color == GREEN:
                        border.color = BEIGE
                if len(stack) == 1:
                    stack.pop()
                else:
                    stack.pop()
                    current_cell = stack[-1]
        self.maze_created = True
        energies = 0
        while energies < (WIDTH * HEIGHT) / (SIZE * SIZE * 20):
            current_cell = random.choice(random.choice(self.maze))
            if not current_cell.energy_point:
                current_cell.energy_point = True
                energies += 1

    def dfs(self, background, player):
        current = self.maze[player.matrix_pos_x][player.matrix_pos_y]
        current.explored = True
        find = False
        while not find:
            current.color = PINK
            for border in [current.right_border, current.bottom_border, current.left_border, current.top_border]:
                if border.color == BEIGE:
                    border.color = PINK
            direct = False
            for i in current.neighbors_connected:
                if not direct and not i.explored:
                    i.parent = current
                    i.explored = True
                    current = i
                    direct = True
                    if i.matrix_pos_x == self.final_coordinate_x and i.matrix_pos_y == self.final_coordinate_y:
                        find = True
            if not direct:
                current.color = ORANGE
                for border in [current.right_border, current.bottom_border, current.left_border, current.top_border]:
                    if border.color == PINK:
                        border.color = ORANGE
                for i in current.neighbors_connected:
                    if i.color != ORANGE:
                        i.color = ORANGE
                        current = i
            self.render(background, player)
            player.render(background)
            self.draw_jerry(background)
            pygame.display.update()
        current = self.maze[self.final_coordinate_x][self.final_coordinate_y]
        while current.parent != None:
            current = current.parent
            current.color = GREEN
            for border in [current.right_border, current.bottom_border, current.left_border, current.top_border]:
                if border.color == PINK:
                    border.color = GREEN
            self.render(background, player)
            player.render(background)
            self.draw_jerry(background)
            pygame.display.update()

    def bs(self, background, player):
        current1 = self.maze[player.matrix_pos_x][player.matrix_pos_y]
        current2 = self.maze[self.final_coordinate_x][self.final_coordinate_y]
        current1.explored = True
        current2.explored = True
        find = False
        queue1 = [current1]
        queue2 = [current2]
        while not find:
            if len(queue1) > 0 and not find:
                queue1[0].color = PINK
                for border in [queue1[0].right_border, queue1[0].bottom_border, queue1[0].left_border, queue1[0].top_border]:
                    if border.color == BEIGE:
                        border.color = PINK
                u = queue1.pop(0)
                for i in u.neighbors_connected:
                    if not i.explored:
                        i.parent1 = u
                        i.explored = True
                        queue1.append(i)
                    if i.color == ORANGE or i.color == BLUE:
                        find = True
                        current1 = u
                        current2 = i
                self.render(background, player)
                player.render(background)
                self.draw_jerry(background)
                pygame.display.update()
            if len(queue2) > 0 and not find:
                queue2[0].color = ORANGE
                for border in [queue2[0].right_border, queue2[0].bottom_border, queue2[0].left_border, queue2[0].top_border]:
                    if border.color == BEIGE:
                        border.color = ORANGE
                u = queue2.pop(0)
                for i in u.neighbors_connected:
                    if not i.explored:
                        i.parent2 = u
                        i.explored = True
                        queue2.append(i)
                    if i.color == PINK or i.color == PURPLE:
                        find = True
                        current2 = u
                        current1 = i
                self.render(background, player)
                player.render(background)
                self.draw_jerry(background)
                pygame.display.update()
        while current1.parent1 != None or current2.parent2 != None:
            if current1.parent1 != None:
                current1.color = GREEN
                current1 = current1.parent1
                for border in [current1.right_border, current1.bottom_border, current1.left_border, current1.top_border]:
                    if border.color == PINK:
                        border.color = GREEN
            if current2.parent2 != None:
                current2.color = GREEN
                current2 = current2.parent2
                for border in [current2.right_border, current2.bottom_border, current2.left_border, current2.top_border]:
                    if border.color == ORANGE:
                        border.color = GREEN
            self.render(background, player)
            player.render(background)
            self.draw_jerry(background)
            pygame.display.update()

    def bfs(self, background, player):
        initial_node = self.maze[player.matrix_pos_x][player.matrix_pos_y]
        initial_node.explored = True
        find = False
        queue = [initial_node]
        while len(queue) > 0 and not find:
            queue[0].color = PINK
            for border in [queue[0].right_border, queue[0].bottom_border, queue[0].left_border, queue[0].top_border]:
                if border.color == BEIGE:
                    border.color = PINK
            u = queue.pop(0)
            for i in u.neighbors_connected:
                if not i.explored:
                    i.parent = u
                    i.explored = True
                    queue.append(i)
                    if i.matrix_pos_x == self.final_coordinate_x and i.matrix_pos_y == self.final_coordinate_y:
                        find = True
            self.render(background, player)
            player.render(background)
            self.draw_jerry(background)
            pygame.display.update()
        current = self.maze[self.final_coordinate_x][self.final_coordinate_y]
        while current.parent != None:
            current = current.parent
            current.color = GREEN
            for border in [current.right_border, current.bottom_border, current.left_border, current.top_border]:
                if border.color == PINK:
                    border.color = GREEN
            self.render(background, player)
            player.render(background)
            self.draw_jerry(background)
            pygame.display.update()

    def hint(self, background, player):
        hint_initial_node = self.maze[player.matrix_pos_x][player.matrix_pos_y]
        hint_initial_node.explored = True
        find = False
        hint_queue = [hint_initial_node]
        while len(hint_queue) > 0 and not find:
            hint_queue[0].color = PINK
            u = hint_queue.pop(0)
            for i in u.neighbors_connected:
                if not i.explored:
                    i.parent = u
                    i.explored = True
                    hint_queue.append(i)
                    if i.matrix_pos_x == self.final_coordinate_x and i.matrix_pos_y == self.final_coordinate_y:
                        find = True
        current = self.maze[self.final_coordinate_x][self.final_coordinate_y]
        while current.parent.parent != None:
            current = current.parent
            current.color = GREEN
            for border in [current.right_border, current.bottom_border, current.left_border, current.top_border]:
                if border.color == BEIGE:
                    border.color = GREEN
        for i in range(0, int(HEIGHT / SIZE)):
            for j in range(0, int(WIDTH / SIZE)):
                self.maze[i][j].matrix_pos_x = i
                self.maze[i][j].matrix_pos_y = j
                if self.maze[i][j].color == PINK:
                    self.maze[i][j].color = BEIGE

    def find_minimum_steps(self, background, player):
        initial_node = self.maze[player.matrix_pos_x][player.matrix_pos_y]
        initial_node.explored1 = True
        find = False
        queue = [initial_node]
        while len(queue) > 0 and not find:
            queue[0].color = PINK
            u = queue.pop(0)
            for i in u.neighbors_connected:
                if not i.explored1:
                    i.parent3 = u
                    i.explored1 = True
                    queue.append(i)
                    if i.matrix_pos_x == self.final_coordinate_x and i.matrix_pos_y == self.final_coordinate_y:
                        find = True
        current = self.maze[self.final_coordinate_x][self.final_coordinate_y]
        while current.parent3 != None:
            current = current.parent3
            self.minimum_steps += 1
        for i in range(0, int(HEIGHT / SIZE)):
            for j in range(0, int(WIDTH / SIZE)):
                self.maze[i][j].matrix_pos_x = i
                self.maze[i][j].matrix_pos_y = j
                if self.maze[i][j].color == PINK:
                    self.maze[i][j].color = BEIGE

    def save_game(self, username):
        with open(username, 'a+') as file:
            for i in range(0, int(HEIGHT / SIZE)):
                for j in range(0, int(WIDTH / SIZE)):
                    self.maze[i][j].matrix_pos_x = i
                    self.maze[i][j].matrix_pos_y = j
                    if self.maze[i][j].color == BEIGE:
                        file.write('0 ')
                    elif self.maze[i][j].color == PURPLE:
                        file.write('1 ')
                    elif self.maze[i][j].color == BLUE:
                        file.write('2 ')
                    if self.maze[i][j].right_border.color == BEIGE:
                        file.write('0 ')
                    elif self.maze[i][j].right_border.color == BLACK:
                        file.write('1 ')
                    if self.maze[i][j].bottom_border.color == BEIGE:
                        file.write('0 ')
                    elif self.maze[i][j].bottom_border.color == BLACK:
                        file.write('1 ')
                    if self.maze[i][j].left_border.color == BEIGE:
                        file.write('0 ')
                    elif self.maze[i][j].left_border.color == BLACK:
                        file.write('1 ')
                    if self.maze[i][j].top_border.color == BEIGE:
                        file.write('0\n')
                    elif self.maze[i][j].top_border.color == BLACK:
                        file.write('1\n')

    def load_game(self, username, name):
        self.minimum_steps = 0
        with open(username, 'r') as file:
            find = False
            i = 0
            j = 0
            for line in file:
                if find:
                    size = line.strip().split()
                    if int(size[0]) == 0:
                        self.maze[i][j].color = BEIGE
                    elif int(size[0]) == 1:
                        self.maze[i][j].color = PURPLE
                    elif int(size[0]) == 2:
                        self.maze[i][j].color = BLUE
                    if int(size[1]) == 0:
                        self.maze[i][j].right_border.color = BEIGE
                    elif int(size[1]) == 1:
                        self.maze[i][j].right_border.color = BLACK
                    if int(size[2]) == 0:
                        self.maze[i][j].bottom_border.color = BEIGE
                    elif int(size[2]) == 1:
                        self.maze[i][j].bottom_border.color = BLACK
                    if int(size[3]) == 0:
                        self.maze[i][j].left_border.color = BEIGE
                    elif int(size[3]) == 1:
                        self.maze[i][j].left_border.color = BLACK
                    if int(size[4]) == 0:
                        self.maze[i][j].top_border.color = BEIGE
                    elif int(size[4]) == 1:
                        self.maze[i][j].top_border.color = BLACK
                    if j < WIDTH / SIZE - 1:
                        j += 1
                    else:
                        j = 0
                        i += 1
                    if i == HEIGHT / SIZE:
                        break
                elif name in line:
                    find = True
                    values = next(file).strip().split()
                    self.initial_coordinate_x = int(values[6])
                    self.initial_coordinate_y = int(values[7])
                    self.final_coordinate_x = int(values[8])
                    self.final_coordinate_y = int(values[9])
        for i in range(0, int(HEIGHT / SIZE)):
            for j in range(0, int(WIDTH / SIZE)):
                self.maze[i][j].matrix_pos_x = i
                self.maze[i][j].matrix_pos_y = j
                self.maze[i][j].neighbors_connected = []
                if self.maze[i][j].right_border.color == BEIGE:
                    self.maze[i][j].neighbors_connected.append(self.maze[i + 1][j])
                if self.maze[i][j].bottom_border.color == BEIGE:
                    self.maze[i][j].neighbors_connected.append(self.maze[i][j + 1])
                if self.maze[i][j].left_border.color == BEIGE:
                    self.maze[i][j].neighbors_connected.append(self.maze[i - 1][j])
                if self.maze[i][j].top_border.color == BEIGE:
                    self.maze[i][j].neighbors_connected.append(self.maze[i][j - 1])

    def draw_jerry(self, background):
        if SIZE == 30:
            background.blit(jerry_easy_mode, (self.final_coordinate_x * SIZE + 1, self.final_coordinate_y * SIZE + 1))
        if SIZE == 15:
            background.blit(jerry_normal_mode, (self.final_coordinate_x * SIZE + 1, self.final_coordinate_y * SIZE + 1))
        if SIZE == 6:
            background.blit(jerry_hard_mode, (self.final_coordinate_x * SIZE + 1, self.final_coordinate_y * SIZE + 1))

    def render(self, background, player):
        if self.maze[player.matrix_pos_x][player.matrix_pos_y].energy_point:
            self.maze[player.matrix_pos_x][player.matrix_pos_y].energy_point = False
        if self.maze[self.final_coordinate_x][self.final_coordinate_y].energy_point:
            self.maze[self.final_coordinate_x][self.final_coordinate_y].energy_point = False
        for i in range(0, int(HEIGHT / SIZE)):
            for j in range(0, int(WIDTH / SIZE)):
                self.maze[i][j].render(background)
                if self.maze[i][j].energy_point:
                    if SIZE == 30:
                        background.blit(cheese_easy_mode, (self.maze[i][j].pos_x + 1, self.maze[i][j].pos_y + 1))
                    if SIZE == 15:
                        background.blit(cheese_normal_mode, (self.maze[i][j].pos_x + 1, self.maze[i][j].pos_y + 1))
                    if SIZE == 6:
                        background.blit(cheese_hard_mode, (self.maze[i][j].pos_x + 1, self.maze[i][j].pos_y + 1))
        if self.maze_created:
            self.maze[self.initial_coordinate_x][self.initial_coordinate_y].color = PURPLE
            self.maze[self.final_coordinate_x][self.final_coordinate_y].color = BLUE

class Player():
    def __init__(self, initial_x, initial_y):
        self.pos_x = initial_x * SIZE + BORDER_THICKNESS
        self.pos_y = initial_y * SIZE + BORDER_THICKNESS
        self.matrix_pos_x = initial_x
        self.matrix_pos_y = initial_y
        self.width = SIZE - 2 * BORDER_THICKNESS
        self.height = SIZE - 2 * BORDER_THICKNESS
        self.color = RED
        self.maze = Maze
        self.steps = 0
        self.remaining_steps = 0
        self.load_time = 0
        self.move_left = True

    def update(self, maze, events):
        for border in [maze[self.matrix_pos_x][self.matrix_pos_y].right_border, maze[self.matrix_pos_x][self.matrix_pos_y].bottom_border, maze[self.matrix_pos_x][self.matrix_pos_y].left_border, maze[self.matrix_pos_x][self.matrix_pos_y].top_border]:
            if border.color == GREEN:
                border.color = BEIGE
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and self.pos_x > BORDER_THICKNESS and maze[self.matrix_pos_x][self.matrix_pos_y].left_border.color != BLACK:
                    if maze[self.matrix_pos_x - 1][self.matrix_pos_y].energy_point:
                        self.remaining_steps += random.randint(1, 5)
                    if maze[self.matrix_pos_x - 1][self.matrix_pos_y].color == GREEN:
                        maze[self.matrix_pos_x - 1][self.matrix_pos_y].color = BEIGE
                    self.pos_x -= SIZE
                    self.matrix_pos_x -= 1
                    self.steps += 1
                    self.remaining_steps -= 1
                    self.move_left = True
                if event.key == pygame.K_RIGHT and self.pos_x + BORDER_THICKNESS < WIDTH - SIZE and maze[self.matrix_pos_x][self.matrix_pos_y].right_border.color != BLACK:
                    if maze[self.matrix_pos_x + 1][self.matrix_pos_y].energy_point:
                        self.remaining_steps += random.randint(1, 5)
                    if maze[self.matrix_pos_x + 1 ][self.matrix_pos_y].color == GREEN:
                        maze[self.matrix_pos_x + 1][self.matrix_pos_y].color = BEIGE
                    self.pos_x += SIZE
                    self.matrix_pos_x += 1
                    self.steps += 1
                    self.remaining_steps -= 1
                    self.move_left = False
                if event.key == pygame.K_UP and self.pos_y > BORDER_THICKNESS and maze[self.matrix_pos_x][self.matrix_pos_y].top_border.color != BLACK:
                    if maze[self.matrix_pos_x][self.matrix_pos_y - 1].energy_point:
                        self.remaining_steps += random.randint(1, 5)
                    if maze[self.matrix_pos_x][self.matrix_pos_y - 1].color == GREEN:
                        maze[self.matrix_pos_x][self.matrix_pos_y - 1].color = BEIGE
                    self.pos_y -= SIZE
                    self.matrix_pos_y -= 1
                    self.steps += 1
                    self.remaining_steps -= 1
                if event.key == pygame.K_DOWN and self.pos_y + BORDER_THICKNESS < HEIGHT - SIZE and maze[self.matrix_pos_x][self.matrix_pos_y].bottom_border.color != BLACK:
                    if maze[self.matrix_pos_x][self.matrix_pos_y + 1].energy_point:
                        self.remaining_steps += random.randint(1, 5)
                    if maze[self.matrix_pos_x][self.matrix_pos_y + 1].color == GREEN:
                        maze[self.matrix_pos_x][self.matrix_pos_y + 1].color = BEIGE
                    self.pos_y += SIZE
                    self.matrix_pos_y += 1
                    self.steps += 1
                    self.remaining_steps -= 1

    def load_game(self, username, name):
        with open(username, 'r') as file:
            for line in file:
                if name in line:
                    values = next(file).strip().split()
                    self.steps = int(values[1])
                    self.remaining_steps = int(values[2])
                    self.load_time = int(values[3])
                    self.matrix_pos_x = int(values[4])
                    self.matrix_pos_y = int(values[5])
                    self.pos_x = int(values[10])
                    self.pos_y = int(values[11])
                    break

    def render(self, background):
        pygame.draw.rect(background, self.color, [self.pos_x, self.pos_y, self.width, self.height])
        if SIZE == 30:
            if self.move_left:
                background.blit(tom_easy_mode, (self.pos_x, self.pos_y))
            else:
                background.blit(pygame.transform.flip(tom_easy_mode, True, False), (self.pos_x, self.pos_y))
        if SIZE == 15:
            if self.move_left:
                background.blit(tom_normal_mode, (self.pos_x, self.pos_y))
            else:
                background.blit(pygame.transform.flip(tom_normal_mode, True, False), (self.pos_x, self.pos_y))
        if SIZE == 6:
            if self.move_left:
                background.blit(tom_hard_mode, (self.pos_x, self.pos_y))
            else:
                background.blit(pygame.transform.flip(tom_hard_mode, True, False), (self.pos_x, self.pos_y))

class Game():
    def __init__(self):
        try:
            pygame.init()
        except:
            print("The pygame module did not start successfully")
        self.background = pygame.display.set_mode(SCREEN_SIZE)
        self.time = 0
        self.username = ''
        self.name = ''
        self.start = False
        self.solved = False
        self.winner = False
        self.random = False
        self.hint = False
        self.end_game = False
        self.logged = False
        self.loaded = False
        self.mute = False

    def load(self):
        self.maze = Maze(self.background)
        self.player = Player(self.maze.initial_coordinate_x, self.maze.initial_coordinate_y)
        if self.random:
            self.maze.initial_coordinate_x = random.randint(0, int(HEIGHT / SIZE) - 1)
            self.maze.initial_coordinate_y = random.randint(0, int(WIDTH / SIZE) - 1)
            self.maze.final_coordinate_x = random.randint(0, int(HEIGHT / SIZE) - 1)
            self.maze.final_coordinate_y = random.randint(0, int(WIDTH / SIZE) - 1)
            while self.maze.final_coordinate_x == self.maze.initial_coordinate_x or self.maze.final_coordinate_y == self.maze.initial_coordinate_y:
                self.maze.final_coordinate_x = random.randint(0, int(HEIGHT / SIZE) - 1)
                self.maze.final_coordinate_y = random.randint(0, int(WIDTH / SIZE) - 1)
            self.maze.create_maze(self.background)
        else:
            self.maze.create_maze(self.background)
            self.maze.render(self.background, self.player)
            self.maze.maze[0][0].color = BEIGE
            self.maze.maze[1][1].color = BEIGE
            initial_coordinate_done = False
            final_coordinate_done = False
            while not initial_coordinate_done or not final_coordinate_done:
                if not self.mute and not pygame.mixer.get_busy():
                    game_music.play()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit(0)
                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos = pygame.mouse.get_pos()
                        if 0 < mouse_pos[0] < 600 and 0 < mouse_pos[1] < 600 and mouse_pos[0] % SIZE != 0 and mouse_pos[1] % SIZE != 0:
                            if not initial_coordinate_done:
                                game_music.stop()
                                button_sound.play()
                                self.maze.initial_coordinate_x = mouse_pos[0] // SIZE
                                self.maze.initial_coordinate_y = mouse_pos[1] // SIZE
                                pygame.draw.rect(self.background, RED, [(mouse_pos[0] // SIZE) * SIZE + 1, (mouse_pos[1] // SIZE) * SIZE + 1, SIZE - 2, SIZE - 2])
                                initial_coordinate_done = True
                            elif not final_coordinate_done:
                                game_music.stop()
                                button_sound.play()
                                self.maze.final_coordinate_x = mouse_pos[0] // SIZE
                                self.maze.final_coordinate_y = mouse_pos[1] // SIZE
                                final_coordinate_done = True
                                pygame.draw.rect(self.background, BLUE, [(mouse_pos[0] // SIZE) * SIZE + 1, (mouse_pos[1] // SIZE) * SIZE + 1, SIZE - 2, SIZE - 2])
                text(self.background, "Click the nodes to select the starting and ending points", WHITE, 30, 25, 630)
                pygame.display.update()
        self.background.blit(bgr, (0, 0))
        self.player = Player(self.maze.initial_coordinate_x, self.maze.initial_coordinate_y)

    def update(self, event):
        if not self.solved and not self.winner:
            self.player.update(self.maze.maze, event)
        if self.player.matrix_pos_x == self.maze.final_coordinate_x and self.player.matrix_pos_y == self.maze.final_coordinate_y:
            self.winner = True

    def load_game(self, username, name):
        with open(username, 'r') as file:
            for line in file:
                if name in line:
                    values = next(file).strip().split()
                    self.final_coordinate_x = int(values[8])
                    self.final_coordinate_y = int(values[9])
                    break

    def initial_game(self):
        game_music.stop()
        while not self.start:
            self.background.blit(bgr, (0, 0))
            text(self.background, "MAZE GAME PROJECT", WHITE, 50, 100, 195)
            mouse_pos = pygame.mouse.get_pos()
            for touch_area in [touch_area6, touch_area7, touch_area8, touch_area9, touch_area10, touch_area11]:
                if touch_area.collidepoint(mouse_pos):
                    draw_rounded_rect(self.background, RED, touch_area, 20)
                else:
                    draw_rounded_rect(self.background, LIGHTBLUE, touch_area, 20)
            text(self.background, "EASY MODE", WHITE, 25, 168, 303)
            text(self.background, "NORMAL MODE", WHITE, 25, 155, 383)
            text(self.background, "HARD MODE", WHITE, 25, 168, 463)
            text(self.background, "LOAD GAME", WHITE, 25, 328, 303)
            text(self.background, "ABOUT US", WHITE, 25, 335, 383)
            text(self.background, "LOG OUT", WHITE, 25, 343, 463)
            if self.mute:
                self.background.blit(speaker_off, (500, 0))
                menu_music.stop()
            else:
                self.background.blit(speaker_on, (500, 0))
                if not pygame.mixer.get_busy():
                    menu_music.play()
            for event in pygame.event.get():
                global SIZE
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area22.collidepoint(event.pos):
                    self.mute = not self.mute
                    menu_music.stop()
                    button_sound.play()
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area11.collidepoint(event.pos):
                    menu_music.stop()
                    button_sound.play()
                    self.logged = False
                    self.username = ''
                    self.name = ''
                    self.run()
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area6.collidepoint(event.pos):
                    menu_music.stop()
                    button_sound.play()
                    SIZE = 30
                    self.start = True
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area8.collidepoint(event.pos):
                    menu_music.stop()
                    button_sound.play()
                    SIZE = 15
                    self.start = True
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area10.collidepoint(event.pos):
                    menu_music.stop()
                    button_sound.play()
                    SIZE = 6
                    self.start = True
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area7.collidepoint(event.pos):
                    menu_music.stop()
                    button_sound.play()
                    name = ''
                    while not self.loaded:
                        self.background.blit(bgr, (0, 0))
                        mouse_pos = pygame.mouse.get_pos()
                        for touch_area in [touch_area10, touch_area11]:
                            if touch_area.collidepoint(mouse_pos):
                                draw_rounded_rect(self.background, RED, touch_area, 20)
                            else:
                                draw_rounded_rect(self.background, LIGHTBLUE, touch_area, 20)
                        text(self.background, "Load game", WHITE, 25, 175, 463)
                        text(self.background, "Back", WHITE, 25, 360, 463)
                        if name == '':
                            text(self.background, "Enter your game name", WHITE, 50, 110, 190)
                        else:
                            text(self.background, name, WHITE, 50, 110, 190)
                        text(self.background, 'List of saved game names:', BLACK, 30, 110, 250)
                        with open(self.username, 'r+') as file:
                            y = 225
                            for line in file:
                                if any(char.isalpha() for char in line):
                                    y += 25
                                    text(self.background, str(line[:-1]), BLACK, 30, 385, y)
                        if self.mute:
                            self.background.blit(speaker_off, (500, 0))
                            menu_music.stop()
                        else:
                            self.background.blit(speaker_on, (500, 0))
                            if not pygame.mixer.get_busy():
                                menu_music.play()
                        for event1 in pygame.event.get():
                            if event1.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)
                            if event1.type == pygame.KEYDOWN and event1.key == pygame.K_BACKSPACE:
                                    name = name[:-1]
                            elif event1.type == pygame.KEYDOWN and event1.key != pygame.K_RETURN:
                                    name += event1.unicode
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area22.collidepoint(event1.pos):
                                self.mute = not self.mute
                                menu_music.stop()
                                button_sound.play()
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area10.collidepoint(event1.pos):
                                menu_music.stop()
                                button_sound.play()
                                if name != '' and valid_name(self.username, name):
                                    name = ''
                                    text(self.background, "This game name", 'salmon', 50, 95, 320)
                                    text(self.background, "does not exit.", 'salmon', 50, 115, 350)
                                    pygame.display.update()
                                    pygame.time.wait(1000)
                                if name != '' and not valid_name(self.username, name):
                                    self.loaded = True
                                    self.name = name
                                    with open(self.username, 'r') as file:
                                        for line in file:
                                            if self.name in line:
                                                SIZE = int(next(file).strip().split()[0])
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area11.collidepoint(event1.pos):
                                menu_music.stop()
                                button_sound.play()
                                self.initial_game()
                        pygame.display.update()
                    self.start = True
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area9.collidepoint(event.pos):
                    menu_music.stop()
                    button_sound.play()
                    back = False
                    while not back:
                        self.background.blit(bgr, (0, 0))
                        text(self.background, "MAZE GAME PROJECT", WHITE, 50, 100, 195)
                        text(self.background, "Project of Group 3 - 23TNT1", BLACK, 35, 135, 275)
                        text(self.background, "23122021 Bui Duy Bao", BLACK, 35, 165, 300)
                        text(self.background, "23122025 Pham Ngoc Duy", BLACK, 35, 145, 325)
                        text(self.background, "23122045 Le Duc Phuc", BLACK, 35, 165, 350)
                        text(self.background, "23122047 Nguyen Xuan Quang", BLACK, 35, 115, 375)
                        text(self.background, "23122050 Nguyen Tan Tai", BLACK, 35, 145, 400)
                        text(self.background, "Press any key to back", BLACK, 35, 170, 425)
                        if self.mute:
                            self.background.blit(speaker_off, (500, 0))
                            menu_music.stop()
                        else:
                            self.background.blit(speaker_on, (500, 0))
                            if not pygame.mixer.get_busy():
                                menu_music.play()
                        for event1 in pygame.event.get():
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area22.collidepoint(event1.pos):
                                self.mute = not self.mute
                                menu_music.stop()
                                button_sound.play()
                            if event1.type == pygame.KEYDOWN:
                                menu_music.stop()
                                button_sound.play()
                                back = True
                        pygame.display.update()
            pygame.display.update()
        if not self.loaded:
            self.select_mode()
        else:
            self.random = True
        self.run_new_size()

    def render(self):
        self.maze.render(self.background, self.player)
        self.maze.draw_jerry(self.background)
        self.player.render(self.background)
        pygame.draw.rect(self.background, BLACK, [0, 600, 150, 80], 1)
        pygame.draw.rect(self.background, RED, [0, 601, 18, 18])
        text(self.background, "- PLAYER", BLACK, 20, 25, 605)
        pygame.draw.rect(self.background, PURPLE, [0, 621, 18, 18])
        text(self.background, "- STARTING POINT", BLACK, 20, 25, 625)
        pygame.draw.rect(self.background, BLUE, [0, 641, 18, 18])
        text(self.background, "- GOAL", BLACK, 20, 25, 645)
        self.background.blit(cheese, (0, 661))
        text(self.background, "- ENERGY POINT", BLACK, 20, 25, 665)
        mouse_pos = pygame.mouse.get_pos()
        for touch_area in [touch_area12, touch_area13, touch_area14, touch_area15, touch_area16, touch_area17, touch_area18]:
            if touch_area.collidepoint(mouse_pos):
                draw_rounded_rect(self.background, RED, touch_area, 10)
            else:
                draw_rounded_rect(self.background, LIGHTBLUE, touch_area, 10)
        for touch_area in [touch_area19, touch_area20, touch_area21]:
            draw_rounded_rect(self.background, LIGHTBLUE, touch_area, 10)
        text(self.background, "SAVE", WHITE, 20, 200, 608)
        text(self.background, "RETRY", WHITE, 20, 300, 608)
        text(self.background, "HINT", WHITE, 20, 410, 608)
        text(self.background, "EXIT", WHITE, 20, 515, 608)
        text(self.background, "BFS", WHITE, 20, 220, 633)
        text(self.background, "DFS", WHITE, 20, 360, 633)
        text(self.background, "BS", WHITE, 20, 505, 633)
        text(self.background, "STEPS: " + str(self.player.steps), WHITE, 20, 350, 658)
        text(self.background, "STEPS LEFT: " + str(2 * self.maze.minimum_steps + self.player.remaining_steps), WHITE, 18, 460, 660)
        if not self.solved and not self.winner:
            if 2 * self.maze.minimum_steps + self.player.remaining_steps == 0:
                self.solved = True
            text(self.background, "TIME: " + str(int((pygame.time.get_ticks() - self.start_time + self.player.load_time) / 10) / 100) + "s", WHITE, 20, 200, 658)
        elif self.winner:
            if not self.end_game:
                self.end_game = True
                self.time = pygame.time.get_ticks()
            text(self.background, "TIME: " + str(int((self.time - self.start_time + self.player.load_time) / 10) / 100) + "s", WHITE, 20, 200, 658)
            pygame.draw.rect(self.background, WHITE, [0, 600, 150, 80])
            pygame.draw.rect(self.background, BLACK, [0, 600, 150, 80], 1)
            text(self.background, "YOU WIN", GREEN, 40, 10, 630)
        else:
            if not self.end_game:
                self.end_game = True
                self.time = pygame.time.get_ticks()
            text(self.background, "TIME: " + str(int((self.time - self.start_time + self.player.load_time) / 10) / 100) + "s", WHITE, 20, 200, 658)
            pygame.draw.rect(self.background, WHITE, [0, 600, 150, 80])
            pygame.draw.rect(self.background, BLACK, [0, 600, 150, 80], 1)
            text(self.background, "YOU LOSE", RED, 40, 5, 630)
        pygame.display.update()

    def select_mode(self):
        menu_music.stop()
        selected = False
        random_mode_clicked = False
        select_mode_clicked = False
        while not selected:
            self.background.blit(bgr, (0, 0))
            text(self.background, "MAZE GAME PROJECT", WHITE, 50, 100, 195)
            mouse_pos = pygame.mouse.get_pos()
            for touch_area in [touch_area4, touch_area5, touch_area10, touch_area11]:
                if touch_area.collidepoint(mouse_pos):
                    draw_rounded_rect(self.background, RED, touch_area, 20)
                else:
                    draw_rounded_rect(self.background, LIGHTBLUE, touch_area, 20)
            if random_mode_clicked:
                draw_rounded_rect(self.background, RED, touch_area4, 20)
            else:
                draw_rounded_rect(self.background, LIGHTBLUE, touch_area4, 20)
            if select_mode_clicked:
                draw_rounded_rect(self.background, RED, touch_area5, 20)
            else:
                draw_rounded_rect(self.background, LIGHTBLUE, touch_area5, 20)
            text(self.background, "Select", WHITE, 35, 183, 458)
            text(self.background, "Back", WHITE, 35, 350, 458)
            text(self.background, "Random location mode", WHITE, 35, 162, 298)
            text(self.background, "Select location mode", WHITE, 35, 175, 378)
            if self.mute:
                self.background.blit(speaker_off, (500, 0))
                game_music.stop()
            else:
                self.background.blit(speaker_on, (500, 0))
                if not pygame.mixer.get_busy():
                    game_music.play()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area22.collidepoint(event.pos):
                    self.mute = not self.mute
                    game_music.stop()
                    button_sound.play()
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area4.collidepoint(event.pos):
                    random_mode_clicked = True
                    select_mode_clicked = False
                    game_music.stop()
                    button_sound.play()
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area5.collidepoint(event.pos):
                    select_mode_clicked = True
                    random_mode_clicked = False
                    game_music.stop()
                    button_sound.play()
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area10.collidepoint(event.pos):
                    game_music.stop()
                    button_sound.play()
                    if random_mode_clicked:
                        self.random = True
                        selected = True
                        self.hint = False
                        self.solved = False
                        self.end_game = False
                    if select_mode_clicked:
                        self.random = False
                        selected = True
                        self.hint = False
                        self.solved = False
                        self.end_game = False
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area11.collidepoint(event.pos):
                    game_music.stop()
                    button_sound.play()
                    self.start = False
                    self.initial_game()
            pygame.display.update()

    def run(self):
        pygame.display.set_caption("Maze Game")
        while not self.logged:
            self.background.blit(bg, (0, 0))
            text(self.background, "MAZE GAME PROJECT", WHITE, 50, 120, 195)
            mouse_pos = pygame.mouse.get_pos()
            for touch_area in [touch_area1, touch_area2, touch_area3]:
                if touch_area.collidepoint(mouse_pos):
                    draw_rounded_rect(self.background, LIGHTBLUE, touch_area, 20)
                else:
                    draw_rounded_rect(self.background, 'blueviolet', touch_area, 20)
            text(self.background, "REGISTER", WHITE, 50, 222, 295)
            text(self.background, "LOGIN", WHITE, 50, 252, 375)
            text(self.background, "EXIT", WHITE, 50, 265, 455)
            if self.mute:
                self.background.blit(speaker_off, (500, 0))
                menu_music.stop()
            else:
                self.background.blit(speaker_on, (500, 0))
                if not pygame.mixer.get_busy():
                    if not pygame.mixer.get_busy():
                        menu_music.play()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area22.collidepoint(event.pos):
                    self.mute = not self.mute
                    menu_music.stop()
                    button_sound.play()
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area1.collidepoint(event.pos):
                    menu_music.stop()
                    button_sound.play()
                    registered = False
                    username_clicked = False
                    password_clicked = False
                    typing_username = False
                    typing_password = False
                    username = ''
                    password = ''
                    while not registered:
                        self.background.blit(bgr, (0, 0))
                        text(self.background, "Create a new account", WHITE, 50, 120, 185)
                        if not username_clicked or (username_clicked and username == ''):
                            text(self.background, "Enter a username", GRAY, 40, 160, 298)
                        if not password_clicked or (password_clicked and password == ''):
                            text(self.background, "Enter a password", GRAY, 40, 160, 378)
                        text(self.background, username, BLACK, 40, 160, 297)
                        text(self.background, '*' * len(password), BLACK, 40, 160, 378)
                        mouse_pos = pygame.mouse.get_pos()
                        for touch_area in [touch_area4, touch_area5]:
                            pygame.draw.rect(self.background, LIGHTBLUE, touch_area, 1)
                        if typing_username:
                            pygame.draw.rect(self.background, RED, touch_area4, 1)
                        if typing_password:
                            pygame.draw.rect(self.background, RED, touch_area5, 1)
                        for touch_area in [touch_area10, touch_area11]:
                            if touch_area.collidepoint(mouse_pos):
                                draw_rounded_rect(self.background, RED, touch_area, 20)
                            else:
                                draw_rounded_rect(self.background, LIGHTBLUE, touch_area, 20)
                        text(self.background, "Create", WHITE, 40, 175, 458)
                        text(self.background, "Back", WHITE, 40, 345, 458)
                        if self.mute:
                            self.background.blit(speaker_off, (500, 0))
                            menu_music.stop()
                        else:
                            self.background.blit(speaker_on, (500, 0))
                            if not pygame.mixer.get_busy():
                                menu_music.play()
                        for event1 in pygame.event.get():
                            if event1.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area22.collidepoint(event1.pos):
                                self.mute = not self.mute
                                menu_music.stop()
                                button_sound.play()
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area4.collidepoint(event1.pos):
                                username_clicked = True
                                typing_username = True
                                typing_password = False
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area5.collidepoint(event1.pos):
                                password_clicked = True
                                typing_password = True
                                typing_username = False
                            if event1.type == pygame.KEYDOWN and event1.key == pygame.K_BACKSPACE:
                                if typing_username:
                                    username = username[:-1]
                                if typing_password:
                                    password = password[:-1]
                            elif event1.type == pygame.KEYDOWN and event1.key != pygame.K_RETURN:
                                if typing_username:
                                    username += event1.unicode
                                if typing_password:
                                    password += event1.unicode
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area10.collidepoint(event1.pos):
                                menu_music.stop()
                                button_sound.play()
                                if username != '' and password != '' and register('data', username):
                                    with open('data', 'a') as file:
                                        file.write(f"\n{username},{password}")
                                    registered = True
                                    draw_rounded_rect(self.background, BLUE, [90, 260, 400, 100], 20)
                                    text(self.background, "Registered successfully.", GREEN, 45, 110, 295)
                                    pygame.display.update()
                                    pygame.time.wait(1000)
                                elif username != '' and password != '' and not register('data', username):
                                    username = ''
                                    password = ''
                                    draw_rounded_rect(self.background, BLUE, [90, 260, 400, 100], 20)
                                    text(self.background, "Name is used. Try again.", 'salmon', 45, 110, 295)
                                    pygame.display.update()
                                    pygame.time.wait(1000)
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area11.collidepoint(event1.pos):
                                menu_music.stop()
                                button_sound.play()
                                registered = True
                        pygame.display.update()
                elif event.type == pygame.MOUSEBUTTONDOWN and touch_area2.collidepoint(event.pos):
                    menu_music.stop()
                    button_sound.play()
                    logged = False
                    username_clicked = False
                    password_clicked = False
                    typing_username = False
                    typing_password = False
                    username = ''
                    password = ''
                    while not logged:
                        self.background.blit(bgr, (0, 0))
                        text(self.background, "Log into account", WHITE, 50, 155, 185)
                        if not username_clicked or (username_clicked and username == ''):
                            text(self.background, "Enter your username", GRAY, 40, 160, 298)
                        if not password_clicked or (password_clicked and password == ''):
                            text(self.background, "Enter your password", GRAY, 40, 160, 378)
                        text(self.background, username, BLACK, 40, 160, 297)
                        text(self.background, '*' * len(password), BLACK, 40, 160, 378)
                        mouse_pos = pygame.mouse.get_pos()
                        for touch_area in [touch_area4, touch_area5]:
                            pygame.draw.rect(self.background, LIGHTBLUE, touch_area, 1)
                        if typing_username:
                            pygame.draw.rect(self.background, RED, touch_area4, 1)
                        if typing_password:
                            pygame.draw.rect(self.background, RED, touch_area5, 1)
                        for touch_area in [touch_area10, touch_area11]:
                            if touch_area.collidepoint(mouse_pos):
                                draw_rounded_rect(self.background, RED, touch_area, 20)
                            else:
                                draw_rounded_rect(self.background, LIGHTBLUE, touch_area, 20)
                        text(self.background, "Log in", WHITE, 40, 178, 458)
                        text(self.background, "Back", WHITE, 40, 345, 458)
                        if self.mute:
                            self.background.blit(speaker_off, (500, 0))
                            menu_music.stop()
                        else:
                            self.background.blit(speaker_on, (500, 0))
                            if not pygame.mixer.get_busy():
                                menu_music.play()
                        for event1 in pygame.event.get():
                            if event1.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area22.collidepoint(event1.pos):
                                self.mute = not self.mute
                                menu_music.stop()
                                button_sound.play()
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area4.collidepoint(event1.pos):
                                username_clicked = True
                                typing_username = True
                                typing_password = False
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area5.collidepoint(event1.pos):
                                password_clicked = True
                                typing_password = True
                                typing_username = False
                            if event1.type == pygame.KEYDOWN and event1.key == pygame.K_BACKSPACE:
                                if typing_username:
                                    username = username[:-1]
                                if typing_password:
                                    password = password[:-1]
                            elif event1.type == pygame.KEYDOWN and event1.key != pygame.K_RETURN:
                                if typing_username:
                                    username += event1.unicode
                                if typing_password:
                                    password += event1.unicode
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area10.collidepoint(event1.pos):
                                menu_music.stop()
                                button_sound.play()
                                if username != '' and password != '' and login('data', username, password):
                                    self.username = username
                                    self.logged = True
                                    logged = True
                                    draw_rounded_rect(self.background, BLUE, [90, 260, 400, 100], 20)
                                    text(self.background, "Logged in successfully.", GREEN, 45, 120, 295)
                                    pygame.display.update()
                                    pygame.time.wait(1000)
                                elif username != '' and password != '' and not login('data', username, password):
                                    username = ''
                                    password = ''
                                    draw_rounded_rect(self.background, BLUE, [90, 260, 400, 100], 20)
                                    text(self.background, "Incorrect. Try again.", 'salmon', 45, 147, 295)
                                    pygame.display.update()
                                    pygame.time.wait(1000)
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area11.collidepoint(event1.pos):
                                logged = True
                                menu_music.stop()
                                button_sound.play()
                        pygame.display.update()
                elif event.type == pygame.QUIT or (event.type == pygame.MOUSEBUTTONDOWN and touch_area3.collidepoint(event.pos)):
                    pygame.quit()
                    sys.exit(0)
            pygame.display.update()
        self.initial_game()

    def run_new_size(self):
        self.load()
        if not self.loaded:
            self.maze.find_minimum_steps(self.background, self.player)
        self.start_time = pygame.time.get_ticks()
        if self.loaded:
            self.maze.load_game(self.username, self.name)
            self.player.load_game(self.username, self.name)
            self.load_game(self.username, self.name)
            self.loaded = False
            menu_music.stop()
        while True:
            if not self.mute and not pygame.mixer.get_busy():
                game_music.play()
            e = pygame.event.get()
            for event in e:
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area13.collidepoint(event.pos):
                    game_music.stop()
                    button_sound.play()
                    self.solved = False
                    self.winner = False
                    self.hint = False
                    self.end_game = False
                    self.run()
                if not self.solved and event.type == pygame.MOUSEBUTTONDOWN and touch_area18.collidepoint(event.pos) and not self.winner and not self.hint:
                    game_music.stop()
                    button_sound.play()
                    self.maze.bs(self.background, self.player)
                    self.solved = True
                if not self.solved and event.type == pygame.MOUSEBUTTONDOWN and touch_area16.collidepoint(event.pos) and not self.winner and not self.hint:
                    game_music.stop()
                    button_sound.play()
                    self.maze.bfs(self.background, self.player)
                    self.solved = True
                if not self.solved and event.type == pygame.MOUSEBUTTONDOWN and touch_area17.collidepoint(event.pos) and not self.winner and not self.hint:
                    game_music.stop()
                    button_sound.play()
                    self.maze.dfs(self.background, self.player)
                    self.solved = True
                if not self.solved and event.type == pygame.MOUSEBUTTONDOWN and touch_area14.collidepoint(event.pos) and not self.winner and not self.hint:
                    game_music.stop()
                    button_sound.play()
                    self.maze.hint(self.background, self.player)
                    self.hint = True
                if event.type == pygame.MOUSEBUTTONDOWN and touch_area15.collidepoint(event.pos):
                    game_music.stop()
                    button_sound.play()
                    self.hint = False
                    self.solved = False
                    self.winner = False
                    self.end_game = False
                    self.initial_game()
                if not self.solved and event.type == pygame.MOUSEBUTTONDOWN and touch_area12.collidepoint(event.pos) and not self.winner and not self.hint:
                    game_music.stop()
                    button_sound.play()
                    saved = False
                    name = ''
                    while not saved:
                        self.background.blit(bgr, (0, 0))
                        mouse_pos = pygame.mouse.get_pos()
                        for touch_area in [touch_area10, touch_area11]:
                            if touch_area.collidepoint(mouse_pos):
                                draw_rounded_rect(self.background, RED, touch_area, 20)
                            else:
                                draw_rounded_rect(self.background, LIGHTBLUE, touch_area, 20)
                        text(self.background, "Save game", WHITE, 25, 175, 463)
                        text(self.background, "Back", WHITE, 25, 360, 463)
                        if name == '':
                            text(self.background, "Enter a game name", WHITE, 50, 115, 190)
                        else:
                            text(self.background, name, WHITE, 50, 115, 190)
                        text(self.background, "Game name must be unique", BLACK, 30, 150, 250)
                        text(self.background, "Game name cannot contain spaces", BLACK, 30, 110, 280)
                        text(self.background, "Game name must be under 15 characters", BLACK, 30, 85, 310)
                        if self.mute:
                            self.background.blit(speaker_off, (500, 0))
                            game_music.stop()
                        else:
                            self.background.blit(speaker_on, (500, 0))
                            if not pygame.mixer.get_busy():
                                game_music.play()
                        for event1 in pygame.event.get():
                            if event1.type == pygame.QUIT:
                                pygame.quit()
                                sys.exit(0)
                            if event1.type == pygame.KEYDOWN and event1.key == pygame.K_BACKSPACE:
                                name = name[:-1]
                            elif event1.type == pygame.KEYDOWN and event1.key != pygame.K_RETURN:
                                name += event1.unicode
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area22.collidepoint(event1.pos):
                                self.mute = not self.mute
                                game_music.stop()
                                button_sound.play()
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area10.collidepoint(event1.pos):
                                game_music.stop()
                                button_sound.play()
                                if name != '' and len(name) < 15 and not valid_name(self.username, name):
                                    name = ''
                                    draw_rounded_rect(self.background, BLUE, [90, 335, 400, 100], 20)
                                    text(self.background, "Name is used. Try again.", 'salmon', 45, 110, 370)
                                    pygame.display.update()
                                    pygame.time.wait(1000)
                                if name != '' and len(name) < 15 and valid_name(self.username, name):
                                    saved = True
                                    with open(self.username, 'a+') as file:
                                        file.write('\n' + name + '\n')
                                        time = int(pygame.time.get_ticks() - self.start_time)
                                        file.write(str(SIZE) + ' ' + str(self.player.steps) + ' ' +
                                                    str(2 * self.maze.minimum_steps + self.player.remaining_steps) + ' ' + str(time) + ' ' +
                                                    str(self.player.matrix_pos_x) + ' ' + str(self.player.matrix_pos_y) + ' ' +
                                                    str(self.maze.initial_coordinate_x) + ' ' + str(self.maze.initial_coordinate_y) + ' ' +
                                                    str(self.maze.final_coordinate_x) + ' ' + str(self.maze.final_coordinate_y) + ' ' +
                                                    str(int(self.player.pos_x)) + ' ' + str(int(self.player.pos_y)) + '\n')
                                    self.maze.save_game(self.username)
                                    draw_rounded_rect(self.background, BLUE, [90, 335, 400, 100], 20)
                                    text(self.background, "Saved successfully.", GREEN, 45, 145, 370)
                                    pygame.display.update()
                                    pygame.time.wait(1000)
                            if event1.type == pygame.MOUSEBUTTONDOWN and touch_area11.collidepoint(event1.pos):
                                game_music.stop()
                                button_sound.play()
                                saved = True
                        pygame.display.update()
            self.update(e)
            self.render()

def main():
    mygame = Game()
    mygame.run()

if __name__ == '__main__':
    main()