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

# TODO 40): Write a program to count the number of words in string
sentence = str(input("Enter a sentence: "))
words = len(sentence.split())
print(f"Number of words: {words}")

# TODO 41): Write a program to check if string is blank
sentence = str(input("Enter a sentence: "))
if sentence == "":
    print("Sentence is blank.")
else:
    print("Sentence is not blank.")

# TODO 42): Write a program to convert string to integer
string = "2005"
convert = int(string)
print(type(string), string)
print(type(convert), convert)

# TODO 43): Write a program to reverse a string
sentence = str(input("Enter a sentence to reverse: "))
reverse = sentence[::-1]
print(reverse)

# TODO 44): Write a program to convert list into string
sentence = ["Hello", "I", "am", "a", "python", "developer"]
new_string = ""
for word in sentence:
    new_string += word + " "

print(new_string)

# TODO 45): Write a program which takes string and converts it to upper case
string = "abcdefg"
upper = string.upper()
print(f"Lower Case: {string}")
print(f"Upper Case: {upper}")

# TODO 46): Write a program which takes an upper case string and converts it to lower case
string = "ABCDEFG"
lower = string.lower()
print(f"Upper Case: {string}")
print(f"Lower Case: {lower}")

# TODO 47): Write a program which displays a tree using "*"
for i in range(1, 5):
    print(' ' * (5 - i), '* ' * i)

# TODO 48): Write a program which displays an upside down tree using "*"
number = 5
for rows in range(number, 0, -1):
    for columns in range(0, number - rows):
        print(end=" ")
    for columns in range(0, rows):
        print("*", end=" ")
    print()

# TODO 49): Write a program which displays a skewed tree using "*"
for i in range(1, 5):
    print(' ' * (i - 5), '* ' * i)

# TODO 50): Write a program which displays a 5 x 5 square using "*"
number = 5
for i in range(number):
    print("* " * number)

# TODO 51): Write a program which displays ascending number steps
for x in range(5):
    for i in range(x + 1):
        print(i + 1, end=" ")
    print("\n")

# TODO 52): Write a program which displays a diamond shape using "*"
height = int(input("please enter diamond's height: "))
for i in range(height):
    print(" " * (height - i), "*" * (i * 2 + 1))
for i in range(height - 2, -1, -1):
    print(" " * (height - i), "*" * (i * 2 + 1))

# TODO 53): Write a program which displays ascending number steps
for x in range(5):
    for i in range(x + 1):
        print(i + 1, end=" ")
    print("\n")

# TODO 54): Write a program which displays ascending alphabet steps
height = int(input("please number of rows: "))
a = 65
for i in range(1, height + 1):
    for j in range(1, i + 1):
        print("%c" % a, end="")
    a += 1
    print()

# TODO 55): Write a program to delete given element of an index
# delete index 3 or "d"
list = ["a", "b", "c", "d", "e", "f", "g"]
list.remove("d")
print(f"List: {list}")

# TODO 56): Write a program to convert minutes to seconds
minutes = int(input("Enter number of minutes to convert to seconds: "))
seconds = minutes * 60
print(f"{minutes} minutes = {seconds} seconds")

# TODO 57): Write a program to convert hours to seconds
hours = int(input("Enter number of hours to convert to seconds: "))
seconds = hours * 60 * 60
print(f"{hours} minutes = {seconds} seconds")

# TODO 58): Write a program to convert age to days
import datetime
year = int(input("Enter your birth year: "))
month = int(input("Enter your birth month: "))
day = int(input("Enter your birth day: "))
birthday = datetime.date(year, month, day)
now = datetime.date.today()
difference = now - birthday
print(difference.days)

# TODO 59): Write a program to concatenate 2 integer lists
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
concatenate_list = list1 + list2
print(concatenate_list)

# TODO 60): Write a program to convert decimal number to binary
num = int(input("Enter a number to convert to binary: "))
print(bin(num))

# TODO 61): Write a program to convert binary number to decimal
num = str(input("Enter a binary number to convert to decimal: "))
print(int(num, 2))   # int() func takes 2nd argument (base of number to be converted), which is 2 for binary numbers.

# TODO 62): Write a program to convert decimal number to octal
num = int(input("Enter a number to convert to octal: "))
print(oct(num))

# TODO 63): Write a program to convert octal number to decimal
num = str(input("Enter an octal number to convert to decimal: "))
print(int(num, 8))   # int() func takes 2nd argument (base of number to be converted), which is 2 for octal numbers.

# TODO 64): Write a program to convert decimal number to hexa-decimal
num = int(input("Enter a number to convert to hexa-decimal: "))
print(hex(num))

# TODO 65): Write a program to convert hexa-decimal number to decimal
num = str(input("Enter a hexa-decimal number to convert to decimal: "))
print(int(num, 16))   # int() func takes 2nd argument (base of number to be converted), which is 16 for hex numbers.

# TODO 66): Write a program to check if word is plural or singular
word = str(input("Enter a word. I will check if its plural or singular: "))
if word[-1] == "s":
    print("Plural")
else:
    print("Singular")

# TODO 67): Write a program to find number of prime numbers in list
import sympy
num_list = [3, 6, 7, 8, 9, 57]
prime_num = []
count = 0
for num in num_list:
    if sympy.isprime(num):   # if prime is True
        prime_num.append(num)
        count += 1

print(f"Prime number(s) are {prime_num}")
print(f"Count: {count}")

# TODO 68): Write a program to find the second largest number from a list
num_list = [2, 45, 64, 23, 21, 3]
second_largest = sorted(num_list)[1]
print(second_largest)

# TODO 69): Write a program to check if string is palindrome or not
sentence = str(input("Enter word or sentence. I will check if it is palindrome: "))
if sentence == sentence[::-1]:
    print("It's palindrome!")
else:
    print("NOT palindrome")

# TODO 70): Write a program to find the average of numbers
num_list = [12, 45, 78, 36, 45, 237.11, -1, 88]
count = 0
for num in num_list:
    count += 1
avg = sum(num_list) / count
print(avg)

# TODO 71): Write a program to count the number of capital characters in string
sentence = str(input("Enter a sentence. I will count the number of capital letters: "))
count = 0
for letter in sentence:
    if letter.isupper():
        count += 1

print(count)

# TODO 72): Write a program to remove the first and last character of a string
sentence = str(input("Enter a sentence: "))
new_sentence = sentence[1:-1]
print(new_sentence)

# TODO 73): Write a program to find union of two given lists
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]
combined_list = list1 + list2
print(combined_list)

# TODO 74): Write a program to find same numbers in two given list
list1 = [1, 2, 3, 4, 5]
list2 = [0, 2, 3, 4, 7]
same_numbers = [num for num in list1 and list2 if num in list1 and list2]
print(same_numbers)

# another way of writing this
same_num = []
for num in list1 and list2:
    if num in list1 and list2:
        same_num.append(num)

print(same_num)

# TODO 75): Write a program to calculate the mean
num_list = [19, 21, 46, 11, 18]
count = 0
for num in num_list:
    count += 1
mean = sum(num_list) / count
print(mean)

# TODO 76): Write a program to calculate the median
import statistics
num_list = [1, 2, 3, 4, 5, 6]
median = statistics.median(num_list)
print(median)

# TODO 77): Write a function which takes int list and returns sum
def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total


print(sum((10, 20, 30, 40)))


# TODO 78): Write a function which creates a list with given range
def num_range(num1, num2):
    for num in range(num1, num2 + 1):
        print(num)
print(num_range(10, 20))

# TODO 79): Write a program to replace given character in a string
# replace "o" with "u"
sentence = "Hello World"
replace = sentence.replace("o", "u")
print(replace)

# TODO 80): Write a program to replace given word in a string
# replace "python" with "fava"
sentence = "I am a python developer."
replace = sentence.replace("python", "java")
print(sentence)
print(replace)

# TODO 81): Write a program to create matrix filled with 0's
import numpy
num = [[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
num = numpy.array(num)
print(num[0].reshape(3, 3))

# TODO 82): Write a program to create matrix filled with 1's
import numpy
num = [[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]]
num = numpy.array(num)
print(num[0].reshape(3, 3))
