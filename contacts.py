import streamlit as st

def app():

    st.write("## Contact Me")

    # Add emojis and larger font with WordArt-like effect
    st.markdown(
        """
        <style>
        .wordart {
            font-size: 30px;
            font-weight: bold;
            color: #FF5733; /* Change color as desired */
            text-shadow: 2px 2px 4px #000000; /* Adds a shadow effect */
            text-align: center;
            margin-bottom: 30px;
        }
        .contact-box {
            border: 2px solid #007BFF; /* Border color */
            border-radius: 10px; /* Rounded corners */
            padding: 10px;
            margin: 10px 0;
            background-color: #f9f9f9; /* Background color */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Shadow effect */
        }
        .contact-box h3 {
            margin: 0;
            font-size: 22px;
            color: #007BFF; /* Heading color */
        }
        .contact-box p {
            margin: 10px 0;
            font-size: 18px;
            color: #333;
        }
        .contact-box a {
            color: #007BFF;
            text-decoration: none;
        }
        .contact-box a:hover {
            text-decoration: underline;
        }
        </style>
        <div class="wordart">Get in Touch!</div>
        <div class="contact-box">
            <h3>Personal Email</h3>
            <p>📧 <a href="mailto:tejanothesaly@gmail.com">tejanothesaly@gmail.com</a></p>
        </div>
        <div class="contact-box">
            <h3>Institutional Email</h3>
            <p>📧 <a href="mailto:thesaly.tejano@cit.edu">thesaly.tejano@cit.edu</a></p>
        </div>
        <div class="contact-box">
            <h3>Work Contact Number</h3>
            <p>📞 +09567849234</p>
        </div>
        <div class="contact-box">
            <h3>Social Media</h3>
            <p>🌐 <a href="https://www.facebook.com/thesaly.tejano7777/" target="_blank">Facebook</a> | 
            <a href="https://www.instagram.com/hearthesly/" target="_blank">Instagram</a></p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Add an engaging GIF
    st.image("https://cdn.dribbble.com/users/3497212/screenshots/11476810/media/c18175dc05724f0c933fa8f49b2ff875.gif", caption="Let's Connect!", use_column_width=True)


if __name__ == "__main__":
    app()
