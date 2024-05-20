import pygame
from var_consts import *

class Canvas_screen:
    def __init__(self):
        self.grid_size = 120
        self.square_size = 6
        self.start_x = 120
        self.start_y = 150
        self.canvas_matrix = [[0] * self.grid_size for _ in range(self.grid_size)]

    def draw_grid(self, screen):
        # Iterate through the canvas matrix and draw squares based on the values
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.canvas_matrix[i][j] == 1:  # If the value is 1, draw a black square
                    pygame.draw.rect(screen, BLACK, (self.start_x + j * self.square_size, self.start_y + i * self.square_size,
                                                      self.square_size, self.square_size))
                else:  # Otherwise, draw a white square
                    pygame.draw.rect(screen, WHITE, (self.start_x + j * self.square_size, self.start_y + i * self.square_size,
                                                      self.square_size, self.square_size))

        # Draw horizontal lines
        for i in range(self.grid_size + 1):
            pygame.draw.line(screen, GRAY, (self.start_x, self.start_y + i * self.square_size),
                             (self.start_x + self.grid_size * self.square_size, self.start_y + i * self.square_size), 1)
        # Draw vertical lines
        for j in range(self.grid_size + 1):
            pygame.draw.line(screen, GRAY, (self.start_x + j * self.square_size, self.start_y),
                             (self.start_x + j * self.square_size, self.start_y + self.grid_size * self.square_size), 1)

    def draw_canvas(self, screen):
        self.draw_grid(screen)
