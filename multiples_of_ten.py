number = "Enter a number and i will tell you whether it is a multiple of "
number += "ten or not: "
number = int(input(number))

if number % 10 == 0:
	print("It is a multiple of ten")
else:
	print("It is not a multiple of ten")