
import streamlit as st

st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    '어떻게 받을래?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    '범위설정',
    0.0, 100.0, (25.0, 75.0)
)
