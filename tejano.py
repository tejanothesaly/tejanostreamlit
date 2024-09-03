import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration first
st.set_page_config(
    page_title="Thesaly Tejano",
)

# Importing the page modules
import home  # Import the home module
import education 
import hobbies
import portfolio
import contacts

class MultiApp:
    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        # Sidebar with option menu
        with st.sidebar:
            # Audio player with local file
            audio_file_path = "audio/sining.mp3"
            st.audio(audio_file_path, format='audio/mp3', start_time=0)
            
            # Navigation menu
            selected_app = option_menu(
                menu_title='Thesaly Tejano',
                options=['Home', 'Education', 'Hobbies', 'Portfolio', 'Contacts'],
                icons=['house', 'book', 'folder', 'folder', 'phone'],
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "23px"},
                    "nav-link": {"color": "white", "font-size": "20px"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        # Run the selected app
        for app in self.apps:
            if app["title"] == selected_app:
                app["function"]()

# Create an instance of MultiApp
app = MultiApp()

# Add applications to the MultiApp instance
app.add_app("Home", home.app)
app.add_app("Education", education.app)
app.add_app("Hobbies", hobbies.app)
app.add_app("Portfolio", portfolio.app)
app.add_app("Contacts", contacts.app)

# Run the app
app.run()
