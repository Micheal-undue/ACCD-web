import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="About | ACDC 2026", layout="wide")

navbar()




# ===== PAGE CONTENT =====
st.markdown("## Track & Selection")
st.markdown("---")

st.write("""
- Digital Economy & Technology  
- Trade & Investment  
- Sustainable Development Goals & Sustainable Lifestyle  
- Entrepreneurship & Innovation  
- Green Economy  
- Cultural & Tourism Exchange  
  

- 数字经济与技术  
- 贸易与投资  
- 可持续发展目标与可持续生活方式  
- 创业与创新  
- 绿色经济  
- 文化与旅游交流
""")



st.markdown("---")
st.write("© 2026 ACDC Organising Committee")
