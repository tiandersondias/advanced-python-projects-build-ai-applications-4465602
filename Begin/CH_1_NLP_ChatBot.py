from textblob import TextBlob

intents = {
    "hours": {
        "keywords": ["hours", "open", "close", "time", "working", "schedule"],
        "response": "We are open from 9 AM to 5 PM, Monday to Friday."
    },
    "return": {
        "keywords": ["refund", "money back", "return", "exchange", "policy", "warranty"],
        "response": "I'd be happy to help you with the return process. Let me transfer you to a live agent."
    },
    "order_status": {
        "keywords": ["order", "status", "track", "tracking", "delivery", "where is my"],
        "response": "You can track your order using the tracking link in your confirmation email. Need help?"
    },
    "product_info": {
        "keywords": ["product", "details", "features", "specs", "availability", "stock"],
        "response": "Can you specify which product you're looking for? I'd be happy to provide more details!"
    },
    "support": {
        "keywords": ["help", "support", "technical", "issue", "problem", "customer service"],
        "response": "I'm here to assist you! What issue are you experiencing?"
    },
    "payment": {
        "keywords": ["payment", "charge", "billing", "invoice", "credit card", "paypal"],
        "response": "We accept all major credit cards and PayPal. Let me know if you need further assistance."
    },
    "shipping": {
        "keywords": ["shipping", "delivery", "cost", "time", "international", "fee"],
        "response": "Standard shipping takes 3-5 business days. International shipping may vary."
    },
    "greeting": {
        "keywords": ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"],
        "response": "Hello! How can I assist you today?"
    },
    "farewell": {
        "keywords": ["bye", "goodbye", "see you", "thanks", "thank you"],
        "response": "You're welcome! Have a great day!"
    }
}

def get_response(message):
    message = message.lower()

    # Check for matching intent
    for intent, intent_data in intents.items():
        if any(word in message for word in intent_data["keywords"]):
            return intent_data["response"]

    # Sentiment analysis if no intent is matched
    sentiment = TextBlob(message).sentiment.polarity
    if sentiment > 0:
        return "That's so great to hear!"
    elif sentiment < 0:
        return "I'm sorry to hear that. How can I help?"
    else:
        return "I see. Can you tell me more about that?"

def chat():
    print("Chatbot: Hi, how can I help you today?")
    
    while True:
        user_message = input("You: ").strip().lower()
        if user_message in ['exit', 'quit', 'bye']:
            print("Chatbot: Thank you for chatting. Have a great day!")
            break

        print(f"Chatbot: {get_response(user_message)}")

if __name__ == "__main__":
    chat()