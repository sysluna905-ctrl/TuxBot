#!/usr/bin/env python3
# TuxBot - Your Linux penguin buddy
# Lesson 5: Real Linux Integration

import random
import subprocess   # NEW: This lets us run real Linux commands

print("🐧 Hello! I'm TuxBot, your friendly Linux penguin.")
print("Type 'exit' or 'quit' anytime to stop chatting.")
print("Try slash commands: /sysinfo, /joke, /clear, /help\n")

# Memory from previous lesson
user_name = None

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

    if user_input.startswith("/"):
        command = user_input[1:]  # Remove the slash - bonus trick to make it cleaner
        if command == "sysinfo":
            result = subprocess.run(["uname", "-a"], capture_output=True, text=True)
            print(f"🐧 TuxBot: Here's your system info:\n{result.stdout}")
        elif command == "joke":
            jokes = [
                "Why do Linux users never get lost? Because they always have a 'path' to follow! 😂",
                "Why did the penguin go to the party? Because it was a Linux bash! 🐧🎉",
                "Why do programmers prefer dark mode? Because light attracts bugs! 🐞💡"
            ]
            print(f"🐧 TuxBot: {random.choice(jokes)}")
        elif command == "clear":
            subprocess.run("clear")  # This will clear the terminal
        else:
            print("🐧 TuxBot: Oops, I don't know that command. Try /sysinfo, /joke, or /clear!")
        continue

    

    # Current placeholder
    if user_input in responses:
        print(f"🐧 TuxBot: {random.choice(responses[user_input])}")
    else:
        print("🐧 TuxBot: Hmm... interesting!")