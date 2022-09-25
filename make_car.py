# Is a module for car.py

def make_car(manufacturer, model_name, **car_info):
	car_info['manufacturer'] = manufacturer
	car_info['model_name'] = model_name
	return car_info