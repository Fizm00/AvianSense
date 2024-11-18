import streamlit as st

def show_about():
    st.markdown("""
    <style>
    .stApp {
        background-color: #F0F8FF;  /* Warna latar belakang aplikasi */
        display: flex;
        flex-direction: column;
        min-height: 100vh;
    }
    .main-content {
        flex: 1;
        margin-top: 40px;
        margin-bottom: 40px;
    }
    .section {
        background-color: #FFFFFF;
        border-radius: 10px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
        padding: 30px;
        transition: transform 0.3s;
    }
    .section:hover {
        transform: scale(1.02);
    }
    .section-title {
        font-size: 36px;
        color: #2C3E50;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center;
    }
    .section-content {
        font-size: 18px;
        color: #34495E;
        line-height: 1.6;
        text-align: justify;
    }
    .team-member {
        text-align: center;
        margin-bottom: 20px;
    }
    .team-member img {
        border-radius: 50%;
        width: 120px;
        height: 120px;
        margin-bottom: 15px;
    }
    .team-member-name {
        font-size: 22px;
        font-weight: bold;
        color: #2C3E50;
    }
    .team-member-role {
        font-size: 18px;
        color: #7F8C8D;
    }
    .contact-info {
        text-align: center;
        font-size: 18px;
        color: #2C3E50;
    }
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #1a5f7a;
        color: white;
        text-align: center;
        padding: 10px;
        z-index: 1000;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2 class="section-title">About Us</h2>
    <p class="section-content">This application was developed by a team of bird enthusiasts and data scientists. Our goal is to create a platform that promotes the appreciation of bird species from around the world. With this app, users can explore various bird species, learn about their characteristics, and gain knowledge about bird conservation efforts.</p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <h2 class="section-title">Our Mission</h2>
    <p class="section-content">Our mission is to raise awareness about the beauty and diversity of birds, and to encourage bird conservation. We strive to create an accessible and engaging platform for bird lovers, researchers, and anyone interested in learning more about the fascinating world of birds.</p>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="section">
        <h2 class="section-title">Our Team</h2>
        <div class="team-member">
            <img src="https://i.pinimg.com/736x/91/26/33/912633979de9728f829ee75f79963497.jpg" alt="Team Member" width="120"/>
            <p class="team-member-name">Fizm</p>
            <p class="team-member-role">Data Scientist & Developer</p>
            <p class="section-content">Fizm is responsible for developing the machine learning models that power our bird classification system. With expertise in data science and AI, Fizm ensures the accuracy and efficiency of our application.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section">
        <h2 class="section-title">Contact Us</h2>
        <p class="contact-info">For any inquiries, feedback, or collaborations, feel free to reach out to us:</p>
        <p class="contact-info">Email: <a href="mailto:himawanfirza21@gmail.com">himawanfirza21@gmail.com</a></p>
        <p class="contact-info">WhatsApp: <a href="https://wa.me/6281320732375" target="_blank">Chat with us on WhatsApp</a></p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        Made with ❤️ by Fizm | © 2024 All Rights Reserved
    </div>
    """, unsafe_allow_html=True)
