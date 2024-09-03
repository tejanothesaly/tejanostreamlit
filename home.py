import streamlit as st

def app():
    # Initialize session state for audio playback if not already done
    if 'audio_played' not in st.session_state:
        st.session_state.audio_played = False

    # Custom CSS for styling
    st.markdown("""
    <style>
        /* General page style */
        body {
            font-family: 'Arial', sans-serif;
            background-color: #1c1c1c; /* Darker background */
            color: #e3e3e3; /* Light text color */
        }
        
        /* Page title styling */
        h1 {
            text-align: center;
            font-size: 3em;
            color: #ff7878; /* Slightly brighter color */
            margin-bottom: 20px;
            animation: fadeInTitle 2s ease-in-out;
        }

        /* Center text styling */
        .center-text {
            text-align: center;
            font-size: 1.2em; /* Adjust font size as needed */
            margin: 20px 0; /* Margin for spacing */
        }

        /* Name styling (same as title) */
        .name {
            text-align: center;
            font-size: 3em; /* Same size as title */
            color: #ff7878; /* Same color as title */
            font-weight: bold; /* Make text bold */
            margin-left: 60px; /* Adjust the space between heading and name */
            display: inline;
        }

        /* Section styles */
        .section {
            margin: 50px 0;
            padding: 30px; /* Increased padding */
            border: 2px solid #ff7878;
            border-radius: 15px;
            background-color: #2c2c2c; /* Darker section background */
            color: #e3e3e3; /* Ensures text is readable */
            transition: transform 0.3s ease-in-out, box-shadow 0.3s ease-in-out;
        }

        /* Flexbox container for image and content */
        .about-container {
            display: flex;
            align-items: center;
        }

        .about-container img {
            border-radius: 15px;
            margin-right: 20px;
            width: 250px; /* Adjust the size as needed */
        }

        .about-container p {
            margin: 0;
        }

        /* Hover effect for sections */
        .section:hover {
            transform: scale(1.02);
            box-shadow: 0px 0px 15px rgba(255, 120, 120, 0.2);
        }

        /* Animation for section content */
        @keyframes fadeIn {
            from {opacity: 0;}
            to {opacity: 1;}
        }

        .fade-in {
            animation: fadeIn 2s ease-in;
        }

        /* Title animation */
        @keyframes fadeInTitle {
            from {opacity: 0; transform: translateY(-50px);}
            to {opacity: 1; transform: translateY(0);}
        }

        /* Audio player styling */
        .audio-player {
            position: fixed;
            bottom: 10px;
            right: 10px;
            background: rgba(0, 0, 0, 0.5);
            border-radius: 10px;
            padding: 10px;
        }

        /* Audio control icon styling */
        .audio-control {
            font-size: 1.5em;
            cursor: pointer;
            color: #e3e3e3; /* Light text color */
        }
    </style>
    """, unsafe_allow_html=True)

    # Title
    st.title("Welcome to my Personal Page")

    # Centered text
    st.markdown('<p class="center-text">Get to know me while playing and listening my favorite song in the side bar menu</p>', unsafe_allow_html=True)

    # Introduction Section with Image
    st.markdown("""
    <div class="section fade-in">
        <div style="display: flex; align-items: center; justify-content: center;">
            <h2 style="margin: 0;">About Me</h2>
            <div>
            <p class="name">Thesaly Tejano</p>
            </div>
        </div>
        <div class="about-container">
            <img src="https://scontent.fmnl13-4.fna.fbcdn.net/v/t39.30808-6/369050660_810576647405195_1323138116615535664_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=a5f93a&_nc_eui2=AeHOp4nzUU_jrLo-fDjfJ5rOJpGVVCKDO4ImkZVUIoM7guG-GnTU3kfck5ZZoq3lOX9PoVxs9wFXKzVHmZyfTwbw&_nc_ohc=0pyXUAD7nqAQ7kNvgF2PTzg&_nc_ht=scontent.fmnl13-4.fna&oh=00_AYBzcvtVL0gV-yu3k8kgLqwV49fhBD32NGeBlbONAwhPjg&oe=66DC71A4" alt="Thesaly Tejano">
            <div>
                <p>Hello! This is my personal space where you can learn more about my education, hobbies, portfolio, and how to contact me.</p>
                <p>On this page, you can get a brief overview of who I am and what I do. Feel free to explore the other sections using the sidebar, Enjoy!</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Background Section
    st.markdown("""
    <div class="section fade-in">
        <h2>Quick Summary</h2>
        <ul>
            <li><strong>Passions and Interests:</strong> I am passionate about technology and enjoy exploring newly built applications.</li>
            <li><strong>Current Projects:</strong> Currently, we are working on building the transport management system for CIT- University.</li>
            <li><strong>Goals and Aspirations:</strong> My goals include successful career in both technology and entertainment industry.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    app()
