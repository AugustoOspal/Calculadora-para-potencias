import unittest
from helpers import Element, update_elements

class UpdateElementsTestCase(unittest.TestCase):
    """It tests the update_elements function"""

    def test_update(self):
        """Test if three elements are append to the other list."""

        elements = []
        temp_elements = list(range(0, 5))
        update_elements(temp_elements, elements)
        for element in temp_elements:
            self.assertIn(element, temp_elements)

class TestElement(unittest.TestCase):
    """It tests the Element class."""

    def setUp(self):
        """Makes two objects, one to test for W and the other for VA."""

        #Check why it dosent let me create the objet and put the attributes in it
        self.W_case = Element()
        self.W_case.name = "Calefactor"
        self.W_case.P = 1200
        self.W_case.fp = 0.7
        self.W_case.quantity = 1

        self.W_case_quantity = Element()
        self.W_case_quantity.name = "Tubos"
        self.W_case_quantity.P = 80
        self.W_case_quantity.fp = 0.55
        self.W_case_quantity.quantity = 4

        self.VA_case = Element(name="Motor", S=2600, fp=0.62, quantity=1)
        self.VA_case.name = "Motor"
        self.VA_case.S = 2600
        self.VA_case.fp = 0.62
        self.VA_case.quantity = 1

    def test_solve_elements_W(self):
        """It tests if it solves a watt case."""

        self.W_case.solve_element(0.25)
        self.assertAlmostEqual(self.W_case.S, 1714.285, 2)
        self.assertAlmostEqual(self.W_case.Qi, 1224.244, 2)
        self.assertAlmostEqual(self.W_case.Qf, 300, 2)
        self.assertAlmostEqual(self.W_case.Qc, 924.244, 2)

    def test_solve_elements_W_case_quantity(self):
        """It tests if it solves a watt case with more than one element."""

        self.W_case_quantity.solve_element(0.25)
        self.assertEqual(self.W_case_quantity.P, 320)
        self.assertAlmostEqual(self.W_case_quantity.S, 581.818, 2)
        self.assertAlmostEqual(self.W_case_quantity.Qi, 485.913, 2)
        self.assertEqual(self.W_case_quantity.Qf, 80)
        self.assertAlmostEqual(self.W_case_quantity.Qc, 405.913, 2)

    def test_solve_elements_VA_case(self):
        """It tests if it solves a VA case."""

        self.VA_case.solve_element(0.25)
        self.assertEqual(self.VA_case.P, 1612)
        self.assertAlmostEqual(self.VA_case.Qi, 2039.964, 2)
        self.assertEqual(self.VA_case.Qf, 403)
        self.assertAlmostEqual(self.VA_case.Qc, 1636.964, 2)

if __name__ == '__main__':
    unittest.main()