# Task 1: Create functions for each arithmetic operation.
# Task 2: Implement user input to receive numbers and an operation choice.
# Task 3: Ensure your program can handle division by zero and other potential errors.


#input numbers
#input function add/ sub / etc 
#set actions for functions 
#else--> potential errors


response = input("Would you like to add, subtract, multiple, or divide? ")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if response == "add":
    result = num1 + num2
    print(result)
elif response == "subtract":
    result = num1 - num2
    print(result)
elif response == "multiply":
    result = num1 * num2
    print(result)
elif response == "divide":
    if num2 == 0:
        print("INVALID, cannot divide by zero")
    else:
     result = num1 / num2
     print(result)
else:
    print("INVALID INPUT")

    
    
# The Shopping List Maker

# Objective:
# The aim of this assignment is to create a program that helps users make a shopping list.

# Task 1: Write a function that lets the user add items to a list.
# Task 2: Include a feature to remove items from the list.
# Task 3: Add a function that prints out the entire list in a formatted way.

# Initialize an empty list to store grocery items
cart = []

print("Lets go grocery shopping!")
while True:
    user_input = input("What would you like to add to you cart? Or if to remove item say remove. If done say done to finish: ")
    if user_input == "done":
        print("Thanks for shopping, here are your items: ")
        for item in cart:
            print(item)
        break
    elif user_input == "remove":
        removal = input("what item would you like to remove? ")
        if removal in cart:
            cart.remove(removal)
            print(removal, " is removed from the shopping cart.")
        else:
            print("Item not found in the grocery list.")
    else:
        cart.append(user_input)
        print(f"Your cart so far {cart}")