from .utils import get_grid_dimensions

def get_layout_options():
    """Return available layout options for UI"""
    return [
        "1 per page", "2 per page", "4 per page", 
        "6 per page", "8 per page", "9 per page", "12 per page"
    ]


def get_layout_description(layout_key):
    """Return description for selected layout"""
    descriptions = {
        "1 per page": "Full A4 size per bill - Best quality",
        "2 per page": "2 bills per A4 page",
        "4 per page": "Classic 2×2 grid - Most popular",
        "6 per page": "2 rows × 3 columns",
        "8 per page": "2 rows × 4 columns",
        "9 per page": "3×3 grid",
        "12 per page": "3 rows × 4 columns - Maximum density",
    }
    return descriptions.get(layout_key, "Custom layout")


def calculate_total_pages(total_bills, bills_per_page):
    """Calculate how many A4 pages will be generated"""
    if bills_per_page == 0:
        return 0
    return (total_bills + bills_per_page - 1) // bills_per_page
