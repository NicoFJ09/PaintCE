import pygame
from var_consts import *

def Constants_screen(screen, icon_font, Menu, Save, Load, Color, Ascii, Undo, Redo, sprite_names):
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
    # Ensure the correct sprite (Color or Ascii) is used based on the sprite_names list
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
    sprite_rects = {}  # Dictionary to store rects for sprites
    for sprite, name in zip(sprites, sprite_names):
        hover_rect = pygame.Rect(x_pos - 10, hover_y_pos, hover_size, hover_size)
        if hover_rect.collidepoint(mouse_pos):
            pygame.draw.rect(screen, LIGHT_GRAY, hover_rect)
        screen.blit(sprite, (x_pos, y_pos))
        
        # Store sprite and hover rect positions
        sprite_rects[name.lower()] = pygame.Rect(x_pos, y_pos, sprite_size, sprite_size)
        hover_rects[name.lower()] = hover_rect
        
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

    # Store the rect positions for all items
    rect_positions = {
        "MENU": menu_hover_rect,
        "UNDO": undo_hover_rect,
        "REDO": redo_hover_rect,
        "MODE": sprite_rects[sprite_names[2].lower()]  # Ensure mode rect is accessible
    }
    
    # Add hover rects for sprites to the rect_positions dictionary
    for name, hover_rect in hover_rects.items():
        rect_positions[name.upper()] = hover_rect
    
    return rect_positions