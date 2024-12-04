import unittest


class Money:
    def __init__(self, amount, currency) -> None:
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, other) -> bool:
        return self.amount == other.amount and self.currency == other.currency


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
        original_money = Money(4002, "KRW")
        actual_money_after_division = original_money.divide(4)
        expected_money_after_division = Money(1000.5, "KRW")
        self.assertEqual(expected_money_after_division,
                         actual_money_after_division)


if __name__ == "__main__":
    unittest.main()
