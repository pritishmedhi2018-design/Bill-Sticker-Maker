import os

# App Configuration
APP_TITLE = "PrintStudio - Bill Sticker Maker"
APP_ICON = "📦"
APP_DESCRIPTION = "Convert bills into printable sticker sheets (like Flipkart/Amazon)"

# Default Settings
DEFAULT_DPI = 300
A4_WIDTH_INCH = 8.27
A4_HEIGHT_INCH = 11.69

# Layout Options (bills per page)
LAYOUT_OPTIONS = {
    "1 per page": (1, 1),
    "2 per page": (1, 2),
    "4 per page": (2, 2),
    "6 per page": (2, 3),
    "8 per page": (2, 4),
    "9 per page": (3, 3),
    "12 per page": (3, 4),
}

# Default layout
DEFAULT_LAYOUT = "4 per page"

# Output settings
OUTPUT_FOLDER = "output"
TEMP_FOLDER = "temp"

# Create folders if they don't exist
os.makedirs(OUTPUT_FOLDER, exist_ok=True)
os.makedirs(TEMP_FOLDER, exist_ok=True)

# UI Settings
SIDEBAR_WIDTH = 300
PREVIEW_WIDTH = 700