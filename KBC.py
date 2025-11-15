# KBC Game

kbc = [
    ["Question1 - What is the language used to create Facebook?", "Python", "JavaScript", "PHP", "C++", 3],
    ["Question2 - What is the capital of Pakistan?", "Karachi", "Lahore", "Islamabad", "Peshawar", 3],
    ["Question3 - Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Question4 - Who invented the light bulb?", "Newton", "Edison", "Einstein", "Tesla", 2],
    ["Question5 - Which animal is known as the king of the jungle?", "Tiger", "Elephant", "Lion", "Cheetah", 3],
]

levels = [1000, 2000, 5000, 10000, 20000]
money = 0

for i in range(len(kbc)):
    question = kbc[i]
    print(f"\nQuestion for Rs. {levels[i]}:")
    print(f"{kbc[i]}")
    print(f"a. {question[1]}         b. {question[2]}")
    print(f"c. {question[3]}         d. {question[4]}")

    reply = int(input("Enter your answer (1-4): "))

    if reply == question[5]:
        print(f"✅ Correct! You won Rs. {levels[i]}")
        money = levels[i]
    else:
        print("❌ Wrong answer!")
        break

print(f"\n🎉 You take home Rs. {money}")
