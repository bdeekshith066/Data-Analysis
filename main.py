import streamlit as st
from streamlit_option_menu import option_menu
st.set_page_config(layout="wide", page_title="DATA ANALYSIS",
        page_icon="📈📊",)

import home , analysis , operations, introduction, Feature_Engineering, Skewness_OutlierDetection



# Reducing whitespace on the top of the page
st.markdown("""
<style>

.block-container
{
    padding-top: 1rem;
    padding-bottom: 0rem;
    margin-top: 1rem;
}

</style>
""", unsafe_allow_html=True)



class MultiApp:
    def __init__(self):
        self.app = []

    def add_app(self, title, func):
        self.app.append({
            "title": title,
            "function": func
        })   

    def run(self):  # Need to include self as the first parameter
        with st.sidebar:
            st.markdown("""
          <style>
            .gradient-text {
              margin-top: -20px;
            }
          </style>
        """, unsafe_allow_html=True)
            
            typing_animation = """
            <h3 style="text-align: left;">
            <img src="https://readme-typing-svg.herokuapp.com/?font=Righteous&size=40&Left=true&vLeft=true&width=500&height=70&lines=DATA DYNAMICS📈📊" alt="Typing Animation" />
            </h3>
            """
            st.markdown(typing_animation, unsafe_allow_html=True)
            
            app = option_menu(
                menu_title='Sections',
                options=['Home','Introduction','Operation','Analysis📊📈','Feature Engineering','Skewness, Outliers, Kurtosis'],
                default_index=0,
            )
            
           
            st.sidebar.write("")
            linkedin_url = "https://www.linkedin.com/in/deekshith2912/"
            linkedin_link = f"[ByteBuddies]({linkedin_url})"
            st.sidebar.subheader(f"Developed  by Deekshith B , Madhurika Priya")
            
        if app == "Home":
            home.app()
        elif app == "Introduction":
            introduction.app()     
        elif app == "Operation":
            operations.app() 
        elif app == "Analysis📊📈":
            analysis.app() 
        elif app == "Feature Engineering":
            Feature_Engineering.app() 
        elif app == "Skewness, Outliers, Kurtosis":
            Skewness_OutlierDetection.app()
       
        
           

# Create an instance of the MultiApp class and run the app
MultiApp().run()