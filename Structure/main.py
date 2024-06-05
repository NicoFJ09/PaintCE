#======================================================================================= MAIN IMPORTS =======================================================================================
import pygame
import sys
import os
sys.path.append('../')
from var_consts import *

#======================================================================================= SCREEN IMPORTS =======================================================================================
from Screens.Intro import Intro_screen

from Screens.Menu import Menu_screen

from Screens.Canvas import Canvas_screen

from Screens.Constants import Constants_screen

from Screens.Save import Save_screen

from Screens.Save import Replace_screen




#======================================================================================= GAME SETUP =======================================================================================
#Library initialization
pygame.init()

# Window setup
def update_caption():
  global CURRENT_FILE  # Access the global variable
  pygame.display.set_caption(f"{CURRENT_FILE} - {TITLE}")
# Set initial caption
update_caption()

LOGO = pygame.image.load('Assets/Sprites/Logo.png')
pygame.display.set_icon(LOGO)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Time setup
clock = pygame.time.Clock()

# Font setup
title_font = pygame.font.Font("Assets/Fonts/Roboto-Light.ttf",60)
subtitle_font = pygame.font.Font("Assets/Fonts/Roboto-Regular.ttf",30)
content_font = pygame.font.Font("Assets/Fonts/Roboto-Thin.ttf",20)
icon_font = pygame.font.Font("Assets/Fonts/Roboto-Light.ttf",15)
menu_font = pygame.font.Font("Assets/Fonts/Roboto-Light.ttf",30)
#==============================================a========================================= ASSET IMPORTS =======================================================================================
#Backgrounds
Intro_background = pygame.transform.scale(pygame.image.load("Assets/Backgrounds/Paint_interface_example.png").convert_alpha(), (SCREEN_WIDTH,SCREEN_HEIGHT))

#Sprites

#(INTRO)
New_file = pygame.transform.scale(pygame.image.load("Assets/Sprites/New_file_blue.png").convert_alpha(), (48,48))
Open_file = pygame.transform.scale(pygame.image.load("Assets/Sprites/Open_file_blue.png").convert_alpha(), (48,48))
New_file_hovered = pygame.transform.scale(pygame.image.load("Assets/Sprites/New_file.png").convert_alpha(), (48,48))
Open_file_hovered = pygame.transform.scale(pygame.image.load("Assets/Sprites/Open_file.png").convert_alpha(), (48,48))

#(HEADER)
Menu = pygame.transform.scale(pygame.image.load("Assets/Sprites/Menu.png").convert_alpha(), (40,40))
Save = pygame.transform.scale(pygame.image.load("Assets/Sprites/Save.png").convert_alpha(), (40,40))
Color = pygame.transform.scale(pygame.image.load("Assets/Sprites/Color_mode.png").convert_alpha(), (40,40))
Ascii = pygame.transform.scale(pygame.image.load("Assets/Sprites/ASCII_mode.png").convert_alpha(), (40,40))
Undo = pygame.transform.scale(pygame.image.load("Assets/Sprites/Undo.png").convert_alpha(), (40,40))
Redo = pygame.transform.scale(pygame.image.load("Assets/Sprites/Redo.png").convert_alpha(), (40,40))
#(SUBHEADER)
Zoom_in = pygame.transform.scale(pygame.image.load("Assets/Sprites/Zoom_in.png").convert_alpha(), (40,40))
Zoom_out = pygame.transform.scale(pygame.image.load("Assets/Sprites/Zoom_out.png").convert_alpha(), (40,40))
Size_up = pygame.transform.scale(pygame.image.load("Assets/Sprites/Size_up.png").convert_alpha(), (40,40))
Size_down = pygame.transform.scale(pygame.image.load("Assets/Sprites/Size_down.png").convert_alpha(), (40,40))

#(LATERAL TOOLS)
black_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/black_icon.png"), (45,45))
white_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/white_icon.png"), (45,45))
red_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/red_icon.png"), (45,45))
green_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/green_icon.png"), (45,45))
blue_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/blue_icon.png"), (45,45))
yellow_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/yellow_icon.png"), (45,45))
orange_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/orange_icon.png"), (45,45))
fucsia_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/fucsia_icon.png"), (45,45))
cyan_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/cyan_icon.png"), (45,45))
purple_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/purple_icon.png"), (45,45))

at_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/at_icon.png"), (45,45))
empty_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/white_icon.png"), (45,45))
exclamation_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/exclamation_icon.png"), (45,45))
colon_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/colon_icon.png"), (45,45))
percent_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/percent_icon.png"), (45,45))
hyphen_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/hyphen_icon.png"), (45,45))
equal_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/equal_icon.png"), (45,45))
ampersand_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/ampersand_icon.png"), (45,45))
dot_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/dot_icon.png"), (45,45))
dollar_icon = pygame.transform.scale(pygame.image.load("Assets/Sprites/dollar_icon.png"), (45,45))

Draw = pygame.transform.scale(pygame.image.load("Assets/Sprites/Draw.png").convert_alpha(), (45,45))
Eraser = pygame.transform.scale(pygame.image.load("Assets/Sprites/Eraser.png").convert_alpha(), (45,45))
Inverter = pygame.transform.scale(pygame.image.load("Assets/Sprites/inverter.png").convert_alpha(), (45,45))
high_contrast = pygame.transform.scale(pygame.image.load("Assets/Sprites/high_contrast.png").convert_alpha(), (45,45))
Rotate_left = pygame.transform.scale(pygame.image.load("Assets/Sprites/Rotate_left.png").convert_alpha(), (45,45))
Rotate_right = pygame.transform.scale(pygame.image.load("Assets/Sprites/Rotate_right.png").convert_alpha(), (45,45))
Flip_horizontal = pygame.transform.scale(pygame.image.load("Assets/Sprites/Flip_horizontal.png").convert_alpha(), (45,45))
Flip_vertical = pygame.transform.scale(pygame.image.load("Assets/Sprites/Flip_vertical.png").convert_alpha(), (45,45))

#(SETTINGS)
Back = pygame.transform.scale(pygame.image.load("Assets/Sprites/Back.png").convert_alpha(), (50,50))
Edit = pygame.transform.scale(pygame.image.load("Assets/Sprites/Edit.png").convert_alpha(), (50,50))
See_image = pygame.transform.scale(pygame.image.load("Assets/Sprites/See_image.png").convert_alpha(), (50,50))
See_matrix =pygame.transform.scale(pygame.image.load("Assets/Sprites/See_matrix.png").convert_alpha(), (50,50))
Edit_unselected = pygame.transform.scale(pygame.image.load("Assets/Sprites/Edit_unselected.png").convert_alpha(), (50,50))
See_image_unselected = pygame.transform.scale(pygame.image.load("Assets/Sprites/See_image_unselected.png").convert_alpha(), (50,50))
See_matrix_unselected = pygame.transform.scale(pygame.image.load("Assets/Sprites/See_matrix_unselected.png").convert_alpha(), (50,50))
Close = pygame.transform.scale(pygame.image.load("Assets/Sprites/Close.png").convert_alpha(), (60,60))
#======================================================================================= MAIN FUNCTIONS =======================================================================================
def handle_quit():
    # This function checks the event queue for quit events and handles them
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#======================================================================================= MAIN LOOP =======================================================================================

def main():
    #================================================ CLASS INIT ================================================
    canvas = Canvas_screen()

    while RUNNING:
        global current_screen, menu_x_offset, last_pressed, current_color, selected_action, display_option, orientation_option,display_mode, current_size, mouse_held, Direction, state_saved, save_option, save_option_replace, input_rect, input_text, input_active, canvas_name, cancel_button_rect, save_button_rect, response, CURRENT_FILE, selected_file, files, display_canvas, see_option
        #================================================ SCREEN DISPLAYS ================================================
        
        #DISPLAY INTRO OPTIONS 
        if current_screen == "INTRO":
            screen.fill(GRAY)
            canvas.draw_canvas(screen, display_option, orientation_option, display_mode)
            orientation_option = ""
            buttons = Intro_screen(screen, title_font, content_font,  New_file, Open_file, New_file_hovered, Open_file_hovered)
        
        #DISPLAY CANVAS AND CONSTANTS
        elif current_screen == "CANVAS":
            response = ""
            screen.fill(GRAY)
            canvas.draw_canvas(screen, display_option, orientation_option, display_mode)
            orientation_option = ""
            constants_rects = Constants_screen(screen, icon_font, Menu, Save, Color, Ascii, sprite_names, Undo, Redo, Zoom_in, Zoom_out, Size_up, Size_down, Draw, Eraser, high_contrast, Inverter, Rotate_left, Rotate_right, Flip_horizontal, Flip_vertical, black_icon, white_icon, red_icon, green_icon, blue_icon, yellow_icon, orange_icon, fucsia_icon, cyan_icon, purple_icon, at_icon, empty_icon, exclamation_icon, colon_icon, percent_icon, hyphen_icon, equal_icon, ampersand_icon, dot_icon, dollar_icon, selected_action, display_option, display_mode, current_color)
            #Draw my mouse
            canvas.draw_outline(screen, mouse_pos, current_size, selected_action)
        
        #DISPLAY MENU OPTIONS
        elif current_screen == "MENU":
                if menu_x_offset < 0:
                    menu_x_offset += menu_speed
                screen.fill(WHITE)
                menu_rect_positions, selected_file= Menu_screen(screen, menu_x_offset, menu_font, Back, New_file_hovered, Open_file_hovered, Edit, See_image, See_matrix, Edit_unselected, See_image_unselected, See_matrix_unselected, Close, last_pressed, selected_file, files, see_option)
                if see_option !="":
                    canvas.draw_static_grid(screen, see_option, display_canvas)
        #DISPLAY FILE SAVE
        elif current_screen == "SAVE":
            canvas.draw_canvas(screen, display_option, orientation_option, display_mode)
            orientation_option = ""
            constants_rects = Constants_screen(screen, icon_font, Menu, Save, Color, Ascii, sprite_names, Undo, Redo, Zoom_in, Zoom_out, Size_up, Size_down, Draw, Eraser, high_contrast, Inverter, Rotate_left, Rotate_right, Flip_horizontal, Flip_vertical, black_icon, white_icon, red_icon, green_icon, blue_icon, yellow_icon, orange_icon, fucsia_icon, cyan_icon, purple_icon, at_icon, empty_icon, exclamation_icon, colon_icon, percent_icon, hyphen_icon, equal_icon, ampersand_icon, dot_icon, dollar_icon, selected_action, display_option, display_mode, current_color)
            if response == "File name already exists. Do you want to overwrite it?":
                cancel_button_rect, save_button_rect = Replace_screen(screen, subtitle_font, content_font)
            else:
                input_rect, cancel_button_rect, save_button_rect = Save_screen(screen, title_font, content_font, input_text, input_active)
        
        #================================================ EVENT MANAGEMENT ================================================

        #Check for X pressing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # INTRO SCREEN CONTROLS
            elif current_screen == "INTRO":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    for button in buttons:
                        if button.collidepoint(mouse_pos):
                            #Screen change management
                            if buttons.index(button) == 0:
                                current_screen = "CANVAS"
                                last_pressed = "New"
                                canvas.__init__()
                                print("New")

                            elif buttons.index(button) == 1:
                                current_screen = "MENU"
                                last_pressed = "Open"
                                files = [f for f in os.listdir('paintings') if f.endswith('.txt')]
                                print("Open")
            
            # CANVAS SCREEN CONTROLS
            elif current_screen == "CANVAS":

                #Click detection
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    
                    mouse_pos = event.pos
                    for name, hover_rect in constants_rects.items():
                        if hover_rect.collidepoint(mouse_pos):
                            last_pressed = name
                            print(name)

                            #Display mode toggle
                            if name == "Mode":
                                if sprite_names[1] == "Color":
                                    display_mode = "Ascii"
                                    sprite_names[1] = display_mode
                                else:
                                    display_mode = "Color"
                                    sprite_names[1] = display_mode

                            #Screen history management
                            elif name == "Menu":
                                current_screen = "MENU"
                                menu_x_offset = -SCREEN_WIDTH

                            #SAVE FILE MANAGEMENT
                            elif name == "Save":
                                #Check if file is untitled
                                if CURRENT_FILE == "Untitled":
                                    #Switch to save screen (name input)
                                    current_screen = "SAVE"
                                else:
                                    canvas.resave_to_file("Paintings", CURRENT_FILE + ".txt")

                            elif name == "Undo":
                                canvas.undo()
                            elif name == "Redo":
                                canvas.redo()

                            #Brush size
                            elif name == "Size up" and current_size<101:
                                current_size += 2
                                print(current_size)

                            elif name == "Size down" and current_size>1:
                                current_size -= 2
                                print(current_size)
                            #Save selected color
                            elif name in colors:
                                current_color = name

                            #Save selected action
                            elif name in selectable_actions:
                                selected_action = name

                            #Toggle display options
                            elif name in display_options:
                                
                                if display_option == name:
                                    display_option = ""
                                else:
                                    display_option = name

                            #Change screen orientation
                            elif name in orientation_options:
                                orientation_option = name

                    #Draw condition
                    if selected_action == "Eraser" or selected_action == "Draw":
                        mouse_held = True
                        canvas.draw_on_canvas(mouse_pos, selected_action, current_color, current_size)

                    elif selected_action == "Zoom in":
                        canvas.zoom_in()
                    elif selected_action == "Zoom out":
                        canvas.zoom_out()
                        

                elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                    mouse_held = False
                    # Save the final state when the mouse is released
                    if state_saved:
                        canvas.save_state()
                        state_saved = False
                        

                elif event.type == pygame.MOUSEMOTION:
                    mouse_pos = event.pos
                    if mouse_held:
                        state_saved = True
                        canvas.draw_on_canvas(mouse_pos, selected_action, current_color, current_size)

            # MENU SCREEN CONTROLS
            elif current_screen == "MENU":
                #Click detection
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    #Image manipulation logic
                    for name, menu_rect in menu_rect_positions.items():
                        if menu_rect.collidepoint(mouse_pos):
                            if name == "Back" and see_option =="":
                                current_screen = "CANVAS"
                                last_pressed = "Back"     
                                selected_file = None
                                files = []
                            elif name == "New" and see_option =="":
                                current_screen = "CANVAS"
                                last_pressed = name
                                CURRENT_FILE = "Untitled"
                                update_caption()
                                selected_file = None
                                files = []
                                canvas.__init__()

                            elif name == "Open" and see_option =="":
                                last_pressed = name
                                files = [f for f in os.listdir('paintings') if f.endswith('.txt')]
                            elif last_pressed == "Open" and name.endswith('.txt') and see_option =="":
                                selected_file = name
                                print(f"Selected file: {selected_file}")  # This will print the selected file name
                            elif name == "Edit" and see_option =="":
                                canvas.load_from_file(selected_file)
                                current_screen = "CANVAS"
                                CURRENT_FILE = selected_file[:-4]
                                update_caption()
                            elif name == "See image":
                                display_canvas = canvas.load_matrix_from_file(selected_file)
                                see_option = name
                            elif name == "See matrix":
                                display_canvas = canvas.load_matrix_from_file(selected_file)
                                see_option = name
                            elif name == "Close":
                                see_option = ""
            # SAVE SCREEN CONTROLS
            elif current_screen == "SAVE":
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_pos = event.pos
                    if response == "File name already exists. Do you want to overwrite it?":
                            if cancel_button_rect.collidepoint(event.pos):
                                print("Cancelled")
                                input_text = ""
                                current_screen = "CANVAS"
                                save_option = ""
                            #Check if saving file
                            elif save_button_rect.collidepoint(event.pos):
                                save_option_replace = "Save"

                    else:
                            #Check if start writing
                            if input_rect.collidepoint(event.pos):
                                input_active = True
                            else:
                                input_active = False
                            
                            #Check if cancelled
                            if cancel_button_rect.collidepoint(event.pos):
                                print("Cancelled")
                                input_text = ""
                                current_screen = "CANVAS"
                                save_option = ""
                                response = ""
                            #Check if saving file
                            elif save_button_rect.collidepoint(event.pos):
                                save_option = "Save"
                                print("saved")
                                
                    #Check for input text
                elif event.type == pygame.KEYDOWN and input_active:
                    if event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode

                if save_option == "Save":
                    canvas_name = input_text
                    response = canvas.save_new_to_file("Paintings", canvas_name + ".txt")
                    if response == "File name already exists. Do you want to overwrite it?":
                        if save_option_replace == "Save":
                            canvas.resave_to_file("Paintings", canvas_name + ".txt")
                            current_screen = "CANVAS"
                            CURRENT_FILE = canvas_name
                            update_caption()
                        else:
                            CURRENT_FILE = "Untitled"
                            update_caption()
                    else:
                        CURRENT_FILE = canvas_name
                        update_caption()
                        current_screen = "CANVAS"

        pygame.display.update()
        clock.tick(60)

if __name__== "__main__":
    main()