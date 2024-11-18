import streamlit as st
import os
import re
import wikipedia
import json

CACHE_DIR = "bird_article_cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def get_cached_article(bird_name):
    cache_file = os.path.join(CACHE_DIR, f"{bird_name.lower().replace(' ', '_')}.json")
    
    if os.path.exists(cache_file):
        with open(cache_file, 'r') as f:
            return json.load(f)
    
    return None

def save_article_to_cache(bird_name, article):
    cache_file = os.path.join(CACHE_DIR, f"{bird_name.lower().replace(' ', '_')}.json")
    
    with open(cache_file, 'w') as f:
        json.dump(article, f)

def get_bird_article(bird_name):
    cached_article = get_cached_article(bird_name)
    if cached_article:
        return cached_article
    
    cleaned_name = bird_name.lower().replace('_', ' ')

    try:
        page = wikipedia.page(cleaned_name + " bird")
        
        article = {
            "title": f"{cleaned_name.title()} - A Comprehensive Overview",
            "content": page.summary[:1000],
            "conservation_status": "Unknown"
        }

        save_article_to_cache(cleaned_name, article)
        
        return article
    except wikipedia.exceptions.DisambiguationError as e:
        try:
            page = wikipedia.page(e.options[0])
            article = {
                "title": f"{e.options[0]} - A Comprehensive Overview",
                "content": page.summary[:1000],
                "conservation_status": "Unknown"
            }
            save_article_to_cache(e.options[0], article)
            return article
        except:
            return {
                "title": "Article Not Found",
                "content": f"No detailed information found for {cleaned_name}.",
                "conservation_status": "Unknown"
            }
    except:
        return {
            "title": "Article Not Found",
            "content": f"We're sorry, but no detailed article is available for {cleaned_name} at the moment.",
            "conservation_status": "Unknown"
        }

def clean_bird_name(bird_name):
    bird_name = re.sub(r'^\d+\.', '', bird_name)
    
    bird_name = bird_name.replace('_', ' ')
    
    bird_name = bird_name.lower()
    
    return bird_name

def show_gallery():
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
    .article-section {
        background-color: #E6F2FF;
        border-radius: 10px;
        padding: 20px;
        margin-top: 20px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    }
    .article-section p {
        text-align: justify;
        line-height: 1.4;
    }
    </style>""", unsafe_allow_html=True)

    st.markdown('<h1 class="gallery-title">Bird Gallery</h1>', unsafe_allow_html=True)
    st.markdown('<p class="gallery-description">Explore our extensive collection of bird species, captured in their natural beauty.</p>', unsafe_allow_html=True)

    image_folder_path = "CUB_200_2011/images/"

    if not os.path.exists(image_folder_path):
        st.error(f"Folder {image_folder_path} not found.")
        return

    subfolders = os.listdir(image_folder_path)
    bird_types = [subfolder for subfolder in subfolders if os.path.isdir(os.path.join(image_folder_path, subfolder))]

    search_term = st.text_input("Search for a bird species")
    
    if search_term:
        bird_types = [bird for bird in bird_types if search_term.lower() in bird.lower()]

    selected_bird_type = st.selectbox("Select a Bird Species", bird_types)

    if selected_bird_type:
        cleaned_bird_name = clean_bird_name(selected_bird_type)
        
        selected_bird_path = os.path.join(image_folder_path, selected_bird_type)
        
        bird_images = os.listdir(selected_bird_path)

        article = get_bird_article(cleaned_bird_name)
        
        col1, col2 = st.columns([1, 1.5])
        
        with col1:
            st.markdown(f"**Displaying images of: {cleaned_bird_name.title()}**")

            image_selection = st.selectbox(
                "Choose Image", 
                range(len(bird_images)), 
                format_func=lambda x: f"Image {x+1}"
            )
            
            bird_image = bird_images[image_selection]
            bird_image_path = os.path.join(selected_bird_path, bird_image)
            
            if bird_image.lower().endswith(('.png', '.jpg', '.jpeg')):
                try:
                    st.image(bird_image_path, caption=bird_image, use_column_width=True)
                except Exception as e:
                    st.error(f"Error loading image {bird_image}: {e}")
        
        with col2:
            st.markdown(f"""
            <div class="article-section">
                <h3>{article['title']}</h3>
                <p>{article['content']}</p>
                <p><strong>Conservation Status:</strong> {article['conservation_status']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        Made with ❤️ by Fizm | © 2024 All Rights Reserved
    </div """, unsafe_allow_html=True)

# Main execution
if __name__ == "__main__":
    show_gallery()