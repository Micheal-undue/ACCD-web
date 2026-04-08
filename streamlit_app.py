import base64
import streamlit as st
from components.navbar import navbar
import textwrap 

# =============================
# Page Configuration
# =============================
st.set_page_config(
    page_title="ACDC 2026 | ASEAN-CHINA " \
    "Regional Cooperation & Development Forum" \
    "2026(ACCD'26)",
    layout="wide"
)

# =============================
# Helper: Convert image to base64
# =============================
def get_base64_image(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# =============================
# File Paths
# =============================
BG_PATH = "assets/background.jpg"

LOGO1 = "assets/logo.jpg"
LOGO2 = "assets/logo2.jpg"
LOGO3 = "assets/logo3.jpg"
LOGO4 = "assets/logo4.png"
LOGO5 = "assets/logo5.png"
LOGO6 = "assets/logo6.jpg"

LOGO11 = "assets/pptmc.png"
LOGO12 = "assets/ukm_gsb.png"
LOGO13 = "assets/huc.png"
LOGO14 = "assets/IVI.png"

LOGO21 = "assets/HNU.jpg"
LOGO22 = "assets/METDC.jpg"
LOGO23 = "assets/WRTO.jpg"
LOGO24 = "assets/UGUK.jpg"
LOGO25 = "assets/SME.jpg"
LOGO26 = "assets/MFC.jpg"
LOGO27 = "assets/AUT.jpg"


BG_BASE64 = get_base64_image(BG_PATH)

LOGO1_BASE64 = get_base64_image(LOGO1)
LOGO2_BASE64 = get_base64_image(LOGO2)
LOGO3_BASE64 = get_base64_image(LOGO3)
LOGO4_BASE64 = get_base64_image(LOGO4)
LOGO5_BASE64 = get_base64_image(LOGO5)
LOGO6_BASE64 = get_base64_image(LOGO6)

LOGO11_BASE64 = get_base64_image(LOGO11)
LOGO12_BASE64 = get_base64_image(LOGO12)
LOGO13_BASE64 = get_base64_image(LOGO13)
LOGO14_BASE64 = get_base64_image(LOGO14)

LOGO21_BASE64 = get_base64_image(LOGO21)
LOGO22_BASE64 = get_base64_image(LOGO22)
LOGO23_BASE64 = get_base64_image(LOGO23)
LOGO24_BASE64 = get_base64_image(LOGO24)
LOGO25_BASE64 = get_base64_image(LOGO25)
LOGO26_BASE64 = get_base64_image(LOGO26)
LOGO27_BASE64 = get_base64_image(LOGO27)



# =============================
# Global CSS
# =============================
st.markdown(f"""
<style>
body {{
    background-color: #ffffff;
}}
.center {{
    text-align: center;
}}
.navbar {{
    padding: 15px 40px;
    background: #222;
    font-weight: 500;
}}

.nav-item {{
    display: inline-block;
    margin: 0 18px;
    color: white;
}}

/* ---------- HERO ---------- */
.hero {{
    position: relative;
    padding: 90px 20px 70px 20px;
    color: white;
    text-align: center;
    background-image: url("data:image/jpg;base64,{BG_BASE64}");
    background-size: cover;
    background-position: center;
}}
.hero h1 {{
    font-size: 66px;
    font-weight: 700;
}}
.hero h2 {{
    font-size: 24px;
    font-weight: 400;
    margin-top: 12px;
}}
.hero p {{
    font-size: 18px;
    margin-top: 18px;
}}

/* ---------- LOGO ---------- */
.logo-section {{
    padding: 50px 20px;
    background: #f9f9f9;
}}
.logo-row {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 40px;
    flex-wrap: wrap;
}}
.logo-box {{
    background: white;
    padding: 18px 28px;
    border-radius: 14px;
    box-shadow: 0 4px 12px rgba(0,0,0,0.08);
}}
.logo-box img {{
    max-height: 70px;
    display: block;
}}

/* ---------- SECTIONS ---------- */
.section {{
    padding: 80px 20px;
}}
.section-title {{
    font-size: 32px;
    font-weight: 600;
    margin-bottom: 25px;
}}
.section-text {{
    font-size: 18px;
    max-width: 900px;
    margin: auto;
}}
.section-text-left {{
    font-size: 18px;
    max-width: 900px;
    margin: auto;
    line-height: 1.8;
    text-align: left;
}}
.section-text-left ul {{
    padding-left: 20px;
}}
.divider {{
    width: 90px;
    height: 3px;
    background-color: #b00020;
    margin: 28px auto;
}}



/* ---------- CARDS ---------- */
.card {{
    border: 1px solid #e5e5e5;
    border-radius: 14px;
    padding: 26px;
    height: 100%;
}}
.card h4 {{
    margin-bottom: 10px;
}}

/* ---------- CTA ---------- */
.cta-btn {{
    display: inline-block;
    padding: 12px 26px;
    margin: 10px;
    border: 1px solid #b00020;
    border-radius: 25px;
    color: #b00020;
    font-weight: 500;
    text-decoration: none;
}}

/* ---------- FOOTER ---------- */
.footer {{
    padding: 45px 20px;
    font-size: 14px;
    color: #ccc;
    background: #222;
}}

/* ---------- HOST SECTION ---------- */
.host-block {{
    margin-top: 40px;
}}

.host-single {{
    margin-bottom: 60px;
    display: flex;
    flex-direction: column;
    align-items: center;
}}

.host-row {{
    display: flex;
    justify-content: center;
    gap: 80px;
    flex-wrap: wrap;
    margin-top: 20px;
}}


.host-logo {{
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    width: 300px; 
}}

.host-logo img {{
    max-height: 80px;
    width: auto;
    margin-bottom: 15px;
}}


</style>
""", unsafe_allow_html=True)

# =============================
# Top Navigation Bar (Clickable)
# =============================



# 引入导航栏
navbar()


# =============================
# Hero Section
# =============================
st.markdown("""
<div class="hero">
    <h1>
        ASEAN-CHINA<br/>
        Regional Cooperation & Development Forum<br/>
        2026 (ACCD'26)</h1>
    <h2>Cross-border Synergy for a Better Future<br/>跨境合作 · 共创未来</h2>
    <div class="divider"></div>
    <p>
        A high-level regional forum integrating academia, industry and policy dialogue<br/>
        to strengthen ASEAN–China cooperation.
    </p>
    <p>
        📍 Universiti Kebangsaan Malaysia &nbsp;&nbsp; | &nbsp;&nbsp;
        🗓 October 2026 &nbsp;&nbsp; | &nbsp;&nbsp;
        🌏 ASEAN · China · Malaysia
    </p>
</div>
""", unsafe_allow_html=True)

# =============================
# Logo Section  (顺序：logo2 → logo5 → logo3 → logo4 → logo6)
# =============================
st.markdown(f"""
<div class="logo-section">
    <div class="logo-row">
        <div class="logo-box">
            <img src="data:image/jpg;base64,{LOGO2_BASE64}" alt="logo2">
        </div>
        <div class="logo-box">
            <img src="data:image/jpg;base64,{LOGO14_BASE64}" alt="logo3">
        </div>
        <div class="logo-box">
            <img src="data:image/png;base64,{LOGO3_BASE64}" alt="logo5">
        </div>
        <div class="logo-box">
            <img src="data:image/png;base64,{LOGO21_BASE64}" alt="logo4">
        </div>
        <div class="logo-box">
            <img src="data:image/png;base64,{LOGO6_BASE64}" alt="logo5">
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================
# About Section
# =============================
st.markdown("""
<div class="section center">
    <div class="section-title">Overview of ACCD'26</div>
    <div class="divider"></div>
    <div class="section-text">
        ACCD'26 is a five-day ASEAN-China platform that strengthens China-Malaysia Educational,Trade, 
            Cultural, Tourism and Regional Cooperation. The programme includes forums, researchpresentations,
             exhibitions, business matching, Malaysia and China trade policies, industry andcultural visits; 
            bringing together government, universities, and industry to promote academicexchange, business partners,
             regional development, and long-term collaboration.
        <br/><br/>
        This is an annual event.This year it is held in Malaysia at UKM;Next year it rotates to be hosted in China
    </div>
</div>
""", unsafe_allow_html=True)


# =============================
# Key Focus Areas (Refined from Objectives)
# =============================
st.markdown("""
<div class="section center">
    <div class="section-title">Objectives of ACCD'26</div>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

focus_items = [
    ("Academic Collaboration",
     "Strengthen Malaysia-China and ASEANacademic collaboration through jointresearch and cultural education initiatives"),
    
    ("Economic Linkages",
     "Enhance Malaysia-China and ASEANeconomic linkages by connecting enterprises,markets, and regional business networks"),
    
    ("Industry - Academia",
     "Promote industry-academia-government integrationto build a sustainable cooperation ecosystem"),
    
    ("Economy Opportunities",
     "Support enterprises in navigating Malaysia'sinvestment landscape, policies,and digital economy opportunities"),
    
    ("Cross - Border Business",
     "Facilitate structured cross-border business matchingamong companies, chambers, and public agencies"),
    
    ("Long - Term Cooperation",
     "Harbin–ASEAN corridors, ice & snow economy, green energy, youth entrepreneurship, cross-border e-commerce, SME incubators, annual ACCD conference")
]

cols = st.columns(3)
for i, item in enumerate(focus_items):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card center">
            <h4>{item[0]}</h4>
            <p>{item[1]}</p>
        </div>
        """, unsafe_allow_html=True)




# =============================
# Programme Structure (Refined)
# =============================
st.markdown("""
<div class="section center">
    <div class="section-title">Programme Structure </div>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

programme = [
    ("Day 1", "Academic Conference Day",
     "Keynote forums, doctoral clinic, roundtables & parallel paper sessions<br/>"
     "Academic exchange, doctoral mentoring & research collaboration<br/>"),

    ("Day 2", "Policy & Industry Engagement",
     "Opening ceremony, policy briefings, corporate & government keynotes<br/>"
     "Business policy, tourism cooperation & regulatory insights<br/>"),

    ("Day 3", "Business & Government Matching",
     "Enterprise, chamber & government matching sessions<br/>"
     "Targeted networking, partnership building & investment dialogue"),

    ("Day 4", "Institutional & Innovation Visits",
     "Government agencies, tech parks & digital economy institutions<br/>"
     "Trade facilitation, innovation ecosystems & investment environment"),

    ("Day 5", "Culture & City Experience",
     "KLCC, Putrajaya, Central Market & heritage city tour<br/>"
     "Cultural exchange, tourism exploration & urban engagement"),

    ("Days 1–3", "Exhibition (Parallel)",
     "Industry, technology, cultural & education exhibitions<br/>"
     "Showcasing innovation, industry and academic cooperation")
]

prog_cols = st.columns(3)
for i, item in enumerate(programme):
    with prog_cols[i % 3]:
        st.markdown(f"""
        <div class="card center">
            <h4>{item[0]}</h4>
            <strong>{item[1]}</strong>
            <p>{item[2]}</p>
        </div>
        """, unsafe_allow_html=True)



# =============================
# Conference Fees (Card Style)
# =============================
st.markdown("""
<div class="section center">
    <div class="section-title">Conference Fees</div>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

fees = [
    ("Student (Malaysia)", "RM 600 / RM 300", "Local student presenter / participant"),
    ("International Student (Early-Bird)", "USD 150 / USD 100", "Discounted early registration"),
    ("International Student", "USD 200 / USD 150", "Standard student rate"),
    ("Regular (Early-Bird)", "USD 300 / USD 150", "Early-bird professional rate"),
    ("Regular", "USD 350 / USD 200", "Standard professional rate")
]

fee_cols = st.columns(3)

for i, item in enumerate(fees):
    with fee_cols[i % 3]:
        st.markdown(f"""
        <div class="card center">
            <h4>{item[0]}</h4>
            <strong>{item[1]}</strong>
            <p>{item[2]}</p>
        </div>
        """, unsafe_allow_html=True)




# =============================
# Hosted & Co-organised & Partners Section
# =============================

html_content = f"""
<div class="section center">
<div class="section-title">Hosted & Co-organised By</div>
<div class="divider"></div>
<div class="host-block">
<div class="host-single" style="display: flex; flex-direction: column; align-items: center; margin-bottom: 50px;">
<h4 style="margin-bottom: 20px;">Hosted By</h4>
<img src="data:image/png;base64,{LOGO11_BASE64}" style="max-height: 80px; margin-bottom: 10px;">
<div style="font-size: 16px;">Malaysia–China Higher Education Exchange Association (PPTMC)</div>
</div>
<h4 style="margin-bottom: 30px;">Co-organised By</h4>
<div class="host-row" style="display: flex; justify-content: center; gap: 60px; flex-wrap: wrap; margin-bottom: 80px;">
<div style="display: flex; flex-direction: column; align-items: center; width: 250px;">
<img src="data:image/jpg;base64,{LOGO14_BASE64}" style="max-height: 80px; margin-bottom: 10px;">
<div style="text-align: center;">UKM Institute of Visual Informatics</div>
</div>
<div style="display: flex; flex-direction: column; align-items: center; width: 250px;">
<img src="data:image/jpg;base64,{LOGO21_BASE64}" style="max-height: 80px; margin-bottom: 10px;">
<div style="text-align: center;">Harbin Normal University (HNU)</div>
</div>
</div>

<div style="margin-top: 50px;">
<h4 style="margin-bottom: 40px;">Potential Co-Partners</h4>
<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; max-width: 1000px; margin: 0 auto;">
<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 30%; margin-bottom: 40px;">
<img src="data:image/jpg;base64,{LOGO13_BASE64}" style="max-height: 75px; margin-bottom: 15px;">
<div style="font-size: 14px; font-weight: 500;">Harbin University of Commerce</div>
</div>
<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 30%; margin-bottom: 40px;">
<img src="data:image/jpg;base64,{LOGO22_BASE64}" style="max-height: 75px; margin-bottom: 15px;">
<div style="font-size: 14px; font-weight: 500;">MATRADE (Tentative)</div>
</div>
<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 30%; margin-bottom: 40px;">
<img src="data:image/jpg;base64,{LOGO23_BASE64}" style="max-height: 75px; margin-bottom: 15px;">
<div style="font-size: 14px; font-weight: 500;">World Research Travel Organisation</div>
</div>

<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 30px;">
<img src="data:image/jpg;base64,{LOGO24_BASE64}" style="max-height: 65px; margin-bottom: 15px;">
<div style="font-size: 13px;">University of Glasgow</div>
</div>
<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 30px;">
<img src="data:image/jpg;base64,{LOGO25_BASE64}" style="max-height: 65px; margin-bottom: 15px;">
<div style="font-size: 13px;">SME Association of Malaysia</div>
</div>
<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 30px;">
<img src="data:image/jpg;base64,{LOGO26_BASE64}" style="max-height: 65px; margin-bottom: 15px;">
<div style="font-size: 13px;">Malaysia Fujian Chamber of Commerce</div>
</div>
<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 30px;">
<img src="data:image/jpg;base64,{LOGO27_BASE64}" style="max-height: 65px; margin-bottom: 15px;">
<div style="font-size: 13px;">Asia University Taiwan</div>
</div>
</div>
</div>
</div>
</div>
"""

st.markdown(html_content, unsafe_allow_html=True)



# =============================
# Cooperation with MATRADE Section
# =============================
st.markdown("""
<div class="section center">
    <div class="section-title">Cooperation with MATRADE</div>
    <div class="divider"></div>
    <div class="section-text-left">
        <ol>
            <li>Provide speakers and educational materials to introduce Malaysia export policies and promotion, international trading between ASEAN and China;</li>
            <li>Connect and invite other ASEAN Trade officers to participate;</li>
            <li>Visit MATRADE office and exchange;</li>
            <li>Advertise and promote ACDC'26 program;</li>
            <li>Use MATRADE logo as co-partner;</li>
            <li>Sponsorship for the event in terms of monetary support, provide 2 buses and lunch when visiting MATRADE.</li>
        </ol>
    </div>
</div>
""", unsafe_allow_html=True)

# =============================
# Potential Sponsorship Section
# =============================
st.markdown("""
<div class="section center">
    <div class="section-title">Potential Sponsorship</div>
    <div class="divider"></div>
    <div class="section-text">
        Malaysia External Trade Development Corporation (MATRADE)<br/><br/>
        MyCEB<br/><br/>
        SME Corporation Malaysia and their members<br/><br/>
        Technology Park Malaysia Corporation Sdn Bhd<br/><br/>
        Malaysia Digital Economy Corporation (MDEC)<br/><br/>
        Chamber of Commerce in Malaysia
    </div>
</div>
""", unsafe_allow_html=True)

# =============================
# Footer  
# =============================
st.markdown("""
<div class="footer center">
    ASEAN–CHINA Regional Development & Cooperation Forum 2026 (ACCD 2026)<br/>
    Universiti Kebangsaan Malaysia (UKM)<br/>
    © 2026 ACDC Organising Committee. All Rights Reserved.
</div>
""", unsafe_allow_html=True)

