import streamlit as st
from PIL import Image
import os

def app():
    # Introduction text with improved styling
    st.markdown("""
    <style>
        .custom-title {
            text-align: center;
            font-size: 35px;
            font-weight: bold;
            color: #ffffff; /* White color for the title */
            margin-bottom: 40px;
            font-family: 'Arial', sans-serif;
        }
        .intro-text {
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: #4783b4; /* Blue color for intro text */
            margin-bottom: 20px;
        }
        .centered-buttons {
            display: flex;
            justify-content: space-between;
            margin-top: 30px;
        }
        .image-gallery {
            display: flex;
            justify-content: center;
            gap: 10px; /* Space between images */
        }
        .image-gallery img {
            width: 300px; /* Fixed width */
            height: 200px; /* Fixed height */
            object-fit: cover;
            border-radius: 8px;
        }
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .center-title {
            text-align: center;
            font-size: 36px; /* Adjust font size as needed */
            font-weight: bold;
            color: #ffffff; /* Change color if needed */
            animation: fadeIn 2s ease-in-out, slideIn 2s ease-in-out;
            transition: color 0.5s ease;
        }
        
        /* Animation for fading in */
        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }
        
        /* Animation for sliding in from the top */
        @keyframes slideIn {
            from {
                transform: translateY(-50px);
                opacity: 0;
            }
            to {
                transform: translateY(0);
                opacity: 1;
            }
        }

        .center-title:hover {
            color: #FFD700; /* Change color on hover */
            cursor: pointer;
        }
        </style>
        <div class="center-title">Hobbies and Extracurricular Activities</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <div class="intro-text">
        Aside from academic pursuits, I also engage in various extracurricular activities
        such as participating in pageants, modeling, and singing.
    </div>
    """, unsafe_allow_html=True)

    # Pageants Section
    with st.expander('Pageants', expanded=False):
        st.write("""
        Participating in pageants has allowed me to develop confidence, public speaking skills, and a strong sense of poise.
        """)

        # Initialize session state for pageant images
        if 'pageant_index' not in st.session_state:
            st.session_state.pageant_index = 0
        if 'pageant_images' not in st.session_state:
            st.session_state.pageant_images = [
                'images/pageant1.jpg',
                'images/pageant2.jpg',
                'images/pageant3.jpg',
                'images/pageant4.jpg',
                'images/pageant5.jpg',
                'images/pageant6.jpg',
                'images/pageant7.jpg',
                'images/pageant8.jpg',
                'images/pageant9.jpg'
            ]

        # Display current pageant image
        if st.session_state.pageant_images:
            current_image_path = st.session_state.pageant_images[st.session_state.pageant_index]
            if os.path.isfile(current_image_path):
                image = Image.open(current_image_path)
                col1, col2, col3 = st.columns([1, 2, 1])
                with col1:
                    st.write("")  # Empty column for centering
                with col2:
                    st.image(image, width=300)
                with col3:
                    st.write("")  # Empty column for centering

        # Navigation buttons for pageants
        st.markdown('<div class="centered-buttons">', unsafe_allow_html=True)
        col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
        with col1:
            if st.session_state.pageant_index > 0:
                if st.button('Previous Image', key='pageant_prev'):
                    st.session_state.pageant_index -= 1
        with col2:
            st.write("")  # Empty column for centering
        with col3:
            st.write("")  # Empty column for centering
        with col4:
            if st.session_state.pageant_index < len(st.session_state.pageant_images) - 1:
                if st.button('Next Image', key='pageant_next'):
                    st.session_state.pageant_index += 1
        st.markdown('</div>', unsafe_allow_html=True)

    # Modeling Section
    with st.expander('Modeling', expanded=False):
        st.write("""
        Modeling gives me the opportunity to express my creativity and work with diverse teams in the fashion industry.
        """)

        # Initialize session state for modeling images
        if 'modeling_index' not in st.session_state:
            st.session_state.modeling_index = 0
        if 'modeling_images' not in st.session_state:
            st.session_state.modeling_images = [
                'images/fs1.jpg',
                'images/fs2.jpg',
                'images/fs3.jpg',
                'images/fs4.jpg',
                'images/fs5.jpg',
                'images/fs6.jpg'
            ]

        # Display current modeling image
        if st.session_state.modeling_images:
            current_image_path = st.session_state.modeling_images[st.session_state.modeling_index]
            if os.path.isfile(current_image_path):
                image = Image.open(current_image_path)
                col1, col2, col3 = st.columns([1, 2, 1])
                with col1:
                    st.write("")  # Empty column for centering
                with col2:
                    st.image(image, width=300)
                with col3:
                    st.write("")  # Empty column for centering

        # Navigation buttons for modeling
        st.markdown('<div class="centered-buttons">', unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 1, 1])
        with col1:
            if st.session_state.modeling_index > 0:
                if st.button('Previous Image', key='modeling_prev'):
                    st.session_state.modeling_index -= 1
        with col2:
            st.write("")  # Empty column for centering
        with col3:
            if st.session_state.modeling_index < len(st.session_state.modeling_images) - 1:
                if st.button('Next Image', key='modeling_next'):
                    st.session_state.modeling_index += 1
        st.markdown('</div>', unsafe_allow_html=True)

    # Singing Section
    with st.expander('Singing', expanded=False):
        st.write("""
        Singing is more than just a hobby to me, it provides a creative outlet and a way to connect with others through music.
        """)

        st.write("")
        st.write("Here's a short clip of me singing:")
        st.write("")
        video_file = 'videos/sing.mp4'
        if os.path.isfile(video_file):
            st.video(video_file, format="video/mp4")
        else:
            st.error(f"Video file not found: {video_file}")

if __name__ == "__main__":
    app()
