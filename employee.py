class Employee:
	def __init__(self, first, last):
		self.first = first
		self.last = last
		self.annual_salary = 0
	def give_raise(self, increase = 5000):
		self.annual_salary += increase
		string = f"Salary: {self.annual_salary}"
		return string