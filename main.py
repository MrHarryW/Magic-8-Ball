import random
while True:
    print("Welcome to the Magic 8 Ball! 🎱")
    question = input("Enter your question: ")
    number = random.randint(1,10)

    if number == 1:
        print("Yes")
    elif number == 2:
        print("Are you sure?")
    elif number == 3:
        print("Maybe")
    elif number == 4:
        print("Spin me again")
    elif number == 5:
        print("I don't think so.")
    else:
        print("No")
