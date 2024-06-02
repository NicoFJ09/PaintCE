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
OVERLAY_DARK = (0,0,0,225)
OVERLAY_GRAY = (128, 128, 128, 128)
DARK_BLUE = (58,98,193)
RED = (255, 0, 0)
FUCSIA = (255, 0, 128)
PURPLE = (162, 25, 255)
BLUE = (0, 0, 255)
CYAN  = (0, 183, 235)
GREEN = (13, 255, 0),
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)

#Screen management
current_screen = "INTRO"
buttons = []

#Canvas
#Color saving
colors = {
    "White": WHITE,
    "Cyan": CYAN,
    "Green": GREEN,
    "Yellow": YELLOW,
    "Orange": ORANGE,
    "Red": RED,
    "Fucsia": FUCSIA,
    "Purple": PURPLE,
    "Blue": BLUE,
    "Black": BLACK
}
#Num to color transformation
colors_codes = {
    0 : "White",
    1 : "Cyan",
    2 : "Green",
    3 : "Yellow",
    4 : "Orange",
    5 : "Red",
    6 : "Fucsia",
    7 : "Purple",
    8 : "Blue",
    9 : "Black"
}
#Monochrome switch
High_contrast_codes = {
    0 : "White",
    1 : "White",
    2 : "White",
    3 : "White",
    4 : "White",
    5 : "Black",
    6 : "Black",
    7 : "Black",
    8 : "Black",
    9 : "Black"
}
#Negative colors
Inverter_codes = {
    0 : "Black",
    1 : "Blue",
    2 : "Purple",
    3 : "Fucsia",
    4 : "Red",
    5 : "Orange",
    6 : "Yellow",
    7 : "Green",
    8 : "Cyan",
    9 : "White"
}
#Color reader for matrix management
Draw_color_reading = {
    "White": 0,
    "Cyan" : 1,
    "Green" : 2,
    "Yellow" : 3,
    "Orange" : 4,
    "Red" : 5,
    "Fucsia" : 6,
    "Purple": 7,
    "Blue" : 8,
    "Black" : 9
}

#Ascii art converter
Ascii_codes = {
    0 : " ",
    1 : ".",
    2 : ":",
    3 : "-",
    4 : "=",
    5 : "¡",
    6 : "&",
    7 : "$",
    8 : "%",
    9 : "@"
}

#Monochrome switch
Ascii_High_contrast_codes = {
    0 : " ",
    1 : " ",
    2 : " ",
    3 : " ",
    4 : " ",
    5 : "@",
    6 : "@",
    7 : "@",
    8 : "@",
    9 : "@"
}
#Negative colors
Ascii_Inverter_codes = {
    0 : "@",
    1 : "%",
    2 : "$",
    3 : "&",
    4 : "¡",
    5 : "=",
    6 : "-",
    7 : ":",
    8 : ".",
    9 : " ",
}

Draw_ascii_reading = {
    " ": 0,
    "." : 1,
    ":" : 2,
    "-" : 3,
    "=" : 4,
    "¡" : 5,
    "&" : 6,
    "$": 7,
    "%" : 8,
    "@" : 9
}

#Selected color
current_color = ""

#Select, erase, or draw
selected_action = ""
selectable_actions = ["Select", "Eraser", "Draw"]

#Contrast or invert
display_option = ""
display_options =  ["Contrast", "Inverter"]

#Rotate or flip
orientation_option = ""
orientation_options = ["Rotate L.", "Rotate R.",  "Flip h.",  "Flip v."]

#Last pressed option
last_pressed = ""
#To handle drawing/erasing while holding
mouse_held = False
#To handle state saving to undo and redo
state_saved = False

#Screen constants
HEADER_HEIGHT = 60
SUBHEADER_HEIGHT = 40
CANVAS_SIZE = 960

#To handle the color to Ascii toggle mostly
sprite_names = ["Save", "Load", "Color"]
display_mode = "Color"

#Brush/eraser size
current_size = 1

#Menu constants
menu_x_offset = -SCREEN_WIDTH
menu_speed = 80  # Adjust this for animation speed
BUTTON_SIZE = 40
HOVER_SIZE = 60
BUTTON_DISTANCE = 128
SHIFT_AMOUNT = 5

#Save management
CURRENT_FILE = "Untitled"
input_text = ""
save_option = ""
save_option_replace = ""
canvas_name = ""
response = ""
input_active = False