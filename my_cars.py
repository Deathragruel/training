from car import Car
from electric_car import ElectricCar

my_new_car = Car('volkswagen', 'beetle', '2019')
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 23
my_new_car.read_odometer()
my_new_car.update_odometer(0)
my_new_car.read_odometer()

print("\n")
my_used_car = Car('subaru', 'outback', '2015')
print(my_used_car.get_descriptive_name())
my_used_car.read_odometer()
my_used_car.update_odometer(23_500)
my_used_car.read_odometer()
my_used_car.increment_odometer(100)
my_used_car.read_odometer()

my_tesla = ElectricCar('tesla', 'roadster', '2019')
print("\n" + my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()