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

#(LATERAL TOOLS)

#(SETTINGS)
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
        global current_screen
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
            constants_rects = Constants_screen(screen, icon_font, Menu, Save, Load, Color, Ascii, Undo, Redo)
        
        elif current_screen == "menu":
            None
        #================================================ EVENT MANAGEMENT ================================================

        #Check for X pressing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #INTRO SCREEN CONTROLS
            elif current_screen == "intro":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for button in buttons:
                        if button.collidepoint(mouse_pos):
                            if buttons.index(button) == 0:
                                current_screen = "canvas"
                                print("NEW")
                            elif buttons.index(button) == 1:
                                current_screen = "menu"
                                print("OPEN")
            
            #CANVAS SCREEN CONTROLS
            elif current_screen == "canvas":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    for name, hover_rect in constants_rects.items():
                        if hover_rect.collidepoint(mouse_pos):
                            print(name)


        #Update
        pygame.display.update()
        clock.tick(60)

if __name__== "__main__":
    main()