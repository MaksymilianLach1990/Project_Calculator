# Text templates

# Greatings template
def greatings():
    print("Welcome to the Universal Calculator!")

# Topics template
def topics():
    print("""Select the calculation category:\n
    1 - Basic calculations\n
    2 - Kalkulator BMI\n
    3 - Przeliczanie miar\n
    4 - Podstawowe wzory z matematyki\n
    5 - Podstawowe wzory z fizyki\n
    6 - Podstawowe wzory z chemii\n
    7 - Przeliczanie walut\n
    8 - Lista stałych fizycznych\n
    9 - Exit\n
    """)

# 1. Basic calculations 
def basic_calculation():
    print("""Select the type of calculations:\n
    1 - Adding numbers\n
    2 - Subtraction\n
    3 - Multiplication\n
    4 - Division\n
    5 - Raising to power\n
    6 - The rest from division\n
    7 - Division without change\n
    8 - Extracting the element\n
    9 - Back\n
    """)

# 2. Calculator BMI
def bmi_calculator():
    print("""To calculate BMI, an increase and weight are needed.

    """)

# 9. Exit
def exit():
    print("Thank you for taking advantage of our calculator.")
    print("Goodbye!")