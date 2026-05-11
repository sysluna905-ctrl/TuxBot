#!/usr/bin/env python3
# TuxBot - Your Linux penguin buddy
# Lesson 3: Response Dictionary + Random Replies

import random

print("🐧 Hello! I'm TuxBot, your friendly Linux penguin.")
print("Type 'exit' or 'quit' anytime to stop chatting.\n")

# TODO: Replace this with a proper responses dictionary
responses = {
    "hi": ["Hey there!", "Hello!", "Hiya!"],
    "hello": ["Hey there!", "Hello!", "Hiya!"],
    "help": ["I can say hi, tell you who I am, or answer basic questions!"],
    "who are you": ["I'm TuxBot, your Linux penguin buddy! 🐧"],
}

while True:
    user_input = input("You: ").strip().lower()
    
    if user_input in ["exit", "quit"]:
        print("🐧 Bye! Come back anytime. TuxBot out! 👋")
        break
    # TODO: Use the dictionary + random.choice() here
    
    if user_input in responses:
        print(f"🐧 TuxBot: {random.choice(responses[user_input])}")
    else:
        print("🐧 TuxBot: Hmm... interesting!")