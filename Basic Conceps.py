#------Simple Operations------

#Enter a calculation directly into the "print" statement

print(2 + 2)
print( 100 -1 + 3)

#use parentheses to determinate wich operations are performed first

print(2*(3+4))


# NOTE: Using a single slash to divide numbers produces a decimal (or float, as it is called in programming). We'll have more about floats in the next lesson.

#A float can be added to an integer, because Python silently converts the integer to a float.

#Exponentation

print( 2**5**2 )

#QUOTIENT
#Floor division is done using two forward slashes and is used to determine the
#quotient of a division (the quantity produced by the division of two numbers).

print( 20//6 )

#Remaider

#The modulo operator is carried out with a percent symbol (%) and is used to get the remainder of a division.

'''
Exponentiation


Exponentiation is the raising of one number to the power of another.
This operation is performed using two asterisks **.

Let's use exponentiation to solve a known problem.
You are offered a choice of either $1.000.000 or $0.01 (one penny) doubled every day for 30 days (the resulting amount is doubled every day).

Task:
Write a program to calculate the amount that will result from the doubling to understand which choice results in a larger amount.

Hint:
Let's see how exponentiation can be useful to perform the calculation.
For example, if we want to calculate how much money we will have on the 5th day, we can use this expression: 0.01*(2**5) = 0.32 dollars (multiply the penny by 2 raised to the power of 5). 

'''

print(0.01*(2**30))