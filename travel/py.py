import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["My name is Chatbot and I'm here to assist you.",]
    ],
    [
        r"how are you ?",
        ["I'm doing well, thank you!", "I'm doing fine, how can I assist you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright, no problem.", "No worries.",]
    ],
    [
        r"(.*) (good|great|fine)",
        ["That's good to hear!",]
    ],
    [
        r"(.*) thank you (.*)",
        ["You're welcome!", "No problem.",]
    ],
    [
        r"exit",
        ["Goodbye! Have a great day ahead!", "Bye-bye! Take care.",]
    ],
]

# Create a chatbot with the defined pairs
chatbot = Chat(pairs, reflections)

# Define a function to interact with the chatbot
def chat():
    print("Hi! I'm Chatbot. How can I assist you today?")
    while True:
        user_input = input("> ")
        response = chatbot.respond(user_input)
        print(response)
        if user_input == "exit":
            break

# Run the chat function to start interacting with the chatbot
if __name__ == "__main__":
    chat()