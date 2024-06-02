import pygame
from var_consts import *

class Canvas_screen:
    def __init__(self):
        self.grid_size = 120
        self.square_size = 6
        self.start_x = 120
        self.start_y = 150
        self.canvas_matrix = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.history = []
        self.current_state = 0
        self.ascii_surface = pygame.Surface((self.grid_size * self.square_size, self.grid_size * self.square_size))
        self.save_state()
        
    def draw_grid(self, screen, display_option, orientation_option, display_mode):
        
        # Pre-render ASCII characters onto the ASCII surface
        if display_mode == "Ascii":
            self.ascii_surface.fill(WHITE)  # Clear the ASCII surface
            font = pygame.font.SysFont('Arial', 8)
            for i in range(self.grid_size):
                for j in range(self.grid_size):
                    if display_option == "":
                        ascii_code = Ascii_codes[self.canvas_matrix[i][j]]
                    elif display_option == "Contrast":
                        ascii_code = Ascii_High_contrast_codes[self.canvas_matrix[i][j]]
                    elif display_option == "Inverter":
                        ascii_code = Ascii_Inverter_codes[self.canvas_matrix[i][j]]
                    color = BLACK  # Default color for characters
                    text_surface = font.render(ascii_code, True, color)
                    text_rect = text_surface.get_rect(center=(j * self.square_size + self.square_size / 2,
                                                            i * self.square_size + self.square_size / 2))
                    self.ascii_surface.blit(text_surface, text_rect)

        # Rotate or flip canvas matrix if needed
        if orientation_option == "Rotate L.":
            self.canvas_matrix = self.rotate_left(self.canvas_matrix)
        elif orientation_option == "Rotate R.":
            self.canvas_matrix = self.rotate_right(self.canvas_matrix)
        elif orientation_option == "Flip h.":
            self.canvas_matrix = self.flip_horizontal(self.canvas_matrix)
        elif orientation_option == "Flip v.":
            self.canvas_matrix = self.flip_vertical(self.canvas_matrix)

        # Draw squares or ASCII characters onto the screen
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if display_mode == "Color":
                    if display_option == "":
                        color_name = colors_codes[self.canvas_matrix[i][j]]
                        color = colors[color_name]
                    elif display_option == "Contrast":
                        color_name = High_contrast_codes[self.canvas_matrix[i][j]]
                        color = colors[color_name]
                    elif display_option == "Inverter":
                        color_name = Inverter_codes[self.canvas_matrix[i][j]]
                        color = colors[color_name]
                    
                    pygame.draw.rect(screen, color, (self.start_x + j * self.square_size, self.start_y + i * self.square_size,
                                                    self.square_size, self.square_size))

                elif display_mode == "Ascii":
                    # Blit the pre-rendered ASCII characters from the ASCII surface
                    screen.blit(self.ascii_surface, (self.start_x, self.start_y))
                    return  # No need to iterate through all cells when rendering ASCII mode


        # Draw horizontal lines
        for i in range(self.grid_size + 1):
            pygame.draw.line(screen, GRAY, (self.start_x, self.start_y + i * self.square_size),
                             (self.start_x + self.grid_size * self.square_size, self.start_y + i * self.square_size), 1)
        # Draw vertical lines
        for j in range(self.grid_size + 1):
            pygame.draw.line(screen, GRAY, (self.start_x + j * self.square_size, self.start_y),
                             (self.start_x + j * self.square_size, self.start_y + self.grid_size * self.square_size), 1)

    def draw_canvas(self, screen, display_option, orientation_option, display_mode):
        self.draw_grid(screen, display_option, orientation_option, display_mode)


    def draw_on_canvas(self, mouse_pos, selected_action, current_color, current_size):
        x, y = mouse_pos
        # Convert mouse coordinates to canvas coordinates
        canvas_x = (x - self.start_x) // self.square_size
        canvas_y = (y - self.start_y) // self.square_size
        # Update canvas matrix based on the selected action
        if 0 <= canvas_x < self.grid_size and 0 <= canvas_y < self.grid_size:
            if display_mode == "Color":
                if selected_action == "Draw" and current_color != "":
                    self.fill_canvas(canvas_x, canvas_y, current_size, Draw_color_reading[current_color])
                elif selected_action == "Eraser":
                    self.fill_canvas(canvas_x, canvas_y, current_size, 0)  # Set the corresponding cell to 0 (white)

    def fill_canvas(self, start_x, start_y, size, value):
        for i in range(start_y, min(start_y + size, self.grid_size)):
            for j in range(start_x, min(start_x + size, self.grid_size)):
                self.canvas_matrix[i][j] = value

    def draw_outline(self, screen, mouse_pos, current_size):
        x, y = mouse_pos
        # Convert mouse coordinates to canvas coordinates
        canvas_x = (x - self.start_x) // self.square_size
        canvas_y = (y - self.start_y) // self.square_size
        # Check if the mouse is within the canvas area
        if 0 <= canvas_x < self.grid_size and 0 <= canvas_y < self.grid_size:
            # Draw outline representing painting area
            outline_size = current_size * self.square_size
            outline_rect = pygame.Rect(self.start_x + canvas_x * self.square_size, 
                                    self.start_y + canvas_y * self.square_size, 
                                    outline_size, outline_size)
            pygame.draw.rect(screen, RED, outline_rect, 1)


    def save_state(self):
        # Save the current canvas matrix to the history list
        self.history = self.history[:self.current_state + 1]
        self.history.append([row[:] for row in self.canvas_matrix])
        self.current_state += 1

    def undo(self):
        if self.current_state > 0:
            self.current_state -= 1
            self.canvas_matrix = [row[:] for row in self.history[self.current_state]]


    def redo(self):
        if self.current_state < len(self.history) - 1:
            self.current_state += 1
            self.canvas_matrix = [row[:] for row in self.history[self.current_state]]

    def rotate_left(self, matrix):
        # Rotate the matrix 90 degrees to the left
        return [list(row) for row in zip(*matrix[::-1])]

    def rotate_right(self, matrix):
        # Rotate the matrix 90 degrees to the right
        return [list(row) for row in zip(*matrix)][::-1]

    def flip_horizontal(self, matrix):
        # Flip the matrix horizontally
        return [row[::-1] for row in matrix]

    def flip_vertical(self, matrix):
        # Flip the matrix vertically
        return matrix[::-1]


    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for row in self.canvas_matrix:
                f.write(' '.join(map(str, row)) + '\n')
