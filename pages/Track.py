import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="Themes | ACCD 2026", layout="wide")

navbar()




# ===== PAGE CONTENT =====
st.markdown("## Themes")
st.markdown("---")

st.write("""
- Digital Economy & Technology  
- Trade & Investment  
- Sustainable Development Goals & Sustainable Lifestyle  
- Entrepreneurship & Innovation  
- Green Economy  
- Cultural & Tourism Exchange  
  

""")



st.markdown("---")
st.write("© 2026 ACDC Organising Committee")
