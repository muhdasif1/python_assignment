while True:
    name: str = input("Please enter your full name: ")

    if name.isalpha():
        age = input("What is your current age? ")

        if age.isdigit():
            print(f"Welcome, {name}! You are age is {age} ")
            break
        else:
            print("Age must be a number. Please try again.")
    else:
        print("Name should only contain letters. Please re-enter your name.")
