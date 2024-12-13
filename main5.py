# Program to demonstrate conditional statements in Python

def check_eligibility(age):
    if age < 0:
        return "Invalid age. Age cannot be negative."
    elif age < 13:
        return "You are a child. You can enjoy kid's activities."
    elif age < 18:
        return "You are a teenager. You can participate in teen programs."
    elif age < 60:
        return "You are an adult. You are eligible for adult activities."
    else:
        return "You are a senior citizen. You can enjoy senior-specific benefits."

# Main program
try:
    user_age = int(input("Enter your age: "))
    result = check_eligibility(user_age)
    print(result)
except ValueError:
    print("Invalid input. Please enter a valid number for age.")
