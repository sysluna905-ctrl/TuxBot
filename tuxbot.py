#!/usr/bin/env python3
# TuxBot - Your Linux penguin buddy
# Lesson 4: Memory & Personality

import random

print("🐧 Hello! I'm TuxBot, your friendly Linux penguin.")
print("Type 'exit' or 'quit' anytime to stop chatting.\n")

# Memory variables (this is what makes TuxBot remember you)
user_name = None

# Dictionary of responses (from previous lesson)
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
    
    # TODO: Add memory logic here
    # 1. If user says their name, remember it
    # 2. Use the name in greetings
    # 3. Add a couple of fun Linux dad jokes / tips
    
    # Current placeholder
    if user_input in responses:
        print(f"🐧 TuxBot: {random.choice(responses[user_input])}")
    else:
        print("🐧 TuxBot: Hmm... interesting!")