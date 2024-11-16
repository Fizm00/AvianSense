import os
import streamlit as st
from PIL import Image
import torch
from torchvision import transforms, datasets
import timm
import torch.nn as nn

dataset_path = "CUB_200_2011/images/"

@st.cache_resource
def get_classes(data_dir):
    all_data = datasets.ImageFolder(data_dir)
    return all_data.classes

classes = get_classes(dataset_path)

@st.cache_resource
def load_model():
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    model = timm.create_model('efficientnet_b2', pretrained=True)
    
    n_inputs = model.get_classifier().in_features
    model.classifier = nn.Sequential(
        nn.Linear(n_inputs, 2048),
        nn.SiLU(),
        nn.Dropout(0.3),
        nn.Linear(2048, len(classes))
    )
    
    model_path = "models/final_model.pt"
    model.load_state_dict(torch.load(model_path, map_location=device))
    model = model.to(device)
    model.eval()
    return model

model = load_model()

def transform_image(image):
    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
    ])
    return preprocess(image).unsqueeze(0)

def predict(image, model):
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    image = image.to(device)
    with torch.no_grad():
        output = model(image)
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        _, predicted_class = torch.max(probabilities, dim=0)
    
    bird_name = classes[predicted_class].split(".", 1)[-1].replace("_", " ")
    return bird_name

# Main app interface
def show_main():
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
    .description {
        color: #4A628A;
        font-size: 20px;
        text-align: left;
        margin-bottom: 30px;
    }
    .result-box {
        background-color: #7AB2D3;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        color: #FFFFFF;
        font-size: 22px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-top: 20px;
        transition: transform 0.3s;
    }
    .result-box:hover {
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

    st.markdown('<h1 class="title">🐦 Bird Species Classifier</h1>', unsafe_allow_html=True)
    st.markdown("""
    <p class="description">
    This application is designed to identify bird species based on the image you upload. 
    Use this tool to learn more about the amazing diversity of birds around you.
    </p>
    """, unsafe_allow_html=True)

    st.markdown("""
    <p class="description">
    <strong>Upload Guidelines:</strong>
    <ul>
        <li>The image file must be in .jpg format.</li>
        <li>The uploaded image should be clear and prominently feature the bird as the main object.</li>
        <li>The file size should not exceed 200 MB.</li>
    </ul>
    </p>
    """, unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Upload your bird image here...", type="jpg")

    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        if st.button("Predict"):
            transformed_image = transform_image(image)
            predicted_class = predict(transformed_image, model)
            
            st.markdown(f"""
            <div class="result-box">
            This image is predicted to be the bird species <strong>{predicted_class}</strong>. 
            <br>The prediction result is based on image analysis using a machine learning model developed with a bird dataset and trained by Fizm.
            </div>
            """, unsafe_allow_html=True)
            
    st.markdown("""
    <div class="footer">
    Made with ❤️ by Fizm | © 2024 All Rights Reserved
    </div>
    """, unsafe_allow_html=True)

# Run the main app
if __name__ == "__main__":
    show_main()
