import random
import string

while True:

    while True:
        try:
            n = int(input("Enter password length: "))
            if n > 0:
                break
            print("Length must be greater than 0.")
        except ValueError:
            print("Please enter a valid number.")

    chars = ""

    while chars == "":
        digits = input("Include digits? (y/n): ")
        uppercase = input("Include uppercase? (y/n): ")
        lowercase = input("Include lowercase? (y/n): ")
        punctuation = input("Include symbols? (y/n): ")

        if digits.lower() == "y":
            chars += string.digits

        if uppercase.lower() == "y":
            chars += string.ascii_uppercase

        if lowercase.lower() == "y":
            chars += string.ascii_lowercase

        if punctuation.lower() == "y":
            chars += string.punctuation

        if chars == "":
            print("Please select at least one character type!")

    password = ""

    for i in range(n):
        password += random.choice(chars)

    print("\nGenerated Password:", password)

    print("\n1. Generate another password")
    print("2. Exit")

    
    while True:
       choice = input("Your Choice: ")
       
       if choice=="1":
          break

       elif choice=="2":
        print("Goodbye")
        exit()

       else:
        print("Enter valid choice")