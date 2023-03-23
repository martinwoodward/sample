
import parse_expenses

import unittest
import datetime

class TestParseExpenses(unittest.TestCase):
    def test_parse_expenses(self):
        expenses_data = '''2023-01-02 -34.01 USD
        2023-01-03 2.59 DKK
        2023-01-03 -2.72 EUR'''
        expected_output = [(-34.01, 'USD', datetime.datetime(2023, 1, 2)), 
                           (2.59, 'DKK', datetime.datetime(2023, 1, 3)), 
                           (-2.72, 'EUR', datetime.datetime(2023, 1, 3))]
        self.assertEqual(parse_expenses.parse_expenses(expenses_data), expected_output)
        
    def test_parse_expenses_with_comments(self):
        expenses_data = '''# This is a comment
        2023-01-02 -34.01 USD
        2023-01-03 2.59 DKK
        # Another comment
        2023-01-03 -2.72 EUR'''
        expected_output = [(-34.01, 'USD', datetime.datetime(2023, 1, 2)), 
                           (2.59, 'DKK', datetime.datetime(2023, 1, 3)), 
                           (-2.72, 'EUR', datetime.datetime(2023, 1, 3))]
        self.assertEqual(parse_expenses.parse_expenses(expenses_data), expected_output)
        
    def test_parse_expenses_with_empty_lines(self):
        expenses_data = '''
        2023-01-02 -34.01 USD
        
        2023-01-03 2.59 DKK
        
        2023-01-03 -2.72 EUR
        '''
        expected_output = [(-34.01, 'USD', datetime.datetime(2023, 1, 2)), 
                           (2.59, 'DKK', datetime.datetime(2023, 1, 3)), 
                           (-2.72, 'EUR', datetime.datetime(2023, 1, 3))]
        self.assertEqual(parse_expenses.parse_expenses(expenses_data), expected_output)
        
    def test_parse_expenses_with_only_comments(self):
        expenses_data = '''# This is a comment
        # Another comment
        # Yet another comment'''
        expected_output = []
        self.assertEqual(parse_expenses.parse_expenses(expenses_data), expected_output)
        
if __name__ == '__main__':
    unittest.main()