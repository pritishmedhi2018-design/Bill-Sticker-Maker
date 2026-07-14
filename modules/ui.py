import streamlit as st

def render_sidebar():
    st.sidebar.title("Settings")
    
    layout_key = st.sidebar.selectbox(
        "Bills per A4 Page",
        ["1 per page", "2 per page", "4 per page", "6 per page", "8 per page", "9 per page", "12 per page"],
        index=2
    )
    
    dpi = st.sidebar.slider("Resolution (DPI)", 200, 600, 300, 50)
    margin = st.sidebar.slider("Margin (px)", 0, 60, 20)
    
    return layout_key, dpi, margin


def render_main_ui(uploaded_files, layout_key):
    if uploaded_files:
        st.success(f"**{len(uploaded_files)} bill(s)** uploaded successfully")
        bills_per_page = int(layout_key.split()[0])
        total_pages = (len(uploaded_files) + bills_per_page - 1) // bills_per_page
        st.info(f"Will generate **{total_pages}** A4 page(s)")
    else:
        st.info("Upload your PDF bills")


def show_success_message(output_path):
    st.success("**Generation Complete!**")
    
    col1, col2 = st.columns(2)
    with col1:
        with open(output_path, "rb") as f:
            st.download_button(
                label="Download as PDF",
                data=f,
                file_name="combined_bills.pdf",
                mime="application/pdf",
                use_container_width=True
            )