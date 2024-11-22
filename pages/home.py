import os
import streamlit as st

def show_home():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    image_path = os.path.join(project_root, 'assets', 'bird_home.png')
    
    if not os.path.exists(image_path):
        st.error(f"File not found: {image_path}")
        return

    st.markdown("""
    <style>
    .stApp {
        background-color: #F0F8FF;
    }
    .title {
        color: #4A628A;
        font-size: 48px;
        text-align: left;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .subtitle {
        color: #4A628A;
        text-align: left;
        font-size: 28px;
        margin-bottom: 15px;
    }
    .description {
        color: #4A628A;
        text-align: left;
        font-size: 20px;
        margin-bottom: 30px;
        text-align: justify;
    }
    .section-title {
        color: #4A628A;
        font-size: 30px;
        font-weight: bold;
        margin-top: 30px;
        margin-bottom: 15px;
    }
    .feature-card {
        background-color: #7AB2D3;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }
    .feature-card:hover {
        transform: scale(1.05);
    }
    .metric-card {
        background-color: #7AB2D3;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }
    .metric-card:hover {
        transform: scale(1.05);
    }
    .testimonial {
        background-color: #7AB2D3;
        border-radius: 10px;
        padding: 15px;
        margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        transition: transform 0.3s;
    }
    .testimonial:hover {
        transform: scale(1.05);
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

    container = st.container()
    with container:
        st.markdown('<h1 class="title">Welcome to AvianSense🐦</h1>', unsafe_allow_html=True)
        st.markdown('<h2 class="subtitle">Discover, Identify, and Learn About Birds</h2>', unsafe_allow_html=True)
        
        st.markdown("""
        <p class="description">
        AvianSense is your go-to platform for identifying bird species effortlessly. 
        Our cutting-edge machine learning model and user-friendly design make it easy for bird enthusiasts and researchers alike to explore the incredible diversity of bird species.
        </p>
        """, unsafe_allow_html=True)

        st.image(image_path, use_column_width=True)

        st.markdown('<h3 class="section-title">🌟 Key Features</h3>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("""
            <div class="feature-card">
                <h4>🔍 Precise Identification</h4>
                <p>Advanced machine learning model with 90% accuracy</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="feature-card">
                <h4>📊 Extensive Database</h4>
                <p>200+ Bird Species Recognized</p>
            </div>
            """, unsafe_allow_html=True)
        
        with col3:
            st.markdown("""
            <div class="feature-card">
                <h4>📱 Easy to Use & user friendly</h4>
                <p>Simple upload and instant results</p>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<h3 class="section-title">📊 Our Impact</h3>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("""
            <div class="metric-card">
                <h4>Total Bird Species</h4>
                <h2>200+</h2>
            </div>
            """, unsafe_allow_html=True)
        
        with col2:
            st.markdown("""
            <div class="metric-card">
                <h4>User Community</h4>
                <h2>5+</h2>
            </div>
            """, unsafe_allow_html=True)

        st.markdown('<h3 class="section-title">💬 What Our Users Say</h3>', unsafe_allow_html=True)
        
        testimonials = [
            "sudah bagus sekali webnya, warnanya bikin nyaman dilihat dan UI nya sudah terlihat rapih, burung saya sendiri ikut terbang melihat design webnya - Brandon (kur).",
            "keren juga yaa aplikasinya, saya sebagai anak organisasi di bidang biologi sangat merasa terbantu sebagai media pembelajaran untuk kegiatan pengamatan burung - Pacar Travis.",
            "tampilan desainnya keliatan modern, minimalis, dan mudah diterima oleh mata. fitur yang diberikan juga terlihat lengkap, good job sir - rheisan"
        ]
        
        for testimonial in testimonials:
            st.markdown(f"""
            <div class="testimonial">
                <p>"{testimonial}"</p>
            </div>
            """, unsafe_allow_html=True)
