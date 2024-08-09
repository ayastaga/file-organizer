import os

SLEEP_TIME = 0.075
COUNTER = 0

# File type categories
FILE_TYPE_LIST = {
    'Documents': ['pdf', 'docx', 'txt', 'xlsx', 'pptx'],
    'Images': ['jpg', 'jpeg', 'png', 'gif', 'bmp'],
    'Audio': ['mp3', 'wav', 'aac'],
    'Video': ['mp4', 'avi', 'mkv'],
}

# Window configuration
WINDOW_TITLE = "File Organizer"
WINDOW_SIZE = "390x535"
WINDOW_BG = "white"

# Font configurations
TITLE_FONT = ("Cormorant Garamond", 45)
LOADING_FONT = ("Cormorant Garamond", 30)
BUTTON_FONT = ("Inter ExtraBold Italic", 13)
BUTTON_FONT_2 = ("Cormorant Garamond", 13)
TEXT_FONT = ("Algol", 10)

# Load extension list
with open("extension_list.txt", "r") as extension_txt:
    EXTENSION_LIST = [ext.strip()[1:] for ext in extension_txt]

# Global variables
PATH = ""
FOLDER_SELECTED = False