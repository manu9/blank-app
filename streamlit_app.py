import streamlit as st
from streamlit_quill import st_quill

text = "Inicio"
text_2 = st.text_input("", value=text)
text = text_2

text_example = '<p>Hola <strong><em>Manuelghhg</em></strong><strong class="ql-size-huge"><em> hgjhgfghj</em></strong></p>'

@st.dialog("Cast your vote")
def vote(item):
    content = st_quill(text_example)
    if st.button("Submit"):
        st.session_state.vote = {"item": item, "reason": reason}
        st.rerun()

if "vote" not in st.session_state:
    st.write("Vote for your favorite")
    if st.button("A"):
        vote("A")
    if st.button("B"):
        vote("B")
else:
    f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"