import requests
from streamlit_lottie import st_lottie
import streamlit as st
from PIL import Image
st.set_page_config(page_title="STUDENTBAE",page_icon=":tada:",layout='wide')
def lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding =lottieurl("https://assets8.lottiefiles.com/packages/lf20_aao5ezov.json")
lottie_coding2 =lottieurl("https://assets8.lottiefiles.com/packages/lf20_eidvjn72.json")
lottie_coding3 = lottieurl("https://assets8.lottiefiles.com/packages/lf20_oyi9a28g.json")
background = Image.open("logo2.png")
col1, col2, col3 = st.columns([0.2, 5, 0.2])
col2.image(background, width=500)
st.subheader("Learning is never done without errors and defeat")
st.title("STUDENTBAE")
st.write("STUDENTBAE is a application, Which makes student life easier by helping them to finish their assignment and helps to  collects notes in the easier way")
st.write("[Project Link >](https://github.com/gamkers/STUDENTBAE)")

with st.container():
    st.write("---")
    left_coloumn, right_coloumn = st.columns(2)
    with left_coloumn:
        st.header("WHY STUDENTBAE?")
        st.write("##")
        st.write(
            """
            Now a Days students are flooded with assignments given by colleges because of that they got stuck and they cant able to develop their skills
            Most of the time their force to do assignments for marks so students does not have any options
            To solve this problem we came up the solutions best we can.""")
        st.write("STUDENTBAE helps you to complete your assignments by:")
        st.write("- just you need to give your topic of your assignments our application directly surf over the internet and collect datas related to the topic.")
        st.write("- Then convert the DATA into handwritten by this student get ride over the assignments.")
        st.write("- Also We added one more use full features, if you give the topic our application direct collect the pdf in the internet. ")

    with right_coloumn:
        st_lottie(lottie_coding,height=500,key="STUDENTS")
with st.container():
    st.write("---")
    left_coloumn, right_coloumn = st.columns(2)
    with left_coloumn:
        st_lottie(lottie_coding2, height=500, key="STUDENTS2")
    with right_coloumn:
        st.header(" Other features:")
        st.write("##")
        st.write("- Get research papers related to topics.")
        st.write("- Get Notes and PDF")
        st.write("- Get Timetables also circulars")
        st.write("- Question Papers")
        st.write("- Information about a organization")
        st.write("- Interview Questions")















with st.container():
    st.write("---")
    left_coloumn, right_coloumn = st.columns(2)
    with left_coloumn:
        st.markdown("<h1 style='text-align: center; color: white ;'>DEVELOPERS</h1>", unsafe_allow_html=True)
        st.subheader("AKASH M")
        st.write("B.Tech CSE")
        st.subheader("Surendharan TG")
        st.write("B.Tech CSE")
        st.subheader("Naveen PK")
        st.write("B.Tech CSE")
        st.subheader("V S Viswanath")
        st.write("B.Tech CSE")
        st.subheader("SUDHA SIRISHA K")
        st.write("B.Tech CSE")
    with right_coloumn:
        st_lottie(lottie_coding3,height=400,key="DEVELOPERS")
            
