import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="Travel | ACCD 2026", layout="wide")

navbar()

# ===============================
# PAGE TITLE
# ===============================
st.markdown("## Venue & Accommodation")
st.markdown("---")

# ==========================================================
# 1️⃣ Conference Venue
# ==========================================================
st.markdown("<h3 style='text-align:center;'>Conference Venue</h3>", unsafe_allow_html=True)

col_left, col_right = st.columns([1.2, 1])

# ---------- LEFT SIDE ----------
with col_left:

    # 地点文本（在平面图上方）
    st.markdown("""
    <div style='text-align:center; margin-bottom:15px;'>
    <strong style="font-size:18px;">
    Dewan Tun Abdullah Mohd Salleh (DTAMS)<br>
    Universiti Kebangsaan Malaysia
    </strong>
    </div>
    """, unsafe_allow_html=True)

    # 平面图
    st.image("assets/venue_map.jpg", use_container_width=True)

    # 参会信息（在平面图下方）
    st.markdown("""
    <div style='text-align:center; margin-top:15px; font-size:14px;'>

    <strong>ESTIMATED PARTICIPANTS</strong><br>
    1000 people (300 international delegates)<br><br>

    <strong>EXHIBITION BOOTHS</strong><br>
    40 booths (20 from ASEAN; 20 from China)

    </div>
    """, unsafe_allow_html=True)


# ---------- RIGHT SIDE ----------
with col_right:

    img_col1, img_col2 = st.columns(2)

    with img_col1:
        st.image("assets/venue_1.jpg", use_container_width=True)
        st.image("assets/venue_3.jpg", use_container_width=True)

    with img_col2:
        st.image("assets/venue_2.jpg", use_container_width=True)
        st.image("assets/venue_4.jpg", use_container_width=True)

st.markdown("---")

# =========================
# 统一图片视觉高度 
# =========================
def uniform_image(path, height="250px"):
    """
    使用透明背景容器，确保图片完整显示且不裁剪。
    object-fit: contain 保持比例缩放。
    """
    import base64
    import os

    if os.path.exists(path):
        with open(path, "rb") as f:
            data = base64.b64encode(f.read()).decode()
        
    
        st.markdown(f"""
            <div style="display: flex; justify-content: center; align-items: center; 
                        height: {height}; background-color: transparent; margin: 10px 0;">
                <img src="data:image/png;base64,{data}" 
                     style="max-height: 100%; max-width: 100%; object-fit: contain;">
            </div>
        """, unsafe_allow_html=True)
    else:
        st.error(f"Image not found: {path}")

# ==========================================================
# 🏨 Featured Hotels 
# ==========================================================
st.markdown("<h3 style='text-align:center; margin-top:50px;'>Featured Hotels</h3>", unsafe_allow_html=True)

st.markdown("""
<div style='text-align: center; font-style: italic; font-size: 15px; color: #444; margin-bottom: 10px;'>
    Shuttle bus will be provided for participants staying at these hotels to the event venue on a daily basis
</div>
""", unsafe_allow_html=True)



# 用于居中标题和简介
def centered_hotel_info(title, subtitle=""):
    st.markdown(f"""
        <div style='text-align: center; margin-bottom: 10px;'>
            <strong style='font-size: 18px;'>{title}</strong><br>
            <span style='font-size: 14px; color: #666;'>{subtitle}</span>
        </div>
    """, unsafe_allow_html=True)

# =========================
# Hotel 1
# =========================
st.markdown("<h4 style='text-align:center;'>BANGI GOLF RESORT (AS OF APRIL 2026) (5-STAR RATING)</h4>", unsafe_allow_html=True)

# 如果酒店2只是展示环境，没有具体房型标题，可以直接放图片
img1, img2, img3 = st.columns(3)
with img1:
    uniform_image("assets/hotel2_1.png", height="220px")
with img2:
    uniform_image("assets/hotel2_2.png", height="220px")
with img3:
    uniform_image("assets/hotel2_3.png", height="220px")

st.markdown("""
<div style='text-align:center; margin-top:12px; font-size: 15px; color: #444;'>
    DELUXE ROOM <br> RM 520 PER NIGHT WITH BREAKFAST AND BATHTUB (TAX NOT INCLUDED)
</div>
""", unsafe_allow_html=True)


# =========================
# Hotel 2
# =========================
st.markdown("<h4 style='text-align:center; margin-top:30px;'>TENERA HOTEL & SUITES BANGI (AS OF APRIL 2026) (4-STAR RATING)</h4>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])

with col1:
    centered_hotel_info("STANDARD KING ", "RM 300 PER NIGHT WITH BREAKFAST (TAX NOT INCLUDED)")
    uniform_image("assets/hotel1_single.png", height="280px")

with col2:
    centered_hotel_info("SUPERIOR TWIN", " RM 300 PER NIGHT WITH BREAKFAST (TAX NOT INCLUDED)")
    uniform_image("assets/hotel1_double.png", height="280px")



# =========================
# Hotel 3
# =========================
st.markdown("<h4 style='text-align:center;'>ROYAL PARK HOTEL @ UNITEN, PUTRAJAYA (AS OF APRIL 2026) (3-STARS RATING)</h4>", unsafe_allow_html=True)
col3_1, col3_2 = st.columns([1, 1])

with col3_1:
    centered_hotel_info("SUPERIOR DOUBLE", " RM 200 PER NIGHT WITH BREAKFAST (TAX NOT INCLUDED)")
    uniform_image("assets/hotel3_single.png", height="280px")

with col3_2:
    centered_hotel_info("SUPERIOR TWIN", "RM 200 PER NIGHT WITH BREAKFAST (TAX NOT INCLUDED)")
    uniform_image("assets/hotel3_double.png", height="280px")


st.markdown("---")


# ==========================================================
# 2 Nearest Hotel
# ==========================================================
st.markdown("<h3 style='text-align:center;'>Other Hotels</h3>", unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center;'>

<ul style="list-style-type:none; padding-left:0;">
<li>The Everly Putrajaya (11.8 km)</li>
<li>Mercure Living Putrajaya (12.8 km)</li>
<li>Le' Meridian Putrajaya (13.6 km)</li>
<li>Moxy Putrajaya (13.8 km)</li>
</ul>

</div>
""", unsafe_allow_html=True)


# ===== PAGE CONTENT =====
st.markdown("---")

# 定义 Google 表单链接
registration_url = "https://docs.google.com/forms/d/e/1FAIpQLSfR1yaq2BaaV_qPLEqsejHNVFym3w4dupWzhq98Y-jjPt3F8w/viewform?usp=header"

# =====================================================
# Registration Section
# =====================================================

# 注入 CSS 样式来匹配图片中的按钮设计
st.markdown("""
<style>
    .registration-container {
        text-align: center;
        padding: 40px 0;
    }
    .registration-title {
        font-size: 28px;
        color: #333;
        margin-bottom: 25px;
        font-weight: 500;
    }
    .register-button {
        display: inline-block;
        padding: 15px 50px;
        background-color: #0b1f3a; 
        color: white !important;
        text-decoration: none !important;
        border-radius: 50px; /* 胶囊形状 */
        font-size: 20px;
        font-weight: bold;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .register-button:hover {
        background-color: #1a3a5f;
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
    }
    .register-button i {
        margin-right: 10px;
    }
</style>
""", unsafe_allow_html=True)

# 渲染注册标题和按钮
st.markdown(f"""
<div class="registration-container">
    <div class="registration-title"></div>
    <a href="{registration_url}" target="_blank" class="register-button">
        📋 Accommodation Form
    </a>
    <p style="margin-top: 20px; color: #666; font-size: 14px;">
        Click the button above to open the Google Form in a new tab.
    </p>
</div>
""", unsafe_allow_html=True)



st.markdown("---")

import streamlit as st

# ==========================================================
# 3️⃣ Must-Visit Destinations (11 Destinations Layout)
# ==========================================================

st.markdown("<h3 style='text-align:center; margin-top:50px;'>Things to see & do in Malaysia</h3>", unsafe_allow_html=True)
st.markdown("<div style='height:2px; background-color:#f0f2f6; margin:20px auto; width:80%;'></div>", unsafe_allow_html=True)

# 核心渲染函数：严格匹配图片格式，所有文字居中
def render_destination(img_path, title, description):
    # 1. 顶部文字部分（标题 + 简介）
    st.markdown(f"""
        <div style="text-align: center; margin-bottom: 10px;">
            <h4 style="color: #1f3b64; margin-bottom: 5px; font-size: 18px; font-weight: bold;">{title}</h4>
            <p style="color: #333; font-size: 14px; margin-bottom: 10px; line-height: 1.3;">{description}</p>
        </div>
    """, unsafe_allow_html=True)
    
    # 2. 中间图片部分 (确保图片本身在容器内居中)
    st.markdown('<div style="display: flex; justify-content: center;">', unsafe_allow_html=True)
    uniform_image(img_path, height="200px")
    st.markdown('</div>', unsafe_allow_html=True)
    


# --- 第一行：4个景点 ---
row1_cols = st.columns(4)
destdata_row1 = [
    ("assets/Dutch Square (Malacca).png", "Dutch Square (Malacca)", "Iconic red colonial square representing Dutch heritage."),
    ("assets/St. Paul's Hill (Malacca).png", "St. Paul's Hill (Malacca)", "Historic hilltop ruins with panoramic views.."),
    ("assets/A Famosa (Malacca).png", "A Famosa (Malacca)", "Portuguese fortress remains symbolizing colonial history."),
    ("assets/Jonker Street (Malacca).png", "Jonker Street (Malacca)", "Vibrant cultural street with markets and heritage shops.")
]

for i, col in enumerate(row1_cols):
    with col:
        render_destination(*destdata_row1[i])

# --- 第二行：4个景点 ---
row2_cols = st.columns(4)
destdata_row2 = [
    ("assets/Petronas Twin Towers (Kuala Lumpur).png", "Petronas Twin Towers (Kuala Lumpur)", "World-famous twin towers symbolizing Malaysia’s progress."),
    ("assets/KL Tower (Kuala Lumpur).png", "KL Tower (Kuala Lumpur)", "Observation tower offering panoramic city views."),
    ("assets/Central Market (Kuala Lumpur).png", "Central Market (Kuala Lumpur)", "A historic cultural hub where visitors can experience Malaysia’s diverse arts, crafts, and heritage in one vibrant, easily accessible location."),
    ("assets/Bukit Bintang (Kuala Lumpur).png", "Bukit Bintang (Kuala Lumpur)", "Lively shopping and entertainment district.")
]

for i, col in enumerate(row2_cols):
    with col:
        render_destination(*destdata_row2[i])

# --- 第三行：最后3个景点 (居中排列) ---
_, c1, c2, c3, _ = st.columns([0.1, 1, 1, 1, 0.1])
destdata_row3 = [
    ("assets/Batu Caves (Selangor).png", "Batu Caves (Selangor)", "Majestic limestone cave temple with colorful steps."),
    ("assets/Putra Mosque (Putrajaya).png", "Putra Mosque (Putrajaya)", "Beautiful pink mosque by the lake."),
    ("assets/Putra Perdana (Putrajaya).png", "Putra Perdana (Putrajaya)", "Prime Minister’s office with grand architecture.")
]

with c1: render_destination(*destdata_row3[0])
with c2: render_destination(*destdata_row3[1])
with c3: render_destination(*destdata_row3[2])


st.markdown("---")
st.write("© 2026 ACDC Organising Committee")