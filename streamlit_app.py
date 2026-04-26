import base64
import streamlit as st
from components.navbar import navbar
import textwrap 


st.set_page_config(
    page_title="ACCD 2026 | ASEAN-CHINA Regional Cooperation & Development Forum",
    layout="wide",
    initial_sidebar_state="collapsed" # 初始状态设为折叠
)

# 深度清理 Streamlit Cloud 专用组件
# 极致隐藏版 CSS
hide_style = """
    <style>
    /* 1. 隐藏顶部 Header 和菜单 */
    header[data-testid="stHeader"] {
        display: none !important;
    }
    
    /* 2. 隐藏侧边栏及其控制按钮 */
    section[data-testid="stSidebar"], 
    button[data-testid="stSidebarCollapsedControl"] {
        display: none !important;
    }

    /* 3. 隐藏底部 "Made with Streamlit" */
    footer {
        display: none !important;
    }

    /* 4. 【核心突破】强力清除右下角管理/部署按钮 */
    /* 针对所有包含 'Deploy' 或 'Toolbar' 字样的容器进行拦截 */
    [data-testid="stAppViewToolbar"],
    .stAppDeployButton,
    .stDeployButton,
    div[class*="stAppDeployButton"],
    div[class*="DeployButton"],
    div[class*="viewerBadge"] {
        display: none !important;
        visibility: hidden !important;
        height: 0 !important;
        width: 0 !important;
        opacity: 0 !important;
        pointer-events: none !important;
    }

    /* 5. 针对移动端可能出现的悬浮管理层 */
    #streamlit_cloud_host_floating_container,
    .st-emotion-cache-1wbqy5l, /* 某些版本中的特定类名 */
    [aria-label="Manage app"] {
        display: none !important;
    }

    /* 6. 移除页面边距 */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
    }
    </style>
"""

st.markdown(hide_style, unsafe_allow_html=True)


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
LOGO28 = "assets/MCEB.png"
LOGO29 = "assets/SEARCH.jpg"


SPEAKER1_PATH = "assets/speaker1.jpg" 
SPEAKER2_PATH = "assets/speaker2.jpg"
SPEAKER3_PATH = "assets/speaker3.jpg"


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
LOGO28_BASE64 = get_base64_image(LOGO28)
LOGO29_BASE64 = get_base64_image(LOGO29)

DEST_1_B64 = get_base64_image("assets/dest_klcc.jpg")
DEST_2_B64 = get_base64_image("assets/dest_aquaria.jpg")
DEST_3_B64 = get_base64_image("assets/dest_twin_towers.jpg")
DEST_4_B64 = get_base64_image("assets/dest_putrajaya.jpg")
DEST_5_B64 = get_base64_image("assets/dest_batu_caves.jpg")
DEST_6_B64 = get_base64_image("assets/dest_central_market.jpg")
DEST_7_B64 = get_base64_image("assets/dest_genting.jpg")


SPEAKER1_B64 = get_base64_image(SPEAKER1_PATH)
SPEAKER2_B64 = get_base64_image(SPEAKER2_PATH)
SPEAKER3_B64 = get_base64_image(SPEAKER3_PATH)

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

/* ----------  Logo 卡片 ---------- */
.logo-section {{
    padding: 60px 20px;
    background: #fdfdfd; /* 极淡的底色，衬托白色卡片 */
}}

.logo-row {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 25px; /* 卡片之间的间距 */
    flex-wrap: wrap;
}}

.logo-box {{
    /* 核心修复：所有卡片固定尺寸 */
    width: 220px;  
    height: 130px;
    
    background: white;
    border-radius: 16px; /* 稍微大一点的圆角更现代 */
    box-shadow: 0 6px 15px rgba(0,0,0,0.05); /* 柔和的阴影 */
    border: 1px solid #f0f0f0; /* 淡淡的边框线，增加质感 */
    
    /* 居中里面的图片 */
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 15px; 
    transition: transform 0.3s ease;
}}

/* 悬停动画 */
.logo-box:hover {{
    transform: translateY(-5px);
    box-shadow: 0 10px 20px rgba(0,0,0,0.1);
}}

.logo-box img {{
    /* 图片默认大小限制 */
    max-width: 85%;
    max-height: 65px; 
    object-fit: contain;
    display: block;
}}
/* ---------- 针对性大小调整 ---------- */

/* 1. 变小 */
.logo-box:nth-child(2) img {{
    max-height: 60px; /* 从 70 调小到 50 */
}}

/* 2. 变大 */
.logo-box:nth-child(1) img {{
    max-height: 95px; /* 从 70 调大到 95 */
}}
.logo-box:nth-child(3) img,
.logo-box:nth-child(4) img
 {{
    max-height: 80px; /* 从 70 调大到 95 */
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

/* ---------- SPEAKERS CARDS ---------- */
.speaker-card {{
    background: #ffffff;
    border: 1px solid #f0f2f6;
    border-radius: 20px;
    padding: 30px 20px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
    transition: transform 0.3s ease;
    height: 100%;
    display: flex;
    flex-direction: column;
    align-items: center;
}}

.speaker-card:hover {{
    transform: translateY(-5px);
    border-color: #b00020;
}}

.details-link {{
    display: inline-block;
    background-color: #e8f0fe;
    color: #0b1f3a !important;
    padding: 10px 15px;
    border-radius: 10px;
    text-decoration: none !important;
    font-size: 24px;
    margin: 15px 0;
    line-height: 1;
}}

.details-link:hover {{
    background-color: #0b1f3a;
    color: #ffffff !important;
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
    <h2>Cross-border Synergy for a Better Future<br/></h2>
    <div class="divider"></div>
    <p>
        A high-level regional forum integrating academia, industry and policy dialogue<br/>
        to strengthen ASEAN–China cooperation.
    </p>
    <p>
        📍 Universiti Kebangsaan Malaysia &nbsp;&nbsp; | &nbsp;&nbsp;
        🗓 2nd until 5th November 2026 &nbsp;&nbsp; | &nbsp;&nbsp;
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
            <img src="data:image/jpg;base64,{LOGO3_BASE64}" alt="logo2">
        </div>
        <div class="logo-box">
            <img src="data:image/jpg;base64,{LOGO14_BASE64}" alt="logo14">
        </div>
        <div class="logo-box">
            <img src="data:image/png;base64,{LOGO2_BASE64}" alt="logo3">
        </div>
        <div class="logo-box">
            <img src="data:image/png;base64,{LOGO21_BASE64}" alt="logo21">
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
The ASEAN–China Regional Cooperation & Development Forum 2026 (ACCD’26) is a premier international platform that brings together visionary leaders, academics, policymakers, and industry pioneers from across ASEAN and China to shape the future of regional collaboration.  
      <br/><br/>
Centered on the theme “Cross-Border Synergy for a Better Future,” ACCD’26 goes beyond a traditional conference—offering a dynamic blend of high-impact forums, cutting-edge research exchanges, business matchmaking, exhibitions, and immersive industry visits.

Designed to spark meaningful connections and real-world outcomes, the forum empowers participants to unlock new trade and investment opportunities, drive innovation in the digital and green economy, and build lasting academic and industry partnerships.

By bridging ideas, people, and markets, ACCD’26 positions itself as a gateway to ASEAN–China cooperation, fostering sustainable growth, cultural understanding, and transformative collaborations for the future.
        <br/><br/>
    </div>
</div>
""", unsafe_allow_html=True)


# =============================
# Keynote Speakers Section
# =============================
st.markdown("""
<div class="section center" style="padding-bottom: 20px;">
    <div class="section-title">Keynote Speakers</div>
    <div class="divider"></div>
</div>
""", unsafe_allow_html=True)

# 1. 定义数据列表 (保持不变，确保 anchor 字段存在)
speakers = [
    {
        "name": "Prof. Ts. Dr. Mohd Helmi Ali",
        "image": SPEAKER3_B64,
        "anchor": "helmi-ali"
    },
    {
        "name": "Prof. Ming-Lang Tseng",
        "image": SPEAKER1_B64,
        "anchor": "ming-lang"
    },
    {
        "name": "Professor Dr. Ming Lim",
        "image": SPEAKER2_B64,
        "anchor": "ming-lim"
    }
]

# 2. 创建容器列
empty_l, col1, col2, col3, empty_r = st.columns([1, 2, 2, 2, 1])
cols = [col1, col2, col3]

# 3. 循环渲染
for i, col in enumerate(cols):
    with col:
        # 【关键修改】 href 中同时加入 query 参数 (?) 和锚点 (#)
        target_link = f"/Committee?speaker={speakers[i]['anchor']}#{speakers[i]['anchor']}"
        
        st.markdown(f"""
        <div class="speaker-card">
            <img src="data:image/jpg;base64,{speakers[i]['image']}" style="width:200px; height:200px; border-radius:50%; object-fit:cover; border:3px solid #f0f2f6;">
            <a href="{target_link}" target="_self" class="details-link">📇</a>
            <div class="speaker-name">{speakers[i]['name']}</div>
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
<style>
    .card-fix {
        min-height: 250px; /* 适当增加高度以确保空间充裕 */
        display: flex;
        flex-direction: column;
        justify-content: center; /* 关键：这会让内容在垂直方向居中 */
        align-items: center;
        text-align: center;
        padding: 25px;
        margin-bottom: 20px;
        box-sizing: border-box;
    }
    
    /* 确保标题和段落没有过大的默认边距干扰居中 */
    .card-fix h4 {
        margin-top: 0;
        margin-bottom: 10px;
    }
    .card-fix p {
        margin-bottom: 0;
    }
</style>
""", unsafe_allow_html=True)

focus_items = [
    ("Technology & Academic Collaboration",
     "Establish joint research centres, Master/PhD programmes, and academic exchanges through the ASEAN-China Regional Cooperation Development Alliance."),

    ("Economic Linkages",
     "Leverage UKM as an ASEAN gateway to connect Harbin and Chinese enterprises with regional markets and government-business networks."),

    ("Industry-Academia-Society",
     "Integrate resources from enterprises, universities, and chambers to build a sustainable cooperation ecosystem and social development."),

    ("Business Environment & Policy",
     "Navigate tax incentives, investment policies, and the MyDIGITAL blueprint to support foreign investment and free trade zone access."),

    ("Technologies Exchange",
     "Facilitate tech transfer among China and ASEAN, focusing on AI application in e-commerce, new media, and digital business models."),

    ("Business Matching Opportunities",
     "Structured matching between Chinese enterprises and Malaysian chambers, companies, and government agencies to foster bilateral growth.")
]

cols = st.columns(3)
for i, item in enumerate(focus_items):
    with cols[i % 3]:
        st.markdown(f"""
        <div class="card center card-fix">
            <h4>{item[0]}</h4>
            <p>{item[1]}</p>
        </div>
        """, unsafe_allow_html=True)



# =============================
# Programme Structure (Refined to 4 Pillars)
# =============================
st.markdown("""
<div class="section center">
    <div class="section-title">Programme Structure</div>
    <div class="divider"></div>
</div>
<style>
    .prog-card {
        min-height: 280px; /* 统一高度确保对齐 */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        text-align: center;
        padding: 20px;
        margin-bottom: 20px;
    }
    .prog-card h4 { color: #FF4B4B; margin-bottom: 5px; }
    .prog-card strong { display: block; margin-bottom: 10px; font-size: 1.1em; }
    .prog-card p { font-size: 0.95em; line-height: 1.5; }
</style>
""", unsafe_allow_html=True)

# 重新整合后的 4 个板块内容
programme = [
    ("Days 1 & 2", "Grand Opening & Academic Summit",
     "<b>Nov 2-3:</b> Opening Ceremony & Keynote Forums.<br/>"
     "Roundtable sessions, doctoral clinics & paper presentations.<br/>"
     "<i>Parallel Exhibition open.</i>"),

    ("Day 3", "Policy & Business Matching",
     "<b>Nov 4:</b> Strategic briefings by MATRADE, JAKIM & Tourism.<br/>"
     "China-Malaysia enterprise, chamber & government matching.<br/>"
     "<i>Parallel Exhibition open.</i>"),

    ("Day 4", "Institutional & Innovation Visits",
     "<b>Nov 5:</b> Field visits to MATRADE & SME Association.<br/>"
     "UKM/UPM Research Institutes & Huawei corporate tech tours.<br/>"
     "Insights into trade facilitation & digital economy."),

    ("Day 5", "Culture & Heritage Experience",
     "<b>Nov 6:</b> Full-day cultural engagement & Melaka historical tour.<br/>"
     "KL city landmarks: KLCC, Putrajaya, Central Market & Batu Caves.<br/>"
     "Deepening regional cultural and tourism bonds.")
]

# 采用 2列 x 2行 的布局，视觉上更平衡
prog_cols = st.columns(2)
for i, item in enumerate(programme):
    with prog_cols[i % 2]:
        st.markdown(f"""
        <div class="card center prog-card">
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
<div style="height: 100px; display: flex; align-items: center; justify-content: center;">
<img src="data:image/png;base64,{LOGO11_BASE64}" style="height: 100px; object-fit: contain;">
</div>
<div style="font-size: 16px; margin-top: 10px;">Malaysia–China Higher Education Exchange Association (PPTMC)</div>
</div>

<h4 style="margin-bottom: 30px;">Co-organised By</h4>
<div class="host-row" style="display: flex; justify-content: center; gap: 60px; flex-wrap: wrap; margin-bottom: 80px;">
<div style="display: flex; flex-direction: column; align-items: center; width: 250px;">
<div style="height: 120px; display: flex; align-items: center; justify-content: center;">
<img src="data:image/jpg;base64,{LOGO14_BASE64}" style="height: 120px; object-fit: contain; padding: 25px 0;">
</div>
<div style="text-align: center; margin-top: 10px;">UKM Institute of Visual Informatics</div>
</div>
<div style="display: flex; flex-direction: column; align-items: center; width: 250px;">
<div style="height: 120px; display: flex; align-items: center; justify-content: center;">
<img src="data:image/jpg;base64,{LOGO21_BASE64}" style="height: 120px; object-fit: contain;">
</div>
<div style="text-align: center; margin-top: 10px;">Harbin Normal University (HNU)</div>
</div>
</div>

<div style="margin-top: 50px;">
<h4 style="margin-bottom: 40px;">Potential Co-Partners</h4>
<div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; max-width: 1000px; margin: 0 auto;">

<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 40px;">
<div style="height: 150px; display: flex; align-items: center; justify-content: center;">
<img src="data:image/jpg;base64,{LOGO13_BASE64}" style="height: 80px; object-fit: contain;">
</div>
<div style="font-size: 14px; font-weight: 500; text-align: center; margin-top: 10px;">Harbin University of Commerce</div>
</div>

<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 40px;">
<div style="height: 150px; display: flex; align-items: center; justify-content: center;">
<img src="data:image/jpg;base64,{LOGO22_BASE64}" style="height: 150px; object-fit: contain;">
</div>
<div style="font-size: 14px; font-weight: 500; text-align: center; margin-top: 10px;">MATRADE (Tentative)</div>
</div>

<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 40px;">
<div style="height: 150px; display: flex; align-items: center; justify-content: center;">
<img src="data:image/jpg;base64,{LOGO23_BASE64}" style="height: 150px; object-fit: contain;">
</div>
<div style="font-size: 14px; font-weight: 500; text-align: center; margin-top: 10px;">World Research Travel Organisation</div>
</div>

<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 40px;">
<div style="height: 150px; display: flex; align-items: center; justify-content: center;">
<img src="data:image/jpg;base64,{LOGO24_BASE64}" style="height: 150px; object-fit: contain;">
</div>
<div style="font-size: 13px; text-align: center; margin-top: 10px;">University of Glasgow</div>
</div>

<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 30px;">
<div style="height: 150px; display: flex; align-items: center; justify-content: center;">
<img src="data:image/jpg;base64,{LOGO25_BASE64}" style="height: 150px; object-fit: contain;">
</div>
<div style="font-size: 13px; text-align: center; margin-top: 10px;">SME Association of Malaysia</div>
</div>

<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 30px;">
<div style="height: 150px; display: flex; align-items: center; justify-content: center;">
<img src="data:image/jpg;base64,{LOGO26_BASE64}" style="height: 150px; object-fit: contain;">
</div>
<div style="font-size: 13px; text-align: center; margin-top: 10px;">Malaysia Fujian Chamber of Commerce</div>
</div>

<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 30px;">
<div style="height: 150px; display: flex; align-items: center; justify-content: center;">
<img src="data:image/jpg;base64,{LOGO27_BASE64}" style="height: 130px; object-fit: contain;">
</div>
<div style="font-size: 13px; text-align: center; margin-top: 10px;">Asia University Taiwan</div>
</div>

<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 30px;">
<div style="height: 150px; display: flex; align-items: center; justify-content: center;">
<img src="data:image/jpg;base64,{LOGO28_BASE64}" style="height: 130px; object-fit: contain;">
</div>
<div style="font-size: 13px; text-align: center; margin-top: 10px;">Malaysia Convention& Exhibition Bureau</div>
</div>

<div style="display: flex; flex-direction: column; align-items: center; flex: 0 0 22%; margin-bottom: 30px;">
<div style="height: 150px; display: flex; align-items: center; justify-content: center;">
<img src="data:image/jpg;base64,{LOGO29_BASE64}" style="height: 130px; object-fit: contain;">
</div>
<div style="font-size: 13px; text-align: center; margin-top: 10px;">Southeast Asia Research Centre for Humanities</div>
</div>

</div>
</div>
</div>
</div>
"""

st.markdown(html_content, unsafe_allow_html=True)



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

