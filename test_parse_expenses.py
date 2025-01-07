import datetime
import pytest
from parse_expenses import parse_expenses

def test_parse_expenses_normal():
    expenses_data = '''2023-01-02 -34.01 USD
2023-01-03 2.59 DKK
2023-01-03 -2.72 EUR'''
    expected = [
        (datetime.datetime(2023, 1, 2), -34.01, 'USD'),
        (datetime.datetime(2023, 1, 3), 2.59, 'DKK'),
        (datetime.datetime(2023, 1, 3), -2.72, 'EUR')
    ]
    assert parse_expenses(expenses_data) == expected

def test_parse_expenses_with_comments():
    expenses_data = '''# This is a comment
2023-01-02 -34.01 USD
# Another comment
2023-01-03 2.59 DKK'''
    expected = [
        (datetime.datetime(2023, 1, 2), -34.01, 'USD'),
        (datetime.datetime(2023, 1, 3), 2.59, 'DKK')
    ]
    assert parse_expenses(expenses_data) == expected

def test_parse_expenses_empty_string():
    expenses_data = ''
    expected = []
    assert parse_expenses(expenses_data) == expected

def test_parse_expenses_invalid_date():
    expenses_data = '2023-01-32 -34.01 USD'
    with pytest.raises(ValueError):
        parse_expenses(expenses_data)

def test_parse_expenses_invalid_value():
    expenses_data = '2023-01-02 -34.01a USD'
    with pytest.raises(ValueError):
        parse_expenses(expenses_data)

def test_parse_expenses_mixed_valid_invalid_lines():
    expenses_data = '''2023-01-02 -34.01 USD
invalid line
2023-01-03 2.59 DKK'''
    with pytest.raises(ValueError):
        parse_expenses(expenses_data)

def test_parse_expenses_with_extra_spaces():
    expenses_data = '''2023-01-02   -34.01   USD
2023-01-03  2.59  DKK'''
    expected = [
        (datetime.datetime(2023, 1, 2), -34.01, 'USD'),
        (datetime.datetime(2023, 1, 3), 2.59, 'DKK')
    ]
    assert parse_expenses(expenses_data) == expected
