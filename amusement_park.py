age = 12

if age < 4:
	price = 0

elif age < 18:
	price = 25

elif age < 65:
	price = 40
# The reason i did not use an else block is to prevent unintended errors.
elif age >= 65:
	price = 20

print(f"Your admission cost is ${price}")