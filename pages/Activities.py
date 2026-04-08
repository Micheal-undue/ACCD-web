import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="Key Activities | ACDC 2026", layout="wide")

navbar()

# ===== PAGE CONTENT =====
st.markdown("## Key Activities")
st.markdown("---")

col1, col2 = st.columns(2)

# ===== LEFT COLUMN =====
with col1:
    with st.expander("Day 1", expanded=True):
        st.markdown("""
**Morning**  
-Co-Chair. Prof Helmi Ali:  
-Co-Chair. HUC: to address the theme of ACCD’26 (from UKM and HUC)  
-SME President Dr Chin Chee:  
-Keynote speakers from Harbin SME:  
                    About the SME Association, members and cooperations  
-Round Table with 4 keynote speakers, Moderator: Prof Helmi Ali  
  
**Afternoon**  
-Room 1: Professors / Doctoral Students Presentations  
A dedicated session to support and mentor doctoral students, guiding research and academic development.  

-Room 2: Paper presentation:   
Multiple concurrent sessions to cover a variety of topics, allowing participants to select areas of interest.  

-Exhibition: Participants visiting the exhibition booths to get information and meet each other.  
  
**Exhibition with** 40 booths  
**Estimated Attendance:** 800-1000   
                    
**上午**  
-联合主席：赫尔米教授  
-联合主席。哈师大：ACCD'26主题探讨和研究报告（来自UKM 和 HUC ）  
-中小企业会长陈祺雄博士：  
-哈尔滨中小企业代表的主题演讲：  
关于马来西亚和中国中小企业历史，未来发展和国际合作  
-圆桌会议，四位主旨演讲嘉宾，主持人：赫尔米教授  
                      
**下午**
-1号会议室：教授/博士生报告  
教授/博士学术报告，指导研究和学术发展。  
                    
-2号会议室：论文报告/产品研究报告：   
多场同时进行的会议涵盖各种主题，产品研究，论文等。参与者可以选择感兴趣的领域。  

-展览：参与者参观展位以获取信息并相互交流。        
  
**展览会**：共 40 个展位  
**预计参观人数：** 800-1000 人  
""")

    with st.expander("Day 2", expanded=True):
        st.markdown("""
**Morning**          
-Opening Ceremony: Inviting the minister for the opening  
-Advisor Speech: (Tan Seri Dr Ng Yen Yen, former minister of MOTAC)  
-UKM Representative Speech: VC / Rep. of UKM  
-HUC Representative Speech:  President of HUC  
-Chairman's Welcome Speech: Prof. Dr Riza Sulaiman  
-Title Sponsor Production Introduction: Industry   
                      
**Afternoon**   
-Room 1: Professors / Doctoral Students / Paper Presentations  
A dedicated session to support and mentor doctoral students, guiding research and academic development.  

-Room 2: Product Introductions:   
SME, Chamber of Commerce, exhibitors and industry players to introduce their products, associations, etc.  

-Exhibition: Participants visiting the exhibition booths to get information and meet each other.  
  
**Exhibition with** 40 booths  
**Estimated Attendance:** 800-1000      
  
**上午**  
-开幕式： 邀请部长出席开幕式和致辞  
-顾问致辞： （丹斯里黄燕燕医生，旅游文化部原部长）  
-马国立代表致辞：马国立校长/代表  
-哈师大代表致辞：哈师大校长/代表  
-大会主席致欢迎辞：礼扎·苏莱曼教授  
-冠名赞助商产品介绍：行业     
  
**下午**  
-1号会议室：教授/博士生/论文报告  
教授/博士/硕士学术报告，指导研究和学术发展。  
                    
-2号会议室：产品介绍：   
中小企业、商会、参展商和行业参与者将在此介绍他们的产品、研究成果等。  

-展览：参与者参观展位以获取信息并相互交流。  
  
**展览会**：共 40 个展位  
**预计参观人数：** 800-1000 人  
""")

    with st.expander("Day 3", expanded=True):
        st.markdown("""
**Morning**  
-MATRADE introduction investment in Malaysia: Policies, procedures and incentives  
-Harbin government representative introduction investment in Harbin: Policies, procedures and incentives  
-JAKIM Keynote: Halal Food insights on regulatory, compliance, and industry-specific matters.  
-Tourism Keynote: 2 Keynote sessions (from Malaysia and Harbin) highlighting tourism opportunities, collaboration, and cultural exchange initiatives.  
  
**Afternoon**  
Room 1: Production Introductions:  
SME, Chamber of Commerce, exhibitors and industry players to introduce their products, associations, etc.  

Room 2: Business Matching:   
1.China–Malaysia Enterprise Matching: Chinese and Malaysian companies participating as exhibitors can explore potential collaborations.  
2.China–Malaysian Chambers Matching: Exhibiting Chinese enterprises can connect with Malaysian chambers of commerce for partnership opportunities.  
3.China–Malaysian Government Matching: Exhibiting Chinese enterprises can meet with relevant Malaysian government departments to discuss regulatory guidance, investment, and collaboration  

Exhibition: Participants visiting the exhibition booths to get information and meet each other.  
  
**Exhibition with** 40 booths  
**Estimated Attendance:** 800-1000  
  
**上午**  
-马来西亚对外贸易发展局(MATRADE )介绍在马来西亚的投资：政策、程序和激励措施  
-哈尔滨市政府代表介绍在哈尔滨的投资：政策、程序和激励措施  
-JAKIM 主题演讲： 清真食品监管、合规和行业特定事项解说。  
-旅游主题演讲： 2 场主题演讲（分别来自马来西亚和哈尔滨），重点介绍旅游机遇、合作和文化交流举措。  
  
**下午**  
1号会议室：产品介绍：  
中小企业、商会、参展商和行业参与者将在此介绍他们的产品、协会等。 
                     
2号会议室：商务对接：   
1.中马企业对接：参展的中国和马来西亚企业可以探讨潜在的合作机会。  
2.中马商会配对：参展的中国企业可以与马来西亚商会联系，寻求合作机会。  
3.中马政府对接：参展的中国企业可与马来西亚相关政府部门会面，探讨监管指导、投资和合作等事宜。  

展览：参与者参观展位以获取信息并相互交流。  
                      
**展览会**：共 40 个展位  
**预计参观人数：** 800-1000 人  
""")

# ===== RIGHT COLUMN =====
with col2:
    with st.expander("Day 4", expanded=True):
        st.markdown("""
**Morning**  
-Buses visiting MATRADE  
-Buses visiting the SME Association   
  
**Afternoon**  
-Buses visiting UKM / UPM Research Institute  
-Buses visiting Huawei Malaysia (TBC)  
  
Industry, Research Institute, Association and Government Office visit  
Targeted 150 participants (100 international participants, 50 local participants)  
  
**上午**  
-2辆巴士参观MATRADE  
-2辆巴士参观中小企业协会   
  
**下午**  
-2辆巴士前往马来西亚国立大学/马来西亚博特拉大学研究所  
-2辆巴士将前往华为马来西亚（待定）  
  
参观行业、研究机构、协会和政府机关  
目标参与人数为 150 人（100 名国际参与者，50 名本地参与者）  
""")

    with st.expander("Day 5", expanded=True):
        st.markdown("""
**Whole Day**  
-1Bus visiting Melaka  
-2Buses visiting KL and the surrounding area:  
Kuala Lumpur Convention Centre, KLCC  
Putrajaya Mosque  
Central Market, KL  
Dataran Merdeka  
Bukit Bintang  
Batu Caves   
  
Cultural experiences, city engagements, tourism and relaxing  
Targeted 100 participants (100 international participants)  
  
**全天**  
1辆巴士游览马六甲  
2 辆巴士游览吉隆坡及周边地区：  
吉隆坡会议中心 (KLCC)  
布城清真寺  
吉隆坡中央市场  
独立广场  
武吉免登  
黑风洞  
  
文化体验、城市活动、旅游和休闲  
目标参与者100人（100名国际参与者）  
""")

st.markdown("---")
st.write("© 2026 ACDC Organising Committee")