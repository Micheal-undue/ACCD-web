import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="Venue & Accommodation | ACDC 2026", layout="wide")

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
    300 persons (180 from ASEAN; 120 from China)<br><br>

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



# =========================
# 工具函数：统一图片视觉高度 (透明背景版)
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
        
        # 移除了 background-color 和 border-radius，使容器与网页融为一体
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
# 🏨 Featured Hotels | 精选酒店 (完整美化版)
# ==========================================================
st.markdown("<h3 style='text-align:center; margin-top:50px;'>Featured Hotels | 精选酒店</h3>", unsafe_allow_html=True)

# 辅助函数：专门用于居中标题和简介
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
st.markdown("<h4 style='text-align:center; margin-top:30px;'>TENERA HOTEL & SUITES BANGI (AS OF APRIL 2026) (4-STAR RATING)</h4>", unsafe_allow_html=True)
col1, col2 = st.columns([1, 1])

with col1:
    centered_hotel_info("STANDARD KING ", "RM 300 PER NIGHT WITH BREAKFAST (TAX NOT INCLUDED)")
    uniform_image("assets/hotel1_single.png", height="280px")

with col2:
    centered_hotel_info("SUPERIOR TWIN", " RM 300 PER NIGHT WITH BREAKFAST (TAX NOT INCLUDED)")
    uniform_image("assets/hotel1_double.png", height="280px")

st.markdown("---")


# =========================
# Hotel 2
# =========================
st.markdown("<h4 style='text-align:center;'>BANGI GOLF RESORT (AS OF APRIL 2026) (5-STAR RATE)</h4>", unsafe_allow_html=True)

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

st.markdown("---")


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


# ==========================================================
# 3️⃣ Must-Visit Destinations | 必去景点 (网格大图版)
# ==========================================================
# 假设图片存放在 assets 文件夹下
DEST_1_B64 = get_base64_image("assets/dest_klcc.jpg")
DEST_2_B64 = get_base64_image("assets/dest_aquaria.jpg")
DEST_3_B64 = get_base64_image("assets/dest_twin_towers.jpg")
DEST_4_B64 = get_base64_image("assets/dest_putrajaya.jpg")
DEST_5_B64 = get_base64_image("assets/dest_batu_caves.jpg")
DEST_6_B64 = get_base64_image("assets/dest_central_market.jpg")
DEST_7_B64 = get_base64_image("assets/dest_genting.jpg")


st.markdown("<h3 style='text-align:center; margin-top:50px;'>Must-Visit Destinations</h3>", unsafe_allow_html=True)
st.markdown("<div class='divider'></div>", unsafe_allow_html=True) # 如果你全局样式里有divider

# 第一行：4个景点
col1, col2, col3, col4 = st.columns(4)

with col1:
    uniform_image("assets/dest_klcc.jpg", height="180px")
    st.markdown("<p style='text-align:center; font-weight:500;'>KL Convention Centre</p>", unsafe_allow_html=True)

with col2:
    uniform_image("assets/dest_aquaria.jpg", height="180px")
    st.markdown("<p style='text-align:center; font-weight:500;'>Aquaria, KLCC</p>", unsafe_allow_html=True)

with col3:
    uniform_image("assets/dest_twin_towers.jpg", height="180px")
    st.markdown("<p style='text-align:center; font-weight:500;'>Petronas Twin Towers</p>", unsafe_allow_html=True)

with col4:
    uniform_image("assets/dest_putrajaya.jpg", height="180px")
    st.markdown("<p style='text-align:center; font-weight:500;'>Putrajaya Lake</p>", unsafe_allow_html=True)

# 第二行：3个景点 (居中排列)
# 我们使用 5 个列，中间 3 个放内容，左右留空实现居中感
_, b1, b2, b3, _ = st.columns([0.5, 1, 1, 1, 0.5])

with b1:
    uniform_image("assets/dest_batu_caves.jpg", height="180px")
    st.markdown("<p style='text-align:center; font-weight:500;'>Batu Caves</p>", unsafe_allow_html=True)

with b2:
    uniform_image("assets/dest_central_market.jpg", height="180px")
    st.markdown("<p style='text-align:center; font-weight:500;'>Central Market, KL</p>", unsafe_allow_html=True)

with b3:
    uniform_image("assets/dest_genting.jpg", height="180px")
    st.markdown("<p style='text-align:center; font-weight:500;'>Genting Highlands</p>", unsafe_allow_html=True)



st.markdown("---")
st.write("© 2026 ACDC Organising Committee")