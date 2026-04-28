import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="Committee | ACCD 2026", layout="wide")

navbar()

# ===============================
# PAGE TITLE
# ===============================
st.markdown("## Committee")


import streamlit as st

# ==========================================================
# 核心功能：增强版自动定位脚本 (保持不变)
# ==========================================================
query_params = st.query_params
target_id = query_params.get("speaker", "") # 这里统一用 speaker 作为参数名，或者你也可以改为 'target'

if target_id:
    st.components.v1.html(
        f"""
        <script>
            setTimeout(function() {{
                var element = window.parent.document.getElementById('{target_id}');
                if (element) {{
                    element.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
                }}
            }}, 500);
        </script>
        """,
        height=0,
    )

# ==========================================================
# 3️⃣ Organising Institutions & Partners
# ==========================================================
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;'>Conference Organizers</h2>", unsafe_allow_html=True)

# 定义通用的左右结构渲染函数
def render_org_row(id_name, title, logo_path, description, is_expanded):
    st.markdown(f'<div id="{id_name}"></div>', unsafe_allow_html=True)
    with st.expander(title, expanded=is_expanded):
        col_logo, col_info = st.columns([1, 3])
        with col_logo:
            # 自动调用 assets 文件夹下的图片
            try:
                st.image(f"assets/{logo_path}", use_container_width=True)
            except:
                st.warning(f"Logo assets/{logo_path} not found")
        with col_info:
            st.markdown(description)

# 使用容器居中
with st.container():
    empty_l, main_col, empty_r = st.columns([1, 10, 1])
    
    with main_col:
        
        # ---------------- Main Organiser ----------------
        st.subheader("Main Organiser")
        
        render_org_row(
            "pptmc", 
            "Malaysia–China Higher Education Exchange Association (PPTMC)",
            "pptmc.png", 
            """
            The Malaysia–China Higher Education Exchange Association (PPTMC) was established to promote cooperation and exchanges between higher education institutions in Malaysia and China. Its main roles include supporting academic collaboration, student exchanges, and providing consultation related to higher education.
            
            PPTMC also organises seminars, conferences, and academic exchange activities. The Association is chaired by **Dato’ Low Kok Thai** and actively organises programmes each year, including the China-ASEAN Music Festival, academic conferences, and education tour programmes, to strengthen collaboration among Malaysia, China, and ASEAN institutions.
            """,
            (target_id == "pptmc")
        )

        # ---------------- Co-organisers ----------------
        st.subheader("Co-organisers")
        
        render_org_row(
            "ukm", 
            "Universiti Kebangsaan Malaysia (UKM) & UKM-IVI",
            "IVI.png", 
            """
            Universiti Kebangsaan Malaysia (UKM), established in 1970, is one of the top five national research universities in Malaysia and is officially designated as a Research University by the Malaysian government. The main campus is located 45 minutes from Kuala Lumpur International Airport, spanning 2,500 acres.

UKM has more than 30,000 students across undergraduate, Master’s, and PhD programmes. It is internationally recognised for multidisciplinary research in engineering, economics and management, medicine, information sciences, social sciences, and cultural studies. UKM maintains partnerships with over 200 universities worldwide and aims to serve as a leading academic hub connecting ASEAN to the world. Current ranking, QS World University Ranking: 126; QS Asia Ranking: 26; Southeast Asia: Top 4; Malaysia: Top 2.

UKM Institute of Visual Informatics (UKM IVI) is one of Malaysia’s most influential AI research projects and a postgraduate institute. The Institute of Visual Informatics is committed to being a leading Centre of Excellence in research and innovation across four thrust areas of visual informatics: Visual Computing, Computer Vision and Simulation, Real-Time Virtual Image Processing, and Social Informatics. The mission of IVI is to be a centre of excellence of choice in the field of Visual Informatics that is of global standing, by conducting frontier and cutting-edge research to lead new knowledge for a better quality of life. To achieve the vision and mission, the institute strives to provide facilities and a conducive environment for the development of human capital, including the postgraduate research skills via MSc and PhD degrees, as well as postdoctoral fellowships.
UKM IVI is industry-focused and globally oriented. It maintains strong corporate partnerships and collaborates closely with government agencies, government-linked companies, multinational corporations, and SMEs. IVI plays a central role in UKM’s AI research and intelligent business study, international research cooperation and is a key academic and organisational pillar of ACCD’26.
            """,
            (target_id == "ukm")
        )

        render_org_row(
            "hnu", 
            "Harbin Normal University (HNU)",
            "HNU.jpg", 
            """
            Founded in 1951, Harbin Normal University (HNU) is a key comprehensive university in Heilongjiang Province. It offers extensive programmes in arts, sciences, engineering, design, education, and management. HNU holds strong academic influence in Northeast China, particularly in Education, Arts & Design, Cultural Industries and Economics & Management.

HNU actively collaborates with Russia, Korea, Japan, and Belt & Road countries, strengthening academic exchange, talent development, and cultural cooperation.
            """,
            (target_id == "hnu")
        )

        # ---------------- 3. Co-partners ----------------
        st.subheader("Co-partners")

        # 3.1 HUC
        render_org_row(
            "huc", 
            "Harbin University of Commerce (HUC)", 
            "huc.png",
            """
            Harbin University of Commerce is located in Harbin City, Heilongjiang Province. It is a provincial key university with a focus on business management and applied economics, and featuring coordinated development across multiple disciplines. The university's history of education can be traced back to 1952, and it has a long and strong influence on the training of business and economics talents. The university has several colleges covering management, economics, food engineering, computer science, law and other disciplines. Among them, the food science and engineering major enjoys a good reputation in China and has provincial-level key laboratories and research platforms.

Harbin University of Commerce attaches great importance to practical teaching and cooperation with enterprises, and is committed to cultivating applied and multi-skilled talents. It is one of the distinctive business universities in Heilongjiang Province.

            """,
            (target_id == "huc")
        )

        # 3.2 MATRADE
        render_org_row(
            "matrade", 
            "Malaysia External Trade Development Corporation (MATRADE)", 
            "METDC.jpg",
            """
            3.2MATRADE is Malaysia’s government agency responsible for promoting international trade. It supports Malaysian enterprises with:
1.Market information  
2.Trade matching  
3.Overseas promotion  
4.Export training  

MATRADE maintains trade offices across China and plays a long-term role in strengthening Malaysia–China economic ties.
            """,
            (target_id == "matrade")
        )

        # 3.3 MyCEB
        render_org_row(
            "myceb", 
            "Malaysia Convention & Exhibition Bureau (MyCEB)", 
            "MCEB.png",
            """
            MyCEB was established in 2009 by Ministry of Tourism, Arts and Culture Malaysia to further strengthen Malaysia’s business tourism brand and position for the international business events market.



A Company Limited by Guarantee (CLBG), MyCEB serves as a central hub to assist meeting and event planners to bid and stage international business events in Malaysia and act as a conduit for national product development. MyCEB’s goal is to improve its rankings as an international meetings destination within International Congress and Convention Association (ICCA) and to grow business tourism arrivals to Malaysia.
In April 2021, MyCEB mapped out the way forward for Malaysia in business events with the launch of ‘Malaysia Business Events Strategic Marketing Plan 2021 - 2030’. MyCEB emphasizes on three strategic axes to expand performance namely optimisation, foresight and competitiveness. These strategic anchors are applied in implementing, planning, and monitoring all initiatives collaboratively with the industry.
            """,
            (target_id == "myceb")
        )

        # 3.4 SME Association
        render_org_row(
            "sme", 
            "SME Association of Malaysia", 
            "SME.jpg",
            """
            One of Malaysia’s most influential SME platforms with thousands of member companies across manufacturing, trade, education, technology, and services. The association actively supports SME internationalisation and frequently participates in business exchange activities with China.
            """,
            (target_id == "sme")
        )

        # 3.5 WRTO
        render_org_row(
            "wrto", 
            "World Research Travel Organization (WRTO)", 
            "WRTO.jpg",
            """
            World Research Travel Organization (WRTO) promotes cross-cultural learning, research-based travel, and sustainable development through the concept of “Travel as Learning.”

With a network of 300+ international experts, WRTO supports research travel standards development, international research travel base certification, international conferences and forums, consultancy for education, tourism, and government sectors, curriculum development, guide training, and cultural/nature exploration programmes
            """,
            (target_id == "wrto")
        )

        # 3.6Federation of Chinese Associations and Chambers of Commerce
        render_org_row(
            "asia-u", 
            "Federation of Chinese Associations and Chambers of Commerce", 
            "ACCCIM.png",
            """
            This federation unites numerous Chinese clan associations and business chambers across Malaysia. It is an influential platform supporting Malaysia–China business connectivity, investment facilitation, and business matchmaking.
            """,
            (target_id == "asia-u")
        )

        # 3.7Malaysia Fujian Chamber of Commerce
        render_org_row(
            "asia-u", 
            "Malaysia Fujian Chamber of Commerce", 
            "MFC.jpg",
            """
            A long-established and well-resourced chamber representing Fujian-origin enterprises in Malaysia. Its members are involved in sectors including manufacturing, construction, logistics, retail, and real estate. The chamber also serves as an important bridge for Chinese enterprises seeking to enter the Malaysian market.
            """,
            (target_id == "asia-u")
        )
        
        # 3.8Malaysian Malay Entrepreneurs Association (Tentative)
        render_org_row(
            "asia-u", 
            "Malaysian Malay Entrepreneurs Association (Tentative)", 
            "asia_u.png",
            """
            The association focuses on supporting Malay entrepreneurs and promoting entrepreneurship, business collaboration, and policy engagement. If participating in ACCD’26, it will offer Chinese enterprises valuable opportunities for direct engagement with Malay business owners.
            """,
            (target_id == "asia-u")
        )

        # 3.9 Asia University
        render_org_row(
            "asia-u", 
            "Asia University, Taiwan", 
            "AUT.jpg",
            """
            Asia University Taiwan is a private university located in Taichung known for its strong focus on innovation, digital technology, healthcare, and international collaboration. The university emphasizes interdisciplinary education, combining fields such as AI, design, management, and medical sciences to prepare students for future industries. With modern research facilities, global partnerships, and an active exchange network, Asia University promotes entrepreneurship, applied research, and cross-border academic cooperation, positioning itself as a forward-looking institution in Asia’s higher education landscape.
            """,
            (target_id == "asia-u")
        )

        # 3.10 University of Glasgow
        render_org_row(
            "glasgow", 
            "University of Glasgow, United Kingdom", 
            "UGUK.jpg",
            """
            The University of Glasgow is one of the United Kingdom’s oldest and most prestigious research universities, founded in 1451 and recognised globally for excellence in teaching, innovation, and scholarship. Located in Scotland, it is a member of the Russell Group and is known for its strengths in science, engineering, medicine, social sciences, and the humanities. The university maintains a strong international outlook, with extensive global partnerships, cutting-edge research centres, and a commitment to addressing real-world challenges through interdisciplinary collaboration and societal impact.
            """,
            (target_id == "glasgow")
        )

        # 3.11 SEARCH
        render_org_row(
            "search", 
            "Southeast Asia Research Centre for Humanities (SEARCH)", 
            "SEARCH.jpg",
            """
            SEARCH is an independent, forward-looking strategic intelligence platform dedicated to strengthening collaboration between government, industry, and academia. We operate with the core belief that sustainable regional growth can only be achieved through inclusive multilateral engagement and evidence-based strategic partnerships.
Rooted in Malaysia yet regionally connected, SEARCH serves as a bridge that fosters meaningful dialogue, knowledge exchange, and cooperative action among key stakeholders under the framework of the Regional Free Trade Network. By aligning public sector priorities, industry capabilities, and academic insights, we aim to co-create scalable, future-ready solutions for complex cross-border challenges in economic development, digital innovation, education, and sustainability.
            """,
            (target_id == "search")
        )

st.markdown("---")

# ==========================================================
# 1️⃣ Committee Table (No Subheading)
# ==========================================================
st.markdown("<h3 style='text-align:center;'>Chairs for Program</h3>", unsafe_allow_html=True)
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
<td style="padding:10px; border:1px solid #ddd;">Chairman</td>
<td style="border:1px solid #ddd;">Prof. Ir. Dr Riza Sulaiman</td>
<td style="border:1px solid #ddd;">
Director of the Institute of Visual Informatics, UKM
</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Co-Chairman</td>
<td style="border:1px solid #ddd;">Prof Ts. Dr. Helmi Ali</td>
<td style="border:1px solid #ddd;">
Professor at the Graduate School of Business, UKM
</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Co-Chairman</td>
<td style="border:1px solid #ddd;">Professor of Harbin Normal University</td>
<td style="border:1px solid #ddd;">
Professor of Harbin Normal University
</td>
</tr>
            
<tr>
<td style="padding:10px; border:1px solid #ddd;">Co-Chairman</td>
<td style="border:1px solid #ddd;">Dato’ Low Kok Thai</td>
<td style="border:1px solid #ddd;">
President of Malaysia–China Higher Education Exchange Association (PPTMC)
</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Co-Chairman</td>
<td style="border:1px solid #ddd;"> Mr. Ian Neo Chee Hua</td>
<td style="border:1px solid #ddd;">
Chief Executive Officer of Southeast Asia Research Centre for Humanities (SEARCH)
</td>
</tr>

</table>

</div>
""", unsafe_allow_html=True)

st.markdown("---")


import streamlit as st

# ==========================================================
# 核心功能：自动定位脚本 (解决跳转后不自动下拉的问题)
# ==========================================================
query_params = st.query_params
target_speaker = query_params.get("speaker", "")

if target_speaker:
    # 这段 JS 脚本会在页面加载后寻找对应的 ID 并将其滚动到视口顶部
    st.components.v1.html(
        f"""
        <script>
            window.parent.document.getElementById('{target_speaker}').scrollIntoView({{
                behavior: 'smooth',
                block: 'start'
            }});
        </script>
        """,
        height=0,
    )

st.markdown("---")

import streamlit as st

# ==========================================================
# 2️⃣ Chairs for Program
# ==========================================================

st.markdown("<h3 style='text-align:center;'>Key Speakers</h3>", unsafe_allow_html=True)

# 【核心逻辑】获取当前 URL 中的参数
# 注意：新版 Streamlit 使用 st.query_params
query_params = st.query_params
target_speaker = query_params.get("speaker", "")

# 使用容器来控制整体宽度
with st.container():
    empty_l, main_col, empty_r = st.columns([1, 10, 1])
    
    with main_col:
        
       
        # ========== 第 2 位成员：Professor Ir. Dr. Riza Sulaiman ==========
        st.markdown(f'<div id="riza-sulaiman"></div>', unsafe_allow_html=True)
        # 假设 target_speaker 逻辑一致，此处设为 riza-sulaiman
        with st.expander("2. Prof. Ir. Dr. Riza Sulaiman, Universiti Kebangsaan Malaysia", expanded=(target_speaker == "riza-sulaiman")):
            col_side2, col_main2 = st.columns([1, 2.5])
               
            with col_side2:
                # 此处图片路径请根据实际情况微调（例如 speaker1.jpg 或相应资源）
                st.image("assets/speaker4.jpg", use_container_width=True)
                st.markdown("""
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #0b1f3a;">
                    <p style="margin-bottom: 5px;"><strong>Expertise:</strong> Visual Informatics</p>
                    <p style="margin-bottom: 5px;"><strong>Domain:</strong> AI & Digital Tech</p>
                </div>
                 """, unsafe_allow_html=True)
                st.caption("Professional Engineer (Ir.)")

            with col_main2:
                st.markdown("### PROF. Ir. DR. RIZA SULAIMAN")
                st.markdown("##### *Director, Institute of Visual Informatics (IVI),Universiti Kebangsaan Malaysia (UKM)*")
                st.markdown("---")
                
                st.markdown("""
                Professor Ir. Dr. Riza Sulaiman is the Director of IVI UKM and a Professional Engineer with expertise in visual informatics, artificial intelligence, and digital technologies. He has led impactful research, industry collaborations, and innovation initiatives. 
                
                As Chair of ACCD’26, he brings strong leadership in advancing ASEAN–China cooperation and promoting technology-driven regional development.
                """)


        # ========== 第 3 位成员 ==========
        st.markdown('<div id="ming-lang"></div>', unsafe_allow_html=True)
        with st.expander("3. Prof. Dr. Ming Lang Tseng, Asia University, Taiwan", expanded=(target_speaker == "ming-lang")):
            col_side3, col_main3 = st.columns([1, 2.5])
            with col_side3:
                st.image("assets/speaker1.jpg", use_container_width=True)
                st.markdown("""
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #0b1f3a;">
                    <p style="margin-bottom: 5px;"><strong>Location:</strong> Taiwan</p>
                    <p style="margin-bottom: 5px;"><strong>Citations:</strong> 32,000+</p>
                    <p style="margin-bottom: 5px;"><strong>Publications:</strong> 500+</p>
                </div>
                """, unsafe_allow_html=True)
                st.caption("Stanford University’s Top 2% Scientists Worldwide")

            with col_main3:
                st.markdown("### Prof. Ming-Lang Tseng")
                st.markdown("##### *Chair Professor & Director, Institute of Innovation and Circular Economy*")
                st.markdown("Asia University, Taiwan")
                st.markdown("---")
                st.markdown("""
                Prof. Ming-Lang Tseng is an internationally acclaimed scholar and thought leader in sustainable supply chain management, circular economy, digital transformation, and innovation-driven industrial development. He currently serves as Chair Professor and Director of the Institute of Innovation and Circular Economy at Asia University, Taiwan, and has held distinguished academic appointments across Malaysia, China, the Philippines, and the United Kingdom. 
                
                With over 500 international publications and more than 32,000 citations, Prof. Tseng is widely recognized for his pioneering work in green supply chains, Industry 4.0, AI-enabled decision systems, sustainable production, and circular business strategies. His research continues to shape policy, industrial innovation, and cross-border sustainability initiatives across Asia and beyond. 

                A globally respected academic leader, he has been consistently recognized among Stanford University’s Top 2% Scientists Worldwide and is ranked among Taiwan’s leading researchers in business management and engineering. He also serves as Editor-in-Chief of the Journal of Industrial and Production Engineering and holds editorial leadership roles in several top-tier international journals. 

                At ACCD’26, Prof. Tseng will bring strategic insights into how ASEAN–China collaboration can accelerate sustainable regional development through circular economy practices, smart industries, digital supply chains, and academia–industry partnerships, directly supporting the Forum’s mission of strengthening innovation ecosystems and regional cooperation.
                """)


        # ========== 第 4 位成员 ==========
        st.markdown('<div id="ming-lim"></div>', unsafe_allow_html=True)
        with st.expander("4. Prof. Dr. Ming K. Lim, University of Glasgow, United Kingdom", expanded=(target_speaker == "ming-lim")):
            col_side4, col_main4 = st.columns([1, 2.5])
            with col_side4:
                st.image("assets/speaker2.jpg", use_container_width=True)
                st.markdown("""
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #0b1f3a;">
                    <p style="margin-bottom: 5px;"><strong>Location:</strong> United Kingdom</p>
                    <p style="margin-bottom: 5px;"><strong>Citations:</strong> 24,000+</p>
                    <p style="margin-bottom: 5px;"><strong>Publications:</strong> 400+</p>
                </div>
                """, unsafe_allow_html=True)
            
            with col_main4:
                st.markdown("### Prof. Dr. Ming Lim")
                st.markdown("##### *Professor of Supply Chain Management and Digitalisation*")
                st.markdown("Adam Smith Business School, University of Glasgow, United Kingdom")
                st.markdown("---")
        
                # 使用三引号包裹多段落内容，确保换行显示正常
                st.markdown(f"""
                Professor Dr. Ming Lim is an internationally distinguished scholar in supply chain management, digitalisation, Industry 4.0, and sustainable logistics systems. He currently serves as Professor of Supply Chain Management and Digitalisation at the Adam Smith Business School, University of Glasgow, and is also a Visiting Professor at the UKM Graduate School of Business, strengthening academic collaboration across the ASEAN region. 

                With more than 400 scholarly publications and nearly 24,000 citations, Prof. Lim is globally recognized for his pioneering work in smart logistics, Internet of Things (IoT), blockchain, AI-driven supply chain analytics, low-carbon logistics, and circular supply chain management. His interdisciplinary research integrates engineering, computer science, information systems, and operations management to address real-world industrial and sustainability challenges. 

                A respected academic leader and industry collaborator, Prof. Lim has led major international research and consultancy projects involving DHL, Rolls-Royce, Toyota, Unilever, NHS, Caterpillar, and multiple SMEs, driving innovation in resilient and technology-enabled supply chains. He also serves as Editor-in-Chief of the International Journal of Logistics Research and Applications, further contributing to the advancement of global knowledge in logistics and supply chain resilience. 

                At **ACCD’26**, Prof. Lim will share strategic perspectives on how ASEAN–China cooperation can accelerate regional competitiveness through digital supply chains, green logistics, Industry 4.0 ecosystems, and academia–industry innovation partnerships, directly supporting the Forum’s vision for sustainable regional growth and economic transformation.
                """)


        # ========== 第 6 位成员：Jamaluddin Ibrahim ==========
        st.markdown('<div id="jamaluddin-ibrahim"></div>', unsafe_allow_html=True)
        with st.expander("6. Jamaluddin Ibrahim, Makiplago Holding Sdn Bhd", expanded=(target_speaker == "jamaluddin-ibrahim")):
            col_side6, col_main6 = st.columns([1, 2.5])
            
            with col_side6:
                # 请确保图片路径与实际相符，例如 "assets/speaker6.jpg"
                st.image("assets/speaker6.jpg", use_container_width=True)
                st.markdown("""
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #0b1f3a;">
                    <p style="margin-bottom: 5px;"><strong>Domain:</strong> E-commerce & Trade</p>
                    <p style="margin-bottom: 5px;"><strong>Expertise:</strong> Halal Ecosystem & Media</p>
                </div>
                """, unsafe_allow_html=True)
                st.caption("Alumnus of Hunan University")

            with col_main6:
                st.markdown("### JAMALUDDIN IBRAHIM")
                st.markdown("##### *Founder & CEO,Makiplago Holding Sdn Bhd*")
                st.markdown("---")
                
                st.markdown("""
                Jamaluddin Ibrahim is a dynamic entrepreneur and media figure with over 40 years of cross-industry experience spanning engineering, international trade, digital platforms, and media. As Founder & CEO of Makiplago Holding Sdn Bhd and Makiplago (Shenzhen) Technology Co., Ltd, he drives innovation in cross-border e-commerce and digital ecosystems, strengthening trade connectivity between ASEAN and China.
                
                An honours graduate in Mechanical Engineering from Hunan University, China, he has held leadership roles across manufacturing, trade, and corporate management, including serving as Managing Director of Paradise Group Sdn Bhd. He is actively engaged in advancing the halal industry ecosystem through policy advocacy, promoting regulatory harmonisation, cross-border standards, and sustainable supply chain frameworks to enhance trade and investment opportunities within the global halal economy.
                
                A respected commentator and former Radio 988 personality, Jamaluddin is known for his sharp insights on socio-economic trends, regional development, and industry transformation.
                
                He brings a compelling perspective on digital economy growth, sustainable development, halal policy frameworks, and ASEAN–China cooperation in an increasingly interconnected global landscape.
                """)


        # ========== 第 5 位成员：Tan Sri Dato’ Sri Dr. Ng Yen Yen J.P. ==========
        st.markdown(f'<div id="ng-yen-yen"></div>', unsafe_allow_html=True)
        with st.expander("5. Tan Sri Dato’ Sri Dr. Ng Yen Yen J.P., Former Minister, Malaysia", expanded=(target_speaker == "ng-yen-yen")):
            col_side5, col_main5 = st.columns([1, 2.5])
            
            with col_side5:
                st.image("assets/speaker5.jpg", use_container_width=True)
                st.markdown("""
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #0b1f3a;">
                   <p style="margin-bottom: 5px;"><strong>Domain:</strong> Public Service</p>
                   <p style="margin-bottom: 5px;"><strong>Expertise:</strong> Tourism & Finance</p>
                </div>
                 """, unsafe_allow_html=True)
                st.caption("Former Cabinet Minister of Malaysia")

            with col_main5:
                st.markdown("### TAN SRI DATO’ SRI DR. NG YEN YEN J.P.")
                st.markdown("##### *Former Minister, Ministry of Tourism, Arts & Culture Malaysia*")
                st.markdown("##### *Former Minister, Ministry of Women, Family and Community Development*")
                st.markdown("---")
                
                st.markdown("""
                Tan Sri Dato’ Sri Dr. Ng Yen Yen J.P. is a distinguished public figure and leader in Malaysia, having held multiple prominent ministerial portfolios and continuing to serve in various advisory and honorary roles. 
                
                **Key Ministerial Roles:**
                - Former Minister, Ministry of Tourism, Arts & Culture Malaysia
                - Former Minister, Ministry of Women, Family and Community Development Malaysia
                - Former Deputy Minister, Ministry of Finance Malaysia
                
                **Advisory & Honorary Positions:**
                - Advisor, Hong Kong Maritime Silk Road Association 
                - Honorary President, World Research Tourism Organization (WRTO)
                - Trustee, Yayasan Tuanku Fauziah
                - Patron, Yayasan Wanita Cemerlang
                
                **Political Leadership:**
                - Former Vice President, Malaysian Chinese Association (MCA)
                - Honorary Life Chairman of Malaysian Chinese Association Women Wing (Wanita MCA)
                """)

                

        # ========== 第 1 位成员：PROF. Ts. DR. MOHD HELMI ALI (更新) ==========
        st.markdown(f'<div id="helmi-ali"></div>', unsafe_allow_html=True)
        with st.expander("1. Prof. Ts. Dr. Mohd Helmi Ali, Universiti Kebangsaan Malaysia", expanded=(target_speaker == "helmi-ali")):
            col_side, col_main = st.columns([1, 2.5])
            
            with col_side:
                st.image("assets/speaker3.jpg", use_container_width=True)
                st.markdown("""
                <div style="background-color: #f8f9fa; padding: 15px; border-radius: 10px; border-left: 4px solid #0b1f3a;">
                    <p style="margin-bottom: 5px;"><strong>Expertise:</strong> Supply Chain</p>
                    <p style="margin-bottom: 5px;"><strong>Industry:</strong> Food, O&G, Maritime</p>
                </div>
                """, unsafe_allow_html=True)
                st.caption("Chartered Member of CILT Malaysia")

            with col_main:
                st.markdown("### PROF. Ts. DR. MOHD HELMI ALI")
                st.markdown("##### *Professor in Supply Chain Management*")
                st.markdown("---")
                
                st.markdown("""
                Mohd Helmi Ali is an Professor at the UKM-Graduate School of Business, Universiti Kebangsaan Malaysia. He has experiences in multiple industries such as food, oil and gas, maritime, transportation, and construction. Despite of his recent involvement in academics, he has worked with many research fields, in particular on food integrity and supply chain, halal-hub. His research interest focus on food integrity, halal food supply chain, sustainable development, operation management and innovation. He also is a chartered member The Chartered Institute of Logistics & Transport Malaysia.
                """)






# ==========================================================
# 核心功能：增强版自动定位脚本 (放在页面底部或逻辑后方)
# ==========================================================
if target_speaker:
    # 使用 setTimeout 确保 DOM 已经完全加载且动画已启动
    st.components.v1.html(
        f"""
        <script>
            setTimeout(function() {{
                var element = window.parent.document.getElementById('{target_speaker}');
                if (element) {{
                    element.scrollIntoView({{
                        behavior: 'smooth',
                        block: 'start'
                    }});
                }}
            }}, 500); // 延迟 500ms 确保页面底部的成员 4 也能被找到
        </script>
        """,
        height=0,
    )

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
<td style="border:1px solid #ddd; padding:10px;">Professor of UKM GSB</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Co-Chairman</td>
<td style="border:1px solid #ddd; padding:10px;">Rep. of Harbin Normal University</td>
<td style="border:1px solid #ddd; padding:10px;">Rep. HNU</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Co-Chairman</td>
<td style="border:1px solid #ddd; padding:10px;">Dato Low Kok Thai</td>
<td style="border:1px solid #ddd; padding:10px;">Chairman of PPTMC</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Vice-Chairman 1</td>
<td style="border:1px solid #ddd; padding:10px;">Rep. of Harbin University of Commerce</td>
<td style="border:1px solid #ddd; padding:10px;">Rep. HUC</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Vice-Chairman 2</td>
<td style="border:1px solid #ddd; padding:10px;">Dr Edmund Koh</td>
<td style="border:1px solid #ddd; padding:10px;">Deputy President of PPTMC</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Secretary 1</td>
<td style="border:1px solid #ddd; padding:10px;">Ms. Najiha</td>
<td style="border:1px solid #ddd; padding:10px;">Secretary of PPTMC</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Secretary 2</td>
<td style="border:1px solid #ddd; padding:10px;">Representative of HNU</td>
<td style="border:1px solid #ddd; padding:10px;">Representative of HNU</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Treasurer</td>
<td style="border:1px solid #ddd; padding:10px;">Datin Kuong Ivy</td>
<td style="border:1px solid #ddd; padding:10px;">Treasurer of PPTMC</td>
</tr>

<tr>
<td style="padding:10px; border:1px solid #ddd;">Group Leaders and Committee Members</td>
<td colspan="2" style="border:1px solid #ddd; padding:10px;">
Ms. Chen Chu Chu (Vice Chairman of PPTMC) </br>
Ms. Melissa Ma Zhou Qun (Vice Chairman of PPTMC) </br>
Dr. Diana Liang Xin Rui (Secretary of PPTMC) </br>
Dr. Zoul Liu Zong Yi (Secretary of PPTMC) </br>
Ivvy Teh (Committee of PPTMC) </br>
Representative of UKM IVI</br>
Representative of UPM</br>
Representative of PPTMC</br>
Representative of HNU</br>
Representative of HNU</br>
Representative of HUC</br>
Representative of UPM
</td>
</tr>

</table>

</div>
""", unsafe_allow_html=True)



st.markdown("---")
st.write("© 2026 ACDC Organising Committee")