def __print_spiral_matrix__(input_array):

    # assigning the limit/boundary of the array
    top,left = 0,0
    bottom,right = len(input_array),len(input_array)

    # direction decides the traversing direction
    # left to right - direction 1
    # top to bottom - direction 2
    # right to left - direction 3
    # bottom to top - direction 4

    direction = 1

    print("Spiral Matrix :", end = ' ')

    # while loop to traverse through the array
    while top <= bottom and left <= right:
        # print(f"inside while {top} {bottom} {left} {right}")
        if direction == 1:
            for counter in range(left,right):
               print(input_array[left][counter], end = ' ')

            top += 1
            direction = 2

        elif direction == 2:
            for counter in range(top,bottom):
                print(input_array[counter][right-1], end = ' ')

            right -= 1
            direction = 3

        elif direction == 3:
            for counter in range(right-1,left-1,-1):
               print(input_array[bottom-1][counter], end = ' ')

            bottom -= 1
            direction = 4

        elif direction == 4:
            for counter in range(bottom-1,top-1,-1):
                print(input_array[counter][left], end = ' ')

            left += 1
            direction = 1


# taking the array input from the user
no_of_rows = int(input("Enter the number of rows : "))
no_of_columns = int(input("Enter the number of columns : "))

input_array = []

print("Enter the array elements row by row")
# Enter a row of elements with a space in between and press enter to input the next row and so on


for index in range(no_of_rows):
    row_list=list(map(int,input().split(" ")))
    input_array.append(row_list)

# function call
__print_spiral_matrix__(input_array)

