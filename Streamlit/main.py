import streamlit as st

from streamlit_option_menu import option_menu

import home , Login, Tumors ,Predict

st.markdown("""
    <style>
            .stApp{
            background-color:black;
            color:white;
            }
            </style>
""",unsafe_allow_html=True)

st.set_page_config(
    page_title="Brain Anatomy",
)

class MultiApp:      # to manage multiple pages
    def __init__(self):
        self.apps = []            #
    def add_app(self,title,func):
        self.apps.append({
            "title":title,
            "function":func
        })
    def run():
        with st.sidebar:
            app = option_menu(
                menu_title="Walk-Through",
                options=['Home','Login','Tumors','Predict'],
                icons=['house-fill','person-fill','trophy-fill'],
                menu_icon='chat-text-fill',
                default_index=1,
                styles={
                    "container":{"padding":"5!important","background-color":'black'},        #sidebar ma menu/container 
                    "icon":{"color":"white","font-size":"20px"},                             #icons mate 
                    "nav-link":{"color":"white","font-size":"20px","text-align":"left","margin":"0px"},  #pages link karva mate
                    "nav-linl-selected":{"background-color":"#02ab21"},                    #navigation kato koi optio mahover kariye to ema color ave ena mate
                }
            )
        if app=='Home':
            home.app()
        if app=='Login':
            Login.app()
        if app=='Tumors':
            Tumors.app()
        if app=='Predict':
            Predict.app()
    run()