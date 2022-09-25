motorcycles = ['honda', 'yamaha', 'aprilia tuono']
print(motorcycles)
motorcycles[2] = 'suzuki'
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)
motorcycles.insert(0, 'kawasaki')
print(motorcycles)
del motorcycles[1]
print(motorcycles)
popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
print(f"My previous motorcycle that i got rid off was {popped_motorcycle.title()}")
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I ever owned was {first_owned.title()}.")
print(motorcycles)
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"A {too_expensive.title()} is way too expensive for me.")