#Assignment 4: Ask user to input 3 numbers. Find and print the biggest number using only the if-else statement.

import customtkinter
from tkinter import *

window = customtkinter.CTk()
window.title("Find the biggest number")
window.geometry("750x750")
window.config(bg="#000000")
window.resizable(False, False)

#Labels

title_label = customtkinter.CTkLabel(window, text="Finding the Digits!")
title_label.pack()

label_first = customtkinter.CTkLabel(window, text="Enter the first number:")
label_first.pack()

label_second = customtkinter.CTkLabel(window, text="Enter the second number:", font=('Poppins', 14, 'bold'), text_color="#CC527A", bg_color="#000000")
label_second.pack()

label_third = customtkinter.CTkLabel(window, text="Enter the third number:", font=('Poppins', 14, 'bold'), text_color="#CC527A", bg_color="#000000")
label_third.pack()

#Entries

#Result

result_label = customtkinter.CTkLabel(window, text="")
result_label.pack()

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
    
def find_and_update_result():
    try:
        first_number = float(enter_first.get())
        second_number = float(enter_second.get())
        third_number = float(enter_third.get())

        biggest_number = find_biggest_number(first_number, second_number, third_number)

        print(f"The largest number is {biggest_number}!")

        result_label.config(text=f"The largest number is {biggest_number}!")

    except ValueError:
        result_label.config(text="Please enter valid numbers")

window.mainloop()