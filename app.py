import streamlit as st
from config import APP_TITLE, APP_DESCRIPTION

from modules.pdf_engine import combine_bills_to_a4
from modules.printer import export_to_pdf
from modules.ui import render_sidebar, render_main_ui, show_success_message
from modules.preview import show_live_preview

st.set_page_config(page_title="PrintStudio", page_icon="📦", layout="wide")

# Custom CSS
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.title(APP_TITLE)
st.markdown(APP_DESCRIPTION)

layout_key, dpi, margin = render_sidebar()

uploaded_files = st.file_uploader(
    "Upload Bill PDFs", 
    type="pdf", 
    accept_multiple_files=True,
    help="You can upload multiple PDFs at once"
)

render_main_ui(uploaded_files, layout_key)

if uploaded_files and st.button("Generate Sticker Sheets", type="primary", use_container_width=True):
    with st.spinner("Processing bills..."):
        pages = combine_bills_to_a4(uploaded_files, layout_key, dpi, margin=margin)
        
        if pages:
            output_path = export_to_pdf(pages)
            if output_path:
                show_success_message(output_path)
                show_live_preview(pages, layout_key)