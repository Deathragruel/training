import unittest
from employee import Employee

class EmployeeTestCase(unittest.TestCase):
	def setUp(self):
		self.employee = Employee('Rafehy', 'bin Asif')

	def test_give_default_raise(self):
		given_raise = self.employee.give_raise()
		self.assertEqual('Salary: 5000', given_raise)
	def test_give_custom_raise(self):
		given_raise = self.employee.give_raise(10000)
		self.assertEqual('Salary: 10000', given_raise)

if __name__ == '__main__':
	unittest.main()