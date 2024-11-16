import streamlit as st
import os
import re

def clean_bird_name(bird_name):
    # Removing leading numbers and period (e.g., "001.")
    bird_name = re.sub(r'^\d+\.', '', bird_name)
    
    # Replace underscores with spaces
    bird_name = bird_name.replace('_', ' ')
    
    # Capitalize the first letter of each word
    bird_name = bird_name.title()
    
    return bird_name

def show_gallery():
    # Custom styling for a more polished look
    st.markdown("""
    <style>
    .stApp {
        background-color: #F0F8FF;
    }
    .gallery-title {
        color: #4A628A;
        font-size: 48px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .gallery-description {
        color: #4A628A;
        text-align: center;
        font-size: 18px;
        margin-bottom: 40px;
        font-style: italic;
    }
    .image-card {
        background-color: #4A628A;
        border-radius: 15px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 4px 10px rgba(0,0,0,0.15);
        transition: transform 0.3s ease;
        margin-bottom: 20px;
    }
    .image-card:hover {
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

    st.markdown('<h1 class="gallery-title">Bird Gallery</h1>', unsafe_allow_html=True)
    st.markdown('<p class="gallery-description">Explore our extensive collection of bird species, captured in their natural beauty.</p>', unsafe_allow_html=True)

    image_folder_path = "CUB_200_2011/images/"

    if not os.path.exists(image_folder_path):
        st.error(f"Folder {image_folder_path} not found.")
        return

    subfolders = os.listdir(image_folder_path)
    bird_types = [subfolder for subfolder in subfolders if os.path.isdir(os.path.join(image_folder_path, subfolder))]

    selected_bird_type = st.selectbox("Select a Bird Species", bird_types)

    if selected_bird_type:
        cleaned_bird_name = clean_bird_name(selected_bird_type)
        
        selected_bird_path = os.path.join(image_folder_path, selected_bird_type)
        
        bird_images = os.listdir(selected_bird_path)

        st.markdown(f"**Displaying images of: {cleaned_bird_name}**")
        
        for bird_image in bird_images:
            bird_image_path = os.path.join(selected_bird_path, bird_image)
            
            if bird_image.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    st.image(bird_image_path, caption=bird_image, use_column_width=True)
                except Exception as e:
                    st.error(f"Error loading image {bird_image}: {e}")

    st.markdown("""
    <div class="footer">
        Crafted with ❤️ by Fizm | © 2024 All Rights Reserved
    </div>
    """, unsafe_allow_html=True)
