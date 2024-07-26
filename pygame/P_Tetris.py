import pygame
import random

# 初始化屏幕和方块大小
pygame.init()
screen_width, screen_height = 640, 480
block_size = 20

# 创建游戏窗口
screen = pygame.display.set_mode((screen_width, screen_height))

# 定义颜色
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# 定义方块种类
shapes = [
    [(0, 0), (1, 0), (0, 1), (1, 1)],  # 方形
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # 横条
    [(0, 0), (1, 0), (2, 0), (2, 1)],  # L形
    [(0, 0), (1, 0), (2, 0), (2, -1)],  # 反L形
    [(0, 0), (1, 0), (1, 1), (2, 1)],  # Z形
    [(0, 0), (1, 0), (1, -1), (2, -1)],  # 反Z形
    [(0, 0), (1, 0), (2, 0), (1, 1)]  # T形
]

# 定义方块类
class Block:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = screen_width // 2
        self.y = 0
        
    # 将方块按照偏移量移动
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        
    # 将方块向左移动
    def move_left(self):
        self.move(-block_size, 0)
        
    # 将方块向右移动
    def move_right(self):
        self.move(block_size, 0)
        
    # 将方块向下移动
    def move_down(self):
        self.move(0, block_size)
        
    # 将方块向上移动
    def move_up(self):
        self.move(0, -block_size)
        
    # 获取方块当前的位置和形状
    def get_state(self):
        return [(self.x + dx * block_size, self.y + dy * block_size) for dx, dy in self.shape], self.color

# 定义游戏类
class Game:
    def __init__(self):
        self.block = Block(random.choice(shapes), random.choice([RED, GREEN, BLUE, YELLOW]))
        self.score = 0
        
    # 检查方块是否可以放置
    def check_collision(self, shape):
        return any(
            0 > x or x >= screen_width or y >= screen_height
            or (x, y) in self.grid
            for x, y in shape
        )
        
    # 将方块固定在格子里
    def add_to_grid(self):
        for x, y in self.block.shape:
            self.grid[self.block.x + x * block_size, self.block.y + y * block_size] = self.block.color
            
    # 处理完整的行
    def handle_lines(self):
        full_lines = []
        for y in range(screen_height):
            if all((x, y) in self.grid for x in range(0, screen_width, block_size)):
                full_lines.append(y)
        for y in sorted(full_lines, reverse=True):
            for x in range(0, screen_width, block_size):
                del self.grid[x, y]
            for x, y in list(self.grid.items()):
                if y < y:
                    self.grid[x, y + block_size] = self.grid.pop((x, y))
            self.score += 100
        
    # 刷新游戏界面
    def draw(self):
        screen.fill(BLACK)
        pygame.draw.rect(screen, WHITE, (0, 0, screen_width, screen_height), 5)
        for (x, y), color in self.grid.items():
            pygame.draw.rect(screen, color, (x, y, block_size, block_size))
        for (x, y) in self.block.shape:
            pygame.draw.rect(screen, self.block.color, (self.block.x + x * block_size, self.block.y + y * block_size, block_size, block_size))
        pygame.display.update()
        
    # 主循环
    def run(self):
        clock = pygame.time.Clock()
        self.grid = {}
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if not self.check_collision([(x - block_size, y) for x, y in self.block.shape]):
                            self.block.move_left()
                    elif event.key == pygame.K_RIGHT:
                        if not self.check_collision([(x + block_size, y) for x, y in self.block.shape]):
                            self.block.move_right()
                    elif event.key == pygame.K_UP:
                        new_shape = [(y, -x) for x, y in self.block.shape]
                        if not self.check_collision([(self.block.x + x * block_size, self.block.y + y * block_size) for x, y in new_shape]):
                            self.block.shape = new_shape
                    elif event.key == pygame.K_DOWN:
                        if not self.check_collision([(x, y + block_size) for x, y in self.block.shape]):
                            self.block.move_down()
                            
            # 将方块固定在格子里
            if self.check_collision([(x, y + block_size) for x, y in self.block.shape]):
                self.add_to_grid()
                self.handle_lines()
                self.block = Block(random.choice(shapes), random.choice([RED, GREEN, BLUE, YELLOW]))
                if self.check_collision(self.block.shape):
                    self.__init__()
            
            # 画出游戏界面
            self.draw()
            
            # 控制游戏速度
            clock.tick(10)
            
# 运行游戏
if __name__ == '__main__':
    game = Game()
    game.run()
    pygame.quit()
