import streamlit as st
from components.navbar import navbar

st.set_page_config(page_title="Registration | ACCD 2026", layout="wide")

navbar()

# ===== PAGE CONTENT =====
st.markdown("## Registration")
st.markdown("---")

# 定义 Google 表单链接
registration_url = "https://docs.google.com/forms/d/e/1FAIpQLSe-Zia5DZCCjrNww-XWUuxNRHYOeduN2xU_HwALmcpAcjhbDg/viewform?usp=header"

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
        background-color: #0b1f3a; /* 匹配你网页的深蓝色调 */
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
    <div class="registration-title">Registration Form</div>
    <a href="{registration_url}" target="_blank" class="register-button">
        📋 Register Here
    </a>
    <p style="margin-top: 20px; color: #666; font-size: 14px;">
        Click the button above to open the Google Form in a new tab.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("---")
# =====================================================
# Registration Fee Table
# =====================================================
st.markdown("<h3 style='text-align:center;'>Registration Fees</h3>", unsafe_allow_html=True)

# 注入表格专用 CSS 样式
st.markdown("""
<style>
    .fee-table {
        width: 90%;
        margin: 20px auto;
        border-collapse: collapse;
        font-family: Arial, sans-serif;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }
    .fee-table th {
        background-color: #0b1f3a;
        color: white;
        padding: 15px;
        text-align: center;
        border: 1px solid #ddd;
    }
    .fee-table td {
        padding: 12px 15px;
        border: 1px solid #ddd;
        text-align: center;
    }
    .fee-table tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    .category-cell {
        font-weight: bold;
        background-color: #f1f3f5;
        width: 25%;
    }
    .price-sub {
        font-size: 12px;
        color: #666;
        display: block;
        margin-top: 4px;
    }
</style>
""", unsafe_allow_html=True)

# 渲染表格内容
st.markdown("""
<table class="fee-table">
    <thead>
        <tr>
            <th>Participant Category</th>
            <th>Early-Bird Rate</th>
            <th>Standard Rate</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td class="category-cell">Student (Malaysia)</td>
            <td><b>RM 300</b><span class="price-sub">Local student participant</span></td>
            <td><b>RM 600</b><span class="price-sub">Local student presenter</span></td>
        </tr>
        <tr>
            <td class="category-cell">International Student</td>
            <td><b>USD 100</b><span class="price-sub">Early registration</span></td>
            <td><b>USD 150 / 200</b><span class="price-sub">Standard student rate</span></td>
        </tr>
        <tr>
            <td class="category-cell">Regular Professional</td>
            <td><b>USD 150 / 300</b><span class="price-sub">Early-bird professional</span></td>
            <td><b>USD 200 / 350</b><span class="price-sub">Standard professional rate</span></td>
        </tr>
    </tbody>
</table>
<p style="text-align: center; font-style: italic; color: #555; font-size: 13px;">
    * Please refer to the specific conditions for each category during registration.
</p>
""", unsafe_allow_html=True)

st.markdown("---")
st.write("© 2026 ACDC Organising Committee")
