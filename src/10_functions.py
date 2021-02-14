# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
# def isDivisible(x, y):
#     if x % y == 0:
#         result = True
#     else:
#         result = False
#
#     return result
#
# print(isDivisible(10, 5))

def is_even(num):
    if num % 2 == 0:
        print('Even!')
    else:
        print('Odd')
    return exit()


# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE
print(is_even(num))
