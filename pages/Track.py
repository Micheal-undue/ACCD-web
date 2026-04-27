import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="Themes | ACCD 2026", layout="wide")

navbar()



import streamlit as st
import base64

def get_image_base64(path):
    """将本地图片转为base64，以便嵌入HTML"""
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except:
        return ""

def show_tracks():
    st.title("Conference Themes")
    st.markdown("---")

    # 自定义 CSS
    st.markdown("""
        <style>
        .track-card {
            background-color: #ffffff;
            border-left: 6px solid #1E3A8A; 
            border-radius: 12px;
            padding: 25px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.08);
            display: flex; 
            align-items: center; /* 垂直居中 */
            justify-content: space-between;
            min-height: 220px;
        }
        .text-container {
            flex: 3; /* 文字占 3 份宽度 */
            padding-right: 20px;
        }
        .img-container {
            flex: 1; /* 图片占 1 份宽度 */
            text-align: center;
        }
        .track-title {
            color: #1E3A8A;
            font-family: 'Arial', sans-serif;
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 12px;
            line-height: 1.2;
        }
        .track-desc {
            color: #334155;
            font-size: 16px;
            line-height: 1.6;
            text-align: justify;
        }
        .track-img {
            max-width: 100px;
            height: auto;
            border-radius: 8px;
            opacity: 0.9;
        }
        </style>
    """, unsafe_allow_html=True)

    tracks = [
        {
            "title": "Digital Economy & Technology",
            "desc": "Exploring how digital transformation, artificial intelligence, and emerging technologies are reshaping industries, governance, and everyday life—driving smarter, more connected economies across ASEAN and China.",
            "img": "assets/theme1.png"
        },
        {
            "title": "Trade & Investment",
            "desc": "Fostering cross-border collaboration by enhancing trade partnerships, investment opportunities, and economic integration to support sustainable regional growth and global competitiveness.",
            "img": "assets/theme2.png"
        },
        {
            "title": "Sustainable Development Goals & Sustainable Lifestyle",
            "desc": "Promoting inclusive growth and responsible living by aligning regional initiatives with the United Nations Sustainable Development Goals, focusing on social well-being, environmental protection, and long-term resilience.",
            "img": "assets/theme3.png"
        },
        {
            "title": "Entrepreneurship & Innovation",
            "desc": "Empowering startups, innovators, and industry leaders to drive economic progress through creative solutions, disruptive technologies, and collaborative ecosystems.",
            "img": "assets/theme4.png"
        },
        {
            "title": "Green Economy",
            "desc": "Advancing environmentally sustainable economic models that prioritize low-carbon growth, resource efficiency, and climate resilience for a greener future.",
            "img": "assets/theme5.png"
        },
        {
            "title": "Cultural & Tourism Exchange",
            "desc": "Strengthening mutual understanding and regional harmony by celebrating cultural diversity, heritage, and tourism collaboration between ASEAN and China.",
            "img": "assets/theme6.png"
        }
    ]

    # 每行一个大卡片，文字在左图片在右（这种布局最不容易显得“奇怪”）
    for track in tracks:
        # 转换图片
        img_base64 = get_image_base64(track["img"])
        img_html = f'<img src="data:image/png;base64,{img_base64}" class="track-img">' if img_base64 else ""
        
        # 渲染纯 HTML 卡片
        st.markdown(f"""
            <div class="track-card">
                <div class="text-container">
                    <div class="track-title">{track['title']}</div>
                    <div class="track-desc">{track['desc']}</div>
                </div>
                <div class="img-container">
                    {img_html}
                </div>
            </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    show_tracks()


st.markdown("---")
st.write("© 2026 ACDC Organising Committee")
