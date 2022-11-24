# Question Three
# Write a Python program that does the following:
# Prints the character at index i in the string "Live happily ".
# my_string = "Live happily ".
# If the index is out of range, the program should print "i is out of range"
# If the string is empty, the program should print "Empty String"

my_string = "Live happily"

i = int(input("Enter index number: "))
length = len(my_string)

if (i < (length-1)) and (i > (-length)):
    print(my_string[i])
elif i > length:
    print(i, "is out of range")
