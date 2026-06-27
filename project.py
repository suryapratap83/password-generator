
import random
import string

n = int(input("Enter length: "))
while n <= 0:
    n = int(input("Enter a valid length (greater than 0): "))

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

print("Your password:", password)