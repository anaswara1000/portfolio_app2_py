import streamlit as st
import pandas
# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("/home/anaswara/Downloads/python/python2app/pythonProject/images (2)/photo.png")

with col2:
    st.title(" Anaswara R")
    content ="""
    hi I am Anaswara.Aspiring software engineer passionate about AI, adept in Python and data structures and algorithms, eager to drive innovation through impactful
projects.
    """
    st.info(content)

content2 ="""
Below you can find some of the apps I have built in Python.Feel free to contact me
"""
st.write(content2)

col3, empty_col, col4 = st.columns([1.5,0.5,1.5])

df=pandas.read_csv("/home/anaswara/Downloads/python/python2app/pythonProject/.venv/data.csv",sep=";")

with col3:
    for index,row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("/home/anaswara/Downloads/python/python2app/pythonProject/images (2)/" + row["image"])
        st.write(f"[Source Code]({row['url']})")


with col4:
    for index,row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("/home/anaswara/Downloads/python/python2app/pythonProject/images (2)/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
