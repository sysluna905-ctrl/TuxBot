#!/usr/bin/env python3
# TuxBot - Your Linux penguin buddy
# Lesson 6: Save & Load Chat History

import random
import subprocess
import os

print("🐧 Hello! I'm TuxBot, your friendly Linux penguin.")
print("Type 'exit' or 'quit' anytime to stop chatting.\n")

# === MEMORY FROM PREVIOUS LESSONS ===
user_name = None

# === LOAD CHAT HISTORY WHEN STARTING ===
history_file = "chat_history.txt"

# Create the file if it doesn't exist
if not os.path.exists(history_file):
    open(history_file, "w").close()   # creates empty file

# Show previous chat history
print("📜 Loading previous chat history...\n")
with open(history_file, "r") as f:
    print(f.read())

print("-" * 40)  # separator

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

    if user_name and user_input in ["hi", "hello"]:
        print(f"🐧 TuxBot: Hey {user_name}! How's it going?")

    # Get TuxBot's reply
    if user_input in responses:
        reply = random.choice(responses[user_input])
    else:
        reply = "Hmm... interesting!"

    print(f"🐧 TuxBot: {reply}")

    # === SAVE TO FILE (append mode) ===
    with open(history_file, "a") as f:
        f.write(f"You: {user_input}\n")
        f.write(f"TuxBot: {reply}\n\n")
