import streamlit as st

def navbar():
    st.markdown("""
    <style>
    .navbar {
        display: flex;
        justify-content: center;
        background-color: #0b1f3a;
        padding: 14px 0;
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
    }
    </style>

    <div class="navbar">
        <a href="/">Home</a>
        <a href="/Track">Track</a>
        <a href="/Activities">Activities</a>
        <a href="/Registration">Registration</a>
        <a href="/Venue">Venue</a>
        <a href="/Committee">Committee</a>
        <a href="/Contact">Contact Us</a>
    </div>
    """, unsafe_allow_html=True)
