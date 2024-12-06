import unittest

from money import Money
from portfolio import Portfolio


class TestMoney(unittest.TestCase):
    def test_multiplication_in_dolloars(self):
        five_dollars = Money(5, 'USD')
        ten_dollars = five_dollars.times(2)
        self.assertEqual(ten_dollars, five_dollars.times(2))

    def test_multiplication_in_euros(self):
        ten_euros = Money(20, 'EUR')
        twenty_euros = ten_euros.times(2)
        self.assertEqual(twenty_euros, ten_euros.times(2))

    def test_division(self):
        four_thousand_two = Money(4002, "KRW")
        one_thousand_point_five = four_thousand_two.divide(4)
        self.assertEqual(one_thousand_point_five, four_thousand_two.divide(4))

    def test_addition(self):
        five_dollars = Money(5, "USD")
        ten_dollars = Money(10, "USD")
        fifteeen_dollars = Money(15, "USD")
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_dollars)
        self.assertEqual(fifteeen_dollars, portfolio.evaluate("USD"))


if __name__ == "__main__":
    unittest.main()
