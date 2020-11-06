"""
# Question 2

### **Question:**

> **_Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8
> Then, the output should be:40320_**
"""

a = int(input("Pls input number: \n"))
s = 1
while a > 1:
    s = s*a
    a -= 1
print("the factorial of a given number is ", s)
