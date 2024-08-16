import streamlit as st
import pandas as pd
from send_email import send_mail

info = []

with st.form(key="email_form"):
    user_email = st.text_input(label="Enter your Email")
    raw_message = st.text_area(label="Enter your message")
    button = st.form_submit_button("Submit")
    message = f"""\
Subject: Mail from {user_email}

From: {user_email}
{raw_message}
    """

    if button:
        send_mail(user_email, message)
        # info.append({"Email": user_email, "Message": message})
        # df = pd.DataFrame(info)
        # # df = pd.read_csv("info.csv", sep=',')
        # df.to_csv('info.csv', mode='a', header=False, index=False)
        # # st.session_state['user_email'] = ""
        # # st.session_state['message'] = ""
        st.write('<meta http-equiv="refresh" content="0">', unsafe_allow_html=True)
