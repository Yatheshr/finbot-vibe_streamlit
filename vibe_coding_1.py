from transformers import pipeline

# Load the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

def get_bot_response(message):
    sentiment = sentiment_analyzer(message)[0]
    label = sentiment['label']

    if label == "NEGATIVE":
        return "I'm really sorry for the trouble. I’ll prioritize your issue and get it fixed right away."
    elif label == "POSITIVE":
        return "Thanks for reaching out! I’m happy to help you with that."
    else:
        return "Thanks for letting us know. Let me look into that for you."

def run_chat():
    print("Welcome to FinBot 💬 (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("FinBot: Goodbye!")
            break
        response = get_bot_response(user_input)
        print(f"FinBot: {response}\n")

if __name__ == "__main__":
    run_chat()
