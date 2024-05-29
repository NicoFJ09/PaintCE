#Main structure
TITLE = "PaintCE"
RUNNING = True

#Screen dimensions
SCREEN_WIDTH=1200
SCREEN_HEIGHT=900

#Colors
WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (125,125,125)
LIGHT_GRAY = (200,200,200)
DARK_GRAY = (50,50,50)
OVERLAY_GRAY = (0,0,0,225)
DARK_BLUE = (58,98,193)

#Screen management
current_screen = "INTRO"
buttons = []

#Screen constants
#Canvas
#Screen constants
HEADER_HEIGHT = 60
SUBHEADER_HEIGHT = 40
CANVAS_SIZE = 960
sprite_names = ["Save", "Load", "Color"]

#Menu
menu_x_offset = -SCREEN_WIDTH
menu_speed = 80  # Adjust this for animation speed
BUTTON_SIZE = 40
HOVER_SIZE = 60
BUTTON_DISTANCE = 128
SHIFT_AMOUNT = 5

last_pressed = ""

colors = {
    "Black": BLACK,
    "Red": (255, 0, 0),
    "Fucsia": (255, 0, 128),
    "Purple": (162, 25, 255),
    "Blue": (0, 0, 255),
    "White": WHITE,
    "Cyan": (0, 183, 235),
    "Green": (13, 255, 0),
    "Yellow": (255, 255, 0),
    "Orange": (255, 128, 0)
}
current_color = ""

selected_function = ""
selectable_functions = ["Select", "Eraser", "Draw"]