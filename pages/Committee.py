import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="Committee | ACDC 2026", layout="wide")

navbar()

# ===============================
# PAGE TITLE
# ===============================
st.markdown("## Committee")
st.markdown("---")


# ==========================================================
# 1️⃣ Committee Table (No Subheading)
# ==========================================================

st.markdown("""
<div style="display:flex; justify-content:center;">

<table style="border-collapse: collapse; width:85%; text-align:left;">
<tr style="background-color:#0b1f3a; color:white;">
<th style="padding:10px; border:1px solid #ddd;">Roles</th>
<th style="padding:10px; border:1px solid #ddd;">Name</th>
<th style="padding:10px; border:1px solid #ddd;">Position</th>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Advisor</td>
<td style="border:1px solid #ddd;">Tan Sri. Dr. Ng Yen Yen</td>
<td style="border:1px solid #ddd;">
Honorary President of the World Research Travel Association (WRTO)<br>
Former Minister of Tourism and Culture
</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Co-Chairman</td>
<td style="border:1px solid #ddd;">Prof. Ts. Dr. Mohd Helmi Ali</td>
<td style="border:1px solid #ddd;">
Deputy Dean (Research & Innovation)<br>
Graduate School of Business (GSB)<br>
Universiti Kebangsaan Malaysia
</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Co-Chairman</td>
<td style="border:1px solid #ddd;">Dato Low Kok Thai</td>
<td style="border:1px solid #ddd;">
Chairman of PPTMC
</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Co-Chairman</td>
<td style="border:1px solid #ddd;">(Pending Confirmation)</td>
<td style="border:1px solid #ddd;">
Professor from Harbin University of Commerce
</td>
</tr>

</table>

</div>
""", unsafe_allow_html=True)

st.markdown("---")


# ==========================================================
# 2️⃣ Chairs for Program
# ==========================================================

st.markdown("<h3 style='text-align:center;'>Chairs for Program</h3>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:left; width:80%; margin:auto;'>

1. Prof. Ts. Dr. Mohd Helmi Ali, Graduate School of Business, UKM, Malaysia  

2. Distinguished Professor from Harbin University of Commerce (Pending Confirmation)  

3. Prof. Dr. Ming Lang Tseng, Asia University, Taiwan  

4. Prof. Dr. Ming K. Lim, University of Glasgow, United Kingdom  

</div>
""", unsafe_allow_html=True)

st.markdown("---")
st.write("© 2026 ACDC Organising Committee")