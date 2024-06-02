#======================================================================================= MAIN IMPORTS =======================================================================================
import pygame
import sys
sys.path.append('../')
import os
from var_consts import *

#======================================================================================= SCREEN IMPORTS =======================================================================================
from Screens.Intro import Intro_screen

from Screens.Menu import Menu_screen

from Screens.Canvas import Canvas_screen

from Screens.Constants import Constants_screen

#======================================================================================= GAME SETUP =======================================================================================
#Library initialization
pygame.init()

# Window setup
FILE_STATE="Untitled"
pygame.display.set_caption(f"{FILE_STATE} - {TITLE}")
LOGO = pygame.image.load('Assets/Sprites/Logo.png')
pygame.display.set_icon(LOGO)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Time setup
clock = pygame.time.Clock()

# Font setup
title_font = pygame.font.Font("Assets/Fonts/Roboto-Light.ttf",60)
content_font = pygame.font.Font("Assets/Fonts/Roboto-Thin.ttf",20)
icon_font = pygame.font.Font("Assets/Fonts/Roboto-Light.ttf",15)
menu_font = pygame.font.Font("Assets/Fonts/Roboto-Light.ttf",30)
#======================================================================================= ASSET IMPORTS =======================================================================================
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
Load = pygame.transform.scale(pygame.image.load("Assets/Sprites/Load.png").convert_alpha(), (40,40))
Color = pygame.transform.scale(pygame.image.load("Assets/Sprites/Color_mode.png").convert_alpha(), (40,40))
Ascii = pygame.transform.scale(pygame.image.load("Assets/Sprites/ASCII_mode.png").convert_alpha(), (40,40))
Undo = pygame.transform.scale(pygame.image.load("Assets/Sprites/Undo.png").convert_alpha(), (40,40))
Redo = pygame.transform.scale(pygame.image.load("Assets/Sprites/Redo.png").convert_alpha(), (40,40))
#(SUBHEADER)
Select = pygame.transform.scale(pygame.image.load("Assets/Sprites/Select.png").convert_alpha(), (40,40))
Zoom_in = pygame.transform.scale(pygame.image.load("Assets/Sprites/Zoom_in.png").convert_alpha(), (40,40))
Zoom_out = pygame.transform.scale(pygame.image.load("Assets/Sprites/Zoom_out.png").convert_alpha(), (40,40))
Size = pygame.transform.scale(pygame.image.load("Assets/Sprites/Size.png").convert_alpha(), (40,40))

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
"""
    0 : " ",
    1 : ".",
    2 : ":",
    3 : "-",
    4 : "=",
    5 : "¡",
    6 : "&",
    7 : "$",
    8 : "%",
    9 : "@"

    "White": 0,
    "Cyan" : 1,
    "Green" : 2,
    "Yellow" : 3,
    "Orange" : 4,
    "Red" : 5,
    "Fucsia" : 6,
    "Purple": 7,
    "Blue" : 8,
    "Black" : 9
"""
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
Scrollbar = pygame.transform.scale(pygame.image.load("Assets/Sprites/Scrollbar.png").convert_alpha(), (50,50))
Scrollbar_pointer = pygame.transform.scale(pygame.image.load("Assets/Sprites/Scrollbar_pointer.png").convert_alpha(), (50,50))

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
        global current_screen, menu_x_offset, last_pressed, current_color, selected_action, display_option, orientation_option,display_mode, current_size, mouse_held, state_saved 
        #================================================ SCREEN DISPLAYS ================================================
        
        if current_screen == "INTRO":
            screen.fill(GRAY)
            canvas.draw_canvas(screen, display_option, orientation_option, display_mode)
            orientation_option = ""
            buttons = Intro_screen(screen, title_font, content_font,  New_file, Open_file, New_file_hovered, Open_file_hovered)
        
        elif current_screen == "CANVAS":
            screen.fill(GRAY)
            canvas.draw_canvas(screen, display_option, orientation_option, display_mode)
            orientation_option = ""
            constants_rects = Constants_screen(screen, icon_font, Menu, Save, Load, Color, Ascii, sprite_names, Undo, Redo, Select, Zoom_in, Zoom_out, Draw, Eraser, high_contrast, Inverter, Rotate_left, Rotate_right, Flip_horizontal, Flip_vertical, black_icon, white_icon, red_icon, green_icon, blue_icon, yellow_icon, orange_icon, fucsia_icon, cyan_icon, purple_icon, at_icon, empty_icon, exclamation_icon, colon_icon, percent_icon, hyphen_icon, equal_icon, ampersand_icon, dot_icon, dollar_icon, selected_action, display_option, display_mode, current_color)
            #Draw my mouse
            canvas.draw_outline(screen, mouse_pos, current_size)

        elif current_screen == "MENU":
                if menu_x_offset < 0:
                    menu_x_offset += menu_speed
                screen.fill(WHITE)
                menu_rect_positions = Menu_screen(screen, menu_x_offset, menu_font, Back, New_file_hovered, Open_file_hovered, Edit, See_image, See_matrix, Edit_unselected, See_image_unselected, See_matrix_unselected, last_pressed)
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
                                print("New")

                            elif buttons.index(button) == 1:
                                current_screen = "MENU"
                                last_pressed = "Open"
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
                                if sprite_names[2] == "Color":
                                    display_mode = "Ascii"
                                    sprite_names[2] = display_mode
                                else:
                                    display_mode = "Color"
                                    sprite_names[2] = display_mode

                            #Screen history management
                            elif name == "Menu":
                                current_screen = "MENU"
                                menu_x_offset = -SCREEN_WIDTH

                            elif name == "Save":
                                canvas.save_to_file('canvas_data.txt')
                                
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
                    if selected_action != "":
                        mouse_held = True
                        canvas.draw_on_canvas(mouse_pos, selected_action, current_color, current_size)



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
                    #Screen change management
                    if menu_rect_positions["Back"].collidepoint(mouse_pos):
                        current_screen = "CANVAS"
                        last_pressed = "Back"
                    #Image manipulation logic
                    for name, menu_rect in menu_rect_positions.items():
                        if menu_rect.collidepoint(mouse_pos):
                            last_pressed = name
                            print(name)
    
                    

        pygame.display.update()
        clock.tick(60)

if __name__== "__main__":
    main()