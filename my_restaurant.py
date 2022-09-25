from restaurant_2 import Restaurant, IceCreamStand

the_restaurant = Restaurant('zakir tikka', 'chicken ginger')
another_restaurant = Restaurant('continental', 'barbecue')
a_different_restaurant = Restaurant('pearl cafe', 'donor')

print(f"Restaurant:- {the_restaurant.restaurant_name.title()}")
print(f"- Specialty:- {the_restaurant.cuisine_type.title()}")
the_restaurant.describe_restaurant()
the_restaurant.open_restaurant()

print(f"\nRestaurant:- {another_restaurant.restaurant_name.title()}")
print(f"- Specialty:- {another_restaurant.cuisine_type.title()}")
another_restaurant.describe_restaurant()
another_restaurant.open_restaurant()

print(f"\nRestaurant:- {a_different_restaurant.restaurant_name.title()}")
print(f"- Specialty:- {a_different_restaurant.cuisine_type.title()}")
a_different_restaurant.describe_restaurant()
a_different_restaurant.open_restaurant()

restaurant = Restaurant('pizza hut', 'pizza (tikka)')
print(f"\n{restaurant.restaurant_name.title()} has served, as of yet, "
	  f"{restaurant.number_served} customers today as it's only been one second"
	  " since opening")
restaurant.number_served = 500
print(f"{restaurant.restaurant_name.title()} has served "
	  f"{restaurant.number_served} customers today and it's only been two hours.")
restaurant.set_number_served(1000)
print(f"{restaurant.restaurant_name.title()} has served "
	  f"{restaurant.number_served} customers today and it's only been four hours.")
restaurant.increment_number_served(3000)
print(f"{restaurant.restaurant_name.title()} has served "
	  f"{restaurant.number_served} customers today and it's only been twelve hours.")

ice_cream_stand = IceCreamStand('jojo', 'ice cream')
ice_cream_stand.describe_restaurant()
ice_cream_stand.display_ice_cream_flavours()