#!/usr/bin/env python3
# TuxBot - Your Linux penguin buddy
# Lesson 4: Memory & Personality

import random

print("🐧 Hello! I'm TuxBot, your friendly Linux penguin.")
print("Type 'exit' or 'quit' anytime to stop chatting.\n")

# Memory - TuxBot will remember your name!
user_name = None

# Dictionary of responses - added the joke category here
responses = {
    "hi": ["Hey there!", "Hello!", "Hiya!"],
    "hello": ["Hey there!", "Hello!", "Hiya!"],
    "help": ["I can say hi, tell you who I am, or answer basic questions!"],
    "who are you": ["I'm TuxBot, your Linux penguin buddy! 🐧"],
    "tell me a joke": [
        "What are clouds made of? Linux servers! 😄",
        "Why do programmers prefer dark mode? Because light attracts bugs! 🐞"
    ],
}

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["exit", "quit"]:
        print("🐧 Bye! Come back anytime. TuxBot out! 👋")
        break

    # === MEMORY: Remember the user's name ===
    if user_input.startswith("my name is "):
        user_name = user_input.replace("my name is ", "").strip().title()
        print(f"🐧 TuxBot: Nice to meet you, {user_name}! I'm TuxBot! 🐧")
        continue

    # === PERSONALIZED GREETING ===
    if user_name and user_input in ["hi", "hello"]:
        print(f"🐧 TuxBot: Hey {user_name}! How's it going?")
        continue

    # Normal dictionary response
    if user_input in responses:
        print(f"🐧 TuxBot: {random.choice(responses[user_input])}")
    else:
        print("🐧 TuxBot: Hmm... interesting!")