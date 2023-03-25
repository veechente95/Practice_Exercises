# Practice Problems Here ---> https://www.youtube.com/watch?v=a6DPueTvN50

# TODO 3): Write a program that finds the square root of a number
number = 100
square_root = (number ** (1/2))
print(square_root)

# TODO 4): Write a program to swap two variables
x = 10
y = 20

x, y = y, x
print(f"x: {x},"
      f"y: {y}")

# TODO 5): Write a program to print 'Hello' 7 times
for _ in range(1, 8):
    print("Hello")


# TODO 6): Wrote a program that generates a random number from 1 to 100
import random

random_num = random.randint(1, 100)
print(random_num)

# TODO 7): Write a program to check if a number is odd or even
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print("Your number is EVEN")
else:
    print("Your number is ODD ")

# TODO 8): Write a program to find the largest number from array / list
num_list = [2, 6, 45, 32, 24, 88, 205, 99]
largest_num = max(num_list)
print(f"Largest number: {largest_num}")

# TODO 9): Write a program to see if a number is prime or not
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is NOT a prime number")

# TODO 10): Write a program to find the factorial of given number. (ex. factorial of 5 is 210 [5*4*3*2*1])
number = int(input("Please enter a number: "))

factorial = 1
for i in range(1, number + 1):
    factorial *= i

print(f"The factorial of {number} is: {factorial}")

# TODO 11): Write a program to find the ASCII value of a character
character = str(input("Please enter any character: "))
ascii_code = ord(character)
print(f"ascii code of {character} is {ascii_code}")


# TODO 12): Write a program to print current date
import datetime
today_date = datetime.date.today()
print(today_date)

# TODO 13): Write a program to perform add, sub, multiply, divide on two given matrices
import numpy

x = [[2, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]

x_array = numpy.array(x).flatten()
y_array = numpy.array(y).flatten()
print(x_array)
print(y_array)

add = x_array + y_array
sub = x_array - y_array
mult = x_array * y_array
div = x_array / y_array

print(f"Addition of two matrices is: {numpy.array(add).reshape(3, 3)}")
print(f"Subtraction of two matrices is: {numpy.array(sub).reshape(3, 3)}")
print(f"Multiplication of two matrices is: {numpy.array(mult).reshape(3, 3)}")
print(f"Division of two matrices is: {numpy.array(div).reshape(3, 3)}")
