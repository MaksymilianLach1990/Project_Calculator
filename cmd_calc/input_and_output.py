# Input operations

# Check input
def check_input(func):
    text = ''
    
# Basic input
def input_():
    text = input("What you choose? Number: ")
    return text

# Take numbers
def numbers():
    print("Enter the number separated by a space:")
    number_a = float(input("First number: "))
    number_b = float(input("Second number: "))
    return number_a, number_b

# Next action
def next_action():
    text = input("Do you wont repeat action? (y/n): ")



# Output operations

# The result of the action
def score(result):
    print(f"The result of the action is {result}")

score(2)