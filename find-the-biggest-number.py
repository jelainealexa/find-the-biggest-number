#Assignment 4: Ask user to input 3 numbers. Find and print the biggest number using only the if-else statement.

import customtkinter
from tkinter import *

window = customtkinter.CTk()
window.title("Find the biggest number")
window.geometry("750x750")
window.config(bg="#000000")
window.resizable(False, False)

#Ask user to input three numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
third_number = float(input("Enter the third number: "))

#Find the biggest number among the inputs using if-else statement
def find_biggest_number(first_number, second_number, third_number):
    if first_number > second_number:
        if first_number > third_number:
            return first_number
    elif second_number > third_number:
        return second_number
    else:
        return third_number

biggest_number = find_biggest_number(first_number, second_number, third_number)

#Display the biggest number
print("Among the numbers you entered, the biggest is:", biggest_number)

window.mainloop()