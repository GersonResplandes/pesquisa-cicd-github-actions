import unittest
from decimal import Decimal
from app import total

class TestTotal(unittest.TestCase):
    def test_multiplicacao(self): self.assertEqual(total("10.00", 3), Decimal("30.00"))
    def test_zero(self): self.assertEqual(total(0, 2), Decimal("0.00"))
    def test_arredondamento(self): self.assertEqual(total("1.005", 1), Decimal("1.01"))
    def test_preco_negativo(self):
        with self.assertRaises(ValueError): total(-1, 1)
    def test_quantidade_zero(self):
        with self.assertRaises(ValueError): total(1, 0)
    def test_quantidade_fracionaria(self):
        with self.assertRaises(ValueError): total(1, 1.5)

if __name__ == "__main__": unittest.main()
