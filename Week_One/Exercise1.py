# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
# Ask the user for their salary and year of service and print the net bonus amount.
# Write a python code to implement this scenario.

print("This application can calculate your net bonus ")
salary = int(input("Enter annual salary: "))
service = int(input("Enter year of service: "))

if service >= 5:
    netBonus = salary * 0.05
    print("Your net bonus per annum is: R" + (str(netBonus)))
else:
    print("You are not eligible for a bonus.")



