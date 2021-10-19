# To print the nth Fibonacci Series - iterative method

# to get the number 'n' for the nth fibonacci series till a valid number is entered
while True:
    f_number = int(input("Enter the of n for the nth fibonacci series : "))
    if f_number <= 0:
        print("Enter a positive integer")
    else:
        break

# initialising the first two numbers of the series
number_1 = 0
number_2 = 1

# to keep the sum of the previous two numbers
sum_12 = 0

# counter for while loop
counter=0

# to print the numbers of the fibonacci series using while loop
print(f"Fibonacci Series of {f_number} : ", end=' ')
while counter < f_number:
    print(number_1, end=' ')
    sum_12 = number_1+number_2
    number_1 = number_2
    number_2 = sum_12
    counter += 1

