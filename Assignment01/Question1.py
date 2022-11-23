# #Write a python program that will display the number and its square in the following format.
# Number              Square
# 1                             1
# 2                             4
# 3                             9
# 4                             14
# 5                             25
# 6                             36

numbers = [1, 2, 3, 4, 5, 6]

print("Number", "\tSquare")
for i in range(len(numbers)):
    print(numbers[i], "\t\t", pow(numbers[i], 2))

