import streamlit as st

# ---- PAGE CONFIG ----
st.set_page_config(page_title="AI Interview Chatbot", page_icon="🤖", layout="wide")

# ---- SIMPLE RESPONSE FUNCTION ----
def get_response(user_input):
    return "This is a demo response for: " + user_input

# ---- CUSTOM CSS ----
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(to right, #141e30, #243b55);
        color: white;
    }
    .title {
        font-size: 40px;
        font-weight: bold;
        text-align: center;
        color: #00c6ff;
    }
    .chat-box {
        background-color: rgba(255,255,255,0.1);
        padding: 15px;
        border-radius: 15px;
        margin-bottom: 10px;
    }
    .user {
        color: #00ffcc;
    }
    .bot {
        color: #ffcc00;
    }
    </style>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.markdown('<p class="title">🤖 AI Interview Preparation Chatbot</p>', unsafe_allow_html=True)

# ---- SESSION STATE ----
if "history" not in st.session_state:
    st.session_state.history = []

# ---- INPUT ----
user_input = st.text_input("💬 Ask your question:")

if user_input:
    response = get_response(user_input)

    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# ---- CHAT DISPLAY ----
for sender, msg in st.session_state.history:
    if sender == "You":
        st.markdown(f'<div class="chat-box user">👤 {msg}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="chat-box bot">🤖 {msg}</div>', unsafe_allow_html=True)
