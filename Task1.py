"""
Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
o	Addition
o	Subtraction
o	Multiplication
o	Division
3.  Displays the results of each operation on the screen.
"""

num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))

print(f"""
Addition       : {num1 + num2}
Subtraction    : {num1 - num2}
Multiplication : { num1 * num2}
Divison        : { num1 / num2}
""")