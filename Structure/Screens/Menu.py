import pygame
from var_consts import *

def Menu_screen(screen, x_offset, menu_font, Back, New, Open, Edit, See_image, See_matrix, last_pressed):
    menu_rect = pygame.Rect(x_offset, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, LIGHT_GRAY, menu_rect)
    
    hover_rects = {}

    y_pos = (HEADER_HEIGHT - BUTTON_SIZE) // 2 - 5
    button_data = {
        "BACK": {"text": "BACK", "image": Back},
        "NEW": {"text": "NEW", "image": New},
        "OPEN": {"text": "OPEN", "image": Open}
    }

    for button_name, button_text in button_data.items():
        button_rect = pygame.Rect(x_offset + SHIFT_AMOUNT, y_pos, BUTTON_SIZE, BUTTON_SIZE)
        text_render = menu_font.render(button_text["text"], True, GRAY)
        text_rect = text_render.get_rect(midleft=(button_rect.right + 10 + SHIFT_AMOUNT, button_rect.centery + 5))
        hover_rect = pygame.Rect(button_rect.left - 10 - SHIFT_AMOUNT, y_pos - 10, text_rect.right - button_rect.left + 20, HOVER_SIZE)
        
        if hover_rect.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.rect(screen, WHITE, hover_rect)
        
        screen.blit(button_text["image"], button_rect.topleft)
        screen.blit(text_render, text_rect)
        
        hover_rects[button_name] = hover_rect
        
        y_pos += BUTTON_SIZE + BUTTON_DISTANCE  # Increased distance between buttons

    # Conditional rendering based on the last button pressed
    button_data_conditional = {
        "EDIT": {"text": "EDIT", "image": Edit},
        "SEE IMAGE": {"text": "SEE IMAGE", "image": See_image},
        "SEE MATRIX" : {"text": "SEE MATRIX", "image": See_matrix}
    }

    for button_name, button_info in button_data_conditional.items():
        button_rect = pygame.Rect(x_offset + SHIFT_AMOUNT, y_pos, BUTTON_SIZE, BUTTON_SIZE)
        text_render = menu_font.render(button_info["text"], True, GRAY if last_pressed == "OPEN" else WHITE)  # Change color based on the last button pressed
        text_rect = text_render.get_rect(midleft=(button_rect.right + 10 + SHIFT_AMOUNT, button_rect.centery + 5))
        hover_rect = pygame.Rect(button_rect.left - 10 - SHIFT_AMOUNT, y_pos - 10, text_rect.right - button_rect.left + 20, HOVER_SIZE)
        
        if hover_rect.collidepoint(pygame.mouse.get_pos()) and last_pressed == "OPEN":
            pygame.draw.rect(screen, WHITE, hover_rect)
        
        screen.blit(button_info["image"], button_rect.topleft)
        screen.blit(text_render, text_rect)
        
        hover_rects[button_name] = hover_rect
        
        y_pos += BUTTON_SIZE + BUTTON_DISTANCE  # Increased distance between buttons

    return hover_rects