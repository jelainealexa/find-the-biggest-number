#Assignment 4: Ask user to input 3 numbers. Find and print the biggest number using only the if-else statement.

#Ask user to input three numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

#Find the biggest number among the inputs using if-else statement
if first_number > second_number:
    if first_number > third_number:
        biggest_number = first_number
elif second_number > first_number:
    if second_number > third_number:
        biggest_number = second_number
else:
    biggest_number = third_number

#Display the biggest number
print("Among the numbers you entered, the largest is:", biggest_number)