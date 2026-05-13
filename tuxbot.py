#!/usr/bin/env python3
# TuxBot - Your Linux penguin buddy
# Lesson 6: Save & Load Chat History

import random
import subprocess
import os   # NEW: helps us work with files

print("🐧 Hello! I'm TuxBot, your friendly Linux penguin.")
print("Type 'exit' or 'quit' anytime to stop chatting.\\n")

# Memory from previous lessons
user_name = None

# TODO 1: Load previous chat history from "chat_history.txt" here
# Hint: Check if the file exists, then read and print it

# Responses dictionary
responses = {
    "hi": ["Hey there!", "Hello!", "Hiya!"],
    "hello": ["Hey there!", "Hello!", "Hiya!"],
    "help": ["Try /sysinfo, /joke, /clear or just chat with me!"],
    "who are you": ["I'm TuxBot, your Linux penguin buddy! 🐧"],
}

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["exit", "quit"]:
        print("🐧 Bye! Come back anytime. TuxBot out! 👋")
        break

    # Memory handling (from Lesson 4)
    if user_input.startswith("my name is "):
        user_name = user_input.replace("my name is ", "").strip().title()
        print(f"🐧 TuxBot: Nice to meet you, {user_name}! I'm TuxBot! 🐧")
        continue

    if user_name and user_input in ["hi", "hello"]:
        print(f"🐧 TuxBot: Hey {user_name}! How's it going?")
        continue

    # Get TuxBot's reply
    if user_input in responses:
        reply = random.choice(responses[user_input])
    else:
        reply = "Hmm... interesting!"

    print(f"🐧 TuxBot: {reply}")

    # TODO 2: Save both the user's message and TuxBot's reply to "chat_history.txt"
    # Hint: Open the file in "a" (append) mode and write the lines