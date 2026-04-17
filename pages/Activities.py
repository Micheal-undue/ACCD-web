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

""")

st.markdown("---")
st.write("© 2026 ACDC Organising Committee")