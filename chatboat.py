import random
import re

# Rule-based chatbot intents
intents = {
    "Greetings": {
        "Patterns": ["Hello", "hye", "howdy", "hola"],
        "Responses": ["Hello!", "Hi there!", "Howdy!"]
    },

    "Goodbyes": {
        "Patterns": ["Bye", "Goodbye", "seeyou", "later"],
        "Responses": ["Goodbye!", "See you later!", "Take care!"]
    },

    "Thanks": {
        "Patterns": ["Thanks", "Thank you", "appreciate it"],
        "Responses": [
            "You're welcome!",
            "No problem!",
            "Happy to help!",
            "Anytime!"
        ]
    },

    "Question": {
        "How are you": [
            "I'm fine, thank you!",
            "Doing great! What about you?"
        ],
        "What's your name": [
            "I'm ChatBuddy. Nice to meet you!"
        ],
        "What can you do": [
            "I can chat with you and answer simple questions."
        ]
    }
}


def match_intent(user_input):
    # Check pattern-based intents
    for intent, intent_data in intents.items():
        if isinstance(intent_data, dict) and "Patterns" in intent_data:
            for pattern in intent_data["Patterns"]:
                if re.search(pattern, user_input, re.IGNORECASE):
                    return random.choice(intent_data["Responses"])

    # Check question-based intents
    for question, responses in intents["Question"].items():
        if question.lower() in user_input.lower():
            return random.choice(responses)

    return None


def get_response(user_input):
    matched_intent = match_intent(user_input)

    if matched_intent:
        return matched_intent
    else:
        return "I didn't quite understand that. Could you please try asking something else?"


def chatbot():
    print("Chatbot: Hi! I'm ChatBuddy. How can I assist you today?")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["bye", "goodbye"]:
            print("Chatbot: Goodbye!")
            break

        response = get_response(user_input)
        print("Chatbot:", response)


# Run chatbot
chatbot()