import pygame
from var_consts import *

def Intro_screen(screen, title_font, content_font, New_file_sprite, Open_file_sprite, New_file_sprite_hovered, Open_file_sprite_hovered):

    # Background gray coating
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)

    overlay.fill(OVERLAY_GRAY)
    screen.blit(overlay, (0, 0))

    # Render welcome text
    welcome_text = title_font.render("Welcome", True, WHITE)
    welcome_text_rect = welcome_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 4))
    screen.blit(welcome_text, welcome_text_rect)

    # Buttons setup
    button_width, button_height = welcome_text.get_width() - 20, 180  # Increased height to fit sprites and text
    button_texts = ["New", "Open"]

    # Variable to control spacing between buttons
    button_spacing = 60  # Adjust this value to increase/decrease spacing

    # Manually positioning buttons
    button1_rect = pygame.Rect(
        (SCREEN_WIDTH / 2 - button_width / 2, welcome_text_rect.bottom + button_spacing),
        (button_width, button_height)
    )
    button2_rect = pygame.Rect(
        (SCREEN_WIDTH / 2 - button_width / 2, button1_rect.bottom + button_spacing),
        (button_width, button_height)
    )

    # Draw button rectangles
    pygame.draw.rect(screen, WHITE, button1_rect)
    pygame.draw.rect(screen, WHITE, button2_rect)

    # Center sprites within buttons
    New_file_sprite_rect = New_file_sprite.get_rect(center=(button1_rect.centerx, button1_rect.centery - 20))
    Open_file_sprite_rect = Open_file_sprite.get_rect(center=(button2_rect.centerx, button2_rect.centery - 20))

    # Check if mouse is hovering over button1
    if button1_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(New_file_sprite_hovered, New_file_sprite_rect)
        pygame.draw.rect(screen, DARK_BLUE, button1_rect, 3)  # Draw blue outline
    else:
        screen.blit(New_file_sprite, New_file_sprite_rect)

    # Check if mouse is hovering over button2
    if button2_rect.collidepoint(pygame.mouse.get_pos()):
        screen.blit(Open_file_sprite_hovered, Open_file_sprite_rect)
        pygame.draw.rect(screen, DARK_BLUE, button2_rect, 3)  # Draw blue outline
    else:
        screen.blit(Open_file_sprite, Open_file_sprite_rect)

    # Render button texts below sprites
    button1_text = content_font.render(button_texts[0], True, DARK_GRAY)
    button1_text_rect = button1_text.get_rect(center=(button1_rect.centerx, New_file_sprite_rect.bottom + 25))
    
    button2_text = content_font.render(button_texts[1], True, DARK_GRAY)
    button2_text_rect = button2_text.get_rect(center=(button2_rect.centerx, Open_file_sprite_rect.bottom + 25))

    # Draw button texts
    screen.blit(button1_text, button1_text_rect)
    screen.blit(button2_text, button2_text_rect)

    # Store button rectangles for event handling
    buttons = [button1_rect, button2_rect]

    pygame.display.flip()
    return buttons
