import streamlit as st
import random

st.set_page_config(page_title="🎉 Birthday Surprise! 🎉", page_icon="🎂", layout="centered")

# Festive random color background
bg_colors = ["#FFDEE9", "#B5FFFC", "#FFD6E0", "#FEFFB8", "#C9FFBF", "#FCCF31", "#F55555"]
chosen_bg = random.choice(bg_colors)
st.markdown(f""" <style>
    .reportview-container {{
        background-color: {chosen_bg};
    }}
</style> """, unsafe_allow_html=True)

# Only ONE "Happy Birthday" main heading
st.markdown(f"<h1 style='text-align: center;'>🎈 Happy Birthday, Punni! 🎈</h1>", unsafe_allow_html=True)

# Fun/funny wishes
funny_wishes = [
    "You’re not old, you’re just… retro. 🎮",
    "Happy Birthday! May your day be more beautiful than your selfie filter.",
    "Congrats on reaching another level in the game of life! Don’t worry, there are still more power-ups.",
    "Remember: Age is just a number. But cake… cake is a solution! 🎂",
    "Wishing you more memes, less stress, and unlimited pizza. 🍕"
]

# Add confetti/snow emojis for more drama
st.snow()

# Display a random funny wish every time
st.markdown(
    f"<h2 style='text-align: center;color:#fc7703;'>{random.choice(funny_wishes)}</h2>",
    unsafe_allow_html=True,
)

# Hilarious GIF
st.image(
    r"https://media.tenor.com/8ryx1CctgfcAAAAM/happy-birthday-march-6.gif",
    caption="Party De Dio or Bromance karna band kar vrna ladki nahi milegi...",
    width = "stretch",
)

# Silly extra footer text
st.markdown(
    "<div style='text-align: center; font-size:18px;'>"
    "P.S. Calories don’t count today. Eat the cake! 🎉"
    "</div>",
    unsafe_allow_html=True,
)
