class Chatbot:
    def __init__(self):
        self.greetings = ["hello", "hi", "hey"]
        self.farewells = ["bye", "goodbye", "see you"]
        self.responses = {
            "how are you": "I'm just a program, so I don't have feelings, but I'm here to help you!",
            "what is your name": "I am a chatbot created to assist you.",
            "what can you do": "I can chat with you and try to answer your questions to the best of my ability."
        }

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Check for greetings
        if any(greet in user_input for greet in self.greetings):
            return "Hello! How can I assist you today?"

        # Check for farewells
        if any(farewell in user_input for farewell in self.farewells):
            return "Goodbye! Have a great day!"

        # Check for known responses
        for question, response in self.responses.items():
            if question in user_input:
                return response

        # Default response
        return "I'm not sure how to respond to that. Can you ask something else?"

# Instantiate the chatbot
chatbot = Chatbot()

# Simulate a conversation
def chat():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

# Start the chat
chat()
