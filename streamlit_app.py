import streamlit as st

st.title("🎈 My new Streamlit app")
st.header("Full of Joy")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
name= st.text_input("Enter Name:")
studymethod = st.selectbox("StudyMethod" ,("Crammer","Pre-Planner","Memory Box"))
button =st.button("Diva?")      


if button:
    with st.spinner("Loading your diva status"):
        if studymethod =="Crammer":
            st.write(f"{name}, You ain't no diva")
        elif studymethod =="Memory Box":
            st.write(f"{name}, You are almost a diva")
        elif studymethod == "Pre-Planner":
            st.write(f"{name},You is a diva")