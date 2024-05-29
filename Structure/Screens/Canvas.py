import pygame
from var_consts import *

class Canvas_screen:
    def __init__(self):
        self.grid_size = 120
        self.square_size = 6
        self.start_x = 120
        self.start_y = 150
        self.canvas_matrix = [[0] * self.grid_size for _ in range(self.grid_size)]

    def draw_grid(self, screen, display_option):
        # Iterate through the canvas matrix and draw squares based on the values
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if display_option == "":
                    color_name = colors_codes[self.canvas_matrix[i][j]]
                    color = colors[color_name]
                elif display_option == "Contrast":
                    color_name = High_contrast_codes[self.canvas_matrix[i][j]]
                    color = colors[color_name]
                elif display_option ==  "Inverter":
                    color_name = Inverter_codes[self.canvas_matrix[i][j]]
                    color = colors[color_name]  
                pygame.draw.rect(screen, color, (self.start_x + j * self.square_size, self.start_y + i * self.square_size,
                                                    self.square_size, self.square_size))
        # Draw horizontal lines
        for i in range(self.grid_size + 1):
            pygame.draw.line(screen, GRAY, (self.start_x, self.start_y + i * self.square_size),
                             (self.start_x + self.grid_size * self.square_size, self.start_y + i * self.square_size), 1)
        # Draw vertical lines
        for j in range(self.grid_size + 1):
            pygame.draw.line(screen, GRAY, (self.start_x + j * self.square_size, self.start_y),
                             (self.start_x + j * self.square_size, self.start_y + self.grid_size * self.square_size), 1)

    def draw_canvas(self, screen, display_option):
        self.draw_grid(screen, display_option)


    def draw_on_canvas(self, mouse_pos, selected_action, current_color):
        x, y = mouse_pos
        # Convert mouse coordinates to canvas coordinates
        canvas_x = (x - self.start_x) // self.square_size
        canvas_y = (y - self.start_y) // self.square_size
        # Update canvas matrix based on the selected action
        if 0 <= canvas_x < self.grid_size and 0 <= canvas_y < self.grid_size:
            if selected_action == "Draw" and current_color!="":
                self.canvas_matrix[canvas_y][canvas_x] = Draw_color_reading[current_color]  # Set the corresponding cell to the current color
            elif selected_action == "Eraser":
                self.canvas_matrix[canvas_y][canvas_x] = 0  # Set the corresponding cell to 0 (white)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.canvas_matrix:
                f.write(' '.join(map(str, row)) + '\n')
