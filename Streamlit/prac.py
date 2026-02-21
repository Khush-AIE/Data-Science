import streamlit as st
st.set_page_config(
    page_title="Practise"
)

st.title('hey there',text_alignment='center')
st.markdown("""
            :orange[India] :yellow[Is] :green[best]
            """)
st.write("Select subjects:")
st.checkbox(label='Bio')
st.checkbox(label='english')
st.checkbox(label='maths')

st.radio("Whats your gender",
         [':rainbow[Male]',
         ':rainbow[Female]'])

st.balloons()
# st.balloons()


with st.form("my form"):
    st.write("Inside the form")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")


st.button("Submit",type='secondary')

# with st.echo():
#      st.write('This code will be print')

st.snow()

st.success('This is success.')
st.warning('This is danger!')
title = st.text_input("Movie title:")
st.write("Title is :",title)
f = open('storage.txt','a')
