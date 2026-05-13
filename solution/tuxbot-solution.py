#!/usr/bin/env python3
# TuxBot - Your Linux penguin buddy
# Lesson 7: Persistent Memory – Remember Your Name Forever

import random
import subprocess
import os

print("🐧 Hello! I'm TuxBot, your friendly Linux penguin.")
print("Type 'exit' or 'quit' anytime to stop chatting.\n")

# Memory
user_name = None
name_file = "user_name.txt"
history_file = "chat_history.txt"

# === LOAD SAVED USER NAME ===
if os.path.exists(name_file):
    with open(name_file, "r") as f:
        user_name = f.read().strip()
    if user_name:
        print(f"👋 Welcome back, {user_name}!\n")

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

    # === SAVE NAME PERMANENTLY ===
    if user_input.startswith("my name is "):
        user_name = user_input.replace("my name is ", "").strip().title()
        with open(name_file, "w") as f:
            f.write(user_name)
        reply = f"Nice to meet you, {user_name}! I'll remember you next time! 🐧"
        print(f"🐧 TuxBot: {reply}")

    # === PERSONALIZED GREETING ===
    elif user_name and user_input in ["hi", "hello"]:
        reply = f"Hey {user_name}! How's it going?"
        print(f"🐧 TuxBot: {reply}")

    # === SHOW LAST MESSAGE ===
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
        continue   # Don't save /last command

    # === OTHER SLASH COMMANDS ===
    elif user_input.startswith("/"):
        command = user_input[1:]   # remove the slash
        if command == "sysinfo":
            result = subprocess.run(["uname", "-a"], capture_output=True, text=True)
            reply = f"Here's your system info:\n{result.stdout}"
            print(f"🐧 TuxBot: {reply}")
        elif command == "joke":
            jokes = [
                "Why do Linux users never get lost? Because they always have a 'path' to follow! 😂",
                "Why did the penguin go to the party? Because it was a Linux bash! 🐧🎉",
                "Why do programmers prefer dark mode? Because light attracts bugs! 🐞💡"
            ]
            reply = random.choice(jokes)
            print(f"🐧 TuxBot: {reply}")
        elif command == "clear":
            subprocess.run("clear")
            reply = "Terminal cleared!"
        else:
            reply = "Oops, I don't know that command. Try /sysinfo, /joke, /clear, or /last!"
            print(f"🐧 TuxBot: {reply}")

    # === NORMAL REPLY ===
    else:
        if user_input in responses:
            reply = random.choice(responses[user_input])
        else:
            reply = "Hmm... interesting!"
        print(f"🐧 TuxBot: {reply}")

    # === SAVE BOTH MESSAGES TO HISTORY FILE ===
    # This now runs for everything except /last
    with open(history_file, "a") as f:
        f.write(f"You: {user_input}\n")
        f.write(f"TuxBot: {reply}\n\n")