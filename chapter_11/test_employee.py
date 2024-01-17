import unittest
from emplyee import Emplyee

class EmployeeTestCase(unittest.TestCase):
    def setUp(self):
        self.jan = Emplyee('jan', 'nowak', 30000)

    def test_give_default_raise(self):
        self.jan.give_raise()
        self.assertEqual(self.jan.salary, 35000)

    def test_give_custom_raise(self):
        self.jan.give_raise(4000)
        self.assertEqual(self.jan.salary, 34000)

if __name__ == '__main__':
    unittest.main()
