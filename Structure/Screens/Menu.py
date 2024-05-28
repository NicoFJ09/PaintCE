import pygame
from var_consts import *

def Menu_screen(screen, x_offset, menu_font, Back, New, Open, Edit, See_image, See_matrix, Edit_unselected, See_image_unselected, See_matrix_unselected, last_pressed):
    menu_rect = pygame.Rect(x_offset, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, LIGHT_GRAY, menu_rect)
    
    hover_rects = {}

    y_pos = (HEADER_HEIGHT - BUTTON_SIZE) // 2 - 5
    button_data = {
        "Back": {"text": "Back", "image": Back},
        "New": {"text": "New", "image": New},
        "Open": {"text": "Open", "image": Open}
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
        "Edit": {"text": "Edit", "selected_image": Edit, "unselected_image": Edit_unselected},
        "See image": {"text": "See image", "selected_image": See_image, "unselected_image": See_image_unselected},
        "See matrix": {"text": "See matrix", "selected_image": See_matrix, "unselected_image": See_matrix_unselected}
    }

    for button_name, button_info in button_data_conditional.items():
        button_rect = pygame.Rect(x_offset + SHIFT_AMOUNT, y_pos, BUTTON_SIZE, BUTTON_SIZE)
        
        # Choose the image based on the last button pressed
        if last_pressed == "Open":
            image = button_info["selected_image"]
            text_color = GRAY
        else:
            image = button_info["unselected_image"]
            text_color = WHITE
        
        text_render = menu_font.render(button_info["text"], True, text_color)
        text_rect = text_render.get_rect(midleft=(button_rect.right + 10 + SHIFT_AMOUNT, button_rect.centery + 5))
        hover_rect = pygame.Rect(button_rect.left - 10 - SHIFT_AMOUNT, y_pos - 10, text_rect.right - button_rect.left + 20, HOVER_SIZE)
        
        if hover_rect.collidepoint(pygame.mouse.get_pos()) and last_pressed == "Open":
            pygame.draw.rect(screen, WHITE, hover_rect)
        
        screen.blit(image, button_rect.topleft)
        screen.blit(text_render, text_rect)
        
        hover_rects[button_name] = hover_rect
        
        y_pos += BUTTON_SIZE + BUTTON_DISTANCE  # Increased distance between buttons

    return hover_rects