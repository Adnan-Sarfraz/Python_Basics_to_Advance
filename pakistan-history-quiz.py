def Questions():
    score = 0

    # Question 1
    print("\n\nWhen did Pakistan become an independent country?")
    print("1-> 22 May 1947")
    print("2-> 25 Aug 1947")
    print("3-> 14 Aug 1947")
    print("4-> 22 Nov 1947")
    choice = int(input("Enter your choice: "))
    if choice == 3:
        print("Hurray! Correct answer!")
        score += 1
    else:
        print("Better luck next time.")

    # Question 2
    print("\n\nWho was the founder of Pakistan?")
    print("1-> Muhammad Ali Jinnah")
    print("2-> Muhammad Ali Akbar")
    print("3-> Allama Iqbal")
    print("4-> Molana Ali Rizvi")
    choice2 = int(input("Enter your choice: "))
    if choice2 == 1:
        print("Hurray! Correct answer!")
        score += 1
    else:
        print("Better luck next time.")

    # Question 3
    print("\n\nWhat is the national language of Pakistan?")
    print("1-> English")
    print("2-> Urdu")
    print("3-> Punjabi")
    print("4-> Arabic")
    choice3 = int(input("Enter your choice: "))
    if choice3 == 2:
        print("Hurray! Correct answer!")
        score += 1
    else:
        print("Better luck next time.")
    
    # Question 4
    print("\n\nWhat is the name of the national poet of Pakistan?")
    print("1-> Jaun Alia")
    print("2-> Allama Iqbal")
    print("3-> Ali Zaryon")
    print("4-> Muhammad Ali")
    choice4 = int(input("Enter your choice: "))
    if choice4 == 2:
        print("Hurray! Correct answer!")
        score += 1
    else:
        print("Better luck next time.")
    
    # Question 5
    print("\n\nWhich city is called the City of Lights in Pakistan?")
    print("1-> Karachi")
    print("2-> Lahore")
    print("3-> Islamabad")
    print("4-> Multan")
    choice5 = int(input("Enter your choice: "))
    if choice5 == 1:
        print("Hurray! Correct answer!")
        score += 1
    else:
        print("Better luck next time.")

    # Question 6
    print("\n\nWhat is the longest river in Pakistan?")
    print("1-> Indus River")
    print("2-> Chenab River")
    print("3-> Jhelum River")
    print("4-> Ravi River")
    choice6 = int(input("Enter your choice: "))
    if choice6 == 1:
        print("Hurray! Correct answer!")
        score += 1
    else:
        print("Better luck next time.")

    # Question 7
    print("\n\nWho was the first President of Pakistan?")
    print("1-> Iskander Mirza")
    print("2-> Ayub Khan")
    print("3-> Zulfikar Ali Bhutto")
    print("4-> Ghulam Ishaq Khan")
    choice7 = int(input("Enter your choice: "))
    if choice7 == 1:
        print("Hurray! Correct answer!")
        score += 1
    else:
        print("Better luck next time.")

    # Question 8
    print("\n\nWhich of these is a famous mountain range in Pakistan?")
    print("1-> Himalayas")
    print("2-> Alps")
    print("3-> Karakoram")
    print("4-> Andes")
    choice8 = int(input("Enter your choice: "))
    if choice8 == 3:
        print("Hurray! Correct answer!")
        score += 1
    else:
        print("Better luck next time.")

    # New Question 9
    print("\n\nWho was the first woman Prime Minister of Pakistan?")
    print("1-> Fatima Jinnah")
    print("2-> Benazir Bhutto")
    print("3-> Asma Jahangir")
    print("4-> Hina Rabbani Khar")
    choice9 = int(input("Enter your choice: "))
    if choice9 == 2:
        print("Hurray! Correct answer!")
        score += 1
    else:
        print("Better luck next time.")

    # New Question 10
    print("\n\nWhat is the capital city of Pakistan?")
    print("1-> Karachi")
    print("2-> Lahore")
    print("3-> Islamabad")
    print("4-> Quetta")
    choice10 = int(input("Enter your choice: "))
    if choice10 == 3:
        print("Hurray! Correct answer!")
        score += 1
    else:
        print("Better luck next time.")

    # Final score
    print("\n\n-----Quiz Completed!-----")
    print(f"Your total score: {score} out of 10")

# Call the function
Questions()
