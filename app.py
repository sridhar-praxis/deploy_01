# this is a cloned copy from github
# after this change it will be pushed back to github


import streamlit as st

batch_names = ["Jan 2022", "July 2022", "Jan 2023", "July 2023"]

selected_batch = st.sidebar.selectbox("Select Batch", batch_names)

st.title(f"Hello!!, {selected_batch} batch!")
st.write("This is a Streamlit web app.")

var = st.sidebar.slider("How is the josh?", 10, 50, 20, 1)
st.write("This class' Josh is", var)

st.write(""" use **markdown** """)

#comments branch changes