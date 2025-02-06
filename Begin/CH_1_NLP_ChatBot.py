# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob

# Defining the ChatBot class for interaction.
intents = {
    "hours":{
        "keywords":["hour","open","close"]
        "response":["We are open from 9 AM to 5 PM. Monday to Friday."]
    }
    "return":{
        "keywords":["refund","money back","return"]
        "response":["I'd be happy to help you with the return process. Let me transfer you to a live agent"]
    }
}
def get_response(message):
            # Convert to lowercase
            message = message.lower()
            #Check keywords
            if any(word in message for word in intent_data["keywords"]):
            #Return the corresponding response if a keyword matches
                return intent_data["response"]        
            # Analyzing the sentiment of the user's message.
                sentiment = TextBlob(message).sentiment.polarity
            # Generating the chatbot's response based on sentiment.
            return ("That's so great to hear!" if sentiment > 0 else
                    "I'm sorry to hear that. How can I help?" if sentiment < 0 else
                    "I see. Can you tell me more about that?")
def chat():
       #Greet the user and prompt for input
       print("Chatbot: Hi, How can I help you today?")
       #Continuosly prompt the user for input until they choose to exit
       while (user_message := input("You: ").strip().lower()) not in ['exit', 'quit', 'bye']
            print(f"\nChatbot: {get.response(user_message)}")
            #Get and print the chatbot's response based on user input
            # Printing the chatbot's response and sentiment.
            # Thank the user for chatting when they exit
            print("Chatbot: Thank you for chatting. Have a great day!")


if __name__ == "__main__":
    # Creating the chatbot and starting the chat loop.
    chatbot = ChatBot()
    chatbot.start_chat()
