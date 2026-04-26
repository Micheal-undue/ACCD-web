import streamlit as st

def navbar():
    st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: center;
        background-color: #0b1f3a;
        padding: 14px 0;
        position: sticky; 
        top: 0;
        z-index: 999;
    }

    .navbar a {
        color: white;
        padding: 14px 25px;
        text-decoration: none;
        font-size: 18px;
        font-weight: 500;
        transition: 0.3s;
    }

    .navbar a:hover {
        background-color: #1c3d6e;
        border-radius: 5px;
        color: #ffffff !important; /* 确保悬停时文字颜色不变 */
    }
    </style>

    <div class="navbar">
        <a href="/" target="_self">Home</a>
        <a href="/Track" target="_self">Themes</a>
        <a href="/Activities" target="_self">Activities</a>
        <a href="/Registration" target="_self">Registration</a>
        <a href="/Venue" target="_self">Travel</a>
        <a href="/Committee" target="_self">Committee</a>
        <a href="/Contact" target="_self">Contact Us</a>
    </div>
    """, unsafe_allow_html=True)