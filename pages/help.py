import streamlit as st

def show_help():
    st.markdown("""
    <style>
    .stApp {
        background-color: #F0F8FF;
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
        border-radius: 15px;
        box-shadow: 0px 6px 15px rgba(0, 0, 0, 0.1);
        margin: 20px 0;
        padding: 30px;
        transition: all 0.3s ease;
        border-left: 5px solid;
    }
    .section:hover {
        transform: translateY(-10px);
        box-shadow: 0px 10px 20px rgba(0, 0, 0, 0.15);
    }
    .section-title {
        font-size: 36px;
        color: #2C3E50;
        font-weight: bold;
        margin-bottom: 20px;
        text-align: center;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .section-title i {
        margin-right: 15px;
        color: #3498db;
    }
    .section-content {
        font-size: 18px;
        color: #34495E;
        line-height: 1.6;
        text-align: justify;
    }
    .faq {
        background-color: #F4F4F4;
        padding: 20px;
        border-radius: 10px;
        margin-top: 15px;
    }
    .tips-section {
        border-left-color: #2ecc71;
    }
    .guide-section {
        border-left-color: #3498db;
    }
    .faq-section {
        border-left-color: #e74c3c;
    }
    .video-section {
        border-left-color: #9b59b6;
    }
    .feedback-section {
        border-left-color: #f39c12;
    }
    .feedback-form {
        background-color: #F9F9F9;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .cta-button {
        display: block;
        width: 100%;
        padding: 12px;
        background-color: #3498db;
        color: white;
        border: none;
        border-radius: 8px;
        transition: all 0.3s ease;
    }
    .cta-button:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css">
    """, unsafe_allow_html=True)

    st.title("Help Center 🆘")
    st.write("""
    Welcome to the Help section! Here you can find detailed guidance on how to use the application, 
    frequently asked questions, and other useful tips to make the most out of the features we offer.
    """)

    st.markdown("""
    <div class="section guide-section">
        <h2 class="section-title"><i class="fas fa-book"></i>User Guide</h2>
        <p class="section-content">Follow these steps to get started:</p>
        <ol class="section-content">
            <li>📸 Upload an image of a bird</li>
            <li>🔍 Click on the 'Predict' button to get the classification</li>
            <li>🌿 Explore the gallery to learn more about different bird species</li>
            <li>💬 Use the 'Feedback Form' to share your thoughts</li>
        </ol>
    </div>
    """, unsafe_allow_html=True)

    faq_content = """
    <div class="section faq-section">
        <h2 class="section-title"><i class="fas fa-question-circle"></i>Frequently Asked Questions</h2>
        <div class="faq">
            <details>
                <summary><strong>How accurate is the model?</strong></summary>
                <p>The model has been trained on a diverse dataset and achieves high accuracy, with an estimated accuracy of around 90%. However, its performance can vary based on image quality.</p>
            </details>
            <details>
                <summary><strong>Can I contribute to the App?</strong></summary>
                <p>Yes! We encourage contributions to improve the app. Please reach out to us via the contact section for more details on how you can contribute to the development of the Streamlit web application.</p>
            </details>
            <details>
                <summary><strong>What types of birds can be classified by this application?</strong></summary>
                <p>This application can classify a wide range of bird species from the CUB-200-2011 dataset, which is available on Kaggle. You can explore the species through our gallery. The dataset can be accessed <a href="https://www.kaggle.com/datasets/veeralakrishna/200-bird-species-with-11788-images/data" target="_blank">here</a>.</p>
            </details>
        </div>
    </div>
    """
    st.markdown(faq_content, unsafe_allow_html=True)

    st.markdown("""
    <div class="section tips-section">
        <h2 class="section-title"><i class="fas fa-lightbulb"></i>Tips & Tricks</h2>
        <div class="faq">
            <ul>
                <li>🌞 Ensure your bird image is clear and well-lit</li>
                <li>🔄 Try uploading different bird species</li>
                <li>📚 Check the gallery regularly to discover new species</li>
            </ul>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="section video-section">
        <h2 class="section-title"><i class="fas fa-video"></i>Video Tutorial</h2>
        <button class="cta-button">Watch Tutorial</button>
    </div>

    <div class="section feedback-section">
        <h2 class="section-title"><i class="fas fa-comment"></i>Feedback Form</h2>
        <div class="feedback-form">
            <textarea placeholder="Share your thoughts..." style="width:100%; height:150px;"></textarea>
            <button class="cta-button" style="margin-top:15px;">Submit Feedback</button>
        </div>
    </div>
    """, unsafe_allow_html=True)