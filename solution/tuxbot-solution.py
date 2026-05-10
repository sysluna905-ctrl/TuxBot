#!/usr/bin/env python3
# TuxBot - Your Linux penguin buddy
# Lesson 2: Smart Command Handling

print("🐧 Hello! I'm TuxBot, your friendly Linux penguin.")
print("Type 'exit' or 'quit' anytime to stop chatting.\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ["exit", "quit"]:
        print("🐧 Bye! Come back anytime. TuxBot out! 👋")
        break
    
    if user_input.lower() in ["hello", "hi", "hey"]:
        print("🐧 TuxBot: Hello there! How can I assist you today?")
    elif user_input.lower() == "help":
        print("🐧 TuxBot: I can help you with basic commands. Try saying 'hello', 'hi', or 'hey' to greet me!")
    elif user_input.lower() == "who are you":
        print("🐧 TuxBot: I'm TuxBot, your friendly Linux penguin!")
    else:
        print("🐧 TuxBot: Hmm... interesting!")