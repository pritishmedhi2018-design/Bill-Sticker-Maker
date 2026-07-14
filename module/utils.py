from PIL import Image
import math

def calculate_a4_dimensions(dpi=300):
    """Return A4 width and height in pixels"""
    width = int(8.27 * dpi)
    height = int(11.69 * dpi)
    return width, height


def get_grid_dimensions(layout_key):
    """Convert layout name to rows and columns"""
    layouts = {
        "1 per page": (1, 1),
        "2 per page": (1, 2),
        "4 per page": (2, 2),
        "6 per page": (2, 3),
        "8 per page": (2, 4),
        "9 per page": (3, 3),
        "12 per page": (3, 4),
    }
    return layouts.get(layout_key, (2, 2))


def resize_bill_image(img, target_width, target_height):
    """Resize image while maintaining aspect ratio"""
    # Calculate aspect ratio
    aspect_ratio = img.width / img.height
    target_ratio = target_width / target_height
    
    if aspect_ratio > target_ratio:
        # Wider than target → fit height
        new_height = target_height
        new_width = int(new_height * aspect_ratio)
    else:
        # Taller than target → fit width
        new_width = target_width
        new_height = int(new_width / aspect_ratio)
    
    return img.resize((new_width, new_height), Image.Resampling.LANCZOS)


def center_image_on_canvas(canvas, img, x_offset, y_offset):
    """Paste image centered in its grid cell"""
    x = x_offset + (canvas.width // 2 - img.width // 2) if canvas else x_offset
    y = y_offset + (canvas.height // 2 - img.height // 2) if canvas else y_offset
    return x, y