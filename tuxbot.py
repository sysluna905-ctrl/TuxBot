#!/usr/bin/env python3
# TuxBot - Your Linux penguin buddy
# Lesson 7: Persistent Memory – Remember Your Name Forever

import random
import subprocess
import os

print("🐧 Hello! I'm TuxBot, your friendly Linux penguin.")
print("Type 'exit' or 'quit' anytime to stop chatting.\\n")

# Memory
user_name = None
name_file = "user_name.txt"
history_file = "chat_history.txt"

# TODO 1: Load saved user name from "user_name.txt" if it exists
# Hint: Use os.path.exists() and with open() to read the file

# Responses dictionary
responses = {
    "hi": ["Hey there!", "Hello!", "Hiya!"],
    "hello": ["Hey there!", "Hello!", "Hiya!"],
    "help": ["Try /sysinfo, /joke, /clear, /last or just chat with me!"],
    "who are you": ["I'm TuxBot, your Linux penguin buddy! 🐧"],
}

while True:
    user_input = input("You: ").strip().lower()

    if user_input in ["exit", "quit"]:
        print("🐧 Bye! Come back anytime. TuxBot out! 👋")
        break

    # TODO 2: Save name permanently when user says "my name is ..."
    # Hint: Use with open(name_file, "w") to write the name

    # Personalized greeting
    if user_name and user_input in ["hi", "hello"]:
        print(f"🐧 TuxBot: Hey {user_name}! How's it going?")
        reply = f"Hey {user_name}! How's it going?"

    # Show last message
    elif user_input == "/last":
        if os.path.exists(history_file):
            with open(history_file, "r") as f:
                lines = [line.strip() for line in f.readlines() if line.strip()]
            if len(lines) >= 2:
                print("📜 Last message:")
                print(lines[-2])
                print(lines[-1])
            else:
                print("No messages yet.")
        else:
            print("No chat history yet.")
        continue   # IMPORTANT: Use continue so /last is NOT saved to history

    # Slash commands from Lesson 5 (these should be logged)
    elif user_input.startswith("/"):
        command = user_input[1:]
        if command == "sysinfo":
            result = subprocess.run(["uname", "-a"], capture_output=True, text=True)
            reply = f"Here's your system info:\\n{result.stdout}"
            print(f"🐧 TuxBot: {reply}")
        elif command == "joke":
            jokes = ["Why do Linux users never get lost? Because they always have a 'path' to follow! 😂",
                     "Why did the penguin go to the party? Because it was a Linux bash! 🐧🎉"]
            reply = random.choice(jokes)
            print(f"🐧 TuxBot: {reply}")
        elif command == "clear":
            subprocess.run("clear")
            reply = "Terminal cleared!"
        else:
            reply = "Oops, I don't know that command."
            print(f"🐧 TuxBot: {reply}")

    # Normal reply
    else:
        if user_input in responses:
            reply = random.choice(responses[user_input])
        else:
            reply = "Hmm... interesting!"
        print(f"🐧 TuxBot: {reply}")

    # TODO 3: Save both the user message and TuxBot's reply to history_file
    # Hint: Open in "a" (append) mode and write the two lines