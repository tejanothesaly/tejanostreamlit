import streamlit as st

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
        <div class="center-title">Portfolio</div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("""
    <style>
        .intro-text {
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            color: #4783b4; /* Blue color for intro text */
            margin-bottom: 20px;
        }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="intro-text">
        As someone who pursues a career in the technology industry, I have been practicing and learning more about the career I am pursuing. Take a look at some of my projects that my team and I have worked on.
    </div>
    """, unsafe_allow_html=True)

    # NextGen Section
    with st.expander("NextGen", expanded=False):
        st.write("This project aims to integrate the PayMongo payment gateway with the AIMS portal to enhance the payment experience for students and administrative staff alike. The system is an integration of both web scraping and Paymongo payment portal.")
        st.write("GitHub Repository: [NextGen](https://github.com/tejanothesaly/NextGen-.git)")
        st.image("images/nextgen1.png", caption="NextGen Payment Portal", use_column_width=True)

    # Campus Compass Section
    with st.expander("Campus Compass", expanded=False):
        st.write("Campus Compass is a map application for CIT aiming to provide help for people who mostly get lost on their way to a certain office in CIT-U ")
        st.write("GitHub Repository: [Campus Compass](https://github.com/risejade/CampusCompassFrontend.git)")
        st.image("images/campuscompass.png", caption="Campus Compass Map", use_column_width=True)

    # CITUMOVE Section
    with st.expander("CITUMOVE", expanded=False):
        st.write("CITUMOVE is an ongoing project focused on developing a comprehensive transport management system for CIT University.")
        st.image("images/transport1.png", caption="CITUMOVE Transport Management System", use_column_width=True)

if __name__ == "__main__":
    app()
