# A program to add numbers until the user enters 0, then print the total

total = 0
current = -1
while (current!=0):
    while True:
        user_input = input("Enter a number: ")
        if user_input.isdigit():
            break
        else:
            print("Please enter an integer (Or 0 to complete the addition): ")
    current = int(user_input)
    total = total + current
print("The total is: ",total)

# Hint: What happens if a user types in something other than a number?