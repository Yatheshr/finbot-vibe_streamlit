import streamlit as st
from transformers import pipeline

# Load sentiment model
sentiment_analyzer = pipeline("sentiment-analysis")

# Title for the web app
st.title("📊 FinBot - Financial Support Chat")

# Text input field for user message
user_message = st.text_input("Type your message here:")

# Define function to generate bot's response
def get_response(msg):
    result = sentiment_analyzer(msg)[0]
    label = result["label"]
    
    if label == "NEGATIVE":
        return "I'm really sorry for the trouble. I’ll prioritize your issue and get it fixed right away."
    elif label == "POSITIVE":
        return "Thanks for reaching out! I’m happy to help you with that."
    else:
        return "Thanks for letting us know. Let me look into that for you."

# Display response if there is a user message
if user_message:
    bot_reply = get_response(user_message)
    st.markdown(f"**FinBot:** {bot_reply}")
