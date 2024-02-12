# A program to multiply two even numbers
while True:
    while True:
        num1 = input("Enter the first number: ")
        if num1.isdigit():
            number1 = int(num1)
            break
        else:
            print("Please enter a number")
    if number1%2 == 0:
        break
    else:
        print("Make sure your number is even")
while True:
    while True:
        num2 = input("Enter the second number: ")
        if num2.isdigit():
            number2 = int(num2)
            break
        else:
            print("Please enter a number")
    if number2%2 == 0:
        break
    else:
        print("Make sure your number is even")
print("The product is: ",number1*number2,"\n")