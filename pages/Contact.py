import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="Contact US | ACDC 2026", layout="wide")

navbar()

# ===============================
# PAGE TITLE
# ===============================
st.markdown("## Contact US")
st.markdown("---")

# Contact Info
st.markdown("""
<div style='text-align:left; font-size:18px;'>
<strong>Email:</strong> @ukm.edu.my
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===============================
# Google Map – Exact Location
# ===============================
st.markdown("""
<div style="display:flex; justify-content:center;">
<iframe
    src="https://www.google.com/maps?q=Lingkungan+Ilmu,,+43600+Bangi,+Selangor,+Malaysia&output=embed"
    width="1000"
    height="450"
    style="border:0; border-radius:10px;"
    allowfullscreen=""
    loading="lazy">
</iframe>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.write("© 2026 ACDC Organising Committee")