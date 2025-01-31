import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
    def test_getDataPoint_calculatePrice(self):
        quotes = [
            {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]
        for quote in quotes:
            expectedDataPoint = (
              quote['stock'],
              quote['top_bid']['price'],
              quote['top_ask']['price'],
              (quote['top_bid']['price'] + quote['top_ask']['price']) / 2
            )
            self.assertEqual(getDataPoint(quote), expectedDataPoint)

    def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
        quotes = [
            {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
            {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453',
             'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
        ]

        for quote in quotes:
            expectedDataPoint = (
              quote['stock'],
              quote['top_bid']['price'],
              quote['top_ask']['price'],
              (quote['top_bid']['price'] + quote['top_ask']['price'])/2
            )
            self.assertEqual(getDataPoint(quote), expectedDataPoint)

    def test_getRatio_price2NotZero_calculatesRatio(self):
        price1 = 117.87
        price2 = 123.34

        self.assertEqual(getRatio(price1, price2), price1/price2)
    def test_getRatio_price2IsZero_returnsNone(self):
        price1 = 117.87
        price2 = 0
        self.assertIsNone(getRatio(price1, price2))

if __name__ == '__main__':
    unittest.main()
