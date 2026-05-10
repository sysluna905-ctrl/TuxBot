#!/usr/bin/env python3
# TuxBot - Your Linux penguin buddy
# Lesson 1: Infinite conversation loop

print("🐧 Hello! I'm TuxBot, your friendly Linux penguin.")
print("Type 'exit' or 'quit' anytime to stop chatting.\n")

while True:
    user_input = input("You: ").strip()
    
    if user_input.lower() in ["exit", "quit"]:
        print("🐧 Bye! Come back anytime. TuxBot out! 👋")
        break
    
    # For now we just echo – we'll make Tux smart in the next lessons
    print("TuxBot: Hmm... interesting!")