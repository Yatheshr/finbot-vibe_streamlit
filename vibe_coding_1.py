import streamlit as st
from transformers import pipeline

# Load the sentiment analysis pipeline once and cache it
@st.cache_resource
def load_sentiment_analyzer():
    return pipeline("sentiment-analysis")

# Create a function to get the response from the bot based on sentiment
def get_bot_response(message, sentiment_analyzer):
    sentiment = sentiment_analyzer(message)[0]
    label = sentiment['label']

    if label == "NEGATIVE":
        return "I'm really sorry for the trouble. I’ll prioritize your issue and get it fixed right away."
    elif label == "POSITIVE":
        return "Thanks for reaching out! I’m happy to help you with that."
    else:
        return "Thanks for letting us know. Let me look into that for you."

# Streamlit app setup
def run_chat():
    # Title for the app
    st.title("FinBot 💬")
    
    # Create a text input box for user input
    user_input = st.text_input("You: ")

    # Load sentiment analyzer (cached)
    sentiment_analyzer = load_sentiment_analyzer()

    if user_input:
        with st.spinner("Analyzing your message..."):
            # Get bot response
            response = get_bot_response(user_input, sentiment_analyzer)
            st.write(f"FinBot: {response}")

if __name__ == "__main__":
    run_chat()
