# YouTube Link to Practice Problems
# https://www.youtube.com/watch?v=a6DPueTvN50

# TODO: Write a program that finds the square root of a number
number = 100
square_root = (number ** (1/2))
print(square_root)

# TODO: Write a program to print 'Hello' 7 times
for _ in range(1, 8):
    print("Hello")


# TODO: Wrote a program that generates a random number from 1 to 100
import random

random_num = random.randint(1, 100)
print(random_num)

# TODO: Write a program to check if a number is odd or even
number = int(input("Please enter a number: "))
if number % 2 == 0:
    print("Your number is EVEN")
else:
    print("Your number is ODD ")

# TODO: Write a program to find the largest number from array / list
num_list = [2, 6, 45, 32, 24, 88, 205, 99]
largest_num = max(num_list)
print(f"Largest number: {largest_num}")

# TODO: Write a program to see if a number is prime or not
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
