import unittest

from src import Contract, Contracts

class TestContracts(unittest.TestCase):
    def test_get_top_N_open_contracts(self):
        contracts = [
            Contract(1, 1), 
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5)
        ]
        renegotiated = [3]  
        top_n = 3           

        expected_open_contracts = [5, 4, 2]  

        contracts_obj = Contracts()
        actual_open_contracts = contracts_obj.get_top_N_open_contracts(contracts, renegotiated, top_n)

        self.assertEqual(expected_open_contracts, actual_open_contracts)

    def test_get_top_N_open_contracts_exception(self):
        contracts = [
            Contract(1, 1), 
            Contract(2, 2),
            Contract(3, 3),
            Contract(4, 4),
            Contract(5, 5)
        ]
        renegotiated = [3]  
        top_n = 0

        contracts_obj = Contracts()
        with self.assertRaises(ValueError):
            actual_open_contracts = contracts_obj.get_top_N_open_contracts(contracts, renegotiated, top_n)

if __name__ == '__main__':
    unittest.main()