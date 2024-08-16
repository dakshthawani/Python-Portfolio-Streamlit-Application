import pandas
import streamlit as st
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.image("images/author.png",width=300)
with col2:
    st.title("Andi More")
    content = """
    Skilled Python Developer with [X] years of experience in designing, developing, and deploying efficient and scalable applications. Proficient in various frameworks and libraries such as Django, Flask, and Pandas. Strong background in object-oriented programming, data analysis, and machine learning. Experienced in working with RESTful APIs, databases (SQL and NoSQL), and version control systems (Git). Adept at problem-solving and optimizing code for performance. Proven ability to collaborate effectively within a team and deliver high-quality software solutions.
    """
    st.info(content)
st.write("Here i am with all Python application built by me,Feel free to contact me")
col3, empty_col, col4 = st.columns([1.5, .5, 1.5])
df = pandas.read_csv("dataset.csv", sep=',')

with col3:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")
with col4:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f"[Source Code]({row['url']})")

