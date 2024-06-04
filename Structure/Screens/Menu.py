import pygame
from var_consts import *

def Menu_screen(screen, x_offset, menu_font, Back, New, Open, Edit, See_image, See_matrix, Edit_unselected, See_image_unselected, See_matrix_unselected, Close, last_pressed, selected_file, files, see_option):
    menu_rect = pygame.Rect(x_offset, 0, SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, LIGHT_GRAY, menu_rect)
    
    hover_rects = {}

    # Define the left and right section rectangles
    left_section_width = (SCREEN_WIDTH - x_offset) // 5
    right_section_width = SCREEN_WIDTH - left_section_width
    left_section_rect = pygame.Rect(x_offset, 0, left_section_width, SCREEN_HEIGHT)
    right_section_rect = pygame.Rect(x_offset + left_section_width, 0, right_section_width, SCREEN_HEIGHT)

    # Draw the left and right section rectangles (for visualization, you can remove these lines later)
    pygame.draw.rect(screen, LIGHT_GRAY, left_section_rect)  # Light gray for left section
    pygame.draw.rect(screen, GRAY, right_section_rect)  # Slightly darker gray for right section

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
        
        if hover_rect.collidepoint(pygame.mouse.get_pos()) and see_option =="":
            pygame.draw.rect(screen, WHITE, hover_rect)
        
        screen.blit(button_text["image"], button_rect.topleft)
        screen.blit(text_render, text_rect)
        
        hover_rects[button_name] = hover_rect
        
        y_pos += BUTTON_SIZE + BUTTON_DISTANCE  # Increased distance between buttons

    # Always show Edit, See image, and See matrix buttons
    button_data_conditional = {
        "Edit": {"text": "Edit", "selected_image": Edit, "unselected_image": Edit_unselected},
        "See image": {"text": "See image", "selected_image": See_image, "unselected_image": See_image_unselected},
        "See matrix": {"text": "See matrix", "selected_image": See_matrix, "unselected_image": See_matrix_unselected}
    }

    for button_name, button_info in button_data_conditional.items():
        button_rect = pygame.Rect(x_offset + SHIFT_AMOUNT, y_pos, BUTTON_SIZE, BUTTON_SIZE)
        
        # Choose the image based on the last button pressed
        if selected_file:
            image = button_info["selected_image"]
            text_color = GRAY
        else:
            image = button_info["unselected_image"]
            text_color = WHITE
        

        text_render = menu_font.render(button_info["text"], True, text_color)
        text_rect = text_render.get_rect(midleft=(button_rect.right + 10 + SHIFT_AMOUNT, button_rect.centery + 5))
        hover_rect = pygame.Rect(button_rect.left - 10 - SHIFT_AMOUNT, y_pos - 10, text_rect.right - button_rect.left + 20, HOVER_SIZE)
        
        if hover_rect.collidepoint(pygame.mouse.get_pos()) and selected_file:
            pygame.draw.rect(screen, WHITE, hover_rect)
            
        #CONDITIONAL FOR SEE MATRIX AND SEE IMAGE
        if button_name == "Edit" and see_option != "":
            pygame.draw.rect(screen, LIGHT_GRAY, hover_rect)  # Keep hover color gray for "Edit" when see_option is not empty
            image = button_info["unselected_image"]
            text_color = WHITE
            text_render = menu_font.render(button_info["text"], True, text_color)

        screen.blit(image, button_rect.topleft)
        screen.blit(text_render, text_rect)
        
        hover_rects[button_name] = hover_rect
        
        y_pos += BUTTON_SIZE + BUTTON_DISTANCE  # Increased distance between buttons

    # Display text files in the right section if "Open" was pressed
    if last_pressed == "Open" and files:
        file_button_height = BUTTON_SIZE
        file_button_spacing = (right_section_rect.height - HEADER_HEIGHT) // (len(files) + 1)
        
        y_pos = HEADER_HEIGHT/2

        for filename in files:
            button_rect = pygame.Rect(right_section_rect.left + SHIFT_AMOUNT, y_pos, right_section_rect.width - 2 * SHIFT_AMOUNT, file_button_height)
            text_render = menu_font.render(filename[:-4], True, GRAY)
            text_rect = text_render.get_rect(center=button_rect.center)
            
            pygame.draw.rect(screen, LIGHT_GRAY, button_rect)

            # Highlight the button if it is the selected file or if the mouse is hovering over it
            if (button_rect.collidepoint(pygame.mouse.get_pos()) or filename == selected_file) and see_option =="":
                pygame.draw.rect(screen, WHITE, button_rect)

            screen.blit(text_render, text_rect)
            
            hover_rects[filename] = button_rect
            
            y_pos += file_button_height + file_button_spacing  # Space between file buttons

        # Add button at the top right corner
        if see_option != "":
            button_rect = pygame.Rect((3*(SCREEN_WIDTH - 120 * 6) // 4) + 120 * 6, ((SCREEN_HEIGHT - 120 * 6) // 2 ), 60, 60)
            screen.blit(Close, button_rect)
            hover_rects["Close"] = button_rect

    return hover_rects, selected_file