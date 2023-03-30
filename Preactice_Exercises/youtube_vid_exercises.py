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

# TODO 14): Write a program to transpose the given matrix
import numpy

x = [[1, 2, 3],
     [4, 5, 6]]

transpose = [[1, 2],
             [3, 4],
             [5, 6]]

x_array = numpy.array(x).flatten().reshape(3, 2)
print(x_array)

# TODO 15): Write a program to sort the list in alphabetical order and number is ascending order
unsorted_list = ["d", "x", "b", "a", "y", "g"]
unsorted_numbers = [3, 56, 34, -21, 0, 99]
sorted_list = sorted(unsorted_list)
sorted_numbers = sorted(unsorted_numbers)
print(sorted_list)
print(sorted_numbers)

# TODO 16): Write a program to find the most frequent number from list/array
from statistics import mode
number_list = [2, 5, 6, 2, 7, 2, 2, 5, 2]
frequent_number = mode(number_list)

print(f"The most frequent number is {frequent_number}")

# TODO 17): Write a program to find the area of a triangle
a = 5
b = 6
c = 7

# calculate the semi-perimeter
s = (a + b + c) / 2
# calculate the area
area = (s * (s - a) * (s - b) * (s - c)) ** 0.5

print(f"The area of the triangle is {round(area, 2)}")

# TODO 18): Write a program to convert kilometers to miles
kilometers = float(input("Enter kilometers: "))
miles = kilometers * 0.621371
print(f"{kilometers} kilometers = {round(miles, 2)} miles")

# TODO 19): Write a program to display calendar
import calendar
month = int(input(" Select a month (1-12): "))
year = int(input(" Select a year: "))
print(calendar.month(year, month))

# TODO 20): Write 2 programs to check leap year
# ------ THIS IS THE LOGICAL WAY ----------
year = int(input("Which year do you want to check?: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("NOT leap year.")
    else:
        print("Leap year.")
else:
    print("NOT leap year.")

# ------ THIS IS USING PACKAGES  ----------
import calendar

year = int(input("Which year do you want to check?: "))
if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is NOT a leap year.")

# TODO 21): Write a program to find sum of natural numbers
number = int(input("Enter a number: "))
natural_numbers = [number for number in range(1, number + 1)]
sum_natural_numbers = sum(natural_numbers)
print(natural_numbers)
print(f"Sum of natural numbers for {number } is {sum_natural_numbers}.")

# TODO 22): Write a program to find L.C.M (Least Common Multiple)
import math
num_1 = int(input("Enter your first number: "))
num_2 = int(input("Enter your second number: "))

lcm = math.lcm(num_1, num_2)
print(f"The LCM of {num_1} and {num_2} is {lcm}.")

# TODO 23): Write a program to find GCD (Greatest Common Divisor) also called HCF (Highest Common Factor)
import math
num_1 = int(input("Enter your first number: "))
num_2 = int(input("Enter your second number: "))

lcm = math.gcd(num_1, num_2)
print(f"The LCM of {num_1} and {num_2} is {lcm}.")

# TODO 24): Write a program to sort words in alphabetical order
sentence = str(input("Enter a sentence to sort words in alphabetical order: "))
words = sentence.split()
sorted_words = sorted(words)

sorted_sentence = ""
for word in sorted_words:
    sorted_sentence += " " + word

print(f"Sorted:{sorted_sentence}")

# TODO 25): Write a program to sort elements from list in ascending order
list = ["a", "b", "z", "x", "g"]
new_list = sorted(list)
print(new_list)

# TODO 26): Write a program to sort elements from list in descending order
list = ["a", "b", "z", "x", "g"]
new_list = sorted(list, reverse=True)
print(f"Original List: {list}")
print(f"Reverse Sorted List: {new_list}")

# TODO 27): Write a program to generate even number series
number = int(input("Enter a number. I will generate an even number series: "))
print([num for num in range(1, number + 1) if num % 2 == 0])
# for num in range(1, number + 1):
#     if num % 2 == 0:
#         print(num)

# TODO 28): Write a program to generate odd number series
number = int(input("Enter a number. I will generate an even number series: "))
print([num for num in range(1, number + 1) if num % 2 != 0])
# for num in range(1, number + 1):
#     if num % 2 != 0:
#         print(num)

# TODO 30): Write a program to generate fibonacci number series\
def fibonacci(num):
    a = 0
    b = 1
    if num == 1:
        print(a)
    else:
        print(a)
        print(b)
        for num in range(2, num):
            c = a + b
            a = b
            b = c
            print(c)


fibonacci(int(input("Enter a number. I will generate a fibonacci number series: ")))

# TODO 31): Write a program to remove "," from the given string
sentence = "Hello, I am a python developer"
new_sentence = sentence.replace(",", "")
print(f"Original: {sentence}")
print(f"New: {new_sentence}")

# TODO 32): Write a program to remove all duplicate values from a given list
list1 = ["a", 1, "a", 1,  "b", 2, "c", 2, "b", 3, "c", 3]
list2 = list(set(list1))
print(list2)

# TODO 33): Write a program to find the smallest number from a list
num_list = [10, 100, -24, 5, 12, 68]
smallest_num = min(num_list)
print(f"Number List: {num_list}")
print(f"The smallest number is {smallest_num}")

# TODO 34): Write a program to find the largest number from a list
num_list = [10, 100, -24, 5, 12, 68]
largest_num = max(num_list)
print(f"Number List: {num_list}")
print(f"The largest number is {largest_num}")

# TODO 35): Write a program to check if character is vowel or consonant
character = str(input("Enter a character: ")).lower()
if character in ["a", "e", "i", "o", "u"]:
    print("Your character is a vowel.")
else:
    print("Your character is a consonant.")

# TODO 36): Write a program to find the sum of all numbers in a list
num_list = [10, 20, 30, 40]
sum = sum(num_list)
print(f"Number list = {num_list}")
print(f"Sum of number list = {sum}")

# TODO 37): Write a program to find the number of digits from a number
number = str(input("Enter a number: "))
num_digits = len(number)
print(f"Number: {number}")
print(f"Number of digits: {num_digits}")

# TODO 38): Write a program to find unique numbers from a list
num_list = [10, 20, 30, 10, 20, 30]
unique_num = list(set(num_list))
print(f"List: {num_list}")
print(f"Unique Numbers: {unique_num}")

# TODO 39): Write a program to count the number of occurrences of a character in string
sentence = str(input("Enter a sentence: "))
character = str(input("Enter the character to count: "))
char_count = sentence.count(character)
print(f"Character Count = {char_count}")
