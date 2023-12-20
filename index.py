# Get user input for name and age
name = input("What is your name? ")
age = input("How old are you? ")

# Convert age to an integer (assuming the user enters a valid integer)
age = int(age)

# Greet the user based on their age
if age < 18:
    print(f"Hello, {name}! You are a minor.")
elif age >= 18 and age < 65:
    print(f"Hello, {name}! You are an adult.")
else:
    print(f"Hello, {name}! You are a senior citizen.")
