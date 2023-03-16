import streamlit as st
import numpy as np

from streamlit_extras.switch_page_button import switch_page
from streamlit_card import card

#Page overall setting
#https://docs.streamlit.io/library/api-reference/utilities/st.set_page_config
st.set_page_config(
    page_title="RoboStock",
    page_icon="📈",
    layout="centered",
    initial_sidebar_state="collapsed",
)

#Disble the sidebar
st.markdown(
    """
<style>
    [data-testid="collapsedControl"] {
        display: none
    }
</style>
""",
    unsafe_allow_html=True,
)

#Import the CSS file for website design format
with open('style_main.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Background Image - Use image to control the background color
page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("https://static.wixstatic.com/media/63fd61_b86a647579344fe0b43290785a1a3af0~mv2.gif");
background-size: 130%;
background-position: top right;
background-repeat: no-repeat;
background-attachment: local;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

"""
For Data Downloading and Create Graphic
"""



#input score from other files
main_score = 0.8
sentiment_signal = "buy"
volume_signal = "buy"
time_signal = "sell"

with st.container():
#Section 1a - Key Message
    #margin
    st.markdown(f"<h5 style='text-align: center; margin-top: 30px;color:#4284CC; font-size: 10px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: center; color:#000000; font-size: 26px; font-family: Oswald, sans-serif'> Twitter says ... </h5>", unsafe_allow_html=True)
    #Section 1b - Buy or Sell
    if main_score >= 0.6:
        st.markdown(f"<h5 style='text-align: center; color:#FF914D; font-size: 60px; font-family: Oswald, sans-serif'> BUY TODAY 🐂 </h5>", unsafe_allow_html=True)
    elif main_score >= 0.4:
        st.markdown(f"<h5 style='text-align: center; color:#FF914D; font-size: 60px; font-family: Oswald, sans-serif'> HOLD TODAY 🐂 </h5>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h5 style='text-align: center; color:#4284CC; font-size: 60px; font-family: Oswald, sans-serif'> SELL TODAY 🧸 </h5>", unsafe_allow_html=True)

    #Section 1c - Score bar
    col_a1, col_a2, col_a3 = st.columns([1,4,1])
    with col_a1:
        st.markdown(f"<h5 style='text-align: center; color:#4284CC; font-size: 60px; font-family: Open Sans Bold, sans-serif'> 🧸 </h5>", unsafe_allow_html=True)
    with col_a2:
        st.progress(main_score, text=None)
    with col_a3:
        st.markdown(f"<h5 style='text-align: center; color:#4284CC; font-size: 60px; font-family: Open Sans Bold, sans-serif'> 🐂 </h5>", unsafe_allow_html=True)

    #margin
    st.markdown(f"<h5 style='text-align: center; margin-top: 30px;color:#4284CC; font-size: 10px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

col_b1, col_b2, col_b3 = st.columns([1,1,1])
with col_b1:
    #Column Title
    st.image("https://static.wixstatic.com/media/63fd61_6dfc87ea0cd94e539e91a960df3c8366~mv2.png")
    # st.markdown(f"<h5 style='text-align: left; margin-top: 16px;color:#4284CC; font-size: 30px; font-family: Open Sans Bold, sans-serif'> 💬 </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: left; color:#FF914D; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Twitter Sentiment Analysis </h5>", unsafe_allow_html=True)

    #Label for Buy, Hold or Sell
    if sentiment_signal == "buy":
        st.image("https://static.wixstatic.com/media/63fd61_9c62560397124eaa8c320e49d4b76408~mv2.png")
    elif sentiment_signal == "hold":
        st.image("https://static.wixstatic.com/media/63fd61_f32341a3d588440fb1bd2b2ff692e29e~mv2.png")
    else:
        st.image("https://static.wixstatic.com/media/63fd61_2f1ddec84fd2427f86035f8ad0d54325~mv2.png")


    if st.button("Read More"):
        switch_page("sentiment")

#Margin
st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

with col_b2:
    #Column Title
    st.image("https://static.wixstatic.com/media/63fd61_a525a4f28cd74e418f5448ef0403f0ba~mv2.png")
    #st.markdown(f"<h5 style='text-align: left; margin-top: 16px;color:#4284CC; font-size: 30px; font-family: Open Sans Bold, sans-serif'> 📊 </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: left; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Twitter Volume Analysis </h5>", unsafe_allow_html=True)

    #Label for Buy, Hold or Sell
    if volume_signal == "buy":
        st.image("https://static.wixstatic.com/media/63fd61_9c62560397124eaa8c320e49d4b76408~mv2.png")
    elif volume_signal == "hold":
        st.image("https://static.wixstatic.com/media/63fd61_f32341a3d588440fb1bd2b2ff692e29e~mv2.png")
    else:
        st.image("https://static.wixstatic.com/media/63fd61_2f1ddec84fd2427f86035f8ad0d54325~mv2.png")

    if st.button("Read more "):
        switch_page("volume")

    #Margin
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

with col_b3:
    #Column Title
    st.image("https://static.wixstatic.com/media/63fd61_a7725d3f2adf4c8b9e6401e344422823~mv2.png")
    #st.markdown(f"<h5 style='text-align: left; margin-top: 16px;color:#4284CC; font-size: 30px; font-family: Open Sans Bold, sans-serif'> ⏳ </h5>", unsafe_allow_html=True)
    st.markdown(f"<h5 style='text-align: left; color:#151515; font-size: 16px; font-family: Open Sans Bold, sans-serif'> Time Series Analysis </h5>", unsafe_allow_html=True)

    #Label for Buy, Hold or Sell
    if time_signal == "buy":
        st.image("https://static.wixstatic.com/media/63fd61_9c62560397124eaa8c320e49d4b76408~mv2.png")
    elif time_signal == "hold":
        st.image("https://static.wixstatic.com/media/63fd61_f32341a3d588440fb1bd2b2ff692e29e~mv2.png")
    else:
        st.image("https://static.wixstatic.com/media/63fd61_2f1ddec84fd2427f86035f8ad0d54325~mv2.png")

    if st.button("Read More  "):
        switch_page("time")

    #Margin
    st.markdown(f"<h5 style='text-align: center; margin-bottom: 16px; color:#4284CC; font-size: 16px; font-family: Open Sans Bold, sans-serif'> </h5>", unsafe_allow_html=True)

st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#FFFFFF; font-size: 10px; font-family: Open Sans, sans-serif'> 2023 © - all rights reserved by CRYPTOBOT</h5>", unsafe_allow_html=True)
st.markdown(f"<h5 style='text-align: center; margin-top: 0px; color:#FFFFFF; font-size: 10px; font-family: Open Sans, sans-serif'> NO INVESTMENT ADVICE <br>The Content is for informational purposes only,<br> you should not construe any such information or other material as legal, tax, investment, financial, or other advice.</h5>", unsafe_allow_html=True)
