from pdf2image import convert_from_path
from PIL import Image
import tempfile
import os

from .utils import calculate_a4_dimensions, resize_bill_image, get_grid_dimensions
from config import DEFAULT_DPI, OUTPUT_FOLDER

def combine_bills_to_a4(uploaded_files, layout_key="4 per page", dpi=DEFAULT_DPI, margin=15):
    """Combine multiple bill PDFs into A4 pages with custom margin"""
    if not uploaded_files:
        return None
    
    rows, cols = get_grid_dimensions(layout_key)
    
    all_bill_images = []
    
    with tempfile.TemporaryDirectory() as tmpdir:
        for uploaded in uploaded_files:
            temp_path = os.path.join(tmpdir, uploaded.name)
            with open(temp_path, "wb") as f:
                f.write(uploaded.getvalue())
            
            images = convert_from_path(temp_path, dpi=dpi)
            all_bill_images.extend(images)
    
    if not all_bill_images:
        return None
    
    a4_width, a4_height = calculate_a4_dimensions(dpi)
    bill_width = a4_width // cols
    bill_height = a4_height // rows
    
    pages = []
    for i in range(0, len(all_bill_images), rows * cols):
        a4_page = Image.new('RGB', (a4_width, a4_height), color='white')
        
        current_bills = all_bill_images[i:i + (rows * cols)]
        
        for idx, bill_img in enumerate(current_bills):
            # Resize with margin
            target_w = bill_width - (margin * 2)
            target_h = bill_height - (margin * 2)
            
            resized_bill = resize_bill_image(bill_img, target_w, target_h)
            
            # Calculate position (centered in cell)
            row = idx // cols
            col = idx % cols
            x_offset = col * bill_width + margin
            y_offset = row * bill_height + margin
            
            # Center the resized bill
            paste_x = x_offset + (target_w - resized_bill.width) // 2
            paste_y = y_offset + (target_h - resized_bill.height) // 2
            
            a4_page.paste(resized_bill, (paste_x, paste_y))
        
        pages.append(a4_page)
    
    return pages


def save_combined_pdf(pages, filename="combined_bills.pdf"):
    """Save PIL images as PDF"""
    if not pages:
        return None
    
    output_path = os.path.join(OUTPUT_FOLDER, filename)
    pages[0].save(
        output_path, 
        save_all=True, 
        append_images=pages[1:], 
        resolution=DEFAULT_DPI,
        quality=95
    )
    return output_path