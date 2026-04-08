import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="Author Guidelines | ACDC 2026", layout="wide")

navbar()

# ===== PAGE TITLE =====
st.markdown("## Author Guidelines")
st.markdown("---")


# =====================================================
# 1️⃣ Potential Publication
# =====================================================
st.markdown("<h3 style='text-align:center;'>Potential Publication</h3>", unsafe_allow_html=True)

st.markdown("""
<div>

<span style="color:#1f4ed8; font-weight:600;">E3S Web of Conferences</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;Scopus, Open Access, areas related to Environment, Energy and Earth Sciences.<br><br>

<span style="color:#1f4ed8; font-weight:600;">IOP Publishing</span><br>
&nbsp;&nbsp;&nbsp;&nbsp;Scopus, Open Access, areas related to Journal of Physics, Earth and Environmental Science or Materials Science and Engineering.

</div>
""", unsafe_allow_html=True)

st.markdown("---")


# =====================================================
# 2️⃣ Important Date
# =====================================================
st.markdown("<h3 style='text-align:center;'>Important Date (to be released)</h3>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center;'>

Online Submission Open : to be confirmed  
Submission Deadline of Abstract : to be confirmed  
Notification of Acceptance : to be confirmed  
Full Paper Submission : to be confirmed  
Payment Deadline : to be confirmed  
Registration and Opening : to be confirmed  
Conference Date : to be confirmed  

</div>
""", unsafe_allow_html=True)

st.markdown("---")


# =====================================================
# 3️⃣ Registration Fee
# =====================================================
st.markdown("<h3 style='text-align:center;'>Registration Fee (Students)</h3>", unsafe_allow_html=True)

st.markdown("""
<div style="display:flex; justify-content:center;">

<table style="border-collapse: collapse; width:75%; text-align:center;">
<tr style="background-color:#0b1f3a; color:white;">
<th style="padding:10px; border:1px solid #ddd;">Category</th>
<th style="padding:10px; border:1px solid #ddd;">Presenter</th>
<th style="padding:10px; border:1px solid #ddd;">Non-Presenter</th>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd; font-weight:600;">Student (Malaysian)</td>
<td style="border:1px solid #ddd;">RM 600</td>
<td style="border:1px solid #ddd;">RM 300</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd; font-weight:600;">International Student (Early-Bird)</td>
<td style="border:1px solid #ddd;">USD 150</td>
<td style="border:1px solid #ddd;">USD 100</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd; font-weight:600;">International Student</td>
<td style="border:1px solid #ddd;">USD 200</td>
<td style="border:1px solid #ddd;">USD 150</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd; font-weight:600;">Regular (Early-Bird)</td>
<td style="border:1px solid #ddd;">USD 300</td>
<td style="border:1px solid #ddd;">USD 150</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd; font-weight:600;">Regular</td>
<td style="border:1px solid #ddd;">USD 350</td>
<td style="border:1px solid #ddd;">USD 200</td>
</tr>

</table>

</div>
""", unsafe_allow_html=True)

st.markdown("<p style='text-align:center; font-size:14px;'>*Early Registration on/before Jun 01, 2026</p>", unsafe_allow_html=True)

st.markdown("---")
st.write("© 2026 ACDC Organising Committee")