import streamlit as st

def show_github():
    st.markdown("""
    <style>
    .stApp {
        background-color: #F0F8FF;
    }
    .github-container {
        background-color: white;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        padding: 30px;
        margin: 20px 0;
    }
    .github-title {
        color: #24292E;
        text-align: center;
        font-size: 42px;
        margin-bottom: 20px;
    }
    .github-section {
        background-color: #F6F8FA;
        border-radius: 10px;
        padding: 20px;
        margin-bottom: 20px;
        transition: all 0.3s ease;
    }
    .github-section:hover {
        transform: translateY(-5px);
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .repo-link {
        display: block;
        background-color: #1a5f7a;
        color: white;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        border-radius: 8px;
        margin-top: 15px;
        transition: background-color 0.3s ease;
    }
    .repo-link:hover {
        background-color: #1a5f7a;
    }
    .tech-stack {
        display: flex;
        justify-content: center;
        flex-wrap: wrap;
        gap: 10px;
        margin-top: 20px;
    }
    .tech-badge {
        background-color: #E5E7EB;
        padding: 5px 10px;
        border-radius: 20px;
        font-size: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<h1 class="github-title">🐱 GitHub Repository</h1>', unsafe_allow_html=True)

    st.markdown("""
    <div class="github-container">
        <div class="github-section">
            <h2>Bird Species Classifier</h2>
            <p>An advanced machine learning application for bird species identification using deep learning techniques.</p>
            <div class="tech-stack">
                <span class="tech-badge">Python</span>
                <span class="tech-badge">Streamlit</span>
                <span class="tech-badge">Torch</span>
                <span class="tech-badge">TorchVision</span>
                <span class="tech-badge">Machine Learning</span>
            </div>
            <a href="https://github.com/yourusername/bird-species-classifier" target="_blank" class="repo-link">
                View Repository 🔗
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="github-container">
        <div class="github-section">
            <h2>Project Details</h2>
            <p>Our Bird Species Classifier is an open-source project aimed at making bird identification accessible and easy. 
            The repository contains:</p>
            <ul>
                <li>📂 Complete source code</li>
                <li>🧠 Machine learning model</li>
                <li>📊 Dataset information</li>
                <li>📝 Documentation and setup instructions</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="github-container">
        <div class="github-section">
            <h2>Contribute to the Project</h2>
            <p>We welcome contributions from the community! Here's how you can help:</p>
            <ul>
                <li>🐛 Report bugs</li>
                <li>✨ Suggest new features</li>
                <li>📝 Improve documentation</li>
                <li>🧩 Submit pull requests</li>
            </ul>
            <a href="https://github.com/yourusername/bird-species-classifier/issues" target="_blank" class="repo-link">
                Open Issues 🚀
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="github-container">
        <div class="github-section">
            <h2>License and Usage</h2>
            <p>This project is open-source and available under the MIT License. 
            Feel free to use, modify, and distribute the code with proper attribution.</p>
            <a href="https://github.com/yourusername/bird-species-classifier/blob/main/LICENSE" target="_blank" class="repo-link">
                View License 📄
            </a>
        </div>
    </div>
    """, unsafe_allow_html=True)