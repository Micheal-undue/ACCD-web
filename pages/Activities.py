import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="Program structure | ACCD 2026", layout="wide")

navbar()

# ===== 表格注入 =====
st.markdown("""
<style>
    .schedule-table {
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 10px;
        font-size: 14px;
    }
    .schedule-table th, .schedule-table td {
        border: 1px solid #e0e0e0;
        padding: 12px;
        text-align: left;
    }
    .schedule-table th {
        background-color: #f8f9fa;
        font-weight: bold;
    }
    .time-label {
        background-color: #f1f3f5;
        font-weight: bold;
        width: 100px;
        text-align: center !important;
        vertical-align: middle;
    }
    .info-footer {
        font-size: 13px;
        color: #666;
        margin-top: 5px;
        padding-left: 5px;
    }
</style>
""", unsafe_allow_html=True)

# ===== PAGE CONTENT =====
st.markdown("## Program structure")
st.markdown("---")

col1, col2 = st.columns(2)

# ===== LEFT COLUMN =====
with col1:
    with st.expander("📅 Day 1 - Academic & Industry Exchange", expanded=True):
        st.markdown(f"""
        <table class="schedule-table">
            <tr>
                <td class="time-label">Morning</td>
                <td>
                    • <b>Co-Chair Prof Helmi Ali & HUC:</b> Addressing the theme of ACCD’26<br>
                    • <b>SME President Dr Chin Chee:</b> Keynote session<br>
                    • <b>Harbin SME Keynote:</b> SME Association, members and cooperations<br>
                    • <b>Round Table:</b> 4 keynote speakers (Moderator: Prof Helmi Ali)
                </td>
            </tr>
            <tr>
                <td class="time-label">Afternoon</td>
                <td>
                    • <b>Room 1:</b> Professors / Doctoral Students Presentations & Mentoring<br>
                    • <b>Room 2:</b> Paper presentation (Concurrent sessions)<br>
                    • <b>Exhibition:</b> Booth visiting & Networking
                </td>
            </tr>
        </table>
        <div class="info-footer">📍 <b>Exhibition:</b> 40 booths | 👥 <b>Attendance:</b> 800-1000</div>
        """, unsafe_allow_html=True)

    with st.expander("📅 Day 2 - Opening Ceremony & Industry", expanded=True):
        st.markdown(f"""
        <table class="schedule-table">
            <tr>
                <td class="time-label">Morning</td>
                <td>
                    • <b>Opening Ceremony:</b> Ministerial opening<br>
                    • <b>Advisor Speech:</b> Tan Seri Dr Ng Yen Yen (Former Minister of MOTAC)<br>
                    • <b>University Speeches:</b> VC/Rep of UKM & President of HUC<br>
                    • <b>Chairman's Welcome:</b> Prof. Dr Riza Sulaiman<br>
                    • <b>Sponsor:</b> Title Sponsor Production Introduction
                </td>
            </tr>
            <tr>
                <td class="time-label">Afternoon</td>
                <td>
                    • <b>Room 1:</b> Doctoral / Paper Presentations<br>
                    • <b>Room 2:</b> Product Introductions (SME, Chamber of Commerce, etc.)<br>
                    • <b>Exhibition:</b> Booth visiting & Networking
                </td>
            </tr>
        </table>
        <div class="info-footer">📍 <b>Exhibition:</b> 40 booths | 👥 <b>Attendance:</b> 800-1000</div>
        """, unsafe_allow_html=True)

    with st.expander("📅 Day 3 - Investment & Business Matching", expanded=True):
        st.markdown(f"""
        <table class="schedule-table">
            <tr>
                <td class="time-label">Morning</td>
                <td>
                    • <b>MATRADE:</b> Investment policies & incentives in Malaysia<br>
                    • <b>Harbin Govt:</b> Investment opportunities in Harbin<br>
                    • <b>JAKIM Keynote:</b> Halal Food regulatory & compliance<br>
                    • <b>Tourism Keynote:</b> Malaysia & Harbin cultural exchange
                </td>
            </tr>
            <tr>
                <td class="time-label">Afternoon</td>
                <td>
                    • <b>Room 1:</b> Production Introductions (SME & Industry Players)<br>
                    • <b>Room 2 (Matching):</b> 
                        1. China–Malaysia Enterprise Matching<br>
                        2. China–Malaysian Chambers Matching<br>
                        3. China–Malaysian Government Matching<br>
                    • <b>Exhibition:</b> Booth visiting & Networking
                </td>
            </tr>
        </table>
        <div class="info-footer">📍 <b>Exhibition:</b> 40 booths | 👥 <b>Attendance:</b> 800-1000</div>
        """, unsafe_allow_html=True)

# ===== RIGHT COLUMN =====
with col2:
    with st.expander("📅 Day 4 - Industrial & Research Visits", expanded=True):
        st.markdown(f"""
        <table class="schedule-table">
            <tr>
                <td class="time-label">Morning</td>
                <td>
                    • <b>Visit 1:</b> Buses visiting MATRADE<br>
                    • <b>Visit 2:</b> Buses visiting the SME Association
                </td>
            </tr>
            <tr>
                <td class="time-label">Afternoon</td>
                <td>
                    • <b>Visit 3:</b> Buses visiting UKM / UPM Research Institute<br>
                    • <b>Visit 4:</b> Buses visiting Huawei Malaysia (TBC)
                </td>
            </tr>
        </table>
        <div class="info-footer">👥 <b>Target:</b> 150 participants (100 Int'l, 50 Local)</div>
        """, unsafe_allow_html=True)

    with st.expander("📅 Day 5 - Cultural Experience & Tourism", expanded=True):
        st.markdown(f"""
        <table class="schedule-table">
            <tr>
                <td class="time-label">Whole Day</td>
                <td>
                    • <b>Route A:</b> 1 Bus visiting Melaka (Historical site)<br>
                    • <b>Route B:</b> 2 Buses visiting KL City Center:<br>
                      <i>KLCC, Putrajaya Mosque, Central Market, Dataran Merdeka, Bukit Bintang, Batu Caves</i>
                </td>
            </tr>
        </table>
        <div class="info-footer">👥 <b>Target:</b> 100 international participants</div>
        """, unsafe_allow_html=True)

st.markdown("---")
st.write("© 2026 ACDC Organising Committee")