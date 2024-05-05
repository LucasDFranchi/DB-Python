import unittest

from src import Orders

class TestOrders(unittest.TestCase):

    def setUp(self):
        self.ordem = Orders()

    def test_combine_orders(self):
        requests_1 = [70, 10, 30]
        n_max_1 = 100

        self.assertEqual(self.ordem.combine_orders(requests_1, n_max_1), 2)

    def test_combine_orders_again(self):
        requests_2 = [100, 90, 95]
        n_max_2 = 100
        
        self.assertEqual(self.ordem.combine_orders(requests_2, n_max_2), 3)

    def test_combine_order_negative(self):
        requests = [100, 90, 95]
        n_max = 0
        with self.assertRaises(Exception):
            self.ordem.combine_orders(requests, n_max)

if __name__ == '__main__':
    unittest.main()
