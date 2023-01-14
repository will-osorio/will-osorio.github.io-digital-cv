import streamlit as st
import requests
from  streamlit_lottie import st_lottie



# ---- HEADER ---- 
st.set_page_config(page_title="My Webpage", page_icon=":D", layout=("wide"))

st.subheader( "Hello,my name is William Osorio!")
st.title("I'm financial anaylist. ")
st.title("I am passionate about using prgroamming to make monotaunus tasks easier.")
st.write("[Learn More >] ")

def load_lottieurl(url):  
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_coding = load_lottieurl("https://assets7.lottiefiles.com/packages/lf20_gzx4caln.json")

# ---- BODY ----
with st.container():
    st.write("---")
    left_column, right_column  = st.columns(2)

with right_column:
    st_lottie(lottie_coding, height="300", key = "coding" )


 