#Assignment 4: Ask user to input 3 numbers. Find and print the biggest number using only the if-else statement.

import customtkinter
from tkinter import *

window = customtkinter.CTk()
window.title("Find the biggest number")
window.geometry("450x450")
window.config(bg="#000000")
window.resizable(False, False)

#Ask user to input three numbers

#Labels and Entries
title_label = customtkinter.CTkLabel(window, text="Finding the Digits!", font=('Poppins', 30, 'bold'), text_color="#E8175D", bg_color="#000000")
title_label.pack(pady=15)

label_first = customtkinter.CTkLabel(window, text="Enter the first number:", font=('Poppins', 14, 'bold'), text_color="#CC527A", bg_color="#000000")
label_first.pack(pady=5)

enter_first = Entry(window, font=('Poppins', 14, 'bold'), width=15, justify='center', fg='#383838', bg='#E3E3E3')
enter_first.pack()

label_second = customtkinter.CTkLabel(window, text="Enter the second number:", font=('Poppins', 14, 'bold'), text_color="#CC527A", bg_color="#000000")
label_second.pack(pady=5)

enter_second = Entry(window, font=('Poppins', 14, 'bold'), width=15, justify='center', fg='#383838', bg='#E3E3E3')
enter_second.pack()

label_third = customtkinter.CTkLabel(window, text="Enter the third number:", font=('Poppins', 14, 'bold'), text_color="#CC527A", bg_color="#000000")
label_third.pack(pady=5)

enter_third = Entry(window, font=('Poppins', 14, 'bold'), width=15, justify='center', fg='#383838', bg='#E3E3E3')
enter_third.pack()

#Result
result_label = customtkinter.CTkLabel(window, text="", font=("Poppins", 25, 'bold'), text_color="#E8175D", bg_color="#000000")
result_label.pack(pady=20)

#Title design
def blink_title(color, blink_count):
    if blink_count > 0:
        title_label.configure(text_color=color)
        window.after(500, blink_title, "#E8175D" if color == "#CC527A" else "#CC527A", blink_count - 1)

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

        result_label.configure(text=f"The largest number is {biggest_number}!")

        continue_button.pack_forget()

    except ValueError:
        result_label.configure(text="Oops! Please enter valid numbers")

#"Continue" button
def continue_button_click():
    find_and_update_result()

continue_button = customtkinter.CTkButton(window, command=continue_button_click, text="Continue", font=('Poppins', 20, 'bold'), fg_color="#E8175D", hover_color="#CC527A", bg_color="#000000", corner_radius=15, cursor="hand2")
continue_button.pack(pady=5)

window.mainloop()