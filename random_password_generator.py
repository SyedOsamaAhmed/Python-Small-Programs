import string
import random


def generatePassword():
    characters = list(string.ascii_letters+string.digits+"@#$%&*()")
    random.shuffle(characters)
    password_length = int(input("Enter password length to generate:"))
    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)
    password = "".join(password)
    print(password)


choice = input("Do you want to generate password? (Yes/NO): ")

if choice == 'Yes':
    generatePassword()
elif choice == 'No':
    print("Goodbye!")
    quit()
