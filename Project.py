import random

# 🎯 List of riddles (Question: Answer)
riddles = {
    "What has to be broken before you can use it?": "egg",
    "I'm tall when I'm young, and short when I'm old. What am I?": "candle",
    "What month of the year has 28 days?": "all",
    "What is full of holes but still holds water?": "sponge",
    "What question can you never answer yes to?": "are you asleep",
    "What gets wetter the more it dries?": "towel",
    "What goes up but never comes down?": "age",
    "What can you catch but not throw?": "cold",
    "What kind of band never plays music?": "rubber band",
    "What has hands but can’t clap?": "clock",
    "Where does today come before yesterday?": "dictionary",
    "What has many keys but can’t open a lock?": "piano",
    "What has one eye but cannot see?": "needle",
    "What gets bigger the more you take away?": "hole",
    "What can travel around the world while staying in a corner?": "stamp",
    "What has a head, a tail, is brown, and has no legs?": "penny",
    "I’m light as a feather, yet the strongest man can’t hold me for much more than a minute. What am I?": "breath",
    "What can you keep after giving to someone?": "your word",
    "What has words, but never speaks?": "book",
    "What has an eye but cannot see?": "needle"
}

print("🧩 Welcome to the Riddle Game!")
print("Try to answer as many riddles as you can. Type 'quit' to stop.\n")

# Convert riddles to list for random order
riddle_items = list(riddles.items())
random.shuffle(riddle_items)

score = 0
total = 0

# 🎮 Game loop
for question, answer in riddle_items:
    print(f"🤔 Riddle: {question}")
    user_answer = input("Your answer: ").lower().strip()

    if user_answer == "quit":
        break

    total += 1
    if user_answer == answer:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! The correct answer was: '{answer}'.\n")

print("🎯 Game Over!")
print(f"You answered {score} out of {total} riddles correctly.")
print("Thanks for playing! 🧠")
