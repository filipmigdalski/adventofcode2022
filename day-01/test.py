import unittest
from main import Calorimeter, Parser


class TestCalorimeter(unittest.TestCase):

    def test_one_element(self):
        # when
        result = Calorimeter.max([[5]])

        # then
        self.assertEqual(result, 5)

    def test_one_inventory(self):
        # when
        result = Calorimeter.max([[5, 7, 9]])

        # then
        self.assertEqual(result, 21)

    def test_happy_path(self):
        # given
        inventories = [[5, 7, 9], [1, 1000, 1000], [2000], [23, 340, 122]]

        # when
        result = Calorimeter.max(inventories)

        # then
        self.assertEqual(result, 2001)

    def test_top3(self):
        # given
        inventories = [[5, 7, 9], [1, 1000, 1000], [2000], [23, 340, 122]]

        # when
        result = Calorimeter.top3(inventories)

        # then
        self.assertEqual(result, 4486)


class TestParser(unittest.TestCase):
    def test_parse_inventories(self):
        # given
        inventories = ["5", "6", "7", "", "8", "9", "", "10"]
        expected = [[5, 6, 7], [8, 9], [10]]

        # when
        result = Parser.parse(inventories)

        # then
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
