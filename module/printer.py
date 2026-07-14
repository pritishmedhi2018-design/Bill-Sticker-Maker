import streamlit as st
from .pdf_engine import save_combined_pdf

def export_to_pdf(pages, filename="combined_bills.pdf"):
    """Export pages to PDF"""
    if not pages:
        st.error("No pages to export")
        return None
    
    output_path = save_combined_pdf(pages, filename)
    
    if output_path:
        st.success(f"✅ File saved to: `{output_path}`")
    return output_path