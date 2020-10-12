import unittest
from helpers import Element, update_elements

class UpdateElementsTestCase(unittest.TestCase):
    """Testea la funcion update_elements."""

    def test_update(self):
        """Test if three elements are append to the other list."""

        elements = []
        temp_elements = list(range(0, 5))
        update_elements(temp_elements, elements)
        for element in temp_elements:
            self.assertIn(element, temp_elements)

if __name__ == '__main__':
    unittest.main()