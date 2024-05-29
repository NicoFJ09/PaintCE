import pygame
from var_consts import *

def Constants_screen(screen, icon_font, Menu, Save, Load, Color, Ascii, sprite_names, Undo, Redo, Select, Zoom_in, Zoom_out, Draw, Eraser, high_contrast, Inverter, Rotate_left, Rotate_right, Flip_horizontal, Flip_vertical, black_icon, white_icon, red_icon, green_icon, blue_icon, yellow_icon, orange_icon, fucsia_icon, cyan_icon, purple_icon, selected_action, display_option, current_color):
    
    
    # Main Options
    header_rect = pygame.Rect(0, 0, SCREEN_WIDTH, HEADER_HEIGHT)
    pygame.draw.rect(screen, WHITE, header_rect)

    # Canvas Options
    subheader_rect = pygame.Rect(0, HEADER_HEIGHT, CANVAS_SIZE, HEADER_HEIGHT)
    pygame.draw.rect(screen, LIGHT_GRAY, subheader_rect)
    
    # Side options
    tools_rect = pygame.Rect(CANVAS_SIZE, HEADER_HEIGHT, SCREEN_WIDTH - CANVAS_SIZE, SCREEN_HEIGHT - HEADER_HEIGHT)
    pygame.draw.rect(screen, LIGHT_GRAY, tools_rect)
    
    #======================================================================================= HEADER OPTIONS DISPLAY =======================================================================================
    # Center sprites within the header with equal spacing
    if sprite_names[2] == "Color":
        sprites = [Save, Load, Color]
    else:
        sprites = [Save, Load, Ascii]
    num_sprites = len(sprites)
    sprite_size = 40
    hover_size = 60
    total_width = SCREEN_WIDTH
    # Set the margins for menu and undo/redo
    edge_margin = 10
    undo_redo_margin = 10

    # Calculate the width of the middle section
    middle_section_start = edge_margin + sprite_size + 20
    middle_section_end = total_width - edge_margin - 2 * (sprite_size + undo_redo_margin)
    middle_section_width = middle_section_end - middle_section_start

    # Calculate the spacing between each centered sprite
    total_sprite_width = num_sprites * sprite_size
    spacing_between_sprites = (middle_section_width - total_sprite_width) // (num_sprites + 1)

    y_pos = (HEADER_HEIGHT - sprite_size) // 2 - 8  # Adjusted the y_pos
    hover_y_pos = (HEADER_HEIGHT - hover_size) // 2

    # Get mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Draw Menu icon manually at the left corner with hover effect and its name
    menu_hover_rect = pygame.Rect(edge_margin - 10, hover_y_pos, hover_size, hover_size)
    if menu_hover_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, LIGHT_GRAY, menu_hover_rect)
    screen.blit(Menu, (edge_margin, y_pos))
    
    # Render text surface for Menu
    menu_text_surface = icon_font.render("Menu", True, GRAY)
    menu_text_rect = menu_text_surface.get_rect(center=(edge_margin + sprite_size // 2, y_pos + sprite_size + 10))
    screen.blit(menu_text_surface, menu_text_rect)

    # Draw centered sprites with hover effect and their names
    x_pos = middle_section_start + spacing_between_sprites
    hover_rects = {}  # Dictionary to store hover rects for sprites

    for sprite, name in zip(sprites, sprite_names):
        hover_rect = pygame.Rect(x_pos - 10, hover_y_pos, hover_size, hover_size)
        if hover_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, LIGHT_GRAY, hover_rect)
        screen.blit(sprite, (x_pos, y_pos))
        
        # Store hover rect positions
        hover_rects[name] = hover_rect
        
        # Render text surfaces
        text_surface = icon_font.render(name, True, GRAY)
        text_rect = text_surface.get_rect(center=(x_pos + sprite_size // 2, y_pos + sprite_size + 10))
        screen.blit(text_surface, text_rect)
        
        x_pos += sprite_size + spacing_between_sprites

    # Draw Undo and Redo icons manually at the right corner with hover effect and their names
    undo_redo_x_start = total_width - edge_margin - 2 * sprite_size - undo_redo_margin
    undo_hover_rect = pygame.Rect(undo_redo_x_start - 20, hover_y_pos, hover_size, hover_size)
    redo_hover_rect = pygame.Rect(undo_redo_x_start + sprite_size + undo_redo_margin - 10, hover_y_pos, hover_size, hover_size)
    
    if undo_hover_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, LIGHT_GRAY, undo_hover_rect)
    screen.blit(Undo, (undo_redo_x_start-10, y_pos))
    
    # Render text surface for Undo
    undo_text_surface = icon_font.render("Undo", True, GRAY)
    undo_text_rect = undo_text_surface.get_rect(center=(undo_redo_x_start + sprite_size // 2 - 10, y_pos + sprite_size + 10))
    screen.blit(undo_text_surface, undo_text_rect)
    
    if redo_hover_rect.collidepoint(mouse_pos):
        pygame.draw.rect(screen, LIGHT_GRAY, redo_hover_rect)
    screen.blit(Redo, (undo_redo_x_start + sprite_size + undo_redo_margin, y_pos))
    
    # Render text surface for Redo
    redo_text_surface = icon_font.render("Redo", True, GRAY)
    redo_text_rect = redo_text_surface.get_rect(center=(undo_redo_x_start + sprite_size + undo_redo_margin + sprite_size // 2, y_pos + sprite_size + 10))
    screen.blit(redo_text_surface, redo_text_rect)
    
    #======================================================================================= SUBHEADER OPTIONS DISPLAY =======================================================================================
    # Addicional Sprites for sub-header with equal spacing
    subheader_sprites = [Select, Zoom_in, Zoom_out]
    subheader_sprite_names = ["Select", "Zoom in", "Zoom out"]
    subheader_num_sprites = len(subheader_sprites)
    
    subheader_sprite_size = 30
    subheader_hover_size = 60

    # Calculate the width of the middle section for subheader
    subheader_middle_section_start = edge_margin
    subheader_middle_section_end = total_width - edge_margin
    subheader_middle_section_width = subheader_middle_section_end - subheader_middle_section_start

    # Calculate the spacing between each centered sprite for subheader
    subheader_total_sprite_width = subheader_num_sprites * subheader_sprite_size
    subheader_spacing_between_sprites = (subheader_middle_section_width - subheader_total_sprite_width) // (subheader_num_sprites + 1)

    subheader_y_pos = HEADER_HEIGHT + (SUBHEADER_HEIGHT - subheader_sprite_size) // 2  # Adjusted the y_pos for subheader
    subheader_hover_y_pos = HEADER_HEIGHT + 10 + (SUBHEADER_HEIGHT - subheader_hover_size) // 2

    # Draw centered sprites in the subheader with hover effect and their names
    subheader_x_pos = subheader_middle_section_start - 103 + subheader_spacing_between_sprites
    
    for sprite, name in zip(subheader_sprites, subheader_sprite_names):
        subheader_hover_rect = pygame.Rect(subheader_x_pos - 10, subheader_hover_y_pos, subheader_hover_size, subheader_hover_size)
        
        if subheader_hover_rect.collidepoint(mouse_pos) or name == selected_action:
            pygame.draw.rect(screen, WHITE, subheader_hover_rect)
        screen.blit(sprite, (subheader_x_pos, subheader_y_pos))
        
        # Render text surfaces for subheader
        subheader_text_surface = icon_font.render(name, True, GRAY)
        subheader_text_rect = subheader_text_surface.get_rect(center=(subheader_x_pos + 5 + subheader_sprite_size // 2, subheader_y_pos + 5 + subheader_sprite_size + 10))
        screen.blit(subheader_text_surface, subheader_text_rect)
        
        # Store hover rect positions for subheader
        hover_rects[name] = subheader_hover_rect

        subheader_x_pos += subheader_sprite_size + subheader_spacing_between_sprites



    #======================================================================================= VERTICAL TOOLS DISPLAY =======================================================================================
    
                                                #======================================= FIRST TOOLS OPTIONS DISPLAY =======================================

    vertical_buttons = [Draw, white_icon, cyan_icon, green_icon, yellow_icon, orange_icon, high_contrast, Rotate_left, Flip_horizontal]
    vertical_button_names = ["Draw", "", "", "", "", "", "Contrast", "Rotate L.", "Flip h."]
    vertical_button_variables = ["Draw", "White", "Cyan", "Green", "Yellow", "Orange", "Contrast", "Rotate L.", "Flip h."]
    button_size = 30
    hover_size = 60
    vertical_margin = 15  # Espacio entre los botones
    vertical_x_pos = SCREEN_WIDTH - 160 - edge_margin - button_size  # Alineados al lado derecho
    vertical_y_start = HEADER_HEIGHT + edge_margin
    
    for i in range(len(vertical_buttons)):
        button = vertical_buttons[i]
        var = vertical_button_variables[i]
        name = vertical_button_names[i]
        vertical_y_pos = vertical_y_start + i * (button_size + vertical_margin + 50)
        
        hover_rect = pygame.Rect(vertical_x_pos - 7, vertical_y_pos - 7, hover_size, hover_size)
        if hover_rect.collidepoint(mouse_pos) or var == current_color or var == selected_action or var == display_option:
            pygame.draw.rect(screen, WHITE, hover_rect)
        screen.blit(button, (vertical_x_pos, vertical_y_pos - 6))
        

        # Render text
        text_surface = icon_font.render(name, True, GRAY)
        text_rect = text_surface.get_rect(center=(hover_rect.centerx, vertical_y_pos + 5 + button_size + 10))
        screen.blit(text_surface, text_rect)
        
        # Store hover rect positions
        hover_rects[var] = hover_rect

    #======================================= SECOND TOOLS OPTIONS DISPLAY =======================================
    vertical_buttons = [Eraser, black_icon, red_icon, fucsia_icon, purple_icon, blue_icon, Inverter, Rotate_right, Flip_vertical]
    vertical_button_names = ["Eraser", "", "", "", "", "", "Inverter", "Rotate R.", "Flip v."]
    vertical_button_variables = ["Eraser", "Black", "Red","Fucsia" , "Purple", "Blue", "Inverter", "Rotate R.", "Flip v."]
    button_size = 30
    hover_size = 60
    vertical_margin = 15  # Espacio entre los botones
    vertical_x_pos = SCREEN_WIDTH - 50 - edge_margin - button_size  # Alineados al lado derecho
    vertical_y_start = HEADER_HEIGHT + edge_margin

    for i in range(len(vertical_buttons)):
        button = vertical_buttons[i]
        var = vertical_button_variables[i]
        name = vertical_button_names[i]
        vertical_y_pos = vertical_y_start + i * (button_size + vertical_margin + 50)
        
        hover_rect = pygame.Rect(vertical_x_pos - 7, vertical_y_pos - 7, hover_size, hover_size)
        if hover_rect.collidepoint(mouse_pos) or var == current_color or var == selected_action or var == display_option:
            pygame.draw.rect(screen, WHITE, hover_rect)
        screen.blit(button, (vertical_x_pos, vertical_y_pos - 6))
        

        # Render text
        text_surface = icon_font.render(name, True, GRAY)
        text_rect = text_surface.get_rect(center=(hover_rect.centerx, vertical_y_pos + 5 + button_size + 10))
        screen.blit(text_surface, text_rect)
        
        # Store hover rect positions
        hover_rects[var] = hover_rect

    #======================================================================================= RECT RETURN MANAGEMENT =======================================================================================
    # Store the rect positions for all items
    rect_positions = {
        "Menu": menu_hover_rect,
        "Undo": undo_hover_rect,
        "Redo": redo_hover_rect,
        "Mode": hover_rects[sprite_names[2]]
    }
    
    # Add hover rects for sprites to the rect_positions dictionary
    for name, hover_rect in hover_rects.items():
        rect_positions[name] = hover_rect

    return rect_positions
