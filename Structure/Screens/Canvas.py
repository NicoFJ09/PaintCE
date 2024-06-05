import pygame
from var_consts import *
import os


class Canvas_screen:
    #Attributes initialization
    def __init__(self):
        self.grid_size = 120
        self.square_size = 6
        self.start_x = 120
        self.start_y = 150
        self.canvas_matrix = [[0] * self.grid_size for _ in range(self.grid_size)]
        #Undo redo attributes
        self.history = []
        self.current_state = 0
        #Display modes attributes
        self.ascii_surface = pygame.Surface((self.grid_size * self.square_size, self.grid_size * self.square_size))
        #Save attribute
        self.save_state()


        #Zoom attributes
        self.zoom_factor = 1.0
        self.zoom_max = 5.0
        self.zoom_min = 1.0  # Minimum zoom size 1
        self.zoom_rect = pygame.Rect(self.start_x, self.start_y, self.grid_size * self.square_size, self.grid_size * self.square_size)
        

    #Draw both the grid pattern in a predetermined white per square and create all conditions to manipulate said grid
    def draw_grid(self, screen, display_option, orientation_option, display_mode):


        scaled_square_size = int(self.square_size * self.zoom_factor)
        # Determinar las coordenadas de inicio y fin dentro del área visible
        start_i = max(0, (self.zoom_rect.top - self.start_y) // scaled_square_size)
        end_i = min(self.grid_size, (self.zoom_rect.bottom - self.start_y) // scaled_square_size + 1)
        start_j = max(0, (self.zoom_rect.left - self.start_x) // scaled_square_size)
        end_j = min(self.grid_size, (self.zoom_rect.right - self.start_x) // scaled_square_size + 1)


        # Pre-render ASCII characters onto the ASCII surface
        if display_mode == "Ascii":
            self.ascii_surface.fill(WHITE)  # Clear the ASCII surface
            font = pygame.font.SysFont('Arial', 8)
            for i in range(start_i, end_i):
                for j in range(start_j, end_j):
                    if display_option == "":
                        ascii_code = Ascii_codes[self.canvas_matrix[i][j]]
                    elif display_option == "Contrast":
                        ascii_code = Ascii_High_contrast_codes[self.canvas_matrix[i][j]]
                    elif display_option == "Inverter":
                        ascii_code = Ascii_Inverter_codes[self.canvas_matrix[i][j]]
                    color = BLACK  # Default color for characters
                    text_surface = font.render(ascii_code, True, color)
                    text_rect = text_surface.get_rect(center=(j * scaled_square_size + scaled_square_size / 2,
                                                            i * scaled_square_size + scaled_square_size / 2))
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


        # Draw squares for color mode onto the screen
        for i in range(start_i, end_i):
            for j in range(start_j, end_j):
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
                   
                    pygame.draw.rect(screen, color, (self.start_x + j * scaled_square_size, self.start_y + i * scaled_square_size,
                                                    scaled_square_size, scaled_square_size))


                elif display_mode == "Ascii":
                    # Blit the pre-rendered ASCII characters from the ASCII surface
                    screen.blit(self.ascii_surface, (self.start_x, self.start_y))
                    return  # No need to iterate through all cells when rendering ASCII mode

        # Draw horizontal lines
        for i in range(self.grid_size + 1):
            pygame.draw.line(screen, GRAY, (self.start_x, self.start_y + i * scaled_square_size),
                             (self.start_x + self.grid_size * scaled_square_size, self.start_y + i * scaled_square_size), 1)
        # Draw vertical lines
        for j in range(self.grid_size + 1):
            pygame.draw.line(screen, GRAY, (self.start_x + j * scaled_square_size, self.start_y),
                             (self.start_x + j * scaled_square_size, self.start_y + self.grid_size * scaled_square_size), 1)


    #To draw and erase on the canvas
    def draw_on_canvas(self, mouse_pos, selected_action, current_color, current_size):
        x, y = mouse_pos
        # Convert mouse coordinates to canvas coordinates
        canvas_x = (x - self.start_x) // int(self.square_size * self.zoom_factor)
        canvas_y = (y - self.start_y) // int(self.square_size * self.zoom_factor)
        # Update canvas matrix based on the selected action
        if 0 <= canvas_x < self.grid_size and 0 <= canvas_y < self.grid_size:
            if selected_action == "Draw" and current_color != "":
                self.fill_canvas(canvas_x, canvas_y, current_size, Draw_color_reading[current_color])
            elif selected_action == "Eraser":
                self.fill_canvas(canvas_x, canvas_y, current_size, 0)  # Set the corresponding cell to 0 (white)

    #To manage the color display per pixel
    def fill_canvas(self, start_x, start_y, size, value):
        for i in range(start_y, min(start_y + size, self.grid_size)):
            for j in range(start_x, min(start_x + size, self.grid_size)):
                self.canvas_matrix[i][j] = value

    #Outline that represents the size of the brush
    def draw_outline(self, screen, mouse_pos, current_size, selected_action):
        x, y = mouse_pos
        # Convert mouse coordinates to canvas coordinates
        scaled_square_size = int(self.square_size * self.zoom_factor)
        canvas_x = (x - self.start_x) // int(self.square_size * self.zoom_factor)
        canvas_y = (y - self.start_y) // int(self.square_size * self.zoom_factor)


        if selected_action == "Draw" or selected_action == "Eraser":
            # Check if the mouse is within the canvas area
            if 0 <= canvas_x < self.grid_size and 0 <= canvas_y < self.grid_size:
                # Draw outline representing painting area
                outline_size = current_size * scaled_square_size
                outline_rect = pygame.Rect(self.start_x + canvas_x * scaled_square_size,
                                        self.start_y + canvas_y * scaled_square_size,
                                        outline_size, outline_size)
                pygame.draw.rect(screen, RED, outline_rect, 1)

    #Variable to manage the undo and redo functions
    def save_state(self):
        # Save the current canvas matrix to the history list
        self.history = self.history[:self.current_state + 1]
        self.history.append([row[:] for row in self.canvas_matrix])
        self.current_state += 1

    #Go back on progress
    def undo(self):
        if self.current_state > 0:
            self.current_state -= 1
            self.canvas_matrix = [row[:] for row in self.history[self.current_state]]

    #Advance after going back
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


    #Get a closer view of the grid
    def zoom_in(self):
       
        self.zoom_factor = min(self.zoom_max, self.zoom_factor + 0.1)
        self.update_zoom_rect()

    #Go further after getting closer
    def zoom_out(self):
        self.zoom_factor = max(self.zoom_min, self.zoom_factor - 0.1)
        self.update_zoom_rect()

    #Update the grid display
    def update_zoom_rect(self):
        new_width = int(self.grid_size * self.square_size * self.zoom_factor)
        new_height = int(self.grid_size * self.square_size * self.zoom_factor)
        center_x, center_y = self.zoom_rect.center  # Use mouse position as center
        self.zoom_rect = pygame.Rect(
            center_x - new_width // 2,
            center_y - new_height // 2,
            new_width,
            new_height
        )
        self.limit_zoom_rect()

    #Establish limits regarding the canvas dimensions
    def limit_zoom_rect(self):
        min_width = self.grid_size * self.square_size
        min_height = self.grid_size * self.square_size


        if self.zoom_rect.width < min_width:
            self.zoom_rect.width = min_width
        if self.zoom_rect.height < min_height:
            self.zoom_rect.height = min_height


        if self.zoom_rect.left < self.start_x:
            self.zoom_rect.left = self.start_x
        if self.zoom_rect.top < self.start_y:
            self.zoom_rect.top = self.start_y
        if self.zoom_rect.right > self.start_x + self.grid_size * self.square_size:
            self.zoom_rect.right = self.start_x + self.grid_size * self.square_size
        if self.zoom_rect.bottom > self.start_y + self.grid_size * self.square_size:
            self.zoom_rect.bottom = self.start_y + self.grid_size * self.square_size

    #Save a new file that was previously untitled
    def save_new_to_file(self, directory, filename):
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, filename)
       
        if os.path.exists(file_path):
            return "File name already exists. Do you want to overwrite it?"


        with open(file_path, 'w') as f:
            for row in self.canvas_matrix:
                f.write(' '.join(map(str, row)) + '\n')
        return "Successfully saved file"

    #Resave the file to update content
    def resave_to_file(self, directory, filename):
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_path = os.path.join(directory, filename)


        with open(file_path, 'w') as f:
            for row in self.canvas_matrix:
                f.write(' '.join(map(str, row)) + '\n')

    #Load a txt from the paintings directory
    def load_from_file(self, filename):
        directory = "paintings"
        file_path = os.path.join(directory, filename)
        try:
            with open(file_path, 'r') as f:
                self.canvas_matrix = [list(map(int, line.split())) for line in f]
            self.save_state()
            return "File loaded successfully"
        except Exception as e:
            return f"Error loading file: {str(e)}"

    #Pull the matrix from the directory to manage the see image and see matrix functions
    def load_matrix_from_file(self, filename):
        directory = "paintings"
        file_path = os.path.join(directory, filename)
        try:
            with open(file_path, 'r') as f:
                matrix = [list(map(int, line.split())) for line in f]
            return matrix
        except Exception as e:
            print(f"Error loading file: {str(e)}")
            return None

    #Display the matrix after recieving its values through load matrix from file and processing in main
    def draw_static_grid(self, screen, display_mode, matrix):
        # Calculate the center position based on the screen size and grid size
        center_x = 3*(SCREEN_WIDTH - self.grid_size * self.square_size) // 4
        center_y = (SCREEN_HEIGHT - self.grid_size * self.square_size) // 2


        if display_mode == "See matrix" and matrix:
            ascii_surface = pygame.Surface((self.grid_size * self.square_size, self.grid_size * self.square_size))
            ascii_surface.fill(WHITE)
            font = pygame.font.SysFont('Arial', 8)
            for i in range(self.grid_size):
                for j in range(self.grid_size):
                    ascii_code = Ascii_codes[matrix[i][j]]
                    text_surface = font.render(ascii_code, True, BLACK)
                    text_rect = text_surface.get_rect(center=(j * self.square_size + self.square_size / 2,
                                                            i * self.square_size + self.square_size / 2))
                    ascii_surface.blit(text_surface, text_rect)
            screen.blit(ascii_surface, (center_x, center_y))
            return


        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if display_mode == "See image":
                    color_name = colors_codes[matrix[i][j]]
                    color = colors[color_name]
                    pygame.draw.rect(screen, color, (center_x + j * self.square_size, center_y + i * self.square_size,
                                                    self.square_size, self.square_size))
                   
        for i in range(self.grid_size + 1):
            pygame.draw.line(screen, (128, 128, 128), (center_x, center_y + i * self.square_size),
                             (center_x + self.grid_size * self.square_size, center_y + i * self.square_size), 1)
            pygame.draw.line(screen, (128, 128, 128), (center_x + i * self.square_size, center_y),
                             (center_x + i * self.square_size, center_y + self.grid_size * self.square_size), 1)

