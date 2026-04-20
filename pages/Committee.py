import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="Committee | ACCD 2026", layout="wide")

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

# 使用容器
with st.container():
    empty_l, main_col, empty_r = st.columns([1, 10, 1])
    
    with main_col:
        # 1. 第一位成员 
        with st.expander("1. Prof. Ts. Dr. Mohd Helmi Ali"):
            st.write("Detailed information to be updated...")

        # 2. 第二位成员 
        with st.expander("2. Distinguished Professor from Harbin University of Commerce"):
            st.info("Pending Confirmation.")

        # 3. 第三位成员 
        with st.expander("3. Prof. Dr. Ming Lang Tseng, Asia University, Taiwan"):
            # 在 Expander 内部再次分栏
            # 左侧 col_side 放置头像和核心信息，右侧 col_main 放置长简历
            col_side, col_main = st.columns([1, 2.5])
            
            with col_side:
                st.image("assets/speaker1.jpg", use_container_width=True)
                
                st.markdown("""
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #0b1f3a;">
                    <p style="margin-bottom: 5px;"><strong>Location:</strong> Taiwan</p>
                    <p style="margin-bottom: 5px;"><strong>Citations:</strong> 32,000+</p>
                    <p style="margin-bottom: 5px;"><strong>Publications:</strong> 500+</p>
                </div>
                """, unsafe_allow_html=True)
                
                st.caption("Stanford University’s Top 2% Scientists Worldwide")

            with col_main:
                st.markdown("### Prof. Ming-Lang Tseng")
                st.markdown("##### *Chair Professor & Director, Institute of Innovation and Circular Economy*")
                st.markdown("---")
                
                # 长文本
                st.markdown("""
                Prof. Ming-Lang Tseng is an internationally acclaimed scholar and thought leader in sustainable supply chain management, circular economy, digital transformation, and innovation-driven industrial development. He currently serves as Chair Professor and Director of the Institute of Innovation and Circular Economy at Asia University, Taiwan, and has held distinguished academic appointments across Malaysia, China, the Philippines, and the United Kingdom. 

                With over **500 international publications** and more than **32,000 citations**, Prof. Tseng is widely recognized for his pioneering work in green supply chains, Industry 4.0, AI-enabled decision systems, sustainable production, and circular business strategies. His research continues to shape policy, industrial innovation, and cross-border sustainability initiatives across Asia and beyond. 

                A globally respected academic leader, he has been consistently recognized among **Stanford University’s Top 2% Scientists Worldwide** and is ranked among Taiwan’s leading researchers in business management and engineering. He also serves as **Editor-in-Chief** of the *Journal of Industrial and Production Engineering* and holds editorial leadership roles in several top-tier international journals. 

                At **ACCD’26**, Prof. Tseng will bring strategic insights into how ASEAN–China collaboration can accelerate sustainable regional development through circular economy practices, smart industries, digital supply chains, and academia–industry partnerships, directly supporting the Forum’s mission of strengthening innovation ecosystems and regional cooperation.
                """)

        # 4. 第四位成员 
        with st.expander("4. Prof. Dr. Ming K. Lim, University of Glasgow, United Kingdom"):
            col_side2, col_main2 = st.columns([1, 2.5])
            with col_side2:
                
                st.image("assets/speaker2.jpg", use_container_width=True)
                st.markdown("""
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #0b1f3a;">
                    <p><strong>Location:</strong> Adam Smith Business School, University of Glasgow, United Kingdom</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_main2:
                st.markdown("### Professor Dr. Ming Lim")
                st.markdown("##### *Professor of Supply Chain Management and Digitalisation*")
                st.markdown("---")
                st.markdown("""
                Professor Dr. Ming Lim is an internationally distinguished scholar in supply chain management, digitalisation, Industry 4.0, and sustainable logistics systems. He currently serves as Professor of Supply Chain Management and Digitalisation at the Adam Smith Business School, University of Glasgow, and is also a Visiting Professor at the UKM Graduate School of Business, strengthening academic collaboration across the ASEAN region.  

                With more than 400 scholarly publications and nearly 24,000 citations, Prof. Lim is globally recognized for his pioneering work in smart logistics, Internet of Things (IoT), blockchain, AI-driven supply chain analytics, low-carbon logistics, and circular supply chain management. His interdisciplinary research integrates engineering, computer science, information systems, and operations management to address real-world industrial and sustainability challenges.  

                A respected academic leader and industry collaborator, Prof. Lim has led major international research and consultancy projects involving DHL, Rolls-Royce, Toyota, Unilever, NHS, Caterpillar, and multiple SMEs, driving innovation in resilient and technology-enabled supply chains. He also serves as Editor-in-Chief of the International Journal of Logistics Research and Applications, further contributing to the advancement of global knowledge in logistics and supply chain resilience. 

                At ACCD’26, Prof. Lim will share strategic perspectives on how ASEAN–China cooperation can accelerate regional competitiveness through digital supply chains, green logistics, Industry 4.0 ecosystems, and academia–industry innovation partnerships, directly supporting the Forum’s vision for sustainable regional growth and economic transformation.
                """)

st.markdown("---")


# ==========================================================
# 3️⃣ Members of the organizing committee
# ==========================================================

st.markdown("<h3 style='text-align:center;'>Members of the organizing committee</h3>", unsafe_allow_html=True)

st.markdown("""
<div style="display:flex; justify-content:center; margin-bottom: 50px;">

<table style="border-collapse: collapse; width:85%; text-align:left;">
<tr style="background-color:#0b1f3a; color:white;">
<th style="padding:10px; border:1px solid #ddd; width:20%;">Roles</th>
<th style="padding:10px; border:1px solid #ddd; width:35%;">Name</th>
<th style="padding:10px; border:1px solid #ddd; width:45%;">Position / Affiliation</th>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Advisor</td>
<td style="border:1px solid #ddd; padding:10px;">Tan Sri. Dr Ng Yen Yen</td>
<td style="border:1px solid #ddd; padding:10px;">Honorary President of the World Research Travel Association (WRTO)<br>Former Minister of Tourism and Culture</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Chairman</td>
<td style="border:1px solid #ddd; padding:10px;">Prof. Dr Riza Sulaiman</td>
<td style="border:1px solid #ddd; padding:10px;">UKM IVI, IVI</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Co-Chairman</td>
<td style="border:1px solid #ddd; padding:10px;">Prof. Ts. Dr Mohd Helmi Ali</td>
<td style="border:1px solid #ddd; padding:10px;">UKM GSB, former Deputy Dean</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Co-Chairman</td>
<td style="border:1px solid #ddd; padding:10px;">Representative of Harbin University of Commerce</td>
<td style="border:1px solid #ddd; padding:10px;">Representative of Harbin University of Commerce</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Co-Chairman</td>
<td style="border:1px solid #ddd; padding:10px;">Dato Low Kok Thai</td>
<td style="border:1px solid #ddd; padding:10px;">Chairman of PPTMC</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Vice-Chairman 1</td>
<td style="border:1px solid #ddd; padding:10px;">Representative of Harbin University of Commerce</td>
<td style="border:1px solid #ddd; padding:10px;">Representative of Harbin University of Commerce</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Vice-Chairman 2</td>
<td style="border:1px solid #ddd; padding:10px;">Dr Edmund Koh</td>
<td style="border:1px solid #ddd; padding:10px;">Deputy President of PPTMC</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Event Coordinator</td>
<td style="border:1px solid #ddd; padding:10px;">Ms. Najiha</td>
<td style="border:1px solid #ddd; padding:10px;">Secretary of PPTMC</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Secretary 1</td>
<td style="border:1px solid #ddd; padding:10px;">Representative of UKM IVI</td>
<td style="border:1px solid #ddd; padding:10px;">Representative of UKM IVI</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Secretary 2</td>
<td style="border:1px solid #ddd; padding:10px;">Representative of Harbin University of Commerce</td>
<td style="border:1px solid #ddd; padding:10px;">Representative of Harbin University of Commerce</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Finance 1</td>
<td style="border:1px solid #ddd; padding:10px;">Datin Kuong Ivy</td>
<td style="border:1px solid #ddd; padding:10px;">Treasurer of PPTMC</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Group Leaders and Committee Members</td>
<td colspan="2" style="border:1px solid #ddd; padding:10px;">
• Ms. Chen Chu Chu (Vice Chairman of PPTMC)<br>
• Ms. Melissa Ma Zhou Qun (Vice Chairman of PPTMC)<br>
• Dr. Diana Liang Xin Rui (Secretary of PPTMC)<br>
• Ivy Teh (Committee of PPTMC)<br>
• Representative of UKM IVI<br>
• Representative of UPM<br>
• Representative of PPTMC<br>
• Representative of HUC<br>
• Representative of HNU
</td>
</tr>

</table>

</div>
""", unsafe_allow_html=True)



st.markdown("---")
st.write("© 2026 ACDC Organising Committee")