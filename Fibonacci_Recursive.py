# To print the nth Fibonacci Series - recursive method

# function to return the sum of the previous two numbers of a given number
def fibonacci_series(number):
    if number <= 1:
        return number
    else:
        return fibonacci_series(number-2) + fibonacci_series(number-1)


# to get the number 'n' for the nth fibonacci series till a valid number is entered
while True:
    f_number = int(input("Enter the of n for the nth fibonacci series : "))
    if f_number <= 0:
        print("Enter a positive integer")
    else:
        break


# to print the fibonacci series recursively
print(f"Fibonacci Series of {f_number} : ", end = ' ')
for counter in range(f_number):
      print(fibonacci_series(counter), end = ' ')
