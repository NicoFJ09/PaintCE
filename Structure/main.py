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
Draw = pygame.transform.scale(pygame.image.load("Assets/Sprites/Edit.png").convert_alpha(), (45,45))
Eraser = pygame.transform.scale(pygame.image.load("Assets/Sprites/Eraser.png").convert_alpha(), (45,45))
Size = pygame.transform.scale(pygame.image.load("Assets/Sprites/Size.png").convert_alpha(), (40,40))
Inverter = pygame.transform.scale(pygame.image.load("Assets/Sprites/inverter.png").convert_alpha(), (45,45))
high_contrast = pygame.transform.scale(pygame.image.load("Assets/Sprites/high_contrast.png").convert_alpha(), (45,45))
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

#(SETTINGS)
Back = pygame.transform.scale(pygame.image.load("Assets/Sprites/Back.png").convert_alpha(), (50,50))
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
        global current_screen, menu_x_offset, last_pressed
        #================================================ SCREEN DISPLAYS ================================================
        
        if current_screen == "intro":
            screen.fill(GRAY)
            canvas.draw_grid(screen)
            canvas.draw_canvas(screen)
            buttons = Intro_screen(screen, title_font, content_font,  New_file, Open_file, New_file_hovered, Open_file_hovered)
        
        elif current_screen == "canvas":
            screen.fill(GRAY)
            canvas.draw_grid(screen)
            canvas.draw_canvas(screen)
            constants_rects = Constants_screen(screen, icon_font, Menu, Save, Load, Color, Ascii, Undo, Redo, Select, Zoom_in, Zoom_out, Draw, Eraser, high_contrast, Inverter, Size, black_icon, white_icon, red_icon, green_icon, blue_icon, yellow_icon, orange_icon, fucsia_icon, cyan_icon, purple_icon)
        
        elif current_screen == "menu":
                if menu_x_offset < 0:
                    menu_x_offset += menu_speed
                screen.fill(WHITE)
                menu_rect_positions = Menu_screen(screen, menu_x_offset, menu_font, Back, New_file_hovered, Open_file_hovered, last_pressed)
        #================================================ EVENT MANAGEMENT ================================================

        #Check for X pressing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()


            # INTRO SCREEN CONTROLS
            elif current_screen == "intro":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in buttons:
                        if button.collidepoint(mouse_pos):
                            if buttons.index(button) == 0:
                                current_screen = "canvas"
                                last_pressed = "NEW"
                                print("NEW")
                            elif buttons.index(button) == 1:
                                current_screen = "menu"
                                last_pressed = "OPEN"
                                print("OPEN")
            
            # CANVAS SCREEN CONTROLS
            elif current_screen == "canvas":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for name, hover_rect in constants_rects.items():
                        if hover_rect.collidepoint(mouse_pos):
                            last_pressed = name
                            print(name)
                            if name == "MODE":
                                if sprite_names[2] == "Color":
                                    sprite_names[2] = "Ascii"
                                    print(sprite_names[2])
                                else:
                                    sprite_names[2] = "Color"
                                    print(sprite_names[2])
                            if name == "MENU":
                                current_screen = "menu"
                                menu_x_offset = -SCREEN_WIDTH
            
            # MENU SCREEN CONTROLS
            elif current_screen == "menu":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    if menu_rect_positions["BACK"].collidepoint(mouse_pos):
                        current_screen = "canvas"
                        last_pressed = "BACK"
                    for name, menu_rect in menu_rect_positions.items():
                        if menu_rect.collidepoint(mouse_pos):
                            last_pressed = name
                            print(name)
    
                    

        pygame.display.update()
        clock.tick(60)

if __name__== "__main__":
    main()