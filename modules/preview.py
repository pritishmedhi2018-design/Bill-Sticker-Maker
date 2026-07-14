import streamlit as st
from PIL import Image
import tempfile
import io

def show_live_preview(pages, layout_key):
    if not pages:
        return
    
    st.subheader("Live Preview")
    st.caption(f"Layout: {layout_key} • First Page")
    
    preview_img = pages[0]
    
    # Convert to bytes for PNG download
    img_byte_arr = io.BytesIO()
    preview_img.save(img_byte_arr, format='PNG')
    img_bytes = img_byte_arr.getvalue()
    
    # Display preview with better control
    st.image(preview_img, width=700)
    
    st.download_button(
        label="⬇️ Download Preview as PNG",
        data=img_bytes,
        file_name="bill_preview.png",
        mime="image/png",
        use_container_width=True
    )