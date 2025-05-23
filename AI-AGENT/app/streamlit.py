
import streamlit as st
from agent.basic_data_agent import create_agent, run_query

st.title(" Data Agent")

upfile = st.file_uploader("Upload CSV", type="csv")

if upfile is not None:
    with open("temp.csv", "wb") as f:
        f.write(upfile.read())
    
    agent = create_agent("temp.csv")

    query = st.text_input("Ask questions:")
    if query:
        answer = run_query(agent, query)
        st.write("Answer:", answer)






















