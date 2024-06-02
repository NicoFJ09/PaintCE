import pygame
from var_consts import *

def draw_button(screen, rect, text, font, text_color, button_color):
    pygame.draw.rect(screen, button_color, rect)
    text_surface = font.render(text, True, text_color)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def Save_screen(screen, title_font, content_font, input_text, input_active):
    # Background gray coating
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill(OVERLAY_GRAY)
    screen.blit(overlay, (0, 0))

    # Rectangular box for input and buttons
    box_width = 400
    box_height = 200
    box_rect = pygame.Rect((SCREEN_WIDTH - box_width) / 2, (SCREEN_HEIGHT - box_height) / 2, box_width, box_height)
    pygame.draw.rect(screen, WHITE, box_rect)

    # Insert file name
    title_text = title_font.render("Enter File Name", True, BLACK)
    title_text_rect = title_text.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3))
    screen.blit(title_text, title_text_rect)

    # Text input area
    input_rect = pygame.Rect(box_rect.left + 20, box_rect.top + 60, box_rect.width - 40, 40)

    # Set input area color based on input_active
    input_area_color = BLACK if input_active else LIGHT_GRAY
    pygame.draw.rect(screen, input_area_color, input_rect, 2)
    
    entered_text = input_text[:15]  # Limit the input text to 20 characters
    entered_text_surface = content_font.render(entered_text, True, DARK_GRAY)
    entered_text_rect = entered_text_surface.get_rect(center=(input_rect.centerx, input_rect.centery - 1))  # Centering the text
    screen.blit(entered_text_surface, entered_text_rect)
    input_text = entered_text

    # Buttons
    button_width = 80
    button_height = 40
    cancel_button_rect = pygame.Rect(box_rect.right - button_width * 2 - 20, box_rect.bottom - button_height - 20, button_width, button_height)
    save_button_rect = pygame.Rect(box_rect.right - button_width - 10, box_rect.bottom - button_height - 20, button_width, button_height)

    draw_button(screen, cancel_button_rect, "Cancel", content_font, WHITE, DARK_GRAY)
    draw_button(screen, save_button_rect, "Save", content_font, WHITE, DARK_GRAY)

    return input_rect, cancel_button_rect, save_button_rect


def Replace_screen(screen, subtitle_font, content_font):

    # Background gray coating
    overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SRCALPHA)
    overlay.fill(OVERLAY_GRAY)
    screen.blit(overlay, (0, 0))

    # Rectangular box for input and buttons
    box_width = 400
    box_height = 200
    vertical_spacing = 40
    box_rect = pygame.Rect((SCREEN_WIDTH - box_width) / 2, (SCREEN_HEIGHT - box_height) / 2, box_width, box_height)
    pygame.draw.rect(screen, WHITE, box_rect)

    # Render the first line of text
    text_line1 = "File name already exists"
    text_surface1 = subtitle_font.render(text_line1, True, DARK_GRAY)
    text_rect1 = text_surface1.get_rect(center=(box_rect.centerx, box_rect.top + text_surface1.get_height()))
    screen.blit(text_surface1, text_rect1)

    # Calculate the vertical position for the second line of text
    second_line_y = text_rect1.bottom + vertical_spacing

    # Render the second line of text
    text_line2 = "Do you want to overwrite it?"
    text_surface2 = subtitle_font.render(text_line2, True, DARK_GRAY)
    text_rect2 = text_surface2.get_rect(center=(box_rect.centerx, second_line_y))
    screen.blit(text_surface2, text_rect2)

    # Buttons
    button_width = 80
    button_height = 40
    cancel_button_rect = pygame.Rect(box_rect.right - button_width * 2 - 20, text_rect2.bottom + vertical_spacing, button_width, button_height)
    save_button_rect = pygame.Rect(box_rect.right - button_width - 10, text_rect2.bottom + vertical_spacing, button_width, button_height)

    draw_button(screen, cancel_button_rect, "Cancel", content_font, WHITE, DARK_GRAY)
    draw_button(screen, save_button_rect, "Save", content_font, WHITE, DARK_GRAY)

    return cancel_button_rect, save_button_rect