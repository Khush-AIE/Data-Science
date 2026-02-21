import streamlit as st

def app():

    st.set_page_config(layout='wide')

    st.markdown("""
    <style>
                .title{
                margin-top: 120px;
                color:white;}
    
                body{
                background-color: white;}
                </style>""",unsafe_allow_html=True)

    col1,col2 = st.columns([1.2,1])

    with col1:
        st.image(r'C:\Users\ADMIN\Desktop\brain2.jpg',width=300)

    with col2:
        st.markdown('<div class="title>',unsafe_allow_html=True)
        st.markdown("## Brain Tumor MRI Detection")
        st.write("Login to access tumor detection system")
        st.markdown('</div>',unsafe_allow_html=True)
        
        username=st.text_input("Username",key='Username')
        password=st.text_input("Password",type="password",key='password')
        if username!="" and password!="":
            if st.button("Login",type='primary'):
                st.success("Logged in !!")
                st.balloons()
        else:
            st.warning("Please enter valid credentials")
        for words in username,password:
             with open('storage.txt','a') as f:
                  f.writelines(words)


app()