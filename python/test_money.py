import unittest
from money import Money
from portfolio import Portfolio
from bank import Bank


class TestMoney(unittest.TestCase):
    
    def setUp(self):
        self.bank = Bank()
        self.bank.add_exchange_rate("EUR", "USD", 1.2)
        self.bank.add_exchange_rate("USD", "KRW", 1100)

    
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
        self.assertEqual(fifteeen_dollars, portfolio.evaluate(self.bank, "USD"))

    def test_addition_dollars_to_euros(self):
        five_dollars = Money(5, "USD")
        ten_euros = Money(10, "EUR")
        portfolio = Portfolio()
        portfolio.add(five_dollars, ten_euros)
        expected_value = Money(17, "USD")
        actual_value = portfolio.evaluate(self.bank, "USD")
        self.assertEqual(expected_value, actual_value, f"{
                         expected_value} != {actual_value}")

    def test_addition_dollars_to_wons(self):
        one_dollar = Money(1, "USD")
        eleven_hundred_won = Money(1100, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar, eleven_hundred_won)
        expected_value = Money(2200, "KRW")
        actual_value = portfolio.evaluate(self.bank, "KRW")
        self.assertEqual(expected_value, actual_value, f"{
                         expected_value} != {actual_value}")

    def test_addition_with_multiple_missing_exchange_rates(self):
        one_dollar = Money(1, "USD")
        one_euro = Money(1, "EUR")
        one_won = Money(1, "KRW")
        portfolio = Portfolio()
        portfolio.add(one_dollar, one_euro, one_won)
        with self.assertRaisesRegex(Exception, r"Missing exchange rates\(s\):\[USD->Kalangid,EUR->Kalangid,KRW->Kalangid\]"):
            portfolio.evaluate(self.bank, "Kalangid")

    def test_conversion(self):
        bank = Bank()
        bank.add_exchange_rate("EUR", "USD", 1.2)
        ten_euros = Money(10, "EUR")
        self.assertEqual(bank.convert(ten_euros, "USD"), Money(12, "USD"))

    def test_converstion_with_missing_exchange_rate(self):
        bank = Bank()
        ten_euros = Money(10, "EUR")
        with self.assertRaisesRegex(Exception, "EUR->Kalangid"):
            bank.convert(ten_euros, "Kalangid")

if __name__ == "__main__":
    unittest.main()
