import io
import sys
import pytest
from lib.cash_register import CashRegister

class TestCashRegister:
    def setup_method(self):
        self.cash_register = CashRegister()
        self.cash_register_with_discount = CashRegister(0.2)

    def test_cash_register_takes_optional_discount(self):
        '''CashRegister in cash_register.py takes one optional argument, a discount, on initialization.'''
        assert self.cash_register.discount == None
        assert self.cash_register_with_discount.discount == 0.2
        assert self.cash_register_with_discount.discount != 20

    def test_cash_register_sets_total(self):
        '''CashRegister in cash_register.py sets an instance variable total to zero on initialization.'''
        assert self.cash_register.total == 0

    def test_cash_register_sets_items(self):
        '''CashRegister in cash_register.py sets an instance variable items to empty list on initialization.'''
        assert self.cash_register.items == []

    def test_add_item_increases_total(self):
        '''CashRegister in cash_register.py accepts a title and a price and increases the total.'''
        self.cash_register.add_item("soda", 2)
        assert self.cash_register.total == 2

    def test_add_item_accepts_optional_quantity(self):
        '''CashRegister in cash_register.py also accepts an optional quantity.'''
        self.cash_register.add_item("soda", 2, 3)
        assert self.cash_register.total == 6

    def test_add_item_doesnt_forget_previous_total(self):
        '''CashRegister in cash_register.py doesn't forget about the previous total'''
        self.cash_register.add_item("soda", 2, 3)
        self.cash_register.add_item("chips", 4)
        assert self.cash_register.total == 10

    def test_apply_discount_applies_discount(self):
        '''CashRegister in cash_register.py applies the discount to the total price.'''
        self.cash_register_with_discount.add_item("macbook air", 1000)
        self.cash_register_with_discount.apply_discount()
        assert(self.cash_register_with_discount.total == 800)

    def test_apply_discount_success_message(self):
        '''prints success message with updated total'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        self.cash_register_with_discount.add_item("macbook air", 1000)
        self.cash_register_with_discount.apply_discount()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "After the discount, the total comes to $800.00.\n")

    def test_apply_discount_reduces_total(self):
        '''reduces the total'''
        self.cash_register_with_discount.add_item("macbook air", 1000)
        self.cash_register_with_discount.apply_discount()
        assert(self.cash_register_with_discount.total == 800)

    def test_apply_discount_error_message(self):
        '''prints a string error message that there is no discount to apply'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        self.cash_register.apply_discount()
        sys.stdout = sys.__stdout__
        assert(captured_out.getvalue() == "There is no discount to apply.\n")

    def test_get_items(self):
        '''returns an array containing all items that have been added'''
        self.cash_register.add_item("soda", 2)
        self.cash_register.add_item("chips", 4)
        assert self.cash_register.items == [{"title": "soda", "price": 2, "quantity": 1}, {"title": "chips", "price": 4, "quantity": 1}]

    def test_get_items_with_multiples(self):
        '''returns an array containing all items that have been added, including multiples'''
        self.cash_register.add_item("soda", 2, 3)
        self.cash_register.add_item("chips", 4)
        assert self.cash_register.items == [{"title": "soda", "price": 2, "quantity": 3}, {"title": "chips", "price": 4, "quantity": 1}]

    def test_remove_last_item(self):
        '''subtracts the last item from the total'''
        self.cash_register.add_item("soda", 2)
        self.cash_register.add_item("chips", 4)
        self.cash_register.remove_last_item()
        assert self.cash_register.total == 2

    def test_remove_last_item_returns_total_to_zero(self):
        '''returns the total to 0.0 if all items have been removed'''
        self.cash_register.add_item("soda", 2)
        self.cash_register.remove_last_item()
        assert self.cash_register.total == 0.0