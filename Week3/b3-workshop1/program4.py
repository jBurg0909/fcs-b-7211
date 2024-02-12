# A program to divide the product of 3 numbers by their average

a = 7
b = 5
c = -12

product = a*b*c
average = (a+b+c)/3
if average == 0:
    print("Your Product is undivisble by the average, as the average is 0")
else:
    result = product/average
    print(result)
