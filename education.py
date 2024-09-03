import streamlit as st
import os

def app():
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
        <div class="center-title">Educational Background</div>
        """,
        unsafe_allow_html=True
    )

    def display_education(school_name, years, description, school_image_url, personal_image_path):
        with st.expander(school_name):
            # Display the school's image
            if school_image_url:
                st.image(school_image_url, use_column_width=True)
            st.write(f"**{school_name}**")
            st.write(f"_({years})_")
            st.write(description)
            # Button to show/hide personal image
            if st.button(f"Picture of myself in {school_name}"):
                if os.path.exists(personal_image_path):  # Check if the image path exists
                    # Display image with Streamlit and center it
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        st.image(personal_image_path, use_column_width=True)
                else:
                    st.error(f"Image not found at {personal_image_path}")

    # Content for each education level
    display_education(
        "Cebu Institute of Technology University",
        "2021-present",
        "A 4th year student currently pursuing a degree in Bachelor of Science in Information Technology.",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSitF4hCPPe21lgjR-Tx4OQ9W38UhQ6HPWTOw&s",  # Replace with the actual URL of the school's image
        "images/me.jpg"  # Make sure 'images' folder is in the same directory as 'education.py'
    )
    display_education(
        "Southwestern University Phinma",
        "2018-2020 Graduated with Honors",
        "Completed senior high school with a focus on Science, Technology, Engineering, and Mathematics.",
        "https://swu.phinma.edu.ph/wp-content/uploads/2021/03/swu-phinma.png",  # Replace with the actual URL of the school's image
        "images/swu.jpg"
    )
    display_education(
        "Abellana National School",
        "2014-2018 Graduated with Honors",
        "Completed secondary education with involvement in Technical Vocational Livelihood major in cookery.",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQvKIKYd5atF96PJ9q8RwQr9oEDxo5MOQiLTN07n35Zd90D3284AJI9T9aAHxFz5c8NUpQ&usqp=CAU",  # Replace with the actual URL of the school's image
        "images/ans.jpg"
    )
    display_education(
        "Lahug Elementary School",
        "2006-2008 Preschool 2008-2014 Elementary",
        "Completed primary education with extra curricular activities participating in Swimming, Volleyball, and Majorettes.",
        "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTh7FX8hQ9f55Uu-FOgHWg3H26EVPaWyEJwx0IbjroRSFPOW74NoF0Leo2ynmpgJBkqHP0&usqp=CAU",  # Replace with the actual URL of the school's image
        "images/les.jpg"
    )

if __name__ == "__main__":
    app()
