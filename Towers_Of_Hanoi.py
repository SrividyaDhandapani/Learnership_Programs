# To print the steps to solve the towers of hanoi problem given the number of disks as n and number of pegs as 3


def __towers_of_hanoi__(number_disks, origin, reserve, target):

    if number_disks == 1:
        print('Move disk 1 from {} peg to {} peg'.format(origin, target))
        return

    __towers_of_hanoi__(number_disks-1,origin, target, reserve)

    print("Move disk {} from {} peg to {} peg".format(number_disks, origin, target))

    __towers_of_hanoi__(number_disks-1,reserve, origin, target)


# to get the number 'n' for the number of disks, till a valid number is entered
while True:
    number_disks = int(input("Input the number of disks : "))
    if number_disks <= 0:
        print("Enter a positive integer")
    else:
        break

# Referring the pegs 1, 2 & 3 as P, Q & R respectively
__towers_of_hanoi__(number_disks, 'P', 'Q', 'R')