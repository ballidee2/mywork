import math

name = input("Enter your name: ")
print(f"Hello, (baljit)! Welcome to the program.")

import math


radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2

print(f"The area of the circle with radius {radius} is: {area:.2f}")




length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))


perimeter = 2 * (length + width)


area = length * width

print(f"The perimeter of the rectangle is: {perimeter:.2f}")
print(f"The area of the rectangle is: {area:.2f}")




num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
num3 = int(input("Enter the third integer: "))


sum_of_numbers = num1 + num2 + num3


product_of_numbers = num1 * num2 * num3


average_of_numbers = sum_of_numbers / 3



print(f"The sum of the numbers is: {sum_of_numbers}")
print(f"The product of the numbers is: {product_of_numbers}")
print(f"The average of the numbers is: {average_of_numbers:.2f}")




LOTS_TO_GRAMS = 13.3
POUNDS_TO_LOTS = 32
TALENTS_TO_POUNDS = 20


talents = int(input("Enter the mass in talents (leiviskä): "))
pounds = int(input("Enter the mass in pounds (naula): "))
lots = int(input("Enter the mass in lots (luoti): "))


total_grams = (talents * TALENTS_TO_POUNDS * POUNDS_TO_LOTS * LOTS_TO_GRAMS) + \
              (pounds * POUNDS_TO_LOTS * LOTS_TO_GRAMS) + \
              (lots * LOTS_TO_GRAMS)


kilograms = int(total_grams // 1000)
grams = total_grams % 1000


print(f"The mass is (kilograms) kilograms and (grams:.2f) grams.")




import random


combination_3_digit = [random.randint(0, 9) for _ in range(3)]

combination_3_digit_str = ''.join(map(str, combination_3_digit))


combination_4_digit = [random.randint(1, 6) for _ in range(4)]

combination_4_digit_str = ''.join(map(str, combination_4_digit))


print(f"3-digit combination (0-9): {combination_3_digit_str}")
print(f"4-digit combination (1-6): {combination_4_digit_str}")


SIZE_LIMIT = 42

zander_length = float(input("Enter the length of the zander in centimeters: "))

if zander_length < SIZE_LIMIT:
    difference = SIZE_LIMIT - zander_length
    print(f"The zander is below the size limit by (difference:.2f) centimeters. Please release it back into the lake.")
else:
    print("The zander meets the size limit. You can keep it.")






cabin_class = input("Enter the cabin class (LUX, A, B, C): ").strip().upper()


if cabin_class == "LUX":
    print("LUX: upper-deck cabin with a balcony.")
elif cabin_class == "A":
    print("A: above the car deck, equipped with a window.")
elif cabin_class == "B":
    print("B: windowless cabin above the car deck.")
elif cabin_class == "C":
    print("C: windowless cabin below the car deck.")
else:
    print("Invalid cabin class. Please enter LUX, A, B, or C.")





year = int(input("Enter a year: "))


if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

