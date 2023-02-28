import streamlit as st

st.title("Streamlit Data App :boom:")
st.snow()

btn_click = st.button("click me")

if btn_click == True:
    st.subheader("Thank you for your time 	:blush:")
    st.balloons()