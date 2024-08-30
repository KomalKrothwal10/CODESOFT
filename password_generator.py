import string
import random

def generating_password(length, security_level_complexity):
    if security_level_complexity == "low":
        characters = string.ascii_lowercase
    elif security_level_complexity == "medium":
        characters = string.ascii_letters + string.digits
    elif security_level_complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Please choose low, medium, or high.")
        return None

    password = ''.join(random.choice(characters) for i in range(length))
    return password

while True:
    try:
        length = int(input("Enter the length od your password: "))
        if length <= 0:
            print("Password length should be positive")
            continue
        break
            
    except ValueError:
        print("Invalid input , please enter a correct number.")


security_level_complexity = input("Enter the complexity of the password (low, medium, high): ")

print("Generated Password : ", generating_password(length, security_level_complexity))